from manim import *

class Eye3D(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        left_eye = Sphere(
            radius=0.6,
            resolution=(32, 32),
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=1
        ).shift(RIGHT * 3).shift(DOWN).scale(1.25)

        right_eye = Sphere(
            radius=0.6,
            resolution=(32, 32),
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=1
        ).shift(RIGHT * 3).shift(DOWN).scale(1.75)

        left_eye.stretch(0.7, dim=1)
        left_eye.stretch(0.35, dim=2)

        right_eye.stretch(0.7, dim=1)
        right_eye.stretch(0.35, dim=2)

        left_eye.shift(LEFT * 2 + DOWN)
        right_eye.shift(RIGHT * 2 + DOWN)

        left_pupil = Sphere(
            radius=0.18,
            resolution=(32, 32),
            color=BLACK,
            fill_opacity=1
        )

        right_pupil = Sphere(
            radius=0.18,
            resolution=(32, 32),
            color=BLACK,
            fill_opacity=1
        )

        left_eye.set_color(WHITE)
        right_eye.set_color(WHITE)
        left_pupil.set_color(BLACK)
        right_pupil.set_color(BLACK)

        left_pupil.move_to(left_eye.get_center() + OUT * 0.35)
        right_pupil.move_to(right_eye.get_center() + OUT * 0.35)

        left_eye_group = VGroup(left_eye, left_pupil)
        right_eye_group = VGroup(right_eye, right_pupil)

        self.left_eye_group = left_eye_group
        self.right_eye_group = right_eye_group
        self.left_eye = left_eye
        self.right_eye = right_eye
        self.left_pupil = left_pupil
        self.right_pupil = right_pupil

        self.add(left_eye_group)
        self.add(right_eye_group)
