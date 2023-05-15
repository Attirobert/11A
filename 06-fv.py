import turtle

def rajzolj_oszlopot(t, magassag):
    """ A t teknőc oszlopot rajzol a megfelelő magassággal """
    t.begin_fill()  # Beállítja az alakzat kitöltését.
    t.left(90)
    t.forward(magassag)
    t.write(" " + str(magassag))    # Kiírja a magasság értékét
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.end_fill()  # Leállítja az alakzat kitöltését.
    t.forward(10)

ablak = turtle.Screen()  # Ablak létrehozása
ablak.bgcolor("lightgreen") # Ablak színe

Toll = turtle.Turtle()  # Toll létrehozása
Toll.color("blue", "red")   # Toll és a kitöltő szín
Toll.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220] # Oszlopok magassága

for m in xs:
    rajzolj_oszlopot(Toll, m)

ablak.mainloop()