import turtle
import random

new_tilt_value = 0
TREE,BIRD = range(2)
state = TREE
Position = [-340,370]
pencolor = 'purple'
fillcolor = 'purple'
class utility():
    def __init__(self):
        pass
    def run(self):
        turtle.Screen().setup(800,800)
        turtle.speed(0)
        turtle.color('light yellow')
        turtle.bgcolor('light yellow')
        turtle.hideturtle()
        turtle.register_shape('bird', ((-22, -39), (-20, -7,), (-7, 3), (-11, 7), (-12, 9),
                                       (-11, 10),(-9, 10), (-3, 7), (10, 24), (30, 16), (13, 18),
                                       (4, 0), (14, -6), (6, -13), (0, -4), (-14, -13), (-22,-39)))

        turtle.shape('bird')
        turtle.penup()
        def handle_click(x,y):
            print('detected a click at', x, y)
            global state
            abs_x = abs(x)
            abs_y = abs(y)
            tree_click = distance(0,370,x,y)
            bird_click = distance(100,370,x,y)
            print('tree distance {}, bird distance {} ' .format(tree_click,bird_click))
            if tree_click <= 10 and state != TREE:
                state = TREE
                turtle.hideturtle()
                draw_circle(0,370,10,'black','green')
                draw_circle(100, 370, 10, 'black', 'light yellow')
            elif bird_click <=10 and state != BIRD:
                state = BIRD
                draw_circle(0, 370, 10, 'black', 'light yellow')
                draw_circle(100, 370, 10, 'black', 'green')
                turtle.hideturtle()
                turtle.setposition(Position[0],Position[1])
                turtle.color('purple')
                turtle.showturtle()
            elif abs_x <= 350 and abs_y <=350:
                if state == TREE:
                    draw_tree(x,y)
                else:
                    draw_stamp(x,y,'purple')
        def save_state():
            global Position,pencolor,fillcolor
            Position[0] = -340
            Position[1] = 370
            pencolor = 'purple'
            fillcolor = 'purple'
        def restore_state():
            turtle.pencolor(pencolor)
            turtle.fillcolor(fillcolor)
            turtle.begin_fill()
            turtle.goto(Position)
            turtle.end_fill()
        def left_keypress():
            print('left key pressed')
            global new_tilt_value
            new_tilt_value += 10
            turtle.tiltangle(new_tilt_value)
        def right_keypress():
            global new_tilt_value
            new_tilt_value -= 10
            turtle.tiltangle(new_tilt_value)
        def draw_circle(center_x, center_y, radius, pen_color, fill_color):
            turtle.penup()
            turtle.setposition(center_x, center_y-radius)
            turtle.pendown()
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            turtle.begin_fill()
            turtle.circle(radius)
            turtle.end_fill()
            turtle.penup()
        def draw_stamp(center_x, center_y, color):
            save_state()
            t = turtle.stamp()
            turtle.color(color)
            turtle.setposition(center_x, center_y)
            turtle.stamp()
            turtle.clearstamp(t)
            restore_state()
            turtle.showturtle()
        def distance(x1, y1, x2,y2):
            return round(((x1-x2)**2+(y1-y2)**2)**(1/2),2)
        def draw_triangle(center_x, center_y, width, height, pen_color, fill_color):
            turtle.penup()
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            initial_x = center_x - (width/2)
            initial_y = center_y - (height/2)
            turtle.setposition(initial_x, initial_y)
            turtle.pendown()
            turtle.begin_fill()
            turtle.forward(distance(initial_x,initial_y,initial_x+width,initial_y))
            turtle.goto(initial_x + (width / 2), initial_y + height)
            turtle.goto(initial_x, initial_y)
            turtle.end_fill()
            turtle.penup()
        def draw_rectangle(center_x, center_y, width, height, pen_color, fill_color):
            turtle.penup()
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            initial_x = center_x - (width / 2)
            initial_y = center_y - (height / 2)
            turtle.setposition(initial_x, initial_y)
            turtle.pendown()
            turtle.begin_fill()
            for x in range(0, 4):
                dw = 0
                if (x % 2 == 0):
                    dw = width
                else:
                    dw = height
                turtle.forward(dw)
                turtle.left(90)
            turtle.end_fill()
            turtle.penup()
        def draw_tree(x,y):
            val = random.uniform(0.7,1.3)
            draw_rectangle(x,y-(40*val),val*15,val*80,'brown','brown')
            va = 50*val*0.6
            for i in range (3):
                draw_triangle(x,y+(25*val+va*i),val*100,val*50,'green','green')


        turtle.pensize(5)
        draw_rectangle(0,0,700,700,'Black','light yellow')
        turtle.pensize(1)
        draw_circle(0,370,10,'black','green')
        turtle.setx(15)
        turtle.write('Tree',False)
        draw_circle(100,370,10,'black','light yellow')
        turtle.setx(115)
        turtle.write('Bird',False)
        turtle.color(fillcolor)
        turtle.setposition(Position)
        turtle.listen()
        turtle.onscreenclick(handle_click)
        turtle.onkey(left_keypress,'Left')
        turtle.onkey(right_keypress,'Right')
        turtle.mainloop()
