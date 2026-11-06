SPECIAL_CLUES = {
    "OSSO": (3, "🐶 O osso do Max! O Grinch esteve por aqui! (+3 pontos)"),
    "RADAR": (5, "🛷 O radar do trenó! Estamos na trilha certa! (+5 pontos)"),
    "REVIVER": (
        10,
        (
            "💚 Reviver o Natal... será que o Grinch está se arrependendo? "
            "(+10 pontos)"
        ),
    ),
    "ARARA": (
        -4,
        (
            "🦜 Era uma arara de brinquedo! O Grinch plantou uma pista falsa! "
            "(-4 pontos)"
        ),
    ),
    "SOS": (
        -2,
        (
            "📻 Era um pedido de socorro falso! O Grinch está nos desviando "
            "do caminho! (-2 pontos)"
        ),
    ),
}


def main():
    print(
        "🎄 Alerta na Vila dos Quem! O Grinch sumiu com os presentes! Vamos "
        "investigar as pistas!"
    )

    investigated = []
    valid = 0
    valid_specials = 0
    points = 0

    while True:
        word = input().upper()

        if word == "FIM":
            valid_percentage = (
                valid / len(investigated) * 100 if investigated else 0
            )

            print("📁 Parece que a investigação terminou!")
            print()
            print("Vamos à Análise Final! 📋")
            print()
            print(f"Pistas investigadas: {len(investigated)}")
            print(f"Palíndromos encontrados: {valid}")
            print(f"Aproveitamento: {valid_percentage:.1f}%")
            print(f"Pontos de Evidência: {points}")
            print()

            if not investigated:
                print(
                    "Sem pistas, sem caso! O Grinch está rindo lá do Monte "
                    "Crumpit... 😈"
                )
            elif valid == 0:
                print(
                    "Nenhuma pista válida! O Grinch fugiu levando até o "
                    "último enfeite! 💨"
                )
            elif valid_specials == 3:
                print(
                    "Caso encerrado! O coração do Grinch cresceu três "
                    "tamanhos e ele devolveu os presentes! 🎅💚"
                )
            elif valid_percentage >= 75:
                print(
                    "Estamos quase lá! O Grinch já está ouvindo os cantos de "
                    "Natal da Vila! 🎶"
                )
            elif valid_percentage >= 50:
                print(
                    "A trilha está esquentando! Mais um pouco e pegamos o "
                    "Grinch! 🔎"
                )
            else:
                print(
                    "Poucas pistas válidas... O Grinch está fazendo piada lá "
                    "do Monte Crumpit. 🏔️"
                )
            return

        print("🔎 Qual será a próxima pista?")

        if word not in investigated:
            investigated.append(word)
            if is_palyndrome(word):
                print(f"✅ Parece que a pista '{word}' é um palíndromo!")
                clue_points, message = SPECIAL_CLUES.get(word, (1, ""))

                if message:
                    print(message)

                valid += 1 if clue_points > 0 else 0
                valid_specials += 1 if clue_points > 1 else 0
                points += clue_points
            else:
                print(
                    f"❌ Poxa! Parece que a pista '{word}' não nos ajudou "
                    "muito..."
                )
        else:
            print("🚫 Pistas repetidas não vão nos ajudar em nada!")


def is_palyndrome(string):
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return is_palyndrome(string[1:-1])


main()
