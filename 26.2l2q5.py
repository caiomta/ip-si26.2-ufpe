print("Quando percebi que contara oito mortes, senti o peso da minha própria lenda")

deaths_attacks = int(input())
got_to_end = False
courage = False

if not deaths_attacks:
    print(
        "Até logo, velho amigo... É bom saber que finalmente posso respirar "
        "fundo e apenas viver o dia de hoje."
    )

a = 0
while a < deaths_attacks and not got_to_end:
    print(
        "Preciso encontrar esse mapa a qualquer custo, nem que seja a última "
        "coisa que eu faça com esta vida!"
    )

    partner = input()

    if partner == "cao perrito":
        print(
            "Olha só... de todas as criaturas do mundo, justo você tinha que "
            "decidir me seguir com esse rabo abanando?"
        )

        n = int(input())

        all_divisible_by_3 = True
        for m in range(n):
            number = int(input())
            all_divisible_by_3 = False if number % 3 else all_divisible_by_3

        if all_divisible_by_3:
            print(
                "Bom trabalho, meu garoto! Quem diria que um cãozinho tão "
                "pequeno seria o grande herói do dia?"
            )

            got_to_end = True
    elif partner == "kitty patamansa":
        print(
            "Kitty... Olhar para você de novo só me faz lembrar que, entre "
            "todas as minhas nove vidas, o meu maior erro foi ter deixado você "
            "esperando."
        )

        item = input()
        # got_to_end = item == "chapeu do gato" or item == "bota do gato"
        if item == "chapeu do gato" or item == "bota do gato":
            print(
                "Impressionante, Kitty... Sempre soube que você era rápida, "
                "mas admito que nada fica melhor nas mãos da melhor ladra de "
                "Tão Tão Distante do que um presente para mim."
            )

            got_to_end = True
    else:
        found_death = False
        while not got_to_end and not found_death:
            phrase = input()
            if "Desfecho" in phrase:
                got_to_end = True
            elif "Morte" in phrase:
                found_death = True

    a += 1


if got_to_end:
    print(
        "Parece que essa família de ursos e sua cachinhos acabam de provar do "
        "verdadeiro felino de botas!"
    )

    courage = "coragem" in input().lower()

    if courage:
        print(
            "A verdadeira vitória não está em vencer a morte, mas em encará"
            "-la de frente e escolher lutar por cada segundo desta vida!"
        )

if deaths_attacks and not (got_to_end and courage):
    print(
        "Pode levar minha espada e meu chapéu... Eu lutei até o fim, mas hoje "
        "a lenda finalmente descansa."
    )
