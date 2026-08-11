from manim import *

class Eye(VGroup):
    def __init__(self, iris_color=BLUE_D, **kwargs):
        super().__init__(**kwargs)

        upper_arc = ArcBetweenPoints(start=LEFT*2, end=RIGHT*2, angle=-TAU/4, color=WHITE)
        lower_arc = ArcBetweenPoints(start=LEFT*2, end=RIGHT*2, angle=TAU/4, color=WHITE)
        self.outline = VGroup(upper_arc, lower_arc)

        iris_full = Circle(radius=1.1, color=iris_color, fill_opacity=0.8)
        eye_area = VMobject().set_fill(WHITE, opacity=1).set_stroke(width=0)
        eye_area.append_points(upper_arc.points)
        eye_area.append_points(lower_arc.points[::-1])
        self.iris = Intersection(iris_full, eye_area, color=iris_color, fill_opacity=0.8, stroke_width=2)

        self.pupil = Circle(radius=0.4, color=BLACK, fill_opacity=1.0, stroke_width=0)

        self.highlight = Circle(radius=0.12, color=WHITE, fill_opacity=1.0, stroke_width=0)
        self.highlight.shift(UP * 0.3 + RIGHT * 0.3)

        self.add(self.outline, self.iris, self.pupil, self.highlight)

class AnimateEye(AnimationGroup):
    def __init__(self, eye: Eye, run_time=1.5, **kwargs):
        animations = [
            Create(eye.outline),
            FadeIn(eye.iris, scale=0.5),
            GrowFromCenter(eye.pupil),
            FadeIn(eye.highlight)
        ]
        super().__init__(*animations, lag_ratio=0, run_time=run_time, **kwargs)
