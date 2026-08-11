from manim import *

class RoundedPrism(VGroup):
    def __init__(
        self, 
        width=3.0, 
        height=2.0, 
        depth=0.5, 
        corner_radius=0.5, 
        resolution=30, 
        fill_color=BLUE, 
        stroke_width=2,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        layers = resolution
        z_step = depth / layers
        
        for i in range(layers):
            rect = RoundedRectangle(
                width=width,
                height=height,
                corner_radius=corner_radius,
                fill_color=fill_color,
                fill_opacity=1.0 if i == layers - 1 else 0.8, # Solid top, semi-transparent inside
                stroke_width=stroke_width
            )
            rect.shift(i * z_step * OUT)
            rect.set_shade_in_3d(True)
            self.add(rect)

class Glasses(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        BODY = "#1A1A1A"
        FRAME = "#2D2D2D"

        left_frame = RoundedPrism(width=2, height=4/3, depth=0.25, corner_radius=1, fill_color=FRAME, color=FRAME).shift(LEFT * 1.5)
        right_frame = left_frame.copy().shift(RIGHT * 3)
        frame_line = Line3D(start=left_frame.get_edge_center(RIGHT), end=right_frame.get_edge_center(LEFT), color=BODY, thickness=0.1)
        left_back_frame = Line3D(start=left_frame.get_edge_center(LEFT), end=left_frame.get_edge_center(LEFT) + IN * 3.25, color=BODY, thickness=0.1)
        right_back_frame = Line3D(start=right_frame.get_edge_center(RIGHT), end=right_frame.get_edge_center(RIGHT) + IN * 3.25, color=BODY, thickness=0.1)
        left_back_frame2 = Line3D(start=left_back_frame.get_end(), end=left_back_frame.get_end() + IN * 0.75 + DOWN * 0.75, color=BODY, thickness=0.1)
        right_back_frame2 = Line3D(start=right_back_frame.get_end(), end=right_back_frame.get_end() + IN * 0.75 + DOWN * 0.75, color=BODY, thickness=0.1)

        self.left_frame = left_frame
        self.right_frame = right_frame

        self.add(left_frame, right_frame, frame_line, left_back_frame, right_back_frame, left_back_frame2, right_back_frame2)
