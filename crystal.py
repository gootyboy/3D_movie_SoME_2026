from manim import *

class CrystalOff(VGroup):
    def __init__(self, housing, **kwargs):
        super().__init__(**kwargs)
        box_width, box_height, box_depth = housing.width, housing.height, housing.depth
        
        num_layers = 12
        z_positions = np.linspace(-box_depth / 2.2, box_depth / 2.2, num_layers)
        x_coords = np.linspace(-box_width / 4, box_width / 4, 3)
        y_coords = np.linspace(-box_height / 4, box_height / 4, 3)
        
        for i, z in enumerate(z_positions):
            fraction = i / (num_layers - 1)
            twist_angle = fraction * 90 * DEGREES
            for x in x_coords:
                for y in y_coords:
                    rod = Line(start=LEFT*0.6, end=RIGHT*0.6, stroke_width=7, color=GOLD)
                    rod.rotate(twist_angle, axis=OUT)
                    rod.move_to(np.array([x, y, z]))
                    self.add(rod)

class CrystalOn(VGroup):
    def __init__(self, housing, **kwargs):
        super().__init__(**kwargs)
        box_width, box_height, box_depth = housing.width, housing.height, housing.depth
        
        num_layers = 12
        z_positions = np.linspace(-box_depth / 2.2, box_depth / 2.2, num_layers)
        x_coords = np.linspace(-box_width / 4, box_width / 4, 3)
        y_coords = np.linspace(-box_height / 4, box_height / 4, 3)
        
        for z in z_positions:
            for x in x_coords:
                for y in y_coords:
                    # Performance Fix: Standing straight up along the Z axis (OUT direction)
                    rod = Line(start=IN*0.6, end=OUT*0.6, stroke_width=7, color=GREEN_A)
                    rod.move_to(np.array([x, y, z]))
                    self.add(rod)