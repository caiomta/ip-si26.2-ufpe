RELIQUIAS_LENDARIAS = {
    "Espada Sagrada": 15,
    "Arco Lendário": 20,
    "Cajado Magistral": 25,
}


def main():
    print(
        "As sombras avançam sobre o Reino Celeste... É chegada a hora de reunir os heróis "
        "dispostos a enfrentar o Rei Demônio!"
    )

    rei_demonio = {
        "Vida": 100,
        "Agilidade": 32,
        "Dano por Ataque": 25,
    }
    time = receber_time()
    memorial = []

    if len(time) < 3:
        print(
            "Poucos atenderam ao chamado do reino... Sem ao menos três heróis para formar a "
            "resistência, o Reino Celeste parece condenado à ruína!"
        )
        return

    print(
        "Os portões do castelo se abrem e os heróis marcham rumo ao campo de batalha. O "
        "confronto contra o Rei Demônio começa agora!"
    )

    while time and rei_demonio["Vida"] > 0:
        nome_heroi = input()
        if nome_heroi not in time:
            print(
                "Nenhum herói com esse nome está no campo de batalha. O Rei Demônio aguarda "
                "impacientemente por seu próximo adversário!"
            )
        else:
            batalhar(time, nome_heroi, rei_demonio, memorial)

    # final
    if not time:
        print(
            "O último herói tombou. Vitorioso, o Rei Demônio retoma sua marcha sombria em "
            "direção ao Reino Celeste!"
        )
        print("--- Memorial dos Heróis Caídos ---")
        print("\n".join(memorial))
    else:
        print(
            f"Com um golpe decisivo, {nome_heroi} derrota o Rei Demônio! Após uma longa "
            "batalha, o Reino Celeste está finalmente livre de sua ameaça!"
        )

        if memorial:
            print(
                "A vitória foi conquistada, mas teve seu preço. Alguns heróis não retornaram do "
                "campo de batalha e seus nomes serão eternizados no Memorial dos Heróis."
            )
            print("--- Memorial dos Heróis Caídos ---")
            print("\n".join(memorial))
        else:
            print(
                "Contra todas as expectativas, todos os heróis retornaram vivos ao Reino "
                "Celeste. Naquela noite, nenhuma nova inscrição precisou ser feita no "
                "Memorial dos Heróis."
            )


def receber_time():
    time = {}
    while True:
        nome = input()
        if nome == "FIM":
            return time

        vida, agilidade, arma = [info.split(maxsplit=1)[1] for info in input().split(" - ")]
        dano = RELIQUIAS_LENDARIAS.get(arma, 0)
        time[nome] = {
            "Vida": int(vida),
            "Agilidade": int(agilidade),
            "Arma": arma,
        }


def batalhar(time, nome_heroi, rei_demonio, memorial):
    heroi = time[nome_heroi]
    dano_heroi = RELIQUIAS_LENDARIAS.get(heroi["Arma"], 0)
    heroi_primeiro = heroi["Agilidade"] > rei_demonio["Agilidade"]

    if heroi_primeiro:
        ataque_heroi(nome_heroi, heroi["Arma"], dano_heroi, rei_demonio)
        if rei_demonio["Vida"] <= 0:
            return
        ataque_rei_demonio(time, nome_heroi, heroi, rei_demonio, memorial)
    else:
        ataque_rei_demonio(time, nome_heroi, heroi, rei_demonio, memorial)
        if heroi["Vida"] <= 0:
            return
        ataque_heroi(nome_heroi, heroi["Arma"], dano_heroi, rei_demonio)


def ataque_heroi(nome_heroi, arma_heroi, dano_heroi, rei_demonio):
    if dano_heroi == 0:
        print(
            "A arma do herói não possui poder suficiente para atravessar a aura sombria do Rei "
            "Demônio!"
        )
        return

    rei_demonio["Vida"] -= dano_heroi
    print(
        f"{nome_heroi} brandiu {arma_heroi} contra o Rei Demônio e causou "
        f"{dano_heroi} pontos de dano!"
    )


def ataque_rei_demonio(time, nome_heroi, heroi, rei_demonio, memorial):
    heroi["Vida"] -= rei_demonio["Dano por Ataque"]
    print(
        f"O Rei Demônio avançou com suas garras infernais e atingiu {nome_heroi}, causando "
        "25 pontos de dano!"
    )

    if heroi["Vida"] <= 0:
        morte_heroi(time, nome_heroi, memorial)


def morte_heroi(time, nome_heroi, memorial):
    del time[nome_heroi]
    memorial.append(nome_heroi)
    print(f"{nome_heroi} tombou diante do poder do Rei Demônio!")


main()
