# Imperative schreibweise

def verdopple_gerade(zahlen):
    result = []
    for z in zahlen:
        if z % 2 == 0:
            result.append(z * 2)
        else:
            result.append(z)
    return result

#Test:
print(verdopple_gerade([1, 2, 3, 4, 5]))  # Sollte [1, 4, 3, 8, 5] ausgeben
print(verdopple_gerade([10, 15, 20]))     # Sollte [20, 15, 40] ausgeben

# deklerative Schreibweise (List Comprehensions)

# Wenn nur if: [ausdruck -> for -> if]
# Wenn if-else: [ausdruckTrue -> if -> bedingung -> else -> ausdruckFalse -> for]

def verdopple_gerade(zahlen):
    return [z *  2 if z % 2 == 0 else z for z in zahlen]

#Test:
print(verdopple_gerade([1, 2, 3, 4, 5]))  # Sollte [1, 4, 3, 8, 5] ausgeben
print(verdopple_gerade([10, 15, 20]))     # Sollte [20, 15, 40] ausgeben
