def main():
    REGIONS = tatar, asphodel, elysium, temple_of_styx
    total_blessings = 0
    obtained_individual_blessings = []

    print(
        "O portão se abre diante de você, revelando o caminho para o Submundo. Uma nova tentativa "
        "começa agora.\n"
    )

    i = 0
    survived = True
    while survived and i < 4:
        total_blessings, survived = REGIONS[i](obtained_individual_blessings, total_blessings)
        i += 1

    print_end(survived, i)


def tatar(obtained_individual_blessings, total_blessings):
    prisioners = input().split(", ")
    bubble_sort(prisioners)
    print(f"Zagreu: Aqui está sua papelada: {', '.join(prisioners)}\n")
    return get_blessings_and_evaluate(obtained_individual_blessings, total_blessings, 3)


def asphodel(obtained_individual_blessings, total_blessings):
    m1, m2 = [[input().split() for _ in range(3)] for _ in range(2)]
    mr = multiply_matrixes(m1, m2)
    coord = max_value_coord_in_matrix(mr)
    print(f"Zagreu: devo lançar minha vara de pesca nesse ponto: {coord}\n")
    return get_blessings_and_evaluate(obtained_individual_blessings, total_blessings, 6)


def elysium(obtained_individual_blessings, total_blessings):
    legacy = 0
    while legacy < 200:
        hero, title = input().split(" O ")
        current = (
            50
            if hero == "Hércules"
            else 40
            if hero == "Aquiles"
            else 35
            if hero == "Odisseu"
            else 20
        )
        current = (
            current * 1.5
            if title == "Imortal"
            else current * 1.2
            if title == "Forte"
            else current + 15
            if title == "Grande"
            else current + 10
        )
        legacy += current
        print(f"O Herói: {hero} O {title} adicionou {current} pontos de Legado.")
    print("Zagreu: Acho que já fizemos história o suficiente por hoje.\n")
    return get_blessings_and_evaluate(obtained_individual_blessings, total_blessings, 9)


# parâmetro ignorado para uso de duck typing
def temple_of_styx(_, total_blessings):
    print("O Templo de Estige... o último obstáculo entre você e a superfície.\n")

    zagreus_hp = 100
    hades_hp = 200

    second_phase = False

    current_round = 1
    while zagreus_hp > 0 and hades_hp > 0:
        if current_round % 3 == 0:
            print("Zagreu: Meu pai parece estar carregando um forte ataque, é melhor desviar!")

        zagreus_action = input()

        if zagreus_action == "ATACAR":
            hades_hp -= 20
            print("Zagreu golpeia Hades, causando 20 de dano.")
        elif zagreus_action == "ATAQUE ESPECIAL":
            hades_hp -= 40
            print("Zagreu golpeia Hades com um ataque especial, causando 40 de dano.")

        if not second_phase and hades_hp <= 100:
            second_phase = True
            print("\nHades: Chega! Isso acaba agora!\n")

        if hades_hp > 0:
            zagreus_hp -= get_hades_damage(current_round, second_phase, zagreus_action)

        current_round += 1
    print()
    return total_blessings, zagreus_hp > 0


def get_blessings(obtained_individual_blessings, total_blessings):
    VALID_GODS = (
        "AFRODITE",
        "ARES",
        "ARTEMIS",
        "ATENA",
        "DEMETER",
        "DIONISIO",
        "HERMES",
        "POSEIDON",
        "ZEUS",
    )

    while True:
        god = input()
        if god == "PARAR":
            print()
            return total_blessings
        if god == "COMBINADA":
            comb = input(), input()
            if not is_contained(comb, VALID_GODS):
                print("Zagreu: Uma Bênção Combinada assim? Acho que você está brincando comigo.")
            elif not is_contained(comb, obtained_individual_blessings):
                print(
                    "Zagreu: Eu ainda não tenho nenhuma Bênção desse(a) Deus(a), não posso "
                    "combiná-la"
                )
            elif comb[0] == comb[1]:
                print(
                    "Zagreu: Os dois Deuses precisam diferentes para realizar uma Bênção "
                    "Combinada..."
                )
            elif "HERMES" in comb:
                print(
                    "Zagreu: Uma Bênção Combinada com Hermes? Acho que ele é competitivo demais "
                    "pra cooperar com os outros."
                )
            else:
                print(f"Zagreu foi abençoado por uma Bênção Combinada de {comb[0]} e {comb[1]}.")
                total_blessings += 1
        elif god in VALID_GODS:
            print(f"Zagreu obteve uma Bênção de {god}.")
            total_blessings += 1
            if god not in obtained_individual_blessings:
                obtained_individual_blessings.append(god)
        else:
            print(
                f"Zagreu: Ah, claro. A Bênção de {god}. Como pude esquecer? Tenho certeza de que "
                "meu pai também deve ter esquecido de mencioná-lo(a)... Você está brincando comigo "
                "não é?."
            )


def get_blessings_and_evaluate(obtained_individual_blessings, total_blessings, required_blessings):
    total_blessings = get_blessings(obtained_individual_blessings, total_blessings)
    evaluation = total_blessings >= required_blessings
    return total_blessings, evaluation


def is_contained(a, b):
    for i in a:
        if i not in b:
            return False
    return True


def bubble_sort(a):
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            return


# both matrixes are 3x3 and of numeric strings
def multiply_matrixes(m1, m2):
    return [
        [sum([int(m1[i][k]) * int(m2[k][j]) for k in range(3)]) for j in range(3)] for i in range(3)
    ]


# m is 3x3
def max_value_coord_in_matrix(m):
    max_value = m[0][0]
    coord = (0, 0)
    for i in range(3):
        for j in range(3):
            if m[i][j] > max_value:
                max_value = m[i][j]
                coord = (i, j)
    return coord


def get_hades_damage(current_round, second_phase, zagreus_action):
    if zagreus_action == "ESQUIVA":
        print("Zagreu esquiva do ataque de Hades, evitando o dano.")
        return 0
    if current_round % 3:
        damage = 25 if second_phase else 15
    else:
        print("Hades: Desapareça!")
        damage = 100 if second_phase else 50
    print(f"Hades causou {damage} de dano em Zagreu.")
    return damage


def print_end(survived, region):
    if survived:
        print(
            "O senhor do Submundo cai diante de Zagreu. Pela primeira vez, não há nada entre ele e "
            "a superfície."
        )
        print("O portão se abre diante de você.")
        print(
            "Zagreu finalmente deixa o Submundo para trás e sente o calor do sol tocar seu rosto. "
            "Pela primeira vez, a superfície está diante de seus olhos."
        )
        print("Você conseguiu escapar. A tentativa foi concluída.")
        return
    if region == 4:
        print("Zagreu: Me desculpe, mãe. Foi tão perto...")
        return
    print(
        "Zagreu cai, derrotado mais uma vez. Seu corpo se desfaz, retornando ao lugar que conhece "
        "tão bem."
    )


main()
