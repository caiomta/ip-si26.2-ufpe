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

is_smiley_present = []
blood_count = []
gun_count = []

for row in janes_quadrant_matrix:
    is_smiley_present.append("Smiley" in row)  # há 'Smiley' nessa linha?
    blood_count.append(row.count("Sangue"))  # quantos 'Sangue' há nessa linha?
    gun_count.append(row.count("Arma"))  # quantas 'Arma' há nessa linha?


is_smiley_present = (
    sum(is_smiley_present) != 0
)  # grande 'or' entre as presenças de Smiley em cada linha
blood_count = sum(blood_count)  # soma das contagens nas linhas
gun_count = sum(gun_count)  # soma das contagens nas linhas

evidence_matrix_rows, evidence_matrix_columns = [int(i) for i in input().split()]

evidence_matrix = [
    [int(item) for item in input().split()] for _ in range(evidence_matrix_rows)
]  # coleta da matriz de evidência com conversão para inteiro

evidence_threshold = int(input())

binary_matrix = [
    [1 if item >= evidence_threshold else 0 for item in row] for row in evidence_matrix
]

pattern = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]
found_pattern = False
i = 0
for i in range(evidence_matrix_rows - 2):
    for j in range(evidence_matrix_columns - 4):
        if (
            not found_pattern
            and binary_matrix[i][j : j + 5] == pattern[0]
            and binary_matrix[i + 1][j : j + 5]
            and binary_matrix[i + 2][j : j + 5]
        ):
            found_pattern = True
            i_found, j_found = i, j

if is_smiley_present or found_pattern:
    encrypted_message = [int(i) for i in input().split()]
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    message = "".join(
        [
            alphabet[((c * 3 + 1) % 27) if c % 2 else ((c // 2) % 27)]
            for c in encrypted_message
        ]
    )
else:
    encrypted_note = list(input())
    encrypted_note.reverse()
    encrypted_note = encrypted_note[::2]
    encrypted_note = [c.upper() if c.islower() else c.lower() for c in encrypted_note]
    message = "".join(encrypted_note)
    obsession_degree = message.lower().count("j")
