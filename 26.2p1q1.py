best_grade = 0
n_best_grade = 0
second_best_grade = 0
n_second_best_grade = 0

running = True
while running:
    code = input()
    if code == 'fim':
        running = False
    else:
        grade = int(input())

        if best_grade < grade:
            second_best_grade = best_grade
            n_second_best_grade = n_best_grade

            best_grade = grade
            n_best_grade = 1
        elif best_grade == grade:
            n_best_grade += 1
        elif second_best_grade < grade:
            second_best_grade = grade
            n_second_best_grade = 1
        elif second_best_grade == grade:
            n_second_best_grade += 1

print(f'Maior nota: {best_grade}')
print(f'Numero de pessoas com maior nota: {n_best_grade}')
print(f'Segunda maior nota: {second_best_grade}')
print(f'Numero de pessoas com a segunda maior nota: {n_second_best_grade}')