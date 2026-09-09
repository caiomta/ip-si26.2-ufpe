santas_health = 100
breus_damage = 15

present_streak = 0
coal_streak = 0

total_presents = 0
total_coal = 0

global_logistic_cost = 0

outer_running = True
while outer_running:
    local_logistic_cost = 0
    is_sled_overloaded = False
    base_cost_per_child = 10

    place = input()

    if place == "FIM":
        outer_running = False
    else:
        continent = input()
        continent_rate = (
            5
            if continent == "Ásia"
            else 4
            if continent == "África"
            else 3
            if continent == "América"
            else 2
            if continent == "Oceania"
            else 1
        )

        country = input()
        country_rate = (
            1.3
            if country == "Rússia"
            else 1.25
            if country == "Canadá"
            else 1.2
            if country == "China"
            else 1.15
            if country == "EUA"
            else 1.1
            if country == "Brasil"
            else 1
        )

        inner_running = True
        while inner_running:
            childs_name_or_event = input()

            if childs_name_or_event == "FIM_LOCAL":
                print(
                    f"Localidade {place} finalizada. Custo logístico: {local_logistic_cost:.2f}"
                )

                global_logistic_cost += local_logistic_cost
                inner_running = False
            elif childs_name_or_event == "Breu":
                # emboscada
                print("Alerta! Breu atacou a entrega!")

                breus_health = 50
                santas_round = input() == "Noel"

                while breus_health > 0 and santas_health > 0:
                    input()  # ataque

                    if santas_round:
                        breus_health -= 20
                    else:
                        santas_health -= breus_damage

                    santas_round = not santas_round

                if santas_health <= 0:
                    outer_running = inner_running = False
                else:
                    print("Noel repeliu a emboscada e as entregas continuam!")
            else:
                # entrega
                behaviour_rate = 0
                valid_behaviour_rate = False
                while not valid_behaviour_rate:
                    behaviour_rate = int(input())

                    if 0 <= behaviour_rate <= 100:
                        valid_behaviour_rate = True
                    else:
                        print("Pontuação inválida, insira novamente.")

                if behaviour_rate >= 70:
                    # presente
                    print(
                        f"{childs_name_or_event} foi uma boa criança este ano e receberá um presente!"
                    )

                    present_streak += 1
                    total_presents += 1
                    coal_streak = 0

                    if present_streak == 3:
                        print(
                            "A fé das crianças fortalece a magia! Noel recuperou 10 de HP."
                        )

                        santas_health += 10
                        present_streak = 0

                        santas_health = min(santas_health, 100)  # normalizar HP
                else:
                    # carvão
                    print(
                        f"{childs_name_or_event} não se comportou bem e receberá carvão."
                    )

                    coal_streak += 1
                    total_coal += 1
                    present_streak = 0

                    if coal_streak == 3:
                        breus_damage += 5
                        coal_streak = 0

                        print(
                            f"O medo e a descrença alimentam as sombras... O dano de Breu aumentou para {breus_damage}!"
                        )

                local_logistic_cost += (
                    base_cost_per_child * country_rate * continent_rate
                )

                if not is_sled_overloaded and local_logistic_cost > 100:
                    print(
                        "O trenó está sobrecarregado pela magia! Custos base aumentados."
                    )

                    base_cost_per_child = 15
                    is_sled_overloaded = True

if santas_health > 0:
    print(
        f"Noite concluída com sucesso! Presentes: {total_presents} | Carvão: {total_coal}"
    )
    print(f"Custo logístico total: {global_logistic_cost:.2f}")
    print(f"HP final do Noel: {santas_health}")
else:
    print(
        "O HP de Noel chegou a zero! O Breu venceu a batalha... O Natal das crianças foi arruinado."
    )
