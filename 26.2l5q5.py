INVENTARIO = {
    "nível": 0,
    "magias": [],
    "itens": {
        "pás": ["Pá do herói"],
    },
    "troféus": {"Capacete do Espectro": 0, "Capacete Gélido": 0},
}

ITENS = {
    "F": {
        "secao": "magias",
        "nome": "Varinha de Chamas",
        "mensagem": "O que é isso? Sinto um fogo emanando do fundo da minha "
        "alma…",
    },
    "V": {
        "secao": "magias",
        "nome": "Varinha de Gelo",
        "mensagem": "Uma magia nova é sempre bom!",
    },
    "P": {
        "secao": "pás",
        "nome": "Pá Espectral",
        "mensagem": "Uma pá transparente, que loucura!",
    },
    "p": {
        "secao": "pás",
        "nome": "Pá comum",
        "mensagem": "Mais uma para minha coleção.",
    },
}

CHEFES = {
    "Specter Knight": {"capacete": "Capacete do Espectro", "nivel_minimo": 2},
    "Polar Knight": {"capacete": "Capacete Gélido", "nivel_minimo": 5},
}

DIRECOES = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

MAGIAS_CATALOGO = [
    "Pergaminho dos Elementos",
    "Varinha da Água",
    "Grimório de 4 folhas",
]


def main():
    fases = (
        {
            "mapa": {
                (0, 2): "p",
                (1, 4): "P",
                (2, 1): "N",
                (2, 2): "N",
                (2, 3): "F",
                (3, 3): "N",
                (3, 4): "N",
                (4, 0): "p",
                (4, 1): "X",
            },
            "mensagem_inicial": (
                "======== CEMITÉRIO DOS LICHS ========\n"
                "Um antigo vilarejo tomado pelos mortos. Me pergunto se "
                "aquele cavaleiro fantasma se esconde por aqui…"
            ),
            "desafio": desafio_cemiterio,
            "requisito": requisito_cemiterio,
            "chefe": "Specter Knight",
            "mensagem_chefe": "Está na hora de caçar fantasmas!",
        },
        {
            "mapa": {
                (0, 4): "X",
                (1, 3): "N",
                (2, 1): "N",
                (2, 2): "N",
                (3, 3): "N",
                (4, 1): "V",
            },
            "mensagem_inicial": (
                "======== NAVIO ENCALHADO ========\n"
                "Uma embarcação antiga do Rei liderada pelo meu antigo "
                "mentor, o que será que encontrarei?"
            ),
            "desafio": desafio_navio,
            "requisito": requisito_navio,
            "chefe": "Polar Knight",
            "mensagem_chefe": (
                "Polar Knight! O que você está fazendo aqui?\nComo pode trair "
                "nosso juramento?"
            ),
        },
    )

    print(
        "Shovel Knight, o lendário guerreiro, está de volta! Salvai-nos, ó "
        "herói da pá!\n"
    )

    inventario = INVENTARIO.copy()
    visitar_mercador(inventario)

    vitoria = True
    i = 0
    while i < 2 and vitoria:
        vitoria = processar_fase(fases[i], inventario)
        i += 1

    if vitoria:
        vitoria = torre(inventario)

    if not vitoria:
        exibir_derrota()

    exibir_relatorio_final(inventario)


def visitar_mercador(inventario):
    entrada = input()
    if entrada != "sim":
        return

    magia = input()
    if magia not in MAGIAS_CATALOGO:
        return

    inventario["magias"].append(magia)


def desafio_cemiterio(inventario):
    print("Black Knight? O que fazes aqui?")
    if inventario["magias"]:
        print("Isso era um desafio?\n")
        return True
    return False


def requisito_cemiterio(inventario):
    return "Pá Espectral" in inventario["itens"]["pás"]


def desafio_navio(inventario):
    print("Você de novo? E que neve toda é essa?")
    if len(inventario["itens"]["pás"]) >= 3:
        print(
            "Engraçado tentar parar um mestre das pás com neve, você se "
            "superou dessa vez!\n"
        )
        return True
    inventario["nível"] -= 3
    if inventario["nível"] > 0:
        print("Que saco! Onde estão minhas outras pás?\n")
        return True
    return False


def requisito_navio(inventario):
    return (
        len(inventario["magias"]) >= 2
        or "Varinha de Gelo" in inventario["magias"]
    )


def processar_fase(fase, inventario):
    print(fase["mensagem_inicial"])
    passou_desafio = fase["desafio"](inventario)

    if not passou_desafio:
        return False

    posicao = (0, 0)

    while True:
        direcao = input()
        posicao = movimentar(posicao, direcao)
        e_chefe = coletar_e_checar_chefe(
            inventario, fase["mapa"], posicao, fase["mensagem_chefe"]
        )
        if e_chefe:
            cumpre_requisito = fase["requisito"](inventario)
            return enfrentar(
                fase["chefe"],
                inventario,
                inventario["nível"],
                cumpre_requisito,
            )


# atualiza a posição no grid 5x5 com base na direção
def movimentar(posicao_atual, direcao):
    posicao_seguinte = ()
    for i in range(2):
        coord = posicao_atual[i] + DIRECOES[direcao][i]
        coord = 0 if coord < 0 else 4 if coord > 4 else coord
        posicao_seguinte += (coord,)
    return posicao_seguinte


def coletar_e_checar_chefe(inventario, mapa_dict, posicao, mensagem_chefe):
    if posicao not in mapa_dict:
        return False

    valor_casa = mapa_dict[posicao]

    if valor_casa == "X":
        print(mensagem_chefe)
        return True

    if valor_casa == "N":
        inventario["nível"] += 1
    elif valor_casa in ITENS:
        item = ITENS[valor_casa]
        if item["secao"] == "magias":
            secao_inventario = inventario["magias"]
        elif item["secao"] == "pás":
            secao_inventario = inventario["itens"]["pás"]
        secao_inventario.append(item["nome"])
        print(item["mensagem"])

    del mapa_dict[posicao]
    return False


def enfrentar(chefe, inventario, nivel, tem_requesito):
    if CHEFES[chefe]["nivel_minimo"] <= nivel and tem_requesito:
        capacete = CHEFES[chefe]["capacete"]
        inventario["troféus"][capacete] = 1
        print()
        return True
    return False


def torre(inventario):
    print("======== TORRE DO DESTINO ========")
    print("Finalmente, aqui de novo…")

    print(f"ANTES - pás: {inventario['itens']['pás']}")
    inventario["itens"]["pás"] = ["coragem do cavaleiro"]
    print(f"DEPOIS - pás: {inventario['itens']['pás']}")
    print("Perdi minhas pás, mas não posso recuar, agora é tudo ou nada!")

    tem_mana = True
    while tem_mana:
        magia = input()
        if magia == "Droga, não tenho mais nada de mana!":
            tem_mana = False
        else:
            magia = magia.split()
            perdeu_nivel = False

            if "morte" in magia:
                inventario["nível"] -= 2
                perdeu_nivel = True
            elif "magia" in magia or "feitiço" in magia:
                inventario["nível"] -= 1
                perdeu_nivel = True

            if perdeu_nivel:
                print(
                    "Não posso recuar de jeito nenhum! Irei superar meus "
                    "limites aqui e agora!"
                )

    if inventario["nível"] > 0:
        print(
            "Minha amada! Finalmente pude revê-la e livrá-la desta terrível "
            "maldição!"
        )
        print("Vamos embora deste lugar amaldiçoado!\n")
        return True
    return False


def exibir_derrota():
    print("A jornada do herói chega a um triste fim…")
    print(
        "Sua pá não foi capaz de cavar uma saída desse buraco de trevas em "
        "que estamos."
    )
    print("O que restou? Nada… brutal.\n")


def exibir_relatorio_final(inventario):
    capacetes = [
        capacete
        for capacete, valor in inventario["troféus"].items()
        if valor == 1
    ]
    print("======== RELATÓRIO FINAL ========")
    print(f"CAPACETES: {', '.join(capacetes) if capacetes else 'NENHUM'}")
    print(
        "MAGIAS:",
        ", ".join(inventario["magias"]) if inventario["magias"] else "NENHUM",
    )
    print(f"PÁS: {', '.join(inventario['itens']['pás'])}")


main()
