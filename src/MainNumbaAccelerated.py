from math import sqrt
from time import perf_counter, sleep
from threading import Thread
from numba import jit
from ArtIntegrated.Final.src import playsound
import random
import turtle
import os
import numpy as np


class Infinity:
    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        self.n += 1
        return self.n


class Utils:
    debug = False

    """@staticmethod
    @jit(nopython=True)
    def clamp(num: float, min_value: float, max_value: float) -> float:
        return max(min(num, max_value), min_value)"""

    @staticmethod
    def frange(start: float, stop: float, step: float):
        while start < stop:
            yield float(start)
            start += step

    @staticmethod
    @jit(nopython=True)
    def lerp(a: np.ndarray, b: np.ndarray, t: float) -> np.ndarray:
        #t = np.clip(t, 0, 1)
        t = np.minimum(1, np.maximum(t, 0))
        return (a * (1 - t)) + (b * t)

    @staticmethod
    @jit(nopython=True)
    def aabb(x1: float, y1: float, x2: float, y2: float, x: float, y: float) -> bool:
        return x1 <= x <= x2 and y1 <= y <= y2

    @staticmethod
    @jit(nopython=True)
    def random_color() -> np.ndarray:
        return np.array([round(random.random() * 255), round(random.random() * 255), round(random.random() * 255)])

    @staticmethod
    def asset(path: str) -> str:
        return os.path.join(os.getcwd(), path)

    @staticmethod
    @jit(nopython=True)
    def distance(p0: np.ndarray, p1: np.ndarray):
        return sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2 + (p0[2] - p1[2]) ** 2)


class App:
    def __init__(self, t: turtle.Turtle, win: turtle._Screen, fps_limit: int = 60):
        self.flags = {"press": False}
        self.t = t
        self.win = win
        self.win.tracer(0)
        self.win.setup(width=1.0, height=1.0, startx=None, starty=None)
        self.win.listen()
        self.win.onkey(self.close, "a")
        self.screen = self.win.getcanvas()
        self.screen.bind('<Motion>', self.mouse)
        self.manager = Intro(self, np.array([233, 5, 100]), np.array([0, 100, 50]))
        self.elapsed = 0.0
        self.fps = fps_limit
        self.motion_funcs = []
        self.music_thread = Thread(target=self.music, daemon=True)
        self.music_thread.start()
        self.mainloop()

    def mainloop(self):
        t0 = perf_counter()
        for frame in self.manager:
            t1 = perf_counter()
            self.elapsed = abs(t1 - t0)
            if self.elapsed > (1 / self.fps):
                self.win.update()
                print(self.elapsed)
            t0 = perf_counter()

    def music(self):
        for i in Infinity():
            playsound.playsound("audio/music.mp3")
            playsound.playsound("audio/music2.mp3")
            playsound.playsound("audio/music3.mp3")

    def sfx(self):
        for i in Infinity():
            if self.flags["press"]:
                playsound.playsound("audio/press.mp3", block=False)
                self.flags["press"] = False

    def mouse(self, event):
        if not self.motion_funcs:
            return
        x, y = event.x - self.win.window_width() // 2, self.win.window_height() // 2 - event.y
        for func in self.motion_funcs:
            func(x, y)

    def close(self):
        self.music_thread.join()
        quit(0)


class FrameManager:
    def __init__(self, app: App):
        self.app = app

    def __iter__(self):
        self.app.t.hideturtle()
        self.app.win.bgcolor("black")
        self.app.win.colormode(255)
        return self

    def __next__(self):
        pass


class Intro(FrameManager):
    def __init__(self, app: App, colorA: np.ndarray, colorB: np.ndarray):
        super().__init__(app)
        self.a = colorA
        self.b = colorB
        self.increment = 1

    def __iter__(self):
        self.n = 0
        self.app.t.hideturtle()
        self.app.win.colormode(255)
        self.app.win.bgcolor(0, 0, 0)
        self.app.t.penup()
        self.app.t.goto(0, 0)
        self.app.t.color(255, 255, 255)
        self.app.t.write("Note: This program has not been optimized much, so you might experience some lag.",
                         False, font=("Arial", 28, "normal"), align="center")
        sleep(3)
        for i in Utils.frange(0, 1, 0.01):
            self.app.t.color(tuple(map(int, Utils.lerp(np.array([255, 255, 255]), np.array([0, 0, 0]), i))))
            self.app.t.write("Note: This program has not been optimized much, so you might experience some lag.",
                             False, font=("Arial", 28, "normal"), align="center")
        self.app.win.clearscreen()
        self.app.win.bgcolor(0, 0, 0)
        self.start = Button(0, -250, Utils.asset("img/start/default.gif"), Utils.asset("img/start/highlight.gif"),
                            240, 140, lambda: print("Clicked!"), self.app)
        self.app.win.colormode(255)
        return self

    def __next__(self):
        self.app.t.color(tuple(map(int, Utils.lerp(self.a, self.b, self.n))))
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
        return


class Button:
    def __init__(self, x: int, y: int,
                 default_img: str, highlight_img: str,
                 img_x: int, img_y: int,
                 click_func, app: App):
        self.default = default_img
        self.highlight = highlight_img
        self.dimensions = (img_x, img_y)
        self.app = app
        self.t = turtle.Turtle()
        self.t.goto(x, y)
        self.app.win.onscreenclick(self.start_click)
        self.click_func = click_func
        self.app.motion_funcs.append(self.hover)
        self.app.win.addshape(self.default)
        self.app.win.addshape(self.highlight)
        self.t.shape(self.default)
        self.not_highlighted = True

    def is_mouse_over(self, x: int, y: int):
        t_x = self.t.xcor() - (self.dimensions[0] // 2)
        t_y = self.t.ycor() - (self.dimensions[1] // 2)
        return Utils.aabb(t_x, t_y, t_x + self.dimensions[0], t_y + self.dimensions[1], x, y)
        
    def hover(self, x: int, y: int):
        """if collides and self.not_highlighted:
            self.t.shape(self.highlight)
            self.not_highlighted = False
        elif not (collides or self.not_highlighted):
            self.t.shape(self.default)
            self.not_highlighted = True"""
        if self.is_mouse_over(x, y):
            self.t.shape(self.highlight)
        else:
            self.t.shape(self.default)

    def start_click(self, x, y):
        if self.is_mouse_over(x, y):
            playsound.playsound("audio/press.mp3", block=False)


if __name__ == '__main__':
    pen = turtle.Turtle()
    window = turtle.Screen()
    application = App(pen, window)
