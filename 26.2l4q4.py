def main():
    total_chips = 0
    available_hand_changes = 4
    hands_played = 0
    active_arcana = []

    goal = get_goal()
    jokers, arcana = get_inventory()
    hand = get_hand()

    while True:
        action = input()
        if action == "Jogar":
            total_chips += play_hand(hand, jokers, active_arcana)
            hands_played += 1
            active_arcana = []  # after playing the arcana's effects clear

            print(f"Total de chips: {total_chips}")

            if check_win(total_chips, goal, hands_played):
                return
            elif hands_played == 4:  # defeat
                print(f"Jimbo: Mais que flop! Faltou {goal - total_chips} chips.")
                return

            # if the player has neither won nor lost yet, they get a new hand
            hand = get_hand()
        elif action == "Trocar" and available_hand_changes:
            hand, available_hand_changes = change_hand(available_hand_changes)
        elif action == "Arcano":
            use_arcana(arcana, active_arcana)


def get_goal():
    goal = int(input())
    print(f"Jimbo: Certo, você tem que conseguir {goal} chips. Boa sorte!")
    return goal


def get_inventory():
    inventory = eval(input())
    jokers, arcana = separate_jokers_from_arcana(inventory)
    print("Curingas:", ", ".join(jokers))
    print("Arcanos:", ", ".join(arcana))
    jokers = apply_blueprint(jokers)
    return jokers, arcana


# semantic function
def get_hand():
    return eval(input())


def change_hand(available_hand_changes):
    return eval(input()), available_hand_changes - 1


def play_hand(hand, jokers, active_arcana):
    filtered_hand, errors = filter_hand_and_count_errors(hand)
    errors = apply_chicot(jokers, errors)
    base_chips, multiplier = process_errors(errors)
    base_chips, multiplier = apply_jokers(jokers, base_chips, multiplier)
    multiplier = apply_arcana(active_arcana, filtered_hand, multiplier)
    return calculate_points(filtered_hand, base_chips, multiplier)


def use_arcana(arcana, active_arcana):
    if not arcana:
        return

    used_arcanum = arcana.pop(0)

    # Tolo's effect is immediate
    if used_arcanum == "Tolo":
        new_arcanum = input()
        arcana.append(new_arcanum)
    elif used_arcanum not in active_arcana:
        active_arcana.append(used_arcanum)

    print("Arcanos:", ", ".join(arcana))


def separate_jokers_from_arcana(inventory):
    JOKERS = ("Joker", "Space Joker", "Blueprint", "Chicot")
    ARCANA = ("Tolo", "Hierofante", "Justiça", "Força")
    return (
        [item for item in inventory if item in JOKERS],
        [item for item in inventory if item in ARCANA],
    )


def filter_hand_and_count_errors(hand):
    hand_copy = ["x"] + hand
    marked_indexes = []
    limit = len(hand_copy) // 2
    for i in range(1, limit):
        for j in range(2):  # [2i, 2i+2)=[2i, 2i+1]
            if hand_copy[i] < hand_copy[2 * i + j]:
                marked_indexes.append(2 * i + j)

    errors = len(marked_indexes)
    filtered_hand = [
        hand_copy[i] for i in range(1, len(hand_copy)) if i not in marked_indexes
    ]
    return filtered_hand, errors


def process_errors(errors):
    print("Classificação da mão: ", end="")

    if errors == 0:
        print("Full House")
        return 40, 4
    if errors == 1:
        print("Três do mesmo")
        return 30, 3
    if errors == 2:
        print("Dois pares")
        return 20, 2
    print("Carta Maior")
    return 5, 1


def apply_chicot(jokers, errors):
    return max(errors - 2 * jokers.count("Chicot"), 0)


def apply_blueprint(jokers):
    return [
        jokers[i + 1] if jokers[i] == "Blueprint" and i + 1 < len(jokers) else jokers[i]
        for i in range(len(jokers))
    ]


def apply_jokers(jokers, chips, multiplier):
    for i in range(len(jokers)):
        joker = jokers[i]

        if joker == "Joker":
            multiplier += 4
        elif joker == "Space Joker":
            chips += 20
            multiplier += 1
    return chips, multiplier


def apply_hierofante(filtered_hand):
    for i in range(len(filtered_hand)):
        if filtered_hand[i] < 30:
            filtered_hand[i] *= 2


def apply_justica(filtered_hand, multiplier):
    n_divisible_by_3_cards = sum([card % 3 == 0 for card in filtered_hand])
    multiplier *= 1.1**n_divisible_by_3_cards
    return multiplier


def apply_forca(filtered_hand):
    for i in range(len(filtered_hand)):
        x = filtered_hand[i]
        sqrt_x = int(x**0.5)
        if sqrt_x**2 == x:
            filtered_hand[i] += 50


def apply_arcana(active_arcana, filtered_hand, multiplier):
    if active_arcana:
        if "Hierofante" in active_arcana:
            apply_hierofante(filtered_hand)
        if "Justiça" in active_arcana:
            multiplier = apply_justica(filtered_hand, multiplier)
        if "Força" in active_arcana:
            apply_forca(filtered_hand)
    return multiplier


def calculate_points(filtered_hand, base_chips, multiplier):
    base_chips += sum(filtered_hand)
    multiplier = round(multiplier, 2)
    total_chips = int(base_chips * multiplier)

    print(f"{base_chips} chips x {multiplier} = {total_chips}")

    return total_chips


def check_win(total_chips, goal, hands_played):
    if goal <= total_chips:
        print("Jimbo: Impressionante, você bateu a aposta.")
        if hands_played == 1:
            print("Jimbo: Balatro Balatrez esta a jugar balatro")
        elif hands_played == 4:
            print("Jimbo: Por pouco você falha, calculou bem.")
        else:
            print("Jimbo: Ainda bem que não apostei contra você.")
        return True
    return False


main()
