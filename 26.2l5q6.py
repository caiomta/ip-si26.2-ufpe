ALPHABET = (
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
)

ITEM_TYPES = {
    "arma": [
        "cajado",
        "machado grande",
        "adaga",
        "adaga dupla",
    ],
    "utilidade": [
        "grimorio",
        "escudo de madeira",
        "alaude",
        "ferramentas de ladrao",
    ],
    "consumivel": [
        "pergaminho oculto",
        "racao de viagem",
        "pocao de cura",
        "bomba de fumaca",
    ],
}

ADVENTURER_CLASSES = {
    "B": "Bardo",
    "G": "Guerreiro",
    "L": "Ladino",
    "M": "Mago",
}

SPECIAL_ITEM_IDEAL_CLASSES = {
    "lira encantada": "Bardo",
    "martelo do trovao": "Guerreiro",
    "olho do abismo": "Ladino",
    "orbe arcano": "Mago",
}

EXTRA_DAMAGE_ITEM_PER_CLASS = {
    "Guerreiro": "racao de viagem",
    "Mago": "pergaminho oculto",
}


def main():
    print(
        "Boa noite a todos!! Sejam bem vindos ao reino de Cinland. A aventura "
        "será longa, mas a gloria é eterna!!"
    )
    print("Vamos as apresentações.")

    adventurers = get_adventurers()
    dungeon_map = get_dungeon_map()
    survived = move_through_dungeon(dungeon_map, adventurers)
    if survived:
        fight_tarrabyte(adventurers)


def get_adventurers():
    adventurers = {}

    print()

    valid = False
    while not valid:
        n = int(input())
        if 1 <= n <= 4:
            valid = True
        else:
            print("Não tem toda essa gente pra jogar não.")

    for _ in range(n):
        name, class_key = input().split()
        adventurer_class = ADVENTURER_CLASSES[class_key]
        adventurer = {"name": name, "inventory": {}}

        item_strings = []
        running = True
        while running:
            info = input()
            if info == "pronto":
                running = False
            else:
                item, key, power = info.split(" - ")
                key = int(key)
                power = int(power)
                item = decrypt_caesar_cypher(item, key)
                item_type = get_item_type(item)

                adventurer["inventory"][item] = {
                    "type": item_type,
                    "power": power,
                }

                item_strings.append(f"{item} [{item_type}, {power}]")

        adventurers[adventurer_class] = adventurer

        print(
            f"{name} ({adventurer_class}):",
            ", ".join(item_strings) if item_strings else "sem itens",
        )

    print(
        "Grupo completamente apresentado, espero que todos estejam preparados "
        "para o que estar por vir."
    )

    return adventurers


def decrypt_caesar_cypher(string, key):
    return "".join(
        [
            c if c == " " else ALPHABET[(ALPHABET.index(c) - key) % 26]
            for c in string
        ]
    )


def get_item_type(item):
    for item_type, items in ITEM_TYPES.items():
        if item in items:
            return item_type


def get_dungeon_map():
    print()
    print(
        "Ao passa pelo arco de pedras, vocês encontram um lugar silencioso, "
        "com um odor nada agradável e um frio sem igual. Um calafrio na "
        "espinha os chama a recuar, mas a jornada começa aqui. Bem vindos a "
        "Dungeon do Grad5."
    )

    size = int(input())
    return [[int(i) for i in input().split()] for _ in range(size)]


def move_through_dungeon(dungeon_map, adventurers):
    ERATOSTENES_SIEVE = calculate_eratostenes_sieve()

    position = (0, 0)
    survived = True
    while True:
        room_value = dungeon_map[position[0]][position[1]]

        if room_value == 99:
            print("Casa visitada: Saída")
            print(
                "Vocês finalmente saem das cavernas escuras e frias. Mas não "
                "parece chegar em um lugar melhor."
            )
            return True

        if room_value == 0:
            room_type = "Entrada"
        elif ERATOSTENES_SIEVE[room_value]:
            room_type = "Armadilha"
        elif is_perfect_square(room_value):
            room_type = "Looting"
        else:
            room_type = "Sala Comum"

        print(f"Casa visitada: {room_type}")

        if room_type == "Armadilha":
            survived = process_trap(adventurers)
        elif room_type == "Looting":
            process_looting(adventurers)

        if not survived:
            print(
                "Os sonhos e objetivos de todos são deixados no chão do "
                "Grad5. Nenhum de vocês restou. A glória nunca será alcançada!"
            )
            return False
        position = get_next_position(position, dungeon_map)


def get_next_position(current_position, dungeon_map):
    max_value = -1
    for difference in (-1, 0), (0, 1), (1, 0), (0, -1):
        c = (
            current_position[0] + difference[0],
            current_position[1] + difference[1],
        )
        if (
            0 <= c[0] < len(dungeon_map)
            and 0 <= c[1] < len(dungeon_map)
            and dungeon_map[c[0]][c[1]] > max_value
        ):
            max_value = dungeon_map[c[0]][c[1]]
            next_position = c
    return next_position


def calculate_eratostenes_sieve():
    limit = 99
    sieve = [True for _ in range(limit + 1)]
    sieve[0] = sieve[1] = False
    n = 2
    while n**2 <= limit:
        if sieve[n]:
            for i in range(n**2, limit + 1, n):
                sieve[i] = False
        n += 1
    return tuple(sieve)


def is_perfect_square(n):
    return int(n ** (1 / 2)) ** 2 == n


# processa a armadilha e retorna se os aventureiros sobreviverão ou não
def process_trap(adventurers):
    trap_type = input()

    if trap_type == "flechas":
        if (
            adventurers.get("Guerreiro", {})
            .get("inventory", {})
            .pop("escudo de madeira", False)
        ):
            print(
                f"O escudo de madeira de {adventurers['Guerreiro']['name']} "
                "protegeu o grupo."
            )
            return True

        last = tuple(adventurers.keys())[-1]

        print(f"{adventurers[last]['name']} sacrificou-se pelo grupo.")

        if last != "Bardo" and (
            adventurers.get("Bardo", {})
            .get("inventory", {})
            .pop("pocao de cura", False)
        ):
            print(
                f"{adventurers['Bardo']['name']} usou a pocao de cura e "
                f"salvou {adventurers[last]['name']}."
            )
            return True

        del adventurers[last]

        # se não houver sobrado ninguém, não sobrevive
        return len(adventurers) > 0
    elif trap_type == "beholder":
        if (
            adventurers.get("Ladino", {})
            .get("inventory", {})
            .pop("bomba de fumaca", False)
        ):
            print(
                f"{adventurers['Ladino']['name']} usou a bomba de fumaça e o "
                "escaparam do Beholder."
            )
            return True

        print(
            "Entraram em uma sala que não deveriam. A ultima visão é tudo "
            "ficando vermelho e em um flash, tudo fica preto. Vocês tão "
            "mortos."
        )
        return False


def process_looting(adventurers):
    print(
        "Finalmente um descanso! Aproveitam as maravilhas presentes na sala."
    )

    lexicographically_sorted_classes = sorted(adventurers.keys())

    bonus = False
    if (
        adventurers.get("Ladino", {})
        .get("inventory", {})
        .pop("ferramentas de ladrao", False)
    ):
        bonus = True
        print(f"{adventurers['Ladino']['name']} arrombou o baú trancado!")

    for _ in range(2 if bonus else 1):
        special_item, receiver_index = input().split(" - ")
        receiver_index = int(receiver_index) % len(adventurers)
        receiver_class = lexicographically_sorted_classes[receiver_index]
        receiver = adventurers[receiver_class]
        is_ideal = SPECIAL_ITEM_IDEAL_CLASSES[special_item] == receiver_class
        receiver["inventory"][special_item] = {"type": "especial"}

        print(
            f"{special_item} foi para {receiver['name']} ({receiver_class})."
        )

        if is_ideal:
            print(
                "O poder que esta em suas mãos é grandioso e parece "
                "chamar-lhe a glória eterna."
            )
        else:
            print(
                "O poder é grande demais, você não consegue extrair o máximo "
                "dele."
            )

        for i in receiver["inventory"].values():
            is_special = i["type"] == "especial"
            if not is_special and is_ideal:
                i["power"] *= 2
            elif not is_special:
                i["power"] *= 1.25
                i["power"] = int(i["power"])


def fight_tarrabyte(adventurers):
    print()
    print(
        "O lugar é silencioso. Até que, de repente, um rugido é ouvido. Uma "
        "criatura surge das sombras: o temido TarraByte!"
    )

    tarrabyte = {}
    tarrabyte["hp"], tarrabyte["ac"] = [int(i) for i in input().split()]
    attack_data = get_attack_data(adventurers)

    print(
        "Ordem de iniciativa:",
        ", ".join([adventurers[a]["name"] for a in attack_data]),
    )

    bard_has_lute = False
    for adventurer_class in attack_data:
        adventurer = adventurers[adventurer_class]

        if adventurer_class == "Bardo" and "alaude" in adventurer["inventory"]:
            bard_has_lute = True

            print(f"{adventurer['name']} inspirou o grupo.")
        else:
            attack_die = attack_data[adventurer_class]["attack_die"]
            critical_attack = attack_die == 20
            bard_bonus = (
                2
                if bard_has_lute
                and adventurer_class in ("Guerreiro", "Ladino")
                else 0
            )

            if critical_attack or attack_die + bard_bonus >= tarrabyte["ac"]:
                # o dano base é o poder da arma mais poderosa do
                # aventureiro atual
                damage = max(
                    [
                        item_data["power"]
                        for item_data in adventurer["inventory"].values()
                        if item_data["type"] == "arma"
                    ],
                    default=0,
                )

                # se o item de dano extra da classe do aventureiro
                # atual estiver em seu inventário, soma-se seu poder ao
                # dano e ele é removido do inventário
                damage += (
                    adventurer["inventory"]
                    .pop(EXTRA_DAMAGE_ITEM_PER_CLASS.get(adventurer_class), {})
                    .get("power", 0)
                )

                damage *= 2 if critical_attack else 1
                tarrabyte["hp"] -= damage

                if critical_attack:
                    print(
                        f"{adventurer['name']} acertou um critico e causou "
                        f"{damage} de dano."
                    )
                else:
                    print(
                        f"{adventurer['name']} acertou e causou {damage} de "
                        "dano."
                    )

                if tarrabyte["hp"] <= 0:
                    print(
                        f"O TarraByte foi derrotado por {adventurer['name']}!"
                    )
                    return True
            else:
                print(f"{adventurer['name']} errou o ataque.")
    print(
        f"O TarraByte sobreviveu com {tarrabyte['hp']} de HP e obliterou o "
        "grupo. Fim da aventura."
    )
    return False


def get_attack_data(adventurers):
    attack_data = {}
    for adventurer_class in adventurers:
        info = input().split()
        attack_data[adventurer_class] = {
            "initiative_die": int(info[0]),
            "attack_die": int(info[1]),
        }

    return dict(
        sorted(
            attack_data.items(),
            key=lambda i: i[1]["initiative_die"],
            reverse=True,
        )
    )


main()
