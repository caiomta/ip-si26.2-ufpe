print("========================================")
print("GDA - HERO DISPATCH SYSTEM")
print("========================================")

HERO_ATTRIBUTE_STRUCTURE = (
    "Nome",
    "Força",
    "Resistência",
    "Velocidade",
    "Inteligência",
    "Experiência",
)

available_heroes = []
running = True
while running:
    hero = input()
    if hero == "FIM":
        running = False
    else:
        hero = hero.split(" - ")
        # converter os atributos para int
        for i in range(1, len(hero)):
            hero[i] = int(hero[i])  # type: ignore
        hero = tuple(hero)  # garantir imutabilidade do herói
        available_heroes.append(hero)

print("[ROBOT] Sistema de despacho iniciado.")
print(f"[ROBOT] {len(available_heroes)} heróis disponíveis.")

# para não recalcular as somas a cada iteração
available_heroes_and_incomplete_sum = []
for hero in available_heroes:
    hero_name = hero[0]
    attribute_values = hero[1:]
    available_heroes_and_incomplete_sum.append((hero_name, sum(attribute_values)))

n_threats = int(input())
for _ in range(n_threats):
    print("========================================")
    print("NOVA AMEAÇA DETECTADA")
    print("========================================")

    threat_name, difficulty_level, main_attribute = input().split(" - ")
    difficulty_level = int(difficulty_level)

    print(f"AMEAÇA: {threat_name}")
    print(f"NÍVEL DE DIFICULDADE: {difficulty_level}")
    print(f"PRIORIDADE: {main_attribute}")

    print("[ROBOT] Analisando heróis disponíveis...")

    m = HERO_ATTRIBUTE_STRUCTURE.index(main_attribute)  # índice do atributo principal
    n = len(available_heroes)

    available_heroes_ranking = []
    for i in range(n):
        main_attribute_value = available_heroes[i][m]
        hero_name, incomplete_attribute_values_sum = (
            available_heroes_and_incomplete_sum[i]
        )

        # no ranking, a estrutura de cada herói é (nome, soma com peso, valor do atributo principal, índice original)
        available_heroes_ranking.append(
            (
                hero_name,
                incomplete_attribute_values_sum + main_attribute_value,
                main_attribute_value,
                i,
            )
        )

    print("[ROBOT] Calculando compatibilidade...")

    swapped = True  # gambiarra
    for i in range(n):
        # gambiarra para não usar break e evitar as iterações internas
        if swapped:
            swapped = False
            # o ponteiro j cobre apenas a parte ainda não ordenada, pois a cada
            # iteração do laço externo, os últimos i elementos estão ordenados
            for j in range(n - i - 1):
                same_sum = (
                    available_heroes_ranking[j][1] == available_heroes_ranking[j + 1][1]
                )
                smaller_sum = (
                    available_heroes_ranking[j][1] < available_heroes_ranking[j + 1][1]
                )
                smaller_main_attribute = (
                    available_heroes_ranking[j][2] < available_heroes_ranking[j + 1][2]
                )

                if smaller_sum or same_sum and smaller_main_attribute:
                    # swap
                    available_heroes_ranking[j], available_heroes_ranking[j + 1] = (
                        available_heroes_ranking[j + 1],
                        available_heroes_ranking[j],
                    )
                    swapped = True

                # se ambos atributos do j-ésimo item forem iguais ou menores ao seguinte, não há alteração na lista, o que conserva a ordem de cadastro

    print("[ROBOT] Análise concluída.")

    print("========================================")
    print("RANKING DE HERÓIS")
    print("========================================")

    for i in range(n):
        print(
            f"{i + 1}. {available_heroes_ranking[i][0]} - {available_heroes_ranking[i][1]} pontos"
        )

    print("----------------------------------------")

    threat_level, dispatched_heroes_amount = (
        ("SIMPLES", 1)
        if 1 <= difficulty_level <= 30
        else ("MODERADA", 2)
        if 31 <= difficulty_level <= 70
        else ("CRÍTICA", 3)
    )

    print(f"[ROBOT] Ameaça {threat_level}.")
    print(f"[ROBOT] {dispatched_heroes_amount} herói(s) serão despachados.")

    dispatched_heroes_names = []

    if n < dispatched_heroes_amount:
        print("[ROBOT] ALERTA!")
        print(f"[ROBOT] São necessários {dispatched_heroes_amount} heróis,")
        print(f"[ROBOT] mas apenas {n} estão disponíveis.")
        print("[ROBOT] Despachando todos os heróis disponíveis.")

        for hero_name, _, _, hero_original_index in available_heroes_ranking:
            # adicionar à lista de envio
            dispatched_heroes_names.append(hero_name)
    else:
        print("[CECIL] Equipe selecionada para a missão.")

        for i in range(dispatched_heroes_amount):
            hero_name, _, _, hero_original_index = available_heroes_ranking[i]

            # adicionar à lista de envio
            dispatched_heroes_names.append(hero_name)

    print("EQUIPE DESPACHADA:")
    for hero in dispatched_heroes_names:
        print(f"> {hero}")
    print("========================================")
