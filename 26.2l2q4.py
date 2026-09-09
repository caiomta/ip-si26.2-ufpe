rounds = int(input())
record = int(input())

print("Tigresa: Duvido você bater o recorde, Po!")
print("Po: Prepare-se para ver o Dragão Guerreiro em ação!")

total_eaten = 0
eaten_this_round = 0
record_beaten = False
record_beaten_during_single_round = False

r = 0
while r < rounds and not record_beaten:
    eaten_this_round = 0
    trays = int(input())

    t = 0
    while t < trays and not record_beaten_during_single_round:
        rice_balls_on_tray = int(input())
        eaten_this_round += rice_balls_on_tray
        record_beaten_during_single_round = eaten_this_round > record
        t += 1

    total_eaten += eaten_this_round
    record_beaten = total_eaten > record

    r += 1
    if record_beaten_during_single_round:
        print("\nTigresa: Mas como?!")
        print("Po: UHUL! CONHEÇA A FORÇA DO DRAGÂO GUERREIRO!!")
    elif eaten_this_round >= 10:
        print("\nPo: Delícia! Mais uma rodada finalizada!")
    else:
        print("\nPo: Ainda tenho espaço para mais!")

    print(f"Rodada {r}: Po comeu {eaten_this_round} bolinhos.")


if record_beaten_during_single_round:
    print("\nPo: Ei! Eu ainda não terminei!")
    print("Tigresa: Acho que não vou mais subestimar sua fome.")
    print(
        f"Que loucura! Po venceu a aposta comendo um total de {eaten_this_round} "
        "bolinhos em uma só rodada!"
    )
elif record_beaten:
    print("\nPo: Eu sabia que conseguiria! O recorde e meu!")
    print("Tigresa: Inacreditável... Você realmente venceu a aposta.")
    print(
        f"Po venceu a aposta! Ele comeu um total de {total_eaten} bolinhos e "
        f"superou o recorde de {record}!"
    )
elif total_eaten == record:
    print("\nPo: Empatamos! Cheguei exatamente no recorde!")
    print(
        "Tigresa: Impressionante, mas empatar não basta para vencer a aposta. "
        "Venha lavar a louça!"
    )
    print(
        f"Houve um empate! Po comeu exatamente {total_eaten} bolinhos e "
        f"igualou o recorde de {record}."
    )
else:
    print("\nTigresa: Eu avisei, Po! A louça do palácio te espera.")
    print("Po: Ah não... Minhas mãos vão ficar enrugadas...")
    print(
        f"Tigresa venceu a aposta! Po comeu apenas {total_eaten} bolinhos e "
        f"não alcançou o recorde de {record}."
    )
