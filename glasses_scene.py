from eye import *
from glasses import *
from manim import *

class GlassesScene(ThreeDScene):
    def construct(self):
        config.max_files_cached = 10
        self.camera.background_color = DARKER_GRAY

        question = Paragraph(
            "How", "Do", "3D Glasses", "Work?", 
            alignment="center",
            t2c={"3D Glasses": YELLOW}
        ).center().scale(3)
        self.wait()
        self.play(Write(question), run_time=3)
        self.wait(5)
        self.play(FadeOut(question), run_time=2)

        tree = ImageMobject(r"/Volumes/Samsung 990 1TB/projects/python__coding/SoME/files/tree.png").set_opacity(0.75)
        tree.scale_to_fit_width(config.frame_width)
        tree.scale_to_fit_height(config.frame_height)
        tree.scale(1.25)
        tree2 = tree.copy().set_opacity(0.5)
        tree.shift(LEFT / 6)
        tree2.shift(RIGHT / 6)
        tree_copy = tree.copy()
        tree2_copy = tree2.copy()

        self.play(FadeIn(tree, tree2), run_time=2)

        x = Cross(tree)

        self.wait()
        self.play(Write(x), run_time=2)
        self.wait(2)
        self.play(FadeOut(x, tree, tree2))

        delays = [0.5, 0.25, 0.1, 0.05, 0.02] + [0.01] * 35 

        tree.set_opacity(1)
        tree2.set_opacity(1)
        self.play(FadeIn(tree))

        current_tree = tree
        next_tree = tree2

        for dt in delays:
            self.remove(current_tree)
            self.add(next_tree)
            self.wait(dt)
            current_tree, next_tree = next_tree, current_tree

        self.remove(current_tree)
        self.add(tree_copy, tree2_copy)
        self.wait(5)
        self.play(FadeOut(tree, tree2, current_tree, next_tree, tree_copy, tree2_copy))

        left_center_x = -3.5
        left_center_z = -3
        left_axis = Line(start=[left_center_x - 2, 0, left_center_z], end=[left_center_x + 2, 0, left_center_z], color=GRAY)
        left_title = Text("Left Filter (Clockwise)", color=BLUE).scale(0.5)

        right_center_x = 3.5
        right_axis = Line(start=[right_center_x - 2, 0, 0], end=[right_center_x + 2, 0, 0], color=GRAY)
        right_title = Text("Right Filter (Counter-Clockwise)", color=RED).scale(0.5)

        self.add(left_axis, right_axis)
        self.add_fixed_in_frame_mobjects(left_title.to_edge(UL), right_title.to_edge(UR))

        time_tracker = ValueTracker()

        left_wave = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                t + left_center_x,
                np.sin(4 * t - time_tracker.get_value() * 6),
                np.cos(4 * t - time_tracker.get_value() * 6) + left_center_z
            ]),
            t_range=[-2, 2],
            color=BLUE
        ))

        right_wave = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                t + right_center_x,
                np.sin(4 * t + time_tracker.get_value() * 6),
                -np.cos(4 * t + time_tracker.get_value() * 6)
            ]),
            t_range=[-2, 2],
            color=RED
        ))

        self.play(Create(left_wave), Create(right_wave), run_time=2)
        self.wait()
        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait()
        self.play(time_tracker.animate.set_value(7.5), run_time=7.5, rate_func=linear)
        self.wait()
        self.play(FadeOut(right_wave, left_wave, left_axis, right_axis, right_title, left_title), run_time=2)
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        glasses = Glasses()
        self.play(Create(glasses))
        self.play(Rotate(glasses, TAU * 0.9, DOWN), run_time=7.5)
        self.play(glasses.animate.shift(LEFT * 2))
        left_center = glasses.left_frame.get_center()

        glasses_time_tracker = ValueTracker()
        glasses_right_wave = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                t,
                np.sin(4 * t + glasses_time_tracker.get_value() * 6),
                -np.cos(4 * t + glasses_time_tracker.get_value() * 6)
            ]),
            t_range=[-2, 5],
            color=RED
        ).shift(LEFT * 2.5, IN * 1.5).rotate(TAU * 0.9, DOWN).scale(0.5))
        glasses_left_wave = always_redraw(lambda: ParametricFunction(
            lambda t: np.array([
                t + left_center[0],
                np.sin(4 * t - glasses_time_tracker.get_value() * 6) + left_center[1],
                np.cos(4 * t - glasses_time_tracker.get_value() * 6) + left_center[2]
            ]),
            t_range=[-2, 5],
            color=BLUE
        ).shift(RIGHT * 2.5, IN * 2.5).rotate(TAU * 0.9, DOWN).scale(0.5))

        self.wait()
        self.play(Create(glasses_right_wave), Create(glasses_left_wave), run_time=2)
        self.wait()
        self.play(glasses_time_tracker.animate.set_value(7.5), run_time=7.5, rate_func=linear)
        self.wait(3)
        self.play(FadeOut(glasses_left_wave, glasses_right_wave))
        self.wait(2)

        self.play(glasses.animate.rotate(TAU * 0.1 + PI, DOWN).center(), run_time=5)
        self.wait(5)
        self.play(FadeOut(glasses))

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "fourk_quality"
    "", "preview": True, "disable_caching": True}):
        scene = GlassesScene()
        scene.render()
