def je_tah_mozny_pesec(cilova_pozice, aktualni_pozice, obsazene_pozice, barva):
    if aktualni_pozice[1] != cilova_pozice[1]:
        return False
    
    if (aktualni_pozice[0] + 1 == cilova_pozice[0]) and (cilova_pozice not in obsazene_pozice):
        return True

    if aktualni_pozice[0] == 2 and (aktualni_pozice[0] + 2 == cilova_pozice[0]):
        if (aktualni_pozice[0] + 1, aktualni_pozice[1]) not in obsazene_pozice:
            return True

    if abs(aktualni_pozice[1] - cilova_pozice[1]) == 1 and abs(aktualni_pozice[0] - cilova_pozice[0]) == 1:
        if cilova_pozice in obsazene_pozice:
            return True

    return False


def je_tah_mozny_jezdec(cilova_pozice, aktualni_pozice, obsazene_pozice):
    for i in [1, 2]:
        if abs(aktualni_pozice[0] - cilova_pozice[0]) == 1 and abs(aktualni_pozice[1] - cilova_pozice[1]) == 2:
            return True
        if abs(aktualni_pozice[0] - cilova_pozice[0]) == 2 and abs(aktualni_pozice[1] - cilova_pozice[1]) == 1:
            return True
    return False


def je_tah_mozny_strelec(cilova_pozice, aktualni_pozice, obsazene_pozice):
    if abs(aktualni_pozice[0] - cilova_pozice[0]) != abs(aktualni_pozice[1] - cilova_pozice[1]):
        return False

    step_x = 1 if cilova_pozice[0] > aktualni_pozice[0] else -1
    step_y = 1 if cilova_pozice[1] > aktualni_pozice[1] else -1

    x, y = aktualni_pozice[0] + step_x, aktualni_pozice[1] + step_y

    while (x, y) != cilova_pozice:
        if (x, y) in obsazene_pozice:
            return False
        x += step_x
        y += step_y

    return True


def je_tah_mozny_vez(cilova_pozice, aktualni_pozice, obsazene_pozice):
    if aktualni_pozice[0] != cilova_pozice[0] and aktualni_pozice[1] != cilova_pozice[1]:
        return False

    if aktualni_pozice[0] == cilova_pozice[0]:
        range_positions = range(min(aktualni_pozice[1], cilova_pozice[1]) + 1, max(aktualni_pozice[1], cilova_pozice[1]))
        for i in range_positions:
            if (aktualni_pozice[0], i) in obsazene_pozice:
                return False

    elif aktualni_pozice[1] == cilova_pozice[1]:
        range_positions = range(min(aktualni_pozice[0], cilova_pozice[0]) + 1, max(aktualni_pozice[0], cilova_pozice[0]))
        for i in range_positions:
            if (i, aktualni_pozice[1]) in obsazene_pozice:
                return False

    return True


def je_tah_mozny_dama(cilova_pozice, aktualni_pozice, obsazene_pozice):
    if je_tah_mozny_vez(cilova_pozice, aktualni_pozice, obsazene_pozice):
        return True

    if je_tah_mozny_strelec(cilova_pozice, aktualni_pozice, obsazene_pozice):
        return True

    return False


def je_tah_mozny_kral(cilova_pozice, aktualni_pozice, obsazene_pozice):
    if abs(aktualni_pozice[0] - cilova_pozice[0]) <= 1 and abs(aktualni_pozice[1] - cilova_pozice[1]) <= 1:
        return True
    return False


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    if cilova_pozice in obsazene_pozice:
        return False

    aktualni_pozice = figurka["pozice"]
    if figurka["typ"] == "pěšec":
        return je_tah_mozny_pesec(cilova_pozice, aktualni_pozice, obsazene_pozice, figurka.get("barva"))
    elif figurka["typ"] == "jezdec":
        return je_tah_mozny_jezdec(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "věž":
        return je_tah_mozny_vez(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "střelec":
        return je_tah_mozny_strelec(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "dáma":
        return je_tah_mozny_dama(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "král":
        return je_tah_mozny_kral(cilova_pozice, aktualni_pozice, obsazene_pozice)
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print()
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print()
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True

    print()
    print(je_tah_mozny(strelec, (1, 8), obsazene_pozice))  # False
