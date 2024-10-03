from turtle import Turtle,Screen
import random
is_game_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_guess = screen.textinput(title="Make a bet",prompt="Which turtle is going t win the race?")
print(user_guess)
y_pos = [-70,-40,-10,20,50,80]
colors = ["red","green","blue","orange","purple","yellow"]
turtles =[]
for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setpos(x=-230,y=y_pos[i])
    turtles.append(new_turtle)
if user_guess:
    is_game_on = True
while is_game_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_game_on=False
            winning_color=turtle.pencolor()
            if winning_color == user_guess:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_int = random.randint(0,10)
        turtle.forward(rand_int)












screen.exitonclick()