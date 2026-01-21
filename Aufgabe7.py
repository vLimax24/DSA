def klassenbester(schueler):
    return min(schueler, key=lambda s: s["note"])

#Test:
klasse = [
    {"name": "Anna", "note": 1.7},
    {"name": "Max", "note": 2.3},
    {"name": "Lisa", "note": 1.3}
]
print(klassenbester(klasse))  # Sollte {'name': 'Lisa', 'note': 1.3} ausgeben