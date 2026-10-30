def main():
    print("SISTEMA DE CALIBRAGEM DA ÁRVORE QUÂNTICA DE NATAL")
    print("Oficina Central do Papai Noel - Setor de Engenharia Fractal v1.0\n")
    print("[INFO] Carregando protocolos de recursão dos duendes...")
    print("[INFO] Conectando ao gerador de auroras boreais...\n")

    n = int(input())

    print(f"[PROCESSANDO] Calculando as camadas fractais para o nível {n}...")
    print(
        "[AGUARDE] Desdobrando a pilha de recursão no núcleo do cristal...\n"
    )

    bf, ae = calc_bf_and_ae(n, {})
    ae = ae[0] / ae[1]
    bf = bf[0] / bf[1]

    print("[RELATÓRIO DE ENERGIA ACUMULADA]")
    print(
        f"A soma dos índices de energia do nível 0 até o nível {n} é "
        f"{ae:.4f}.\n"
    )

    if n == 0:
        print(
            "[AVISO DO DUENDE CHEFE]: Você acessou o Núcleo Primordial (Nível "
            "0)!"
        )
        print(
            "Este cristal não possui camadas externas, mas sua pureza de "
            f"{bf:.4f} é máxima.\n"
        )
    elif bf < 0.35:
        print(f"[STATUS DO CRISTAL]: Fator de Brilho = {bf:.4f}")
        print(
            "Resultado: Brilho Fraco! O cristal está absorvendo pouca energia."
        )
        print(
            "Dica do Papai Noel: Tente aumentar o nível da árvore para "
            "iluminar o Polo Norte!\n"
        )
    elif bf > 0.42:
        print(f"[STATUS DO CRISTAL]: Fator de Brilho = {bf:.4f}")
        print("Resultado: SUPERCARGA ENERGÉTICA DETECTADA!")
        print(
            "Cuidado! O cristal está gerando tanto brilho que pode fazer o "
            "trenó voar mais rápido do que o permitido!\n"
        )
    else:
        print(f"[STATUS DO CRISTAL]: Fator de Brilho = {bf:.4f}")
        print("Resultado: RESSONÂNCIA PERFEITA!")
        print(
            "Atenção, duendes! Este cristal está pronto para ir direto para o "
            "topo de nossa Árvore de Natal!\n"
        )

    print("Calibração encerrada com sucesso!")
    print("Que o seu código compile na primeira tentativa. Feliz Natal!")


def calc_bf_and_ae(
    n,
    memo,  # memo is a dictionary memoization for recursion optimization
):
    if n == 0:
        # the returned values are tuples of (numerator, denominator) for
        # increased accuracy
        return ((1, 1), (1, 1))
    if n == 1:
        return (1, 3), (4, 3)
    if n in memo:
        return memo[n]

    last_bf, last_ae = calc_bf_and_ae(n - 1, memo)
    second_to_last_bf, _ = calc_bf_and_ae(n - 2, memo)

    # bf = den(bf_{n-1}) / 2 * den(bf_{n-1}) + den(bf_{n-2})
    bf = (last_bf[1], (2 * last_bf[1] + second_to_last_bf[1]))

    # ae = sum(bf_{0..n})
    ae = sum_fraction_tuples(bf, last_ae)

    memo[n] = (bf, ae)
    return memo[n]


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return 0 if not (a and b) else abs(a * b) // gcd(a, b)


def sum_fraction_tuples(a, b):
    d = lcm(a[1], b[1])
    n = a[0] * d // a[1] + b[0] * d // b[1]
    return (n, d)


main()
