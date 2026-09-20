print("--- FASE 1: A VARREDURA ---")

rows = int(input())

crime_scene_matrix = [
    input().split(", ") for _ in range(rows)
]  # coleta da cena do crime

start_i, end_i, start_j, end_j = [
    int(i) for i in input().split()
]  # intervalo do quadrante

janes_quadrant_matrix = [
    crime_scene_matrix[i][start_j:end_j] for i in range(start_i, end_i)
]  # separação do quadrante do Jane

print("Lisbon: Jane, focamos as buscas no quadrante delimitado.")

is_smiley_present = []
blood_count = []
gun_count = []

for row in janes_quadrant_matrix:
    print(row)

    is_smiley_present.append("Smiley" in row)  # há 'Smiley' nessa linha?
    blood_count.append(row.count("Sangue"))  # quantos 'Sangue' há nessa linha?
    gun_count.append(row.count("Arma"))  # quantas 'Arma' há nessa linha?


is_smiley_present = (
    sum(is_smiley_present) != 0
)  # grande 'or' entre as presenças de Smiley em cada linha
blood_count = sum(blood_count)  # soma das contagens nas linhas
gun_count = sum(gun_count)  # soma das contagens nas linhas

print(
    f"Evidencias encontradas: Sangue ({blood_count}), Arma ({gun_count}). Smiley ({'Sim' if is_smiley_present else 'Nao'})\n"
)

print("--- FASE 2: A MATRIZ DE EVIDÊNCIAS ---")

evidence_matrix_rows, evidence_matrix_columns = [int(i) for i in input().split()]

evidence_matrix = [
    [int(item) for item in input().split()] for _ in range(evidence_matrix_rows)
]  # coleta da matriz de evidência com conversão para inteiro

evidence_threshold = int(input())

binary_matrix = [
    [1 if item >= evidence_threshold else 0 for item in row] for row in evidence_matrix
]

print("Patrick Jane: Às vezes, a verdade está escondida bem diante dos nossos olhos.")
for row in binary_matrix:
    for j in range(evidence_matrix_columns):
        print(row[j], end=("\n" if j == evidence_matrix_columns - 1 else " "))

pattern = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]
found_pattern = False
i = 0
for i in range(evidence_matrix_rows - 2):
    for j in range(evidence_matrix_columns - 4):
        if (
            not found_pattern
            and binary_matrix[i][j : j + 5] == pattern[0]
            and binary_matrix[i + 1][j : j + 5] == pattern[1]
            and binary_matrix[i + 2][j : j + 5] == pattern[2]
        ):
            found_pattern = True
            i_found, j_found = i, j

if found_pattern:
    print("Patrick Jane: Eu conheço esse sorriso.")
    print("RED JOHN DEIXOU UMA ASSINATURA!")
    print(f"ASSINATURA ENCONTRADA EM [{i_found}][{j_found}]")  # type: ignore
else:
    print("Patrick Jane: Nada aqui parece familiar.")

print()

if is_smiley_present or found_pattern:
    print("--- FASE 3: A MENSAGEM ---")

    encrypted_message = [int(i) for i in input().split()]
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    message = "".join(
        [
            alphabet[((c * 3 + 1) % 27) if c % 2 else ((c // 2) % 27)]
            for c in encrypted_message
        ]
    )

    print(f'Mensagem decodificada: "{message}"')
    print("Jane: Ele acha que é mais esperto que eu. Nós vamos pegá-lo.")
else:
    print("--- FASE 3: O CÓDIGO ---")
    print("Patrick Jane: Vamos ver o que ele quis dizer dessa vez.")

    encrypted_note = list(input())
    encrypted_note.reverse()
    encrypted_note = encrypted_note[::2]
    encrypted_note = [c.upper() if c.islower() else c.lower() for c in encrypted_note]
    message = "".join(encrypted_note)
    obsession_degree = message.lower().count("j")

    print("MENSAGEM DECODIFICADA!")
    print(f"Patrick Jane: '{message}'...")
    print("Patrick Jane: Esse caso acabou de dar uma reviravolta interessante.")
    print(f"Grau de Obsessão: {obsession_degree} aparição(ões) da letra J na mensagem.")
    print("--- CASO ENCERRADO (por enquanto...) ---")
