n = int(input())

opportunities = ""
not_reps = 0
reps = 0

for i in range(n):
    current_opportunity = input()

    if current_opportunity in opportunities:
        reps += 1
    else:
        not_reps += 1
        opportunities += f" - {current_opportunity}" if i else current_opportunity

print("Parabéns formandos! E agora iniciaremos sua carreira nas indústrias Honex.")
print(opportunities)
print(f"Quantidade de cargos repetidos: {reps}")
print(
    "Pelo menos Barry tem opções!"
    if not_reps > reps
    else "Mais do mesmo. Barry será apenas uma engrenagem na máquina de mel."
)
