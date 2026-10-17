def main():
    inventory = {}

    while True:
        command = input()

        if command == "FIM":
            print_inventory(inventory)
            return

        item = input()
        amount = int(input())

        if command == "ADICIONAR":
            add_item(item, amount, inventory)
        elif command == "REMOVER":
            remove_item(item, amount, inventory)


def add_item(item, amount, inventory):
    if item in inventory:
        inventory[item] += amount
        return
    inventory[item] = amount


def remove_item(item, amount, inventory):
    if item not in inventory:
        print("ERRO! Item não está no Inventário!")
        return
    if inventory[item] < amount:
        print("ERRO! Quantidade insuficiente no Inventário!")
        return
    if inventory[item] == amount:
        del inventory[item]
        return
    inventory[item] -= amount


def print_inventory(inventory):
    if not inventory:
        print("Inventário Vazio!")
        return

    for item, amount in inventory.items():
        print(f"{item} - {amount}")


main()
