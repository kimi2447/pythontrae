# 导入绘图函数
from py import *
import turtle

# 设置画布
def setup_canvas():
    turtle.setup(800, 600)  # 设置窗口大小
    turtle.title("组合图形绘制")
    turtle.bgcolor("skyblue")  # 设置天空蓝背景
    turtle.speed(0)  # 最快的绘图速度
    turtle.hideturtle()  # 隐藏海龟

# 绘制太阳
def draw_sun():
    turtle.penup()
    turtle.goto(200, 150)
    turtle.pendown()
    draw_circle(50, "yellow")
    
    # 绘制太阳光芒
    for _ in range(12):
        turtle.penup()
        turtle.goto(200, 150)
        turtle.pendown()
        turtle.pensize(3)
        turtle.forward(70)
        turtle.left(30)

# 绘制房子
def draw_house():
    # 绘制房子主体
    turtle.penup()
    turtle.goto(-200, -100)
    turtle.pendown()
    draw_square(150, "brown")
    
    # 绘制房顶
    turtle.penup()
    turtle.goto(-200, 50)
    turtle.pendown()
    turtle.pencolor("red")
    turtle.begin_fill()
    turtle.fillcolor("red")
    for i in range(3):
        turtle.forward(150)
        turtle.left(120)
    turtle.end_fill()
    
    # 绘制门
    turtle.penup()
    turtle.goto(-150, -100)
    turtle.pendown()
    draw_rectangle(50, 80, "blue")
    
    # 绘制窗户
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()
    draw_square(40, "white")
    turtle.begin_fill()
    turtle.fillcolor("white")
    draw_square(40, "white")
    turtle.end_fill()

# 绘制花朵
def draw_flower():
    turtle.penup()
    turtle.goto(100, -150)
    turtle.pendown()
    
    # 绘制花瓣
    for _ in range(8):
        draw_equilateral_pentagon(30, "purple")
        turtle.left(45)
    
    # 绘制花芯
    turtle.penup()
    turtle.goto(100, -150)
    turtle.pendown()
    draw_circle(15, "yellow")
    turtle.begin_fill()
    turtle.fillcolor("yellow")
    draw_circle(15, "yellow")
    turtle.end_fill()

# 绘制草地
def draw_grass():
    turtle.penup()
    turtle.goto(-400, -200)
    turtle.pendown()
    turtle.pencolor("green")
    turtle.begin_fill()
    turtle.fillcolor("green")
    draw_rectangle(800, 100, "green")
    turtle.end_fill()

# 绘制星星
def draw_stars():
    positions = [(-300, 200), (-250, 150), (-150, 180), (0, 220), (150, 200)]
    for pos in positions:
        turtle.penup()
        turtle.goto(pos)
        turtle.pendown()
        draw_star(20, "white")

# 主函数
def main():
    setup_canvas()
    draw_grass()
    draw_house()
    draw_sun()
    draw_flower()
    
    # 在右侧绘制一些几何图形
    turtle.penup()
    turtle.goto(250, -50)
    turtle.pendown()
    draw_hexagon(30, "orange")
    
    turtle.penup()
    turtle.goto(250, -150)
    turtle.pendown()
    draw_octagon(25, "cyan")
    
    # 完成绘图
    turtle.exitonclick()
    # 隐藏海龟
    turtle.hideturtle()
    # 等待用户关闭窗口
    turtle.done()
    # 绘制星星
    draw_stars()

# 运行程序
if __name__ == "__main__":
    main()
