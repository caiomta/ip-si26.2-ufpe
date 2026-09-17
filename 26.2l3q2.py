RICKS_KIT = ["colt_357", "distintivo", "radio_comunicador", "cantil", "curativo"]
MICHONNES_KIT = ["katana", "amolador", "binoculo", "faixa_curativo", "mapa"]
DARYLS_KIT = ["arco e flecha", "flechas", "faca_de_caca", "corda", "carne_seca"]
CAROLS_KIT = ["facao", "bomba_de_fumaca", "sangue_zumbi", "fosforos", "biscoito"]

my_kit = [
    "taco_beisebol",
    "besta",
    "kit_medico",
    "feijao_enlatado",
    "walkie_talkie",
    "garrafa_agua",
    "biscoito",
]

partner = input()

if partner == "Rick":
    print(
        "Um grande líder sempre ajuda sua equipe, Rick lhe dá uma lanterna para a noite"
    )
    partners_kit = RICKS_KIT
    my_kit.append("lanterna")

    # dia 1
    my_kit.remove("taco_beisebol")
    partners_kit.append("taco_beisebol")
    print(f"Kit atual sobrevivente: {my_kit}")
elif partner == "Michonne":
    print(
        "Michonne é uma ótima combatente, ela te dá uma arma para você não passar apertos."
    )
    partners_kit = MICHONNES_KIT
    my_kit.append("faca_afiada")

    # dia 1
    my_kit.remove("kit_medico")
    print("Você usou o kit médico para socorrer Michonne!")
    print(f"Kit atual sobrevivente: {my_kit}")
elif partner == "Daryl":
    print("Daryl é um ótimo caçador. Ele te dá carne para comer na refeição")
    partners_kit = DARYLS_KIT
    my_kit.append("carne")

    # dia 1

    # my_kit.remove("besta")
    # partners_kit.append("besta")
    # partners_kit.remove("arco e flecha")
    # my_kit.append("arco e flecha")

    besta_index = my_kit.index("besta")
    bow_index = partners_kit.index("arco e flecha")

    my_kit.pop(besta_index)
    partners_kit.pop(bow_index)

    my_kit.insert(besta_index, "arco e flecha")
    partners_kit.insert(bow_index, "besta")

    print(f"Kit atual sobrevivente: {my_kit}")
    print(f"Kit atual Daryl: {partners_kit}")
elif partner == "Carol":
    print("Carol sabe como se esconder dos zumbis. Ela te dá uma ajuda.")
    partners_kit = CAROLS_KIT
    my_kit.append("roupa_de_camuflagem")

    # dia 1
    partners_kit.remove("bomba_de_fumaca")
    partners_kit.remove("sangue_zumbi")
    partners_kit.remove("fosforos")

    partners_kit += my_kit[2:4]
    my_kit = my_kit[:2] + my_kit[4:]

# dia 2
partners_kit += my_kit[2:]
my_kit = my_kit[:2]
print("Agora com as costas mais leves, podemos continuar com a nossa caminhada\n")

# dia 3
print("Finalmente chegamos em Alexandria!\n")
print(f"Ufa, podemos ficar aqui por um tempo,{partner}\n")
print(f"Kit do sobrevivente: {my_kit}\n")
print(f"Kit do {partner}: {partners_kit}")
