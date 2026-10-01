def main():
    feitico_anterior = ""
    poder = 0

    meta = int(input())
    moli = int(input())
    lotus = int(input())
    cinzas = int(input())
    tentativas = int(input())

    for _ in range(tentativas):
        nome, intensidade = input().split()
        intensidade = int(intensidade)

        custo_moli, custo_lotus, custo_cinzas = calcular_requisitos(nome, intensidade)

        if possui_ingredientes(
            moli,
            lotus,
            cinzas,
            custo_moli,
            custo_lotus,
            custo_cinzas,
        ):
            moli, lotus, cinzas, poder_obtido, _ = conjurar_feitico(
                moli,
                lotus,
                cinzas,
                custo_moli,
                custo_lotus,
                custo_cinzas,
                poder,
                nome,
                feitico_anterior,
            )
            poder += poder_obtido
            feitico_anterior = nome
        else:
            exibir_ingredientes_insuficientes(nome)

    exibir_relatorio(poder, moli, lotus, cinzas)
    checar_poder(meta, poder)


def calcular_requisitos(nome, intensidade):
    if nome == "LUA":
        return intensidade, 1, 0
    if nome == "SOMBRAS":
        return 0, intensidade, 2
    if nome == "FAMILIAR":
        return 1, 1, intensidade


def possui_ingredientes(moli, lotus, cinzas, custo_moli, custo_lotus, custo_cinzas):
    return moli >= custo_moli and lotus >= custo_lotus and cinzas >= custo_cinzas


def conjurar_feitico(
    moli,
    lotus,
    cinzas,
    custo_moli,
    custo_lotus,
    custo_cinzas,
    poder_base,
    nome,
    feitico_anterior,
):
    moli -= custo_moli
    lotus -= custo_lotus
    cinzas -= custo_cinzas

    if nome == "LUA":
        poder_obtido = 10 * custo_moli
    elif nome == "SOMBRAS":
        poder_obtido = 12 * custo_lotus
    elif nome == "FAMILIAR":
        poder_obtido = 15 * custo_cinzas

    bonus = 5 if feitico_anterior and feitico_anterior != nome else 0
    poder_obtido += bonus

    print(f"Melinoë conjurou {nome} e obteve {poder_obtido} de poder.")

    if bonus:
        print("Sinergia lunar ativada! Selene concedeu 5 de poder extra.")
        print("Hécate: A luz de Selene responde à sua feitiçaria. Faça-a valer.")
    elif not feitico_anterior:
        print("Hécate: Foi para isto que treinamos todas essas noites, Melinoë.")
    else:
        print(
            "Hécate: Disciplina, Melinoë. Uma bruxa vence antes mesmo de deixar a Encruzilhada."
        )

    print("Que assim seja!")

    return moli, lotus, cinzas, poder_obtido, bonus


def exibir_ingredientes_insuficientes(nome):
    print(f"Ingredientes insuficientes para conjurar {nome}.")
    print(
        "Hécate: Intenção sem preparo não basta. Reúna os ingredientes e tente outra vez."
    )


def exibir_relatorio(poder, moli, lotus, cinzas):
    print()
    print(f"Poder acumulado: {poder}")
    print(f"Ingredientes restantes: {moli} moli, {lotus} lotus e {cinzas} cinzas.")


def checar_poder(meta, poder):
    if meta <= poder:
        print("Melinoë está pronta para enfrentar Cronos.")
        print(
            "Hécate: Você está pronta para partir. Lembre-se do que aprendeu na Encruzilhada — e retorne para nós."
        )
    else:
        print("Melinoë precisa se preparar melhor antes de enfrentar Cronos.")
        print(
            "Hécate: Cronos não terá piedade de você. Eu tampouco terei durante seu treinamento."
        )


main()
