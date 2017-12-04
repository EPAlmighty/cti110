import turtle

def main():
    bob = turtle.Turtle()
    wn = turtle.Screen()
    bob.color("white")
    bob.speed(1000000000000000000000000)
    wn.bgcolor("black")
    x=1
    while x < 10000000:
        bob.forward(90)
        bob.left(89)
        bob.forward(1+x)

main()
