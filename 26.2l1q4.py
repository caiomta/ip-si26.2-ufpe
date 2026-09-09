is_raining = input() == "S"
temperature = int(input())
energy_level = int(input())

if is_raining and energy_level > 3:
    print("Brincar de bolinha no laboratório")
elif is_raining:
    print("Soneca na caminha do CIn")
elif temperature > 30 and energy_level > 3:
    print("Nadar no lago da UFPE")
elif temperature > 30:
    print("Descansar na sombra da árvore")
elif temperature > 14 and energy_level > 3:
    print("Longo passeio no parque")
elif temperature > 14:
    print("Passeio curto no quarteirão")
else:
    print("Passeio com roupinha de frio")