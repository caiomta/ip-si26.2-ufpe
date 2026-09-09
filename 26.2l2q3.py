print(
    "Shrek achava que morar em um pântano afastado seria suficiente para "
    "manter as pessoas longe. Ele estava muito enganado."
)

shreks_patience = int(input())

nobody = False
total_visitors = 0

while shreks_patience > 0 and not nobody:
    visitor = input()
    donkey = visitor == "Burro"
    nobody = visitor == "ninguém"
    patience_spent = 0 if nobody else int(input())

    if donkey:
        subject = input()
        patience_spent /= 2 if subject == "sanduíche" else 1

    if nobody:
        print("Ufa! Ninguém apareceu. Finalmente, um pouco de paz no pântano!")
    elif shreks_patience >= patience_spent:
        total_visitors += 1

        if donkey:
            print("Burro?! Eu acabei de pedir um pouco de paz!")
            if subject == "sanduíche":
                print("Ah, isso sim é um bom assunto!")
            elif subject == "Fiona":
                print("É o Burro! E, como sempre, ele só sabe falar da Fiona.")
            elif subject == "pântano":
                print("Burro, isso é MEU pântano...")
        elif visitor == "Gato de Botas":
            print("O Gato de Botas chegou! Shrek já está de olho nas suas botas.")
        elif visitor == "Pinóquio":
            print("Pinóquio chegou! Shrek espera que ele não esteja mentindo.")
        elif visitor == "Lobo Mau":
            print("Lobo Mau?! Shrek abriu a porta, mas já está se arrependendo!")
        else:
            print(
                "Visitante desconhecido! Shrek não sabe quem você é, mas pode "
                "entrar por sua conta em risco."
            )
    shreks_patience -= patience_spent

if shreks_patience <= 0:
    print("A paciência do Shrek acabou! Dê meia-volta antes que ele perca o controle!")

print(
    f"Ao todo, {total_visitors} visitantes passaram pelo pântano. Shrek "
    "sobreviveu a mais um dia!"
)
