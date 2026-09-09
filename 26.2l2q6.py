print("=== WABAC: SISTEMA DE EMERGÊNCIA ===")
print("Alvo: Ano 2026 | Peças Necessárias: 3")
print("Sherman, mantenha as mãos longe dos botões! Iniciando saltos...")

origin_year = int(input())
prohibited_year = int(input())
energy = int(input())

current_year = origin_year
temporal_tear = 0
pieces = 0
has_jumped = False
interrupt = False
abort = False

while not interrupt:
    jump = fix = history_class = False
    manages_to_find_piece = False

    action = input()

    if action == "SALTAR":
        jump = True
        has_jumped = True
        current_year += int(input())
        energy -= int(input())
        temporal_tear += 10
    elif action == "CONSERTAR":
        fix = True
        difficulty = int(input())
        effort = int(input())

        if difficulty <= effort:
            pieces += 1
            energy -= 10
            manages_to_find_piece = True
        else:
            energy -= 15
            temporal_tear += 20
    elif action == "AULA DE HISTÓRIA":
        history_class = True
        energy += 25
        temporal_tear += 15
    elif action == "ABORTAR":
        abort = True

    # normalização
    energy = max(energy, 0)
    temporal_tear = min(temporal_tear, 100)

    # casos de interrupção
    if (current_year == prohibited_year or current_year == origin_year) and has_jumped:
        interrupt = True

        print(
            f"ALERTA CRÍTICO: Peabody encontrou sua própria versão no ano {current_year}!"
        )
        print("O continuum espaço-tempo ruiu em uma espiral paradoxal.")
    elif energy == 0:
        interrupt = True

        print("A WABAC desligou completamente por falta de energia.")
        print("Peabody e Sherman estão vagando sem rumo pela linha do tempo...")
    elif temporal_tear == 100:
        interrupt = True

        print("O rasgo temporal atingiu massa crítica!")
        print(
            "O universo foi engolido por um buraco negro sobre a cidade de Nova York."
        )
    elif abort:
        interrupt = True

        print("Mr. Peabody acionou o protocolo de parada manual.")
        print("A viagem foi cancelada antes de sua conclusão.")
    elif pieces >= 3 and current_year >= 2026:
        interrupt = True

        print(
            f"A WABAC emergiu com sucesso no ano de {current_year}! Com as 3 peças coletadas, Mr. Peabody selou o rasgo temporal e salvou o presente!"
        )

    if not interrupt:
        if jump:
            print(f"WABAC saltou para o ano {current_year}!")
            print(f"Energia restante: {energy} | Rasgo Temporal: {temporal_tear}%")
        elif fix and manages_to_find_piece:
            print('Sherman: "Consegui, Mr. Peabody! Encontrei uma peça de calibragem!"')
            print(f"Peças coletadas: {pieces}/3 | Energia: {energy}")
        elif fix:
            print(
                'Mr. Peabody: "Tenha mais cuidado, Sherman! Essa falha desestabilizou o tempo!"'
            )
            print(f"Energia: {energy} | Rasgo Temporal: {temporal_tear}%")
        elif history_class:
            print(
                'Mr. Peabody: "Como disse Galileu Galilei, a matemática é a linguagem com a qual Deus escreveu o universo."'
            )
            print(f"Energia recarregada para {energy}!")
