def gemeinsame_hobbys(person1, person2):
    result = set()

    for hobby in person1:
        if hobby in person2:
            result.add(hobby)

    return result

anna = {"Lesen", "Sport", "Musik", "Reisen"}
tom = {"Sport", "Gaming", "Musik", "Kochen"}
print(gemeinsame_hobbys(anna, tom))  # Sollte {'Sport', 'Musik'} ausgeben

# Mit set operations:

def gemeinsame_hobbys(person1, person2):
    return person1 & person2

anna = {"Lesen", "Sport", "Musik", "Reisen"}
tom = {"Sport", "Gaming", "Musik", "Kochen"}
print(gemeinsame_hobbys(anna, tom))  # Sollte {'Sport', 'Musik'} ausgeben
