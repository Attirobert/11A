import turtle
ablak = turtle.Screen()

ablak.bgcolor("lightgreen")
ablak.title("Eszti & Sanyi")

Eszti = turtle.Turtle() # Hozd létre Esztit és add meg tulajdonságait!
Eszti.color("hotpink")
Eszti.pensize(5)

Sanyi = turtle.Turtle() # Hozd létre Sanyit!

Eszti.forward(80) # Rajzoltass Esztivel egy egyenlő oldalú háromszöget!
Eszti.left(120)
Eszti.forward(80)
Eszti.left(120)
Eszti.forward(80)
Eszti.left(120) # Fejezd be a háromszöget!

Eszti.right(180) # Eszti forduljon meg!
Eszti.forward(80) # Mozdítsd el őt a kiindulóponttól!

Sanyi.forward(50) # Rajzoltass Sanyival egy négyzetet!
Sanyi.left(90)
Sanyi.forward(50)
Sanyi.left(90)
Sanyi.forward(50)
Sanyi.left(90)
Sanyi.forward(50)
Sanyi.left(90)

ablak.mainloop()