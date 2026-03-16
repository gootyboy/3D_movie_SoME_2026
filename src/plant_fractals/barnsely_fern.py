import pygame
import random
from pgzero.rect import Rect
import matplotlib.pyplot as plt
import turtle
import pgzrun

class BarnselyFern:
    def __init__(self, iterations):
        points = []
        xpoints = []
        ypoints = []

        x_prev = 0
        y_prev = 0

        for i in range(iterations):
            num = random.random()
            if 0 <= num <= 0.01:
                x = 0
                y = 0.16 * y_prev
            elif 0.01 < num <= 0.86:
                x = 0.85 * x_prev + 0.04 * y_prev
                y = -0.04 * x_prev + 0.85 * y_prev + 1.6
            elif 0.86 < num <= 0.93:
                x = 0.2 * x_prev - 0.26 * y_prev
                y = 0.23 * x_prev + 0.22 * y_prev + 1.6
            elif 0.93 < num <= 1:
                x = -0.15 * x_prev + 0.28 * y_prev
                y = 0.26 * x_prev + 0.24 * y_prev + 0.44

            x_prev = x
            y_prev = y

            points.append((x, y))
            xpoints.append(x)
            ypoints.append(y)

        self.points = points
        self.iterations = iterations
        self.ypoints = ypoints
        self.xpoints = xpoints

    def draw_pygame(self, surface, scale = 30, thickness = 1, color = "green", pos = (300, 300)):
        surface.fill("white")
        for point in self.points:
            pygame.draw.rect(surface, color, pygame.rect.Rect(point[0] * scale + pos[0], point[1] * scale + pos[1], thickness, thickness))

    def draw_pgzero(self, screen, scale, thickness = 1, color = "green", pos = (300, 300)):
        screen.fill("white")
        for point in self.points:
            screen.draw.rect(Rect(point[0] * scale + pos[0], point[1] * scale + pos[1], thickness, thickness), color = color)

    def plot_matplotlib(self, thickness = 0.2, edgecolors = "black", linewidths = 0.1, facecolors = "skyblue", color = None, *args, **kwargs):
        plt.scatter(
            self.xpoints, self.ypoints,
            s=thickness,
            edgecolors=edgecolors,
            linewidths=linewidths,
            facecolors=facecolors,
            c=color,
            *args,
            **kwargs
        )

    def draw_turtle(self, pen: turtle.Turtle, color = "green", instant = False, speed = 0, end_turtle = False):
        start_color = pen.color()[0]
        start_speed = pen.speed()
        start_tracer = turtle.tracer()
        if instant:
            turtle.tracer(0)
        pen.color(color)
        for point in self.points:
            pen.penup()
            pen.speed(0)
            pen.goto(*point)
            pen.speed(speed)
            pen.pendown()
            pen.begin_fill()
            for i in range(4):
                pen.forward(1)
                pen.left(90)
            pen.end_fill()
        pen.color(start_color)
        pen.speed(start_speed)
        turtle.tracer(start_tracer)
        if end_turtle:
            turtle.done()

def draw():
    BarnselyFern(10000).draw_pgzero(screen, 30)

def update():
    pass

