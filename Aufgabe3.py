def notenbuch(name, note):
    return dict(name = name, note = note)

#Test:
print(notenbuch("Anna", 1.7))    # Sollte {'name': 'Anna', 'note': 1.7} ausgeben
print(notenbuch("Max", 2.3))     # Sollte {'name': 'Max', 'note': 2.3} ausgeben

# optimierte Version

def notenbuch(name, note, fach=None):
    if fach:
        return {"name": name, "note": note, "fach": fach}
    return {"name": name, "note": note}

#Test:
print(notenbuch("Anna", 1.7, "Deutsch"))    # Sollte {'name': 'Anna', 'note': 1.7, 'fach': 'Deutsch'} ausgeben
print(notenbuch("Max", 2.3))     # Sollte {'name': 'Max', 'note': 2.3} ausgeben