login = input()
password = input()

uppercase_password = password.upper()
has_letters = (
    "A" in uppercase_password
    or "B" in uppercase_password
    or "C" in uppercase_password
    or "D" in uppercase_password
    or "E" in uppercase_password
    or "F" in uppercase_password
    or "G" in uppercase_password
    or "H" in uppercase_password
    or "I" in uppercase_password
    or "J" in uppercase_password
    or "K" in uppercase_password
    or "L" in uppercase_password
    or "M" in uppercase_password
    or "N" in uppercase_password
    or "O" in uppercase_password
    or "P" in uppercase_password
    or "Q" in uppercase_password
    or "R" in uppercase_password
    or "S" in uppercase_password
    or "T" in uppercase_password
    or "U" in uppercase_password
    or "V" in uppercase_password
    or "W" in uppercase_password
    or "X" in uppercase_password
    or "Y" in uppercase_password
    or "Z" in uppercase_password
)
has_digits = (
    "0" in password
    or "1" in password
    or "2" in password
    or "3" in password
    or "4" in password
    or "5" in password
    or "6" in password
    or "7" in password
    or "8" in password
    or "9" in password
)
has_special_chars = (
    "@" in password
    or "_" in password
    or "&" in password
    or "%" in password
    or "#" in password
)

only_letters = has_letters and not (has_digits or has_special_chars)

print("Byte irá julgar a sua senha.")

if len(password) < 8 or only_letters or password.isnumeric() or " " in password:
    print("Essa senha nem chega perto do que eu aceito. Tente de novo.")
else:
    print("Vamos fazer a contagem dos pontos.")

    points = 0

    if len(password) > 11:
        points += len(password) - 11

    only_special_chars = has_special_chars and not (has_letters or has_digits)

    # tem ao menos uma letra maiúscula e uma letra minúscula
    if not (
        only_special_chars
        or password == password.upper()
        or password == password.lower()
    ):
        points += 5

    if "@" in password:
        points += 1
    if "_" in password:
        points += 1
    if "&" in password:
        points += 1
    if "%" in password:
        points += 1
    if "#" in password:
        points += 1

    if len(password) > 14:
        print("Que senha grande! Não seria difícil esquecer dela.")

    if login.lower() in password.lower():
        print("Olha o que eu encontrei aqui, não deixarei isso passar tão fácil.")
        points -= 10

    if points < 1:
        points_needed = 1 - points
        print("Infelizmente terá que mudar sua senha, é para o seu bem.")
        print(f"Melhore sua senha em {points_needed} ponto(s) e ela será suficiente.")
    elif points < 11:
        print("Pode manter a sua senha, ela parece adequada.")
    else:
        print("Parabéns! Nem o maior hacker do mundo encontraria uma senha assim.")
