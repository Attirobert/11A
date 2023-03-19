import turtle

# Ablak előkészítése
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
ablak.title("Szia Attila")

# Rajzeszköz előkészítése
Toll = turtle.Turtle()
Toll.color("blue")
Toll.pensize(3)

# Háromszöget rajzolunk
Toll.forward(50)
Toll.left(120)
Toll.forward(50)

Toll.left(120)
Toll.forward(50)

ablak.mainloop()