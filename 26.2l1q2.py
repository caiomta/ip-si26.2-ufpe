preparing_level = 0

byte_energy = int(input())
snack_amount = int(input())
water_bottle_amount = int(input())
collar_battery_level = int(input())
is_gps_on = input() == "sim"
has_ball = input() == "sim"
is_rainy = input() == "sim"
temperature = int(input())
signal_strength = int(input())

print("Byte recebeu um novo chamado! Preparando-se para a aventura...")

if byte_energy >= 70:
    print("Byte está cheio de energia!")
    preparing_level += 2
elif byte_energy < 30:
    print("Byte está muito cansado... A missão ficou mais difícil.")
    preparing_level -= 2

if snack_amount >= 2 and water_bottle_amount >= 1:
    print("Suprimentos preparados!")
    preparing_level += 2

if collar_battery_level >= 50 and is_gps_on:
    print("Coleira tecnológica preparada!")
    preparing_level += 2
elif collar_battery_level <= 20:
    print("A bateria da coleira está crítica! Isso pode atrapalhar a missão.")
    preparing_level -= 1

if has_ball or snack_amount >= 4:
    print("Byte está ainda mais animado para a aventura!")
    preparing_level += 1

if is_rainy or temperature > 32:
    print("O clima não está ajudando... Isso vai dificultar a missão.")
    preparing_level -= 2

if signal_strength >= 70:
    print("O sinal está forte! Há algo estranho por perto...")
    preparing_level += 1

print()
print(f"Nível de preparo: {preparing_level}")

if preparing_level >= 5:
    print("Byte está pronto! A nova aventura começa agora!")
else:
    print("Byte ainda não está pronto. Melhor se preparar um pouco mais!")
