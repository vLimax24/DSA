def spaltensumme(matrix, spalte):
    result = 0

    for row in matrix:
        result += row[spalte]

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spaltensumme(matrix, 0))  # Sollte 12 ausgeben (1+4+7)
print(spaltensumme(matrix, 1))  # Sollte 15 ausgeben (2+5+8)

# optimiert

def spaltensumme(matrix, spalte):
    return sum(row[spalte] for row in matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spaltensumme(matrix, 0))  # Sollte 12 ausgeben (1+4+7)
print(spaltensumme(matrix, 1))  # Sollte 15 ausgeben (2+5+8)