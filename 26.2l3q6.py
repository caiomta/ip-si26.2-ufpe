rows = int(input())
columns = int(input())

if rows > 0 and columns > 0:
    print("Avatar: A Lenda de Aang - Planejamento da Invasão!")
    print("Sokka: Mapeando os setores da Nação do Fogo...")

    matrix = []
    even_values = 0
    odd_values = 0

    total_resistance = 0
    most_critical_sector_coordinate = (-1, -1)
    most_critical_sector_value = -1

    for i in range(rows):
        row = []
        for j in range(columns):
            value = int(input())
            value *= 2 if i == j else 1
            value += 5 if rows == columns and i + j == rows - 1 else 0
            value = 0 if value < 15 else value

            if value % 2:
                odd_values += 1
                value += 1
            else:
                even_values += 1

            row.append(value)

            total_resistance += value

            if most_critical_sector_value < value:
                most_critical_sector_coordinate = (i, j)
                most_critical_sector_value = value
        matrix.append(row)

    for row in matrix:
        for j in range(columns):
            print(row[j], end=("\n" if j == columns - 1 else " "))

    print("--- RELATÓRIO DO TÚNEL E AMEAÇAS ---")
    print(f"Soma Total de Resistência: {total_resistance}")
    print(
        f"Setor Mais Crítico: {most_critical_sector_coordinate} com valor {most_critical_sector_value}"
    )

    if total_resistance < 100:
        print("Sokka: O mapa revela poucas defesas inimigas!")
        print("Aang: Parece que o caminho está livre.")
        print("Katara: Conseguimos passar sem grandes problemas!")
        print("Estratégia aprovada! O Avatar está pronto para a batalha.")
    elif total_resistance < 200:
        print("Sokka: Atenção! Detectamos resistência nas defesas da Nação do Fogo.")
        print("Toph: Sinto muitas tropas pelo solo, mas podemos avançar com cuidado.")
        print("Aang: Então vamos atentos. A Equipe Avatar está pronta!")
        print("Estratégia aprovada, mas a invasão será realizada com cautela.")
    else:
        print("Sokka: Alerta! As defesas inimigas são muito fortes!")
        print("Toph: A linha de defesa deles é densa demais para atravessarmos.")
        print("Aang: Então precisamos recuar e repensar nosso plano.")
        print("Alerta vermelho: Nível de ameaça crítico! Invasão adiada.")

    ally = input()
    energy_limit = int(input())

    if ally == "Aang":
        success = total_resistance < energy_limit
    elif ally == "Katara":
        success = even_values > odd_values
    elif ally == "Toph":
        success = most_critical_sector_value <= 50
    elif ally == "Sokka":
        success = rows == columns

    if success:  # type: ignore
        print(
            f"{ally} usou sua especialidade com maestria e garantiu o sucesso na missão!"
        )
    else:
        print(
            f"{ally} encontrou barreiras intransponíveis e a missão precisou ser abortada..."
        )
else:
    print("Dimensões do mapa inválidas!")
