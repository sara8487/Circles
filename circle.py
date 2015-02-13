import turtle

def draw_square (some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():      
    window = turtle.Screen()
    window.bgcolor("red")
    brad =   turtle.Turtle()
    brad.shape ("turtle")
    brad.color ("yellow")
    brad.speed (4)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)



    window.exitonclick()
draw_art()

echo "# circle.py" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/sara8487/circle.py.git
git push -u origin master
