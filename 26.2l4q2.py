def main():
    exibir_inicio()
    venceu = False
    tentativas = 0

    while not venceu and tentativas < 2:
        tentativas += 1
        posicao = [0, 0]
        personagem, hp_maximo = selecionar_personagem()
        hp = hp_maximo

        if tentativas == 1:
            masmorra = receber_masmorra()
        else:
            masmorra = transpor_masmorra(masmorra)

        comandos = input()

        passos = 0
        i = 0
        while hp and not venceu:
            passos = movimentar(posicao, comandos[i], passos)
            sala = masmorra[posicao[1]][posicao[0]]
            hp, venceu = aplicar_efeito_sala(sala, personagem, hp, hp_maximo, tentativas, passos)
            i += 1


# inicia seleção de personagem e retorna seu nome e HP máximo
def selecionar_personagem():
    personagem = input()

    print(f"O(A) {personagem} é o(a) herói(na) lendário(a) escolhido(a)!")

    if personagem == "Cavaleiro":
        hp_maximo = 55
    elif personagem == "Paladino":
        hp_maximo = 80
    elif personagem == "Sacerdotisa":
        hp_maximo = 60
    elif personagem == "Necromante":
        hp_maximo = 40
    elif personagem == "Assassino":
        hp_maximo = 45
    elif personagem == "Bruxa":
        hp_maximo = 50

    return personagem, hp_maximo


# calcula a direção, altera a posição respeitando os limites e retorna os passos até o momento
def movimentar(posicao, comando, passos):
    COMANDOS = ("^", ">", "v", "<")
    for i in range(-1, 3):
        if comando == COMANDOS[i]:
            direcao = (i + 1) % 2
            mudanca, limite = (-1, 0) if i <= 0 else (1, 4)
            if posicao[direcao] == limite:
                return passos
            posicao[direcao] += mudanca
            return passos + 1


# aplica o efeito da sala atual e retorna o HP resultante e o estado de vitória atual
def aplicar_efeito_sala(sala, personagem, hp, hp_maximo, tentativas, passos):
    if sala == "+":
        hp = min(hp + 20, hp_maximo)
    elif sala == "c":
        hp = max(hp - 15, 0)
        if hp:
            exibir_vitoria_no_combate(personagem, hp)
        else:
            exibir_morte(tentativas)
    elif sala == "@":
        hp = max(hp - 25, 0)
        if hp:
            exibir_vitoria(hp, passos)
            return hp, True
        exibir_morte(tentativas)
    return hp, False


def receber_masmorra():
    return [input().split() for _ in range(5)]


def transpor_masmorra(masmorra):
    return [[masmorra[i][j] for i in range(5)] for j in range(5)]


def exibir_inicio():
    print(
        "A jornada pela Pedra Mágica tem início! O destino do reino está selado, e esta guerra "
        "finalmente encontrará o seu fim.\n"
    )


def exibir_morte(tentativas):
    if tentativas == 1:
        print("Ainda não é o fim! A jornada continua…\n")
    else:
        print("Sem heróis. Sem esperança. O Reino caiu.")


def exibir_vitoria(hp, passos):
    print("A profecia se cumpriu e a paz reina mais uma vez!")
    print(
        f"Cruzando as profundezas da masmorra em {passos} passos de pura bravura, o(a) nosso(a) "
        f"herói(na) ergue-se triunfante com {hp} HP."
    )


def exibir_vitoria_no_combate(personagem, hp):
    print(f"O(A) {personagem} prevalece no combate, mantendo-se firme com {hp} HP!")


main()
