warriors = int(input())

print("Nossa, que lindo cavalo! Mas deixe-me verificar apenas uma coisa...")

if not warriors:
    print("ENTRADA LIBERADA")
else:
    print("ARMADILHA")
    duos = warriors // 2
    print(
        f"OS GUERREIROS FORMARAM {duos} DUPLAS E UM GUERREIRO FICOU SOZINHO"
        if warriors % 2  # if ímpar (resto 1 do modulus é truthy)
        else f"OS GUERREIROS FORMARAM {duos} DUPLAS"
    )