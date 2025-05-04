from turtle import *
def draw_square(length, color):
    pencolor(color)
    for i in range(4):
        forward(length)
        left(90)
def draw_rectangle(length, width, color):
    pencolor(color)
    for i in range(2):
        forward(length)
        left(90)
        forward(width)
        left(90)
def draw_triangle(length, color):
    pencolor(color)
    for i in range(3):
        forward(length)
        left(120)
def draw_star(length, color):
    pencolor(color)
    for i in range(5):
        forward(length)
        right(144)
def draw_circle(radius, color):
    pencolor(color)
    circle(radius)
def draw_polygon(sides, length, color):
    pencolor(color)
    angle = 360 / sides
    for i in range(sides):
        forward(length)
        left(angle)
def draw_hexagon(length, color):
    draw_polygon(6, length, color)
def draw_octagon(length, color):
    draw_polygon(8, length, color)
def draw_equilateral_triangle(length, color):
    draw_triangle(length, color)
def draw_isosceles_triangle(length, color):
    draw_triangle(length, color)
def draw_scalene_triangle(length, color):
    draw_triangle(length, color)
def draw_right_triangle(length, color):
    draw_triangle(length, color)
def draw_equilateral_pentagon(length, color):
    draw_polygon(5, length, color)
def draw_equilateral_hexagon(length, color):
    draw_polygon(6, length, color)
def draw_equilateral_octagon(length, color):
    draw_polygon(8, length, color)
def draw_equilateral_decagon(length, color):
    draw_polygon(10, length, color)
def draw_equilateral_hundredagon(length, color):
    draw_polygon(100, length, color)
def draw_equilateral_thousandagon(length, color):
    draw_polygon(1000, length, color)
def draw_equilateral_millionagon(length, color):
    draw_polygon(1000000, length, color)
def draw_equilateral_billionagon(length, color):
    draw_polygon(1000000000, length, color)


