from manim import *

class FilmCamera(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        BODY_COLOR = "#1A1A1A"
        RIG_COLOR = "#2D2D2D"
        GLASS_COLOR = "#00E5FF"
        ACCENT_COLOR = "#FF3366"
        SCREEN_COLOR = "#0D1B2A"

        self.body = Cube(side_length=1.0, color=BODY_COLOR, fill_opacity=1).scale(np.array([1.6, 1.2, 1.2])).rotate(PI/2, axis=RIGHT).shift(UP * 0.6)
        
        handle_grip = Cube(side_length=0.2, color=RIG_COLOR, fill_opacity=1).scale(np.array([1.2, 1.0, 1.0])).next_to(self.body, UP, buff=0.2).shift(LEFT * 0.2)
        handle_post1 = Line3D(start=self.body.get_top() + LEFT * 0.5, end=handle_grip.get_left(), color=RIG_COLOR, thickness=0.05)
        handle_post2 = Line3D(start=self.body.get_top() + RIGHT * 0.1, end=handle_grip.get_right(), color=RIG_COLOR, thickness=0.05)
        self.top_handle = VGroup(handle_grip, handle_post1, handle_post2)

        lens_barrel = Line3D(start=self.body.get_left(), end=self.body.get_left() + LEFT * 0.6, color=BODY_COLOR, thickness=0.3)

        matte_box = Prism(dimensions=[0.05, 1.4, 1.4], color=RIG_COLOR, fill_opacity=1).next_to(lens_barrel, LEFT, buff=0)

        lens_flare = Prism(dimensions=[0.01, 1.2, 1.2], color=GLASS_COLOR, fill_opacity=0.6).move_to(matte_box.get_left() + LEFT * 0.01)
        self.lens_assembly = VGroup(lens_barrel, matte_box, lens_flare)

        monitor_arm = Line3D(start=self.body.get_right() + UP * 0.2, end=self.body.get_right() + RIGHT * 0.4 + UP * 0.4, color=RIG_COLOR, thickness=0.04)
        monitor_frame = Cube(side_length=0.5, color=BODY_COLOR, fill_opacity=1).scale(np.array([0.2, 2.0, 1.4])).move_to(monitor_arm.get_end() + RIGHT * 0.1).rotate(PI / 12, axis=UP)

        monitor_screen = Prism(dimensions=[0.01, 0.6, 0.9], color=SCREEN_COLOR, fill_opacity=1).move_to(monitor_frame.get_right() + RIGHT * 0.01)
        self.monitor = VGroup(monitor_arm, monitor_frame, monitor_screen)

        dial_outer = Cylinder(radius=0.18, height=0.05, color=RIG_COLOR, fill_opacity=1).rotate(PI / 2, axis=RIGHT).move_to(self.body.get_boundary_point(OUT) + UP * 0.1)
        dial_inner = Cylinder(radius=0.08, height=0.06, color=ACCENT_COLOR, fill_opacity=1).rotate(PI / 2, axis=RIGHT).move_to(dial_outer.get_center())
        self.focus_dial = VGroup(dial_outer, dial_inner)

        baseplate = Cube(side_length=1.0, color=RIG_COLOR, fill_opacity=1).scale(np.array([1.8, 0.15, 1.4])).next_to(self.body, DOWN, buff=0)
        rod_l = Line3D(start=[-1.2, -0.15, 0.4], end=[0.8, -0.15, 0.4], color=GREY_A, thickness=0.03)
        rod_r = Line3D(start=[-1.2, -0.15, -0.4], end=[0.8, -0.15, -0.4], color=GREY_A, thickness=0.03)
        self.rig_base = VGroup(baseplate, rod_l, rod_r)

        self.camera_rig = VGroup(self.top_handle, self.lens_assembly, self.body, self.monitor, self.focus_dial, self.rig_base)

        fluid_head = Cube(side_length=1.0, color=BODY_COLOR, fill_opacity=1).scale(np.array([0.8, 0.6, 0.8])).next_to(baseplate, DOWN, buff=0)
        pan_handle = Line3D(start=fluid_head.get_center(), end=fluid_head.get_center() + RIGHT * 1.4 + DOWN * 0.4 + OUT * 0.3, color=RIG_COLOR, thickness=0.04)
        self.tripod_top = VGroup(fluid_head, pan_handle)

        leg_fl = Line3D(start=fluid_head.get_bottom() + LEFT * 0.1 + OUT * 0.1, end=[-1.2, -3.5, 1.2], color=RIG_COLOR, thickness=0.06)
        leg_fr = Line3D(start=fluid_head.get_bottom() + RIGHT * 0.1 + OUT * 0.1, end=[1.2, -3.5, 1.2], color=RIG_COLOR, thickness=0.06)
        leg_b = Line3D(start=fluid_head.get_bottom() + IN * 0.1, end=[0.0, -3.5, -1.5], color=BODY_COLOR, thickness=0.06)

        spreader_fl = Line3D(start=[-0.6, -1.9, 0.6], end=[0.0, -1.9, 0.0], color=RIG_COLOR, thickness=0.03)
        spreader_fr = Line3D(start=[0.6, -1.9, 0.6], end=[0.0, -1.9, 0.0], color=RIG_COLOR, thickness=0.03)
        spreader_b = Line3D(start=[0.0, -1.9, -0.75], end=[0.0, -1.9, 0.0], color=RIG_COLOR, thickness=0.03)

        self.tripod_legs = VGroup(leg_fl, leg_fr, leg_b, spreader_fl, spreader_fr, spreader_b)
        self.tripod_assembly = VGroup(self.tripod_top, self.tripod_legs)

        self.add(self.tripod_assembly, self.camera_rig)

class AnimateCamera(AnimationGroup):
    def __init__(self, camera: FilmCamera, **kwargs):
        animations = [
            Create(camera.tripod_legs, run_time=0.4),
            Succession(
                Wait(0.2),
                DrawBorderThenFill(camera.tripod_top, run_time=0.2)
            ),
            Succession(
                Wait(0.4),
                AnimationGroup(
                    FadeIn(camera.rig_base, shift=UP),
                    FadeIn(camera.body, shift=UP),
                    run_time=0.3
                )
            ),
            Succession(
                Wait(0.6),
                AnimationGroup(
                    Create(camera.lens_assembly),
                    Create(camera.top_handle),
                    FadeIn(camera.monitor, shift=RIGHT),
                    GrowFromCenter(camera.focus_dial),
                    run_time=0.4
                )
            )
        ]
        super().__init__(*animations, lag_ratio=0, **kwargs)
