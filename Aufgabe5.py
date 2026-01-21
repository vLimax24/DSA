def koordinaten_distanz(punkt1, punkt2):
    return ((punkt2[0] - punkt1[0])**2 + (punkt2[1] - punkt1[1])**2)**0.5

# info: tuple.index(x) sucht nach wert x in tuple 

#Test:
print(koordinaten_distanz((0, 0), (3, 4)))    # Sollte 5.0 ausgeben
print(koordinaten_distanz((1, 2), (4, 6)))    # Sollte 5.0 ausgeben

# Lesbarere Version:

def koordinaten_distanz(punkt1, punkt2):
    x1, y1 = punkt1
    x2, y2 = punkt2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

#Test:
print(koordinaten_distanz((0, 0), (3, 4)))    # Sollte 5.0 ausgeben
print(koordinaten_distanz((1, 2), (4, 6)))    # Sollte 5.0 ausgeben