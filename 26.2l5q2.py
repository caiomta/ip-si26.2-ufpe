HERO_DATA = {
    "Vax": {
        "special_weapon": "Adaga Mágica",
        "special_message": "Uma arma dada pela própria rainha dos corvos, agora apenas preciso "
        "saber se isso é uma dádiva ou uma maldição.",
    },
    "Pike": {
        "special_weapon": "Placa do Mártir",
        "special_message": "Everlight, espero que um dia você me perdoe, mas não vou mais depender "
        "de você.",
    },
    "Grog": {
        "special_weapon": "Manoplas de Titanstone",
        "special_message": "Estou maior agora, e pronto para entrar em fúria!",
    },
    "Percy": {
        "special_weapon": "The List",
        "special_message": "Não, ele novamente não, Orthax já me dominou uma vez, não posso deixar "
        "isso acontecer de novo.",
    },
    "Scanlan": {
        "special_weapon": "Caça Mitos",
        "special_message": "A espada lendária capaz de matar todos os Dragões... nas mãos do "
        "Scanlan?!",
    },
    "Vex": {
        "special_weapon": "Fenthras",
        "special_message": "Um arco mágico, capaz de controlar todos os elementos? isso é perfeito "
        "para mim querido!",
    },
    "Keyleth": {
        "special_weapon": "Pináculo da Confluência",
        "special_message": "Com isso e meu aramenté completo, a natureza inteira estará sobre meu "
        "controle.",
    },
}


def main():
    team_weapons = {hero: {} for hero in HERO_DATA}
    while True:
        info = input()
        if info == "FIM":
            print_best_weapons(team_weapons)
            return
        handle_weapon_getting(info, team_weapons)


def handle_weapon_getting(info, team_weapons):
    hero, weapon, power = info.split(" , ")
    team_weapons[hero][weapon] = int(power)
    current_hero_data = HERO_DATA[hero]
    if weapon == current_hero_data["special_weapon"]:
        print(current_hero_data["special_message"])


def print_best_weapons(team_weapons):
    for hero, weapons in team_weapons.items():
        if weapons:
            best_weapon = max(
                weapons,
                key=weapons.get,  # `weapons.get` funciona como `lambda w: weapons[w]` na prática
            )
            power = weapons[best_weapon]
            print(f"A arma mais forte de {hero} é a {best_weapon} com {power} Pontos de Poder.")
        else:
            print(f"{hero} não possui nenhuma arma.")


main()
