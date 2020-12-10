"""
MIT License

Copyright (c) 2020 RedMiner2005

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from math import sqrt
from time import perf_counter, sleep
from threading import Thread
from importlib import import_module
import random
import turtle
import os


development = True
if development:
    from src import playsound
    from src.code import viewturtle
else:
    import playsound
    from code import viewturtle


class Infinity:
    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        self.n += 1
        return self.n


class Vector:
    def __init__(self, x: float, y: float, z: float = None):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z if z is not None else -1)

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)

    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)

    def __truediv__(self, k):
        return Vector(self.x / k, self.y / k, self.z / k)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def tuple(self):
        return self.x, self.y, self.z

    def ituple(self):
        return int(self.x), int(self.y), int(self.z)

    @staticmethod
    def get_origin(z : bool = True):
        return Vector(0, 0, 0) if z else Vector(0, 0)

    @staticmethod
    def distance(p0, p1, z= True):
        if z:
            return sqrt((p0.x - p1.x) ** 2 + (p0.y - p1.y) ** 2 + (p0.z - p1.z) ** 2)
        else:
            return sqrt((p0.x - p1.x) ** 2 + (p0.y - p1.y) ** 2)


class Utils:
    debug = False

    @staticmethod
    def clamp(num: float, min_value: float, max_value: float) -> float:
        return max(min(num, max_value), min_value)

    @staticmethod
    def frange(start: float, stop: float, step: float):
        while start < stop:
            yield float(start)
            start += step

    @staticmethod
    def lerp(a: Vector, b: Vector, t: float) -> Vector:
        t = Utils.clamp(t, 0, 1.0)
        return (a * (1 - t)) + (b * t)

    @staticmethod
    def aabb(x1: float, y1: float, x2: float, y2: float, x: float, y: float) -> bool:
        if Utils.debug:
            dim = turtle.pos()
            col = turtle.color()
            turtle.color(255, 0, 0)
            turtle.penup()
            turtle.goto(x1, y1)
            turtle.pendown()
            turtle.begin_fill()
            turtle.goto(x1, y2)
            turtle.goto(x2, y2)
            turtle.goto(x2, y1)
            turtle.goto(x1, y1)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(*dim)
            turtle.color(*col)
        return x1 <= x <= x2 and y1 <= y <= y2

    @staticmethod
    def random_color() -> Vector:
        return Vector(round(random.random() * 255), round(random.random() * 255), round(random.random() * 255))

    @staticmethod
    def asset(path: str) -> str:
        return os.path.join(os.getcwd(), path)


class App:
    def __init__(self, t: turtle.Turtle, win: turtle._Screen, fps_limit: int = 60):
        self.t = t
        self.win = win
        self.win.setup(width=1.0, height=0.95, startx=None, starty=None)
        self.win.cv._rootwindow.resizable(False, False)
        self.win.tracer(0)
        #self.win.onscreenclick(self.click)
        self.screen = self.win.getcanvas()
        self.screen.bind('<Motion>', self.mouse)
        self.dim = [self.win.window_width(), self.win.window_height()]
        self.managers = [Intro(self, Vector(233, 5, 100), Vector(0, 100, 50)),
                         PostIntro(self, Vector(0, 0, 0)),
                         PostPostIntro(self),
                         Menu(self)]
        self.manager = self.managers[0]
        self.elapsed = 0.0
        self.fps = 1 / fps_limit
        self.motion_funcs = []
        self.click_funcs = []
        self.click_running = False
        self.hover_running = False
        self.music_thread = Thread(target=self.music, daemon=True)
        self.music_thread.start()
        self.mainloop()

    def mainloop(self):
        self.t.penup()
        try:
            for i in Infinity():
                t0 = perf_counter()
                for frame in self.manager:
                    t1 = perf_counter()
                    self.elapsed = abs(t1 - t0)
                    if self.elapsed > self.fps:
                        self.win.update()
                    self.win.onscreenclick(self.click_check)
                    t0 = t1
        except Exception as e:
            print(e)

    def music(self):
        for i in Infinity():
            playsound.playsound("audio/music.mp3")
            playsound.playsound("audio/music2.mp3")
            playsound.playsound("audio/music3.mp3")

    def mouse(self, event):
        if not self.motion_funcs:
            return
        if self.hover_running:
            return
        self.hover_running = True
        x, y = event.x - self.dim[0] // 2, self.dim[1] // 2 - event.y
        for function in self.motion_funcs:
            function(x, y)
        self.hover_running = False

    def click_check(self, x, y):
        if not self.click_funcs:
            return
        if self.hover_running:
            return
        self.click_running = True
        for function in self.click_funcs:
            function(x, y)
        self.click_running = False

    def switch(self, index):
        self.manager = self.managers[index]

    def close(self):
        self.music_thread.join()
        quit(0)


class Button:
    def __init__(self, name: str, x: int, y: int,
                 default_img: str, highlight_img: str,
                 img_x: int, img_y: int,
                 click_func, app: App):
        self.name = name
        self.default = default_img
        self.highlight = highlight_img
        self.dimensions = (img_x, img_y)
        self.app = app
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.enabled = False
        self.t.goto(x, y)
        self.click_func = click_func
        #self.app.win.onscreenclick(self.start_click)
        self.app.motion_funcs.append(self.hover)
        self.app.click_funcs.append(self.start_click)
        self.app.win.addshape(self.default)
        self.app.win.addshape(self.highlight)
        self.t.shape(self.default)
        self.not_highlighted = True

    def destruct(self):
        self.app.motion_funcs.remove(self.hover)
        self.app.click_funcs.remove(self.start_click)

    def show(self):
        self.enabled = True
        self.t.showturtle()

    def hide(self):
        self.enabled = False
        self.t.hideturtle()

    def is_mouse_over(self, x: int, y: int):
        t_x = self.t.xcor() - (self.dimensions[0] // 2)
        t_y = self.t.ycor() - (self.dimensions[1] // 2)
        return Utils.aabb(t_x, t_y, t_x + self.dimensions[0], t_y + self.dimensions[1], x, y) and self.enabled

    def hover(self, x: int, y: int):
        """if collides and self.not_highlighted:
            self.t.shape(self.highlight)
            self.not_highlighted = False
        elif not (collides or self.not_highlighted):
            self.t.shape(self.default)
            self.not_highlighted = True"""
        #self.t.goto(x, y)
        if self.is_mouse_over(x, y):
            self.t.shape(self.highlight)
        else:
            self.t.shape(self.default)

    def start_click(self, x, y):
        #print(x, y)
        if self.is_mouse_over(x, y):
            playsound.playsound("audio/press.mp3", block=False)
            self.click_func()


class MenuButton(Button):
    def __init__(self, name: str, x: int, y: int, img_x: int, img_y: int, app: App):
        super(MenuButton, self).__init__(name, x, y, f"img/{name}/default.gif", f"img/{name}/highlight.gif",
                                         img_x, img_y, self.click, app)
        self.module = import_module(f"src.code.{self.name}.{self.name}"
                                    if development else
                                    f"code.{self.name}.{self.name}")
        self.screen = None

    def click(self):
        if self.screen is None:
            self.screen = viewturtle.Screen()
        self.screen.clearscreen()
        try:
            self.module.main(viewturtle)
        except Exception as e:
            print(e)


class FrameManager:
    def __init__(self, app: App):
        self.app = app
        self.destruct = False

    def __iter__(self):
        self.app.t.hideturtle()
        self.app.win.clearscreen()
        self.app.win.colormode(255)
        self.app.win.bgcolor(0, 0, 0)
        self.app.t.penup()
        return self

    def __next__(self):
        return


class Intro(FrameManager):
    def __init__(self, app: App, colorA: Vector, colorB: Vector):
        super().__init__(app)
        self.a = colorA
        self.b = colorB
        self.increment = 1

    def __iter__(self):
        super(Intro, self).__iter__()
        self.n = 0
        self.app.t.goto(0, 0)
        self.app.t.color(255, 255, 255)
        """self.app.t.write("Note: Please don't move the mouse too fast. The app will crash😂",
                         False, font=("Arial", 28, "normal"), align="center")
        sleep(3)
        for i in Utils.frange(0, 1, 0.01):
            self.app.t.color(*Utils.lerp(Vector(255, 255, 255), Vector(0, 0, 0), i).ituple())
            self.app.t.write("Note: Please don't move the mouse too fast. The app will crash😂",
                             False, font=("Arial", 28, "normal"), align="center")"""  # Yes, this was once a problem
        self.app.win.clearscreen()
        self.app.win.bgcolor(0, 0, 0)
        self.start = Button("start",
                            0, -250, Utils.asset("img/start/default.gif"), Utils.asset("img/start/highlight.gif"),
                            240, 140, self.menu, self.app)
        self.start.show()
        self.app.win.colormode(255)
        return self

    def __next__(self):
        if self.destruct:
            del self.start
            raise StopIteration
        self.app.t.color(*Utils.lerp(self.a, self.b, self.n).ituple())
        self.app.t.goto(0, 0)
        self.app.t.write("Computers Art Integrated Activity", False, font=("Arial", 36, "normal"), align="center")
        self.app.t.sety(-50)
        self.app.t.write("Team leader/Chief programmer: Pratyush Nair", False, font=("Arial", 24, "normal"),
                         align="center")
        if self.n >= 1:
            self.increment = -self.increment
            self.a = Utils.random_color()
        elif self.n <= 0:
            self.increment = abs(self.increment)
            self.b = Utils.random_color()
        if self.app.elapsed > 1:
            self.n += self.increment
        else:
            self.n += (self.increment * self.app.elapsed)
        #self.n += (self.increment * self.app.elapsed)
        return

    def menu(self):
        self.app.switch(1)
        self.destruct = True


class Menu(FrameManager):
    def __init__(self, app: App):
        super().__init__(app)

    def __iter__(self):
        self.app.t.hideturtle()
        self.app.t.penup()
        self.app.t.goto(0, (self.app.win.window_height() // 2) - 100)
        self.app.t.color(0, 0, 0)
        self.pratyush = MenuButton("pratyush", -585, 170, 275, 157, self.app)
        self.abhay = MenuButton("abhay", -293, 170, 275, 157, self.app)
        self.siva = MenuButton("siva", 0, 170, 275, 157, self.app)
        self.gouri = MenuButton("gouri", 293, 170, 275, 157, self.app)
        self.vignesh = MenuButton("vignesh", 585, 170, 275, 157, self.app)
        self.aniya = MenuButton("aniya", -585, 2, 275, 157, self.app)
        self.eva = MenuButton("eva", -293, 2, 275, 157, self.app)
        self.neeraj = MenuButton("neeraj", 0, 2, 275, 157, self.app)
        self.niveditha = MenuButton("niveditha", 293, 2, 275, 157, self.app)
        self.selin = MenuButton("selin", 585, 2, 275, 157, self.app)
        self.snigdha = MenuButton("snigdha", 0, -144, 275, 157, self.app)
        return self

    def __next__(self):
        self.app.t.color(255, 255, 255)
        self.app.t.write("Welcome. Please choose the shape you wish to see:",
                         False, font=("Arial", 28, "normal"), align="center")
        self.pratyush.show()
        self.abhay.show()
        self.siva.show()
        self.gouri.show()
        self.vignesh.show()
        self.aniya.show()
        self.eva.show()
        self.neeraj.show()
        self.niveditha.show()
        self.selin.show()
        self.snigdha.show()


class PostIntro(FrameManager):
    def __init__(self, app: App, circle_color: Vector):
        super(PostIntro, self).__init__(app)
        self.color = circle_color

    def __iter__(self):
        self.app.t.hideturtle()
        self.app.win.colormode(255)
        self.app.t.penup()
        self.grow_n = 1
        self.fade_n = 0
        self.max = min(self.app.dim) + 1000
        self.grown = False
        self.destruct = False
        self.increment = 1000
        self.fade_rate = 4
        return self

    def __next__(self):
        if self.grown:
            self.app.win.bgcolor(*Utils.lerp(self.color, Vector(0, 0, 0), self.fade_n).ituple())
            self.fade_n += self.fade_rate * self.app.elapsed
            if self.fade_n > 1:
                self.app.win.clearscreen()
                self.app.win.colormode(255)
                self.app.win.bgcolor(0, 0, 0)
                self.app.switch(2)
                raise StopIteration
        else:
            self.app.t.goto(0, 0)
            self.app.t.dot(self.grow_n, self.color.ituple())
            self.grow_n += self.increment * self.app.elapsed
            if self.grow_n > self.max:
                self.grown = True
                self.app.win.clearscreen()
                self.app.win.colormode(255)
                self.app.win.bgcolor(*self.color.ituple())


class PostPostIntro(FrameManager):
    def __init__(self, app: App):
        super().__init__(app)
        self.title_n = 0
        self.title_increment = 1

    def __iter__(self):
        self.app.t.hideturtle()
        self.app.t.penup()
        self.app.t.goto(0, (self.app.win.window_height() // 2) - 100)
        self.app.t.color(0, 0, 0)
        return self

    def __next__(self):
        if self.title_n < 1:
            self.app.t.color(*Utils.lerp(Vector(0, 0, 0), Vector(255, 255, 255), self.title_n).ituple())
            self.app.t.write("Welcome. Please choose the shape you wish to see:",
                             False, font=("Arial", 28, "normal"), align="center")
            self.title_n += self.title_increment * self.app.elapsed
        else:
            self.app.t.color(255, 255, 255)
            self.app.t.write("Welcome. Please choose the shape you wish to see:",
                             False, font=("Arial", 28, "normal"), align="center")
            self.app.switch(3)
            raise StopIteration


if __name__ == '__main__':
    pen = turtle.Turtle()
    window = turtle.Screen()
    application = App(pen, window)
