import turtle


def tobbszinu_negyzet_rajzolas(t, h):
    """"Egy h oldalhosszúságú, többszínű négyzet rajzoltatása a t teknőccel"""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(h)
        t.left(90)


# Egy ablak létrehozása és a tulajdonságainak beállítása
a = turtle.Screen()
a.bgcolor("lightgreen")

# Toll létrehozása és tulajdonságainak beállítása
Toll = turtle.Turtle()
Toll.pensize(3)


meret = 20  # A legkisebb négyzet mérete
for i in range(15):
    tobbszinu_negyzet_rajzolas(Toll, meret)
    meret = meret + 10  # Növeljük a következő négyzet méretét
    Toll.forward(10)  # Kicsit arrébb léptetjük a teknőcöt
    Toll.right(18)  # és kicsit elfordítjuk

a.mainloop()