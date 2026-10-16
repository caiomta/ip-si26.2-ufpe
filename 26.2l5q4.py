REGISTRATION = {
    "a": "aáàâãäAÁÀÂÃÄ",
    "e": "eéèêëEÉÈÊË",
    "i": "iíìîïIÍÌÎÏ",
    "o": "oóòôõöOÓÒÔÕÖ",
    "u": "uúùûüUÚÙÛÜ",
}


def main():
    phrase = input()
    disguise_book = get_disguise_book(phrase)
    census = get_census_from_disguise_book(disguise_book)
    print(census_to_str(census))
    investigated_animago = input()
    investigate_animago(investigated_animago, census, disguise_book)


def get_disguise_book(phrase):
    phrase = "".join([c for c in phrase if c.isupper() or c.islower()])
    disguise_book = {}
    for c in phrase:
        animago = get_animago(c)
        if animago in disguise_book:
            disguise_book[animago][c] = disguise_book[animago].get(c, 0) + 1
        else:
            disguise_book[animago] = {c: 1}
    return disguise_book


def get_census_from_disguise_book(disguise_book):
    census = [(c, sum(d.values())) for c, d in disguise_book.items()]
    bottom_up_duples_merge_sort(census)
    return dict(census)


def get_animago(c):
    for animago, disguises in REGISTRATION.items():
        if c in disguises:
            return animago
    return c.lower()


def bottom_up_duples_merge_sort(duples):
    n = len(duples)
    block_len = 1

    while block_len < n:
        for i in range(0, n, 2 * block_len):
            middle = min(i + block_len, n)
            end = min(i + 2 * block_len, n)
            interleave_halves(duples, i, middle, end)
        block_len *= 2


def interleave_halves(duples, start, middle, end):
    left_side = duples[start:middle]
    right_side = duples[middle:end]
    i = j = 0
    k = start

    while i < len(left_side) and j < len(right_side):
        if left_side[i][1] >= right_side[j][1]:
            duples[k] = left_side[i]
            i += 1
        else:
            duples[k] = right_side[j]
            j += 1
        k += 1

    for d in left_side[i:] + right_side[j:]:
        duples[k] = d
        k += 1


def census_to_str(census):
    census = [f"{c[1]}{c[0]}" for c in census.items()]
    return " ".join(census)


def investigate_animago(animago, census, disguise_book):
    appearances = census[animago]
    disguise_amount = len(disguise_book[animago])
    favourite_disguise = max(
        disguise_book[animago],
        key=disguise_book[animago].get,  # get funciona como lambda d: disguise_book[animago][d]
    )

    print(f"Total de ocorrências: {appearances}")
    print(f"Quantidade de variações: {disguise_amount}")
    print(
        f"Variação mais frequente: {favourite_disguise} ({disguise_book[animago][favourite_disguise]})"
    )


main()
