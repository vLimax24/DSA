def warenkorb_preis(artikel):
    items = artikel.keys()
    print("Es wird der folgende Preis für die folgenden Artikel berechnet:", ", ".join(str(i) for i in items))
    return sum(artikel.values())

korb1 = {"Apfel": 0.5, "Brot": 1.2, "Milch": 0.9}
print(warenkorb_preis(korb1))  # Sollte 2.6 ausgeben

korb2 = {"Pizza": 3.5, "Cola": 1.5}
print(warenkorb_preis(korb2))  # Sollte 5.0 ausgeben