def mittelwert(zahlen):
    if len(zahlen) == 0: # Leere Liste ist falsy deswegen geht auch if not 
        return None
    result = 0 # var wird durch sum() überflüssig

    for z in zahlen: # Sum() ersetzt schleife
        result += z

    return result / len(zahlen)

print(mittelwert([2, 4, 6, 8]))
print(mittelwert([10, 20, 30]))
print(mittelwert([]))


# optimierte Version

def mittelwert(zahlen):
    if not zahlen:
        return None
    return sum(zahlen) / len(zahlen)

print(mittelwert([2, 4, 6, 8]))
print(mittelwert([10, 20, 30]))
print(mittelwert([]))