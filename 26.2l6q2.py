def main():
    pascals_triangle = {}

    n_sectors = int(input())
    min_possibilities = int(input())
    possibilities_per_sector = [
        newtons_binomial(int(input()), int(input()), pascals_triangle)
        for _ in range(n_sectors)
    ]

    print("Relatório dos escudos de Norte:")

    approved = 0
    for index, possibilities in enumerate(possibilities_per_sector):
        if possibilities >= min_possibilities:
            print(
                f"Setor {index + 1}: {possibilities} possibilidade(s). "
                "Variedade suficiente!"
            )
            approved += 1
        else:
            print(
                f"Setor {index + 1}: {possibilities} possibilidade(s). "
                "Precisa de mais alternativas!"
            )

    print(f"Setores que atingiram a meta: {approved} de {n_sectors}.")

    if approved == n_sectors:
        print("Tudo pronto! O planejamento dos escudos foi aprovado!")
    else:
        print("Norte precisa revisar o planejamento!")


# com memoization, este algoritmo passa a ser O(n*k)
def newtons_binomial(n, k, pascals_triangle):
    # simetria
    if k > n / 2:
        k = n - k

    if k == 0:
        return 1
    if k == 1:
        return n
    if (n, k) in pascals_triangle:  # memoization
        return pascals_triangle[n, k]

    value = newtons_binomial(
        n - 1,
        k - 1,
        pascals_triangle,
    ) + newtons_binomial(
        n - 1,
        k,
        pascals_triangle,
    )

    pascals_triangle[n, k] = value  # memoization
    return value


main()
