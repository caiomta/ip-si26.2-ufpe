place = input()
clue = input()
suspect = input()
is_suspect_professor = not (suspect == "Jaobé" or suspect == "Jorge Arthur")
alibi = input()

print(
    "Um bom faro nunca falha! E o meu tá apontando pra uma covardia: sumiram TODOS os monitores! Eu passo o dia perseguindo o próprio rabo, mas juro que hoje acho eles mais rápido que isso!"
)

# de acordo com o lugar
if place == "Grad 5":
    print(
        "O laboratório mais movimentado do CIn... e nenhum sinal de monitor por aqui."
    )
elif place == "Kaonelle":
    print("Byte farejou cada mesa da Kaonelle em busca de pistas.")
elif place == "DA":
    print("A sala de convivência estava vazia. Até as bolinhas de ping pong sumiram.")
elif place == "Feirinha do CIn":
    print("No meio da Feirinha, muita gente, mas nenhum monitor à vista.")

# de acordo com a pista
if clue == "nota fiscal":
    if place == "Kaonelle":
        print(
            "A nota fiscal é de uma compra de 350 cãoxinhas. Alguém está planejando alimentar um exército — ou uma festa e tanto."
        )
    else:
        print("Uma nota fiscal misteriosa, mas as informações estão meio apagadas.")
elif clue == "boné":
    print("Um boné caído no chão. Alguém saiu correndo e esqueceu a cabeça descoberta.")
elif clue == "balão":
    print("Um balão murcho no chão... isso aqui cheira a comemoração.")
elif clue == "passagem para Catende":
    print("Uma passagem de ônibus para Catende. Alguém tem raízes por lá.")

# de acordo com o suspeito
if is_suspect_professor:
    if clue == "balão" or clue == "nota fiscal" and place == "Kaonelle":
        print(
            f"{suspect} alega o álibi: {alibi}. Diz estar ocupado com os preparativos de algo... mas não entrega do que se trata."
        )
    else:
        print(
            f"{suspect} alega o álibi: {alibi}. Diz só estar corrigindo provas atrasadas. Nada a ver com o caso."
        )
elif suspect == "Jaobé":
    if clue == "passagem para Catende":
        print(
            f"Diante da pista encontrada, Jaobé gagueja e alega o álibi: {alibi}. A coincidência é grande demais."
        )
    else:
        print(
            f"Jaobé alega o álibi: {alibi}. Sem essa pista específica, nada o liga ao caso."
        )
elif suspect == "Jorge Arthur":
    if clue == "boné":
        print(
            f"Jorge Arthur alega o álibi: {alibi}... mas, estranhamente, está sem boné pela primeira vez na vida. Algo não bate."
        )
    else:
        print(
            f"Jorge Arthur alega o álibi: {alibi}. Sem essa pista específica, nada o liga ao caso."
        )


# desfechos finais
if (
    is_suspect_professor
    and (clue == "balão" or clue == "nota fiscal" and place == "Kaonelle")
    and alibi == place
):
    print(
        "CASO ENCERRADO: Não houve crime algum! Os monitores, emocionados com a volta de Byte, prepararam uma festa surpresa, com direito a muita cãoxinha e bolinho de ração pra ele. O banquete foi ótimo... pelo menos pra quem é cachorro."
    )
elif (
    suspect == "Jaobé"
    and clue == "passagem para Catende"
    and alibi == place
    or suspect == "Jorge Arthur"
    and clue == "boné"
    and alibi == place
):
    print(
        "CASO ENCERRADO: Jaobé e Jorge Arthur, enfurecidos por não terem honra o suficiente para serem conselheiros, sequestraram todos os monitores e só os libertariam em troca dos cargos. Byte percebe que o álibi contado bate exatamente com o lugar onde a pista foi encontrada, o flagrante perfeito! Byte morde a canela dos dois e resgata a equipe. Os culpados levam um puxão de orelha e são exilados da monitoria."
    )
else:
    print(
        "CASO EM ABERTO: Byte se distraiu perseguindo um esquilo no meio do pátio e esqueceu completamente onde tinha parado a investigação. Sem solução dessa vez."
    )
