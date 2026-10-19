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
    "arma": ["cajado", "machado grande", "adaga", "adaga dupla"],
    "utilidade": ["grimorio", "escudo de madeira", "alaude", "ferramentas de ladrao"],
    "consumivel": ["pergaminho oculto", "racao de viagem", "pocao de cura", "bomba de fumaca"],
}

ADVENTURER_CLASSES = {"B": "Bardo", "G": "Guerreiro", "L": "Ladino", "M": "Mago"}


def main(): ...


def get_adventurers():
    adventurers = []
    valid = False
    while not valid:
        n = int(input())
        if 1 <= n <= 4:
            valid = True

    for _ in range(n):
        name, class_key = input().split()
        adventurer_class = ADVENTURER_CLASSES[class_key]
        adventurer = {"name": name, "class": adventurer_class, "inventory": {}}

        running = True
        while running:
            info = input()
            if info == "pronto":
                running = False
            item, key, power = info.split(" - ")
            key = int(key)
            power = int(power)
            item = decrypt_caeser_cypher(item, key)
            item_type = get_item_type(item)
            adventurer["inventory"][item] = {"type": item_type, "power": power}

        adventurers.append(adventurer)
    return adventurers


def decrypt_caeser_cypher(string, key):
    decrypted_string = ""
    for c in string:
        if c == " ":
            decrypted_string += c
        else:
            i = ALPHABET.index(c)
            j = (i + key) % 26
            decrypted_string += ALPHABET[j]
    return decrypted_string


def get_item_type(item):
    for item_type, items in ITEM_TYPES.items():
        if item in items:
            return item_type


def get_matrix():
    size = int(input())
    return [[int(i) for i in input().split()] for _ in range(size)]


def move(current_position, matrix):
    neighbours = {}
    for i in range(4):
        difference = -int(((i + 1) % 3 == 0))


main()
