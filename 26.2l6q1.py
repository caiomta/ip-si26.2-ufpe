def main():
    pixies_val, elves_val = int(input()), int(input())
    pixies_prod, elves_prod = factorial(pixies_val), factorial(elves_val)

    if pixies_prod > elves_prod:
        print("Os duendes se superaram dessa vez.")
    elif pixies_prod < elves_prod:
        print("É, os elfos tiveram um resultado melhor.")
    else:
        print("Ué, houve um empate.")

    box_size = gcd(pixies_prod, elves_prod)

    if box_size > 10:
        print(
            "Caixas gigantes! O Papai Noel vai precisar de um guindaste para "
            "empacotar tudo."
        )
    else:
        print("Caixas compactas e organizadas perfeitamente.")

    stability_divisor = calculate_stability_divisor(
        pixies_prod, elves_prod, box_size
    )

    if stability_divisor > 50:
        print("Atenção: O divisor de estabilidade está altíssimo!")
    else:
        print("Divisor calculado com sucesso. A rampa está equilibrada.")

    print("Calculando a inclinação geométrica do canhão...")

    geometric_hypotenuse = calculate_geometric_hypotenuse(
        pixies_prod, elves_prod
    )

    if geometric_hypotenuse % stability_divisor != 0:
        print("Lançamento autorizado!")
    else:
        print("Lançamento não autorizado!")


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def calculate_stability_divisor(pixies_prod, elves_prod, box_size):
    return (pixies_prod + elves_prod) // 2 + box_size


def power(a, b):
    return 1 if b == 0 else a * power(a, b - 1)


def calculate_geometric_hypotenuse(a, b):
    return power(a, 2) + power(b, 2)


main()
