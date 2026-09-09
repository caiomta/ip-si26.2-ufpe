destination = input()  # apenas Tsinghua e Shenzhen | TODO: validar
charisma_level = int(input())
interest_for_football_level = int(input())
interest_for_table_tennis_level = int(input())

if destination == "Tsinghua":
    if charisma_level >= 90:
        if interest_for_football_level > interest_for_table_tennis_level:
            print(
                "Todos os torcedores do Santa Cruz passam a ter acesso ao intercâmbio para a Tsinghua University."
            )
        else:
            print(
                "Os chineses gostam do Santa Cruz, mas preferem tênis de mesa e solicitam a criação do Santa Cruz Tênis de Mesa China."
            )
    else:
        print(
            "Byte consegue fazer amigos na universidade, mas a paixão pelo Santa Cruz fica para a próxima."
        )
elif destination == "Shenzhen":
    if interest_for_football_level >= 80:
        if charisma_level == 100:
            print("Todos os chineses passam a torcer para o Santa Cruz.")
        else:
            print(
                "O Santa Cruz ganha um patrocínio de uma gigante de tecnologia de Shenzhen!"
            )
    else:
        print(
            "Byte falha em converter os chineses ao Santa Cruz, mas aproveita a viagem visitando Shenzhen."
        )
else:
    print("Passaporte invalido. Byte deve retornar a Recife.")
