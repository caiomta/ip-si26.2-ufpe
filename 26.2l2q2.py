rounds = int(input())
danger = 100

print("Os pinguins começaram sua fuga. Operação: sair de Mônaco vivos!")

r = 0
while r < rounds and danger > 0:
    action = input()

    if action == "CHANTEL DUBOUIS":
        print(
            "Parece que a Capitã Dubouis ganhou uma ajudinha extra na "
            "caçada... Como se ela precisasse."
        )

        support = input()

        if support == "helicóptero":
            print(
                "Pendurada em um helicóptero, Dubouis se aproxima cada vez "
                "mais dos fugitivos!"
            )
            danger += 15
        elif support == "rastrear":
            print(
                "Dubouis encontrou os rastros dos animais. Infelizmente, "
                "despistar essa mulher não estava no plano."
            )
            danger += 20
        elif support == "SCOOTER":
            print(
                "ELA PEGOU A LENDÁRIA SCOOTER! OS PINGUINS REALMENTE TÊM "
                "ALGUMA CHANCE?!"
            )
            danger += 35
        elif support == "Non, je ne regrette rien":
            print(
                "INACREDITÁVEL! A VOZ ANGELICAL DE DUBOIS REANIMOU TODA A "
                "EQUIPE! ISSO É PERMITIDO?!"
            )
            danger += 100
        else:
            print(
                "Um dos capangas encontrou uma pista dos animais. Pequena "
                "pista, enorme problema."
            )
            danger += 5
    elif action == "kowalski":
        print(
            "Kowalski teve uma ideia! Por algum milagre, ela realmente "
            "funcionou e atrasou a caçadora."
        )
        danger -= 30
    elif action == "capitão":
        print(
            "Após uma troca de golpes com Dubouis, o Capitão conseguiu atrasá"
            "-la. Liderança também envolve pancadaria."
        )
        danger -= 40
    elif action == "RICO":
        print(
            "Rico sacou uma bomba de procedência extremamente duvidosa e "
            "acertou em cheio! Clássico Rico."
        )
        danger -= 50
    else:
        print(
            "Parece que o Recruta vai tentar ajudar na fuga... Que os céus "
            "protejam essa operação."
        )
        was_private_successful = input() == "sucesso"

        if was_private_successful:
            print(
                "ELE CONSEGUIU! A fofura do Recruta distraiu os guardas de "
                "Dubouis. Uma arma verdadeiramente devastadora."
            )
            danger -= 15
        else:
            print(
                "Ele tentou... mas deixou um rastro enorme para os guardas. "
                "Pelo menos a intenção foi boa."
            )
            danger += 10

    r += 1

print(
    "Os pinguins não tiveram chance... A maior caçadora de animais de Mônaco "
    "é simplesmente IMPLACÁVEL!"
    if danger > 0
    else "ELES CONSEGUIRAM! Deixaram a grandiosa CHANTEL DUBOUIS para trás e "
    "seguiram rumo a Madagascar!"
)
