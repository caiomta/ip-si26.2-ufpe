base_reactors = (
    "Metilamina",
    "Fenilacetona",
    "Hidróxido de Sódio",
    "Ácido Clorídrico",
    "Metilamina",
)
base_reactors_volumes = (500, 250, 150, 100, 300)

print("Sistema HeisenbergOS v2.0 - Monitor do Reator Inicializado...\n")

operator = input()

tank_pressure = input()

if tank_pressure.isnumeric():
    tank_pressure = int(tank_pressure)

    if operator == "Hank Schrader" or operator == "Gomez":
        print("Alerta Vermelho: Agente do DEA detectado no laboratório!")

    mike_status = input()
    if mike_status.isupper():
        print("Abaixe o tom de voz! Mike está escutando no microfone!")

    running = True
    while running:
        action = input()

        if action == "FIM":
            running = False
        elif action == "contar":
            target_ingredient = input()
            appearances = base_reactors.count(target_ingredient)

            if appearances:
                print(
                    f"O ingrediente {target_ingredient} aparece {appearances} vez(es) na receita base."
                )
            else:
                print(
                    f"O Ingrediente {target_ingredient} não foi encontrado, precisamos melhorar o nosso estoque!"
                )
        elif action == "posicao":
            target_ingredient = input()

            if target_ingredient in base_reactors:
                print(
                    f"O ingrediente {target_ingredient} foi encontrado primeiro na posicao {base_reactors.index(target_ingredient)} da tupla."
                )
            else:
                print(
                    f"Ingrediente {target_ingredient} nao encontrado no registro fixo!"
                )
        elif action == "varrer":
            target_ingredient = input()

            total_volume = 0
            for i in range(len(base_reactors)):
                if base_reactors[i] == target_ingredient:
                    print(
                        f"Lote encontrado: {target_ingredient} - {base_reactors_volumes[i]}ml"
                    )
                    total_volume += base_reactors_volumes[i]

            print(f"Volume total de {target_ingredient} no reator: {total_volume}ml")
        elif action == "concatenar":
            new_reactor = input()
            new_reactor_volume = int(input())

            base_reactors += (new_reactor,)
            base_reactors_volumes += (new_reactor_volume,)

            print(
                f"Ingrediente adicionado à nova tupla! Tamanho atualizado: {len(base_reactors)}"
            )
        elif action == "desempacotar":
            print(
                f"Últimos 3 reativos do registro: {base_reactors[-3]} "
                f"({base_reactors_volumes[-3]}ml), {base_reactors[-2]} "
                f"({base_reactors_volumes[-2]}ml) e {base_reactors[-1]} "
                f"({base_reactors_volumes[-1]}ml)."
            )

    if tank_pressure >= 50 and mike_status.lower() == "tranquilo":
        print("Reação perfeita! Lote de 99.1% de pureza pronto para distribuição.")
    elif tank_pressure < 15:
        print("Pressão crítica muito baixa! A mistura estragou, descarte o lote!")
    elif mike_status.lower() == "alerta" and len(base_reactors) > 5:
        print(
            "A receita ficou muito complexa para o tempo hábil! Limpe o reator antes que Mike chegue!"
        )
    else:
        print("Ajustando exaustores... Mantenha o reator sob observação!")
else:
    print(
        "Yo Jesse! Você colocou tempero onde devia ter um número de pressão! O reator pifou!"
    )
