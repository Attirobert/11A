# Állandók
kamatláb = 0.08
időszakok = 12
futamidő = 5


def kamatos_kamat(c, r, m, t):  # befektetettOsszeg, kamatláb, időszakok, futamidő
    """A futamidő végén kapott érték számítása c befektetett összegre a kamatos kamat képletének megfelelően."""

    fv = c * (1 + r/m) ** (m*t)
    return fv  # Ez az újdonság tesz a függvényt *produktív* függvénnyé.


# Most, hogy van egy függvényünk, hívjuk is meg!
befektetettOsszeg = float(input("Mekkora összeget kíván befektetni?"))
vegOsszeg = kamatos_kamat(befektetettOsszeg, kamatláb, időszakok, futamidő)
print("A futamidő végén Önnek ennyi pénze lesz: ", vegOsszeg)