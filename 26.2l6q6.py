def main():
    print(
        "🎄 O Natal chegou na Cozinha! Vamos preparar um Biscoito digno do "
        "Papai Noel!"
    )

    m = get_biscuit_matrix()
    decorations = get_decoration_matrix(len(m))
    apply_decorations(m, decorations)
    m = convert_matrix_to_tuple(m)  # the memo dictionary needs a hashable type
    deliciousness = laplace_determinant(m, memo={})

    print("Vamos a Análise Final!")
    print(f"\nGostosura: {deliciousness}")

    if deliciousness < 0:
        print("Nem o Grinch teria Coragem de provar esse Biscoito!")
    elif deliciousness == 0:
        if is_there_decorations(decorations):
            print("Tanta Decoração para nada! A Magia do Biscoito se Anulou.")
        else:
            print("A Magia do Biscoito se Anulou.")
    else:
        decoration_count = count_decorations(decorations)
        if 0 not in decoration_count.values():
            print(
                "Um Pedaço de cada Encanto Natalino! Esse vai para o Papai "
                "Noel! 🎅"
            )
        elif decoration_count["F"] > sum(
            v for k, v in decoration_count.items() if k != "F"
        ):
            print(
                "Gostoso e Congelante! Sirva com uma Caneca de Chocolate "
                "Quente! ❄️"
            )
        elif decoration_count["A"] and not decoration_count["F"]:
            print("Uma Floresta de gostosura! As Renas vão Adorar! 🎄")
        else:
            print(
                "Receita Aprovada! Já pode colocar ao lado do Copo de Leite! "
                "🥛"
            )


def get_biscuit_size():
    while True:
        rows, columns = [int(i) for i in input().split()]
        if rows > 0 and rows == columns:
            return rows
        print(
            "Esse Biscoito não cabe na Receita! Precisamos de um Quadrado com "
            "dimensões positivas!"
        )


def get_biscuit_matrix():
    size = get_biscuit_size()
    print("🍪 Hora de preparar a Massa! Qual a Gostosura de cada pedaço?")
    return [[int(x) for x in input().split()] for _ in range(size)]


def get_decoration_matrix(size):
    print(
        "Vamos dar um toque de Magia! Onde colocaremos os Enfeites Natalinos?"
    )
    return [input().split() for _ in range(size)]


def apply_decorations(m, decorations):
    size = len(m)
    for i in range(size):
        for j in range(size):
            if decorations[i][j] == "E":
                m[i][j] *= 2
            elif decorations[i][j] == "F":
                m[i][j] *= -1
            elif decorations[i][j] == "P":
                m[i][j] += 5
            elif decorations[i][j] == "A":
                m[i][j] **= 2


def convert_matrix_to_tuple(m):
    return tuple(tuple(row) for row in m)


def laplace_determinant(m, memo):
    size = len(m)
    if size == 1:
        return m[0][0]

    if m not in memo:
        r = det = 0
        for c in range(size):
            if m[r][c] != 0:
                # the auxiliary matrix is the original one without the
                # `r` row and `c` column, therefore a (size-1) square
                # matrix
                aux = tuple(
                    row[:c] + row[c + 1 :] for i, row in enumerate(m) if i != r
                )
                cofactor = (-1) ** (r + c) * laplace_determinant(aux, memo)
                det += m[r][c] * cofactor
        memo[m] = det
    return memo[m]


def count_decorations(decorations):
    c = {k: 0 for k in ("E", "F", "P", "A")}
    for row in decorations:
        for item in row:
            if item != ".":
                c[item] += 1
    return c


def is_there_decorations(decorations):
    for row in decorations:
        for item in row:
            if item != ".":
                return True
    return False


main()
