danger_level = 0
time_passed_minutes = 0
died = False
got_egg = False
battled_troia = False

print("Byte: Au! Vou conseguir esse ovo!!")

# --- FASE 1 ---
phase1_events = input()
time_passed_minutes += len(phase1_events) * 5

found_iron = "ferro" in phase1_events.lower()
found_gold = False
found_beds = False
found_nether_portal = False

if phase1_events.isupper():
    danger_level += 30
else:
    danger_level += 10

if "monstros" in phase1_events.lower():
    print("Você não pode dormir agora, há monstros por perto.")
    danger_level += 25
    time_passed_minutes += 20
    if "4" in phase1_events:
        print("Byte desbloqueou a conquista: [Caçador de Monstros]")
        danger_level *= 2

if found_iron:
    print("Byte desbloqueou a conquista: [A Idade do Ferro]")
    danger_level -= 15
    danger_level = max(0, danger_level)  # normaliza
    time_passed_minutes += 5

if "diamante" in phase1_events.lower():
    if found_iron:
        print("Byte desbloqueou a conquista: [Diamantes!]")
        danger_level -= 40
        danger_level = max(0, danger_level)  # normaliza
    else:
        time_passed_minutes += 15

if "ouro" in phase1_events.lower():
    if found_iron:
        found_gold = True
        time_passed_minutes += 10
    else:
        time_passed_minutes += 5

if "estrutura" in phase1_events.lower():
    structure = input()
    if "vila" in structure.lower():
        print("Byte desbloqueou a conquista: [Negócio Fechado!]")
        found_beds = True
        time_passed_minutes += 10
    if "portal" in structure.lower():
        found_nether_portal = True
    if "templo" in structure.lower():
        danger_level += 100
    if "mansao" in structure.lower():
        if danger_level > 100:
            print("Byte desbloqueou a conquista: [À beira da Morte]")
        danger_level -= 150
        danger_level = max(0, danger_level)  # normaliza
        time_passed_minutes += 40
    if "camara" in structure.lower():
        print("Byte desbloqueou a conquista: [Minecraft: Jogos Vorazes]")
        danger_level += 50
        time_passed_minutes += 60

if danger_level > 100:
    died = True
else:
    print(
        f"Byte: Ufa, finalmente acabei, demorei apenas {time_passed_minutes} minutos, vamos ao Nether!"
    )

    # --- FASE 2 ---
    if not found_nether_portal:
        print("Byte desbloqueou a conquista: [Entrando numa fria]")
        time_passed_minutes += 5

    print("Byte desbloqueou a conquista: [O buraco é mais embaixo]")
    danger_level += 30

    n1 = float(input())
    n2 = float(input())

    # se a soma não for inteira...
    if n1 + n2 != int(n1 + n2):
        if found_gold:
            print("Byte desbloqueou a conquista: [Meu precioso!]")
            danger_level += 10
        else:
            danger_level += 20
            time_passed_minutes += 30

    blaze_result = input()
    is_blaze_result_numeric = blaze_result.isnumeric()

    if is_blaze_result_numeric and int(blaze_result) > 12:
        time_passed_minutes += 10
    elif is_blaze_result_numeric and int(blaze_result) > 0:
        time_passed_minutes += 20
    else:
        time_passed_minutes += 30
        danger_level += 40

    if danger_level > 100:
        died = True
    else:
        # --- FASE 3 ---
        danger_level -= 20
        danger_level = max(0, danger_level)  # normaliza

        stronghold_x = float(input())
        stronghold_z = float(input())

        distance_to_stronghold = int(
            ((100 - stronghold_x) ** 2 + (200 - stronghold_z) ** 2) ** 0.5
        )
        print(f"Byte: Estou a {distance_to_stronghold} blocos da Stronghold!")
        time_passed_minutes += distance_to_stronghold * 2

        danger_level += 30

        if time_passed_minutes >= 300:
            print("Troia desbloqueou a conquista: [Liberte o End]")
            print("Byte desbloqueou a conquista: [É o fim?]")
            battled_troia = True
        elif found_beds:
            print("Byte desbloqueou a conquista: [É o fim?]")
            print("Byte: Como eu amo o [Design Intencional do Jogo]!")
            # como as camas mataram o dragão, não há conquista
            got_egg = True
            danger_level -= 30
            danger_level = max(0, danger_level)  # normaliza
        elif 180 < time_passed_minutes < 300:
            print("Troia desbloqueou a conquista: [É o fim?]")
            print("Byte desbloqueou a conquista: [É o fim?]")

            battled_troia = True
            danger_level += 10

            arrows = int(input())
            targets = int(input())

            if arrows == 1 and targets == 1:
                print("Byte: Uma flecha, Uma chance.")
            elif targets == 1:
                print(
                    "Byte: Troia já destruiu todos os cristais, agora é só o Dragão..."
                )

            # se a divisão for inteira e maior que zero...
            if arrows / targets == arrows // targets and arrows // targets > 0:
                print("Byte desbloqueou a conquista: [Liberte o End]")
                got_egg = True
                time_passed_minutes += 10
            else:
                print("Byte: Droga! Não tenha flechas suficientes, Troia vai ganhar...")
                time_passed_minutes += 20
        else:
            print("Byte desbloqueou a conquista: [É o fim?]")
            print("Byte desbloqueou a conquista: [Liberte o End]")
            got_egg = True
            time_passed_minutes += 5

        if danger_level > 100:
            got_egg = False
            died = True

# OUTPUT FINAL
if got_egg:
    print("Byte desbloqueou a conquista: [A nova geração]")
    print("Byte: Aauauau! O ovo é meu! que rolem os créditos!")

if died:
    print("Byte foi morto.")

if not got_egg:
    print("Byte: auu.... Não consegui pegar o ovo...")

# RELATÓRIO
danger_level_message = ""

if danger_level == 100 or battled_troia:
    danger_level_message = "Odisseia de Byte."
elif danger_level < 30:
    danger_level_message = "Passeio no Parque."
elif danger_level < 70:
    danger_level_message = "Jornada Complicada."
elif danger_level < 100:
    danger_level_message = "Aventura Perigosa."
elif danger_level > 100:
    danger_level_message = "Letal."

time_taken_hours = int(time_passed_minutes // 60)
time_taken_minutes = int(time_passed_minutes % 60)

print()
print(f"🚨Avaliação de nível de perigo: {danger_level_message}")
print()
print(f"Timer: {time_taken_hours} h e {time_taken_minutes} minutos")
