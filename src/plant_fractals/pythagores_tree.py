import pgzrun
import pygame
from pgzero.rect import Rect
import math

WIDTH = 800
HEIGHT = 800
CENTERX = WIDTH / 2
CENTERY = HEIGHT / 2
CENTER = (CENTERX, CENTERY)

def rotate_rect(rect, anchor=None, target=None, angle=45):
    rect_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    rect_surf.fill("green")

    rot_surf = pygame.transform.rotate(rect_surf, angle)
    rot_rect = rot_surf.get_rect(center=rect.center)

    if anchor and target:
        setattr(rot_rect, anchor, target)

    return rot_surf, rot_rect

def scale_rect(rect):
    return rect.scale_by(math.sqrt(2)/2, math.sqrt(2)/2)

rects = []

def add_to_rects(*squares):
    global rects
    squares = list(squares)
    mid = len(squares) //2
    rects.extend(squares[:mid])
    rects.extend(reversed(squares[mid:]))

base = Rect(0, 0, 100, 100)
base.midbottom = (CENTERX, HEIGHT)
rects.append(rotate_rect(base, angle=0))

base = scale_rect(base)
add_to_rects(
    rotate_rect(base, "midbottom", rects[-1][1].topleft),
    rotate_rect(base, "midbottom", rects[-1][1].topright)
)

base = scale_rect(base)
add_to_rects(
    rotate_rect(base, "bottomleft", rects[-1][1].midright, angle=90), 
    rotate_rect(base, "bottomleft", rects[-1][1].midtop, angle=90),
    rotate_rect(base, "bottomright", rects[-2][1].midleft, angle=90),
    rotate_rect(base, "bottomright", rects[-2][1].midtop, angle=90)
)

base = scale_rect(base)
add_to_rects(
    rotate_rect(base, "midright", rects[-1][1].bottomleft, angle=135),
    rotate_rect(base, "midright", rects[-1][1].topleft, angle=135),
    rotate_rect(base, "midbottom", rects[-2][1].topleft, angle=135),
    rotate_rect(base, "midbottom", rects[-2][1].topright, angle=135),
    rotate_rect(base, "midbottom", rects[-3][1].topleft, angle=135),
    rotate_rect(base, "midbottom", rects[-3][1].topright, angle=135),
    rotate_rect(base, "midleft", rects[-4][1].topright, angle=135),
    rotate_rect(base, "midleft", rects[-4][1].bottomright, angle=135)
)

def draw():
    screen.fill("white")
    for surf, r in rects:
        screen.blit(surf, r)

pgzrun.go()
