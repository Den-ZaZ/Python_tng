import turtle
from random import choice

color_1 = "#3D73BF"
color_2 = "#B2AC36"

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width = 1.0, height = 1.0)
window.bgcolor("#464646")
window.tracer(2)

ping_pong = turtle.Turtle()
ping_pong.penup()
ping_pong.hideturtle()
ping_pong.color("#4D4D4D")
ping_pong.goto(-260, 390)
ping_pong.write("Ping-Pong", font=("Arial", 80, "bold"))
ping_pong.color("#434343")
ping_pong.goto(-254, 390)
ping_pong.write("Ping-Pong", font=("Arial", 78, "bold"))
ping_pong.color("#4D4D4D")
ping_pong.goto(-220, -340)
ping_pong.write('"Все права защищены абсолютно ничем(с)"', font=("Arial", 15, "bold"))

border = turtle.Turtle()
border.speed(0)
border.color(color_1)
border.penup()
border.begin_fill()
border.goto(-500, 300)
border.pendown()
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()
border.hideturtle()

bruh = turtle.Turtle()
bruh.penup()
bruh.hideturtle()
bruh.color("#5289D7")
bruh.goto(-500, -200)
bruh.write("BRUH", font=("Arial", 260, "bold"))

frame = turtle.Turtle()
frame.speed(0)
frame.color(color_2)
frame.penup()
frame.pensize(10)
frame.goto(-505, 305)
frame.pendown()
frame.goto(505, 305)
frame.goto(505, -305)
frame.goto(-505, -305)
frame.goto(-505, 305)
frame.goto(0, 305)
frame.goto(0, -305)
frame.goto(0, 305)
frame.goto(-505, 305)
frame.goto(-505, 365)
frame.goto(0, 365)
frame.goto(0, 305)
frame.goto(0, 365)
frame.goto(505, 365)
frame.goto(505, 305)
frame.hideturtle()

control_1 = turtle.Turtle()
control_1.penup()
control_1.hideturtle()
control_1.color(color_2)
control_1.goto(-475, 260)
control_1.write("Control W/S", font=("Arial", 18, "bold"))

control_2 = turtle.Turtle()
control_2.penup()
control_2.hideturtle()
control_2.color(color_2)
control_2.goto(345, 260)
control_2.write("Control P/L", font=("Arial", 18, "bold"))

circ = turtle.Turtle()
circ.color(color_2)
circ.shape("circle")
circ.shapesize(outline=40)

rocket_1 = turtle.Turtle()
rocket_1.speed(0)
rocket_1.color(color_2)
rocket_1.penup()
rocket_1.shape("square")
rocket_1.shapesize(stretch_len=1, stretch_wid=5)
rocket_1.goto(-450, 0)

rocket_2 = turtle.Turtle()
rocket_2.speed(0)
rocket_2.color(color_2)
rocket_2.penup()
rocket_2.shape("square")
rocket_2.shapesize(stretch_len=1, stretch_wid=5)
rocket_2.goto(450, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.color("#AB9F32")
ball.penup()
ball.shape("square")
ball.shapesize(outline=5)
ball.dx = 2
ball.dy = 2

PlayerPoint_1 = 0
PlayerPoint_2 = 0

point_1 = turtle.Turtle()
point_1.penup()
point_1.hideturtle()
point_1.color(color_2)
point_1.goto(-31, 307)
point_1.write(PlayerPoint_1, font=("Arial", 34, "bold"))

point_2 = turtle.Turtle()
point_2.penup()
point_2.hideturtle()
point_2.color(color_2)
point_2.goto(9, 307)
point_2.write(PlayerPoint_2, font=("Arial", 34, "bold"))

def up1():
	y = rocket_1.ycor() + 50
	if y > 250:
		y = 250
	rocket_1.sety(y)

def down1():
	y = rocket_1.ycor() - 50
	if y < -250:
		y = -250
	rocket_1.sety(y)

def up2():
	y = rocket_2.ycor() + 50
	if y > 250:
		y = 250
	rocket_2.sety(y)

def down2():
	y = rocket_2.ycor() - 50
	if y < -250:
		y = -250
	rocket_2.sety(y)

window.listen()
window.onkeypress(up1, "w")
window.onkeypress(down1, "s")
window.onkeypress(up2, "p")
window.onkeypress(down2, "l")

Game = 0

while Game == 0:

	window.update()

	while PlayerPoint_1 < 10 and PlayerPoint_2 < 10:
		window.update()
			
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)

		if ball.xcor() >= 490:
			ball.goto(0, 0)

			ball.dx = choice([-2, 2])
			ball.dy = choice([-2, 2])

			point_1.undo()
			PlayerPoint_1 = PlayerPoint_1 + 1
			point_1.write(PlayerPoint_1, font=("Arial", 34, "bold"))

		if ball.xcor() <= -490:
			ball.goto(0, 0)

			ball.dx = choice([-2, 2])
			ball.dy = choice([-2, 2])

			point_2.undo()
			PlayerPoint_2 = PlayerPoint_2 + 1
			point_2.write(PlayerPoint_2, font=("Arial", 34, "bold"))

		if ball.ycor() >= 290:
			ball.dy = -ball.dy

		if ball.ycor() <= -290:
			ball.dy = -ball.dy

		if ball.ycor() >= rocket_1.ycor() - 60 and ball.ycor() <= rocket_1.ycor() + 60 and ball.xcor() >= rocket_1.xcor() - 20 and ball.xcor() <= rocket_1.xcor() + 20:
			ball.dx = -ball.dx
		
		if ball.ycor() >= rocket_2.ycor() - 60 and ball.ycor() <= rocket_2.ycor() + 60 and ball.xcor() >= rocket_2.xcor() - 20 and ball.xcor() <= rocket_2.xcor() + 20:
			ball.dx = -ball.dx

	if PlayerPoint_1 == 10:
		point_1.undo()
		point_1.goto(-58, 308)
		point_1.write(PlayerPoint_1, font=("Arial", 34, "bold"))
		point_2.undo()
		point_2.write("Player 2 is Bruh", font=("Arial", 34, "bold"))

	if PlayerPoint_2 == 10:
		point_1.undo()
		point_1.goto(-346, 308)
		point_1.write("Player 1 is Bruh", font=("Arial", 34, "bold"))
	
	Game = 1

again = turtle.Turtle()
again.speed(0)
again.color("#464646")
again.penup()
again.begin_fill()
again.goto(-200, 250)
again.pendown()
again.goto(200, 250)
again.goto(200, 150)
again.goto(-200, 150)
again.goto(-200, 250)
again.end_fill()
again.hideturtle()

frame.penup()
frame.speed(0)
frame.goto(-200, 250)
frame.pendown()
frame.goto(200, 250)
frame.goto(200, 150)
frame.goto(-200, 150)
frame.goto(-200, 250)
frame.goto(-200, 250)
	
total = turtle.Turtle()
total.speed(0)
total.penup()
total.hideturtle()
total.color(color_2)
total.goto(-145, 170)

if PlayerPoint_1 == 10:
	total.write("Player 1 wins", font=("Arial", 34, "bold"))

if PlayerPoint_2 == 10:
	total.write("Player 2 wins", font=("Arial", 34, "bold"))
	
window.mainloop()

