import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.shape("turtle")
Eszti.color("blue")

Eszti.penup() # Ez új
meret = 20
for i in range(30):
    Eszti.stamp() # Hagyj egy lenyomatot a vásznon!
    meret = meret + 3 # Növeld a méretet minden ismétlésnél!
    Eszti.forward(meret) # Mozgasd ...
    Eszti.right(24) # ... és fordítsd Esztit!

ablak.mainloop()