def main():
    print("Leshy - Outro desafiante. Já faz tanto tempo...")

    cards = []
    totem_class = ""
    phase = 0
    while phase < 3:
        print_phase(phase)
        cards += get_cards()
        items, totem_class = get_items_and_totem(totem_class)
        print_items(items)
        # totem change may affect previously added items coefficients
        player_coefficient = calculate_player_coefficient(cards, items, totem_class)
        won = battle(player_coefficient, cards, phase)
        if not won:
            return
        phase += 1

    print(
        "Leshy - A luz cálida da cabana atravessa o denso nevoeiro... seus infortúnios acabam aqui."
    )


def get_cards():
    cards = []
    while True:
        card = input().lower()
        if card == "fim":
            print(f"{len(cards)} cartas foram adicionadas ao baralho")
            return cards
        cards.append(card)


def get_items_and_totem(totem_class):
    items = []
    while True:
        item = input()
        if item == "FIM":
            return items, totem_class
        if item.lower() == "totem":
            totem_class = input().lower()
            print(f"Totem ativo: {totem_class.capitalize()}")
        elif len(items) < 3:
            items.append(item)
        else:
            print("Inventario cheio")


def calculate_player_coefficient(cards, items, totem_class):
    RARE_CARDS = ("urayuli", "louva-a-deus rei", "ameba", "tubarão", "urso")
    CLASSES = ("canideos", "insetos", "aves", "cervideos", "repteis")
    CLASSES_ANIMALS = (
        ("lobo", "coiote", "cachorro"),
        ("louva-a-deus", "abelha", "formiga"),
        ("corvo", "urubu", "pardal"),
        ("antilocapra", "alce", "caribu"),
        ("rã", "tartaruga", "víbora"),
    )

    coefficient = 0
    totem_class_index = CLASSES.index(totem_class) if totem_class else -1

    for card in cards:
        if "filhote de" in card or "ovo de" in card:
            current_coefficient = 5
        elif card in RARE_CARDS:
            current_coefficient = 20
        elif "pele" in card:
            current_coefficient = 0
        else:
            current_coefficient = 10

        if totem_class_index + 1 and is_card_in_animal_class(
            card, CLASSES_ANIMALS[totem_class_index]
        ):
            current_coefficient *= 2

        coefficient += current_coefficient

    # sum of the amount of non-blank chars in all items
    coefficient += sum([sum([len(j) for j in i.split()]) for i in items])
    return coefficient


def calculate_player_average_coefficient(player_coefficient, cards):
    return player_coefficient // len(cards)


def is_card_in_animal_class(card, class_animals):
    for animal in class_animals:
        if animal in card:
            return True
    return False


def battle(player_coefficient, cards, phase):
    PHASES = (battle_goldwasher, battle_fisher, battle_trader)
    return PHASES[phase](player_coefficient, cards)


def battle_goldwasher(player_coefficient, _):
    print("Garimpeiro - É o Garimpeiro! OPA!")

    enemy_coefficient = 40
    player_coefficient //= 2

    if player_coefficient > enemy_coefficient:
        print("Garimpeiro - Oxe!")
        return True

    if player_coefficient == enemy_coefficient:
        print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
    else:
        print("Garimpeiro - Mais ouro pra mim!")
    return False


def battle_fisher(player_coefficient, cards):
    print("Pescador - Eu sou o Pescador. Quer pescar?")

    player_average_coefficient = player_coefficient // len(cards)
    enemy_coefficient = 90 + player_average_coefficient

    if player_coefficient > enemy_coefficient:
        print("Pescador - Vai pescar...")
        return True

    if player_coefficient == enemy_coefficient:
        print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
    else:
        print("Pescador - Hum. Vai pescar.")
    return False


def battle_trader(player_coefficient, cards):
    print("Comerciante - Vamos negociar.")

    player_skin_cards = sum(["pele" in c for c in cards])
    enemy_coefficient = 160 - player_skin_cards * 10
    player_coefficient += player_skin_cards * 10

    if player_coefficient > enemy_coefficient:
        print("Comerciante - Hmm... muito bem.")
        return True

    if player_coefficient == enemy_coefficient:
        print("Leshy - A fome se instala. Que lástima... chegou a hora da sua ruína.")
    else:
        print("Comerciante - Você vai virar uma pele deslumbrante.")
    return False


def print_phase(phase):
    PHASE_MESSAGES = (
        "Leshy - O sol banha os abetos sonolentos, você adentrou o... matagal.",
        (
            "Leshy - O ar úmido é tomado pelo cheiro fétido de mofo e morte, você caminha "
            "cautelosamente até entrar na... charneca."
        ),
        (
            "Leshy - O alívio do ar fresco logo dá lugar a um arrepio álgido. Você escala até a... "
            "linha de neve."
        ),
    )
    print(PHASE_MESSAGES[phase])


def print_items(items):
    print("Itens no inventario: ", end="")
    for i in range(len(items)):
        print(items[i], end=("\n" if i == len(items) - 1 else ", "))


main()
