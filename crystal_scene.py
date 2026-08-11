from crystal import *
from wave_funcs import *

class CrystalScene(ThreeDScene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(0.15)
        
        screen = Square(side_length=3.0)
        screen.set_fill(color=GRAY, opacity=0.3)
        screen.rotate(90 * DEGREES, axis=RIGHT)
        screen.move_to(np.array([0, -2.5, 0]))
        self.play(Write(screen))
        
        housing = Prism(dimensions=[3.0, 1.5, 3.0])
        housing.set_stroke(color=WHITE, width=1.5, opacity=0.3)
        housing.set_fill(color=BLUE_E, opacity=0.05)
        housing.move_to(np.array([0, 0, 0]))
        self.play(Create(housing))
            
        chaotic_wave = ParametricFunction(
            chaotic_wave_func,
            t_range=[0, 0.3, 0.01],
            stroke_width=3.5,
            color=BLUE_A
        ).rotate(90 * DEGREES, UP).scale(2).shift(DOWN * 2)
        
        left_wave = ParametricFunction(
            left_circular_polarized,
            t_range=[0.75, 1.75],
            stroke_width=4.5,
            color=GOLD
        ).shift(DOWN * 2)

        self.play(FadeIn(chaotic_wave), run_time=1.0)
        self.wait(0.5)
        self.play(FadeIn(left_wave), run_time=1.0)
        self.wait(2.3)
        self.stop_ambient_camera_rotation()
        question_mark = Tex(r"$?$", color=GREEN).scale(2)
        self.add_fixed_in_frame_mobjects(question_mark)
        self.remove(question_mark)
        self.play(Write(question_mark))
        self.wait(2)
        self.play(FadeOut(question_mark))
        self.begin_ambient_camera_rotation()
        self.wait()

        housing0 = Prism(dimensions=[3.0, 0.5, 3.0])
        housing0.set_stroke(color=WHITE, width=1.5, opacity=0.3)
        housing0.set_fill(color=BLUE_E, opacity=0.05)
        housing0.move_to(housing.get_bottom())
        housing0.shift(UP * 0.5)

        housing1 = Prism(dimensions=[3.0, 1, 3.0])
        housing1.set_stroke(color=WHITE, width=1.5, opacity=0.3)
        housing1.set_fill(color=BLUE_E, opacity=0.05)
        housing1.move_to(housing.get_top())
        housing1.shift(UP)

        grid_lines = VGroup()
        num_lines = 9
        y_positions = np.linspace(-1.3, 1.3, num_lines)

        for y in y_positions:
            line3d = Prism(
                dimensions=[0.5, 0.06, 2.8],
                fill_color=GRAY_A,
                fill_opacity=0.15,
                stroke_color=BLACK,
                stroke_width=0.5
            )
            line3d.move_to([0, y, 0])
            grid_lines.add(line3d)

        grid_lines.rotate(90 * DEGREES, IN).shift(DOWN * 0.25)

        wave0 = chaotic_wave.copy()
        wave1 = ParametricFunction(
            left_circular_polarized,
            t_range=[1, 2],
            stroke_width=4.5,
            color=GOLD
        ).shift(DOWN)
        group = VGroup(housing1, housing0)

        self.play(
            ReplacementTransform(housing, group),
            ReplacementTransform(chaotic_wave, wave0),
            ReplacementTransform(left_wave, wave1)
        )
        self.wait(0.5)
        self.play(Write(grid_lines))
        self.wait()

        wave = ParametricFunction(
            linear_wave_func,
            t_range=[0, 0.3, 0.01],
            stroke_width=3.5,
            color=BLUE_A
        ).rotate(90 * DEGREES, UP).scale(2)

        self.play(Create(wave))

        housing2 = Prism(dimensions=[3.0, 0.5, 3.0])
        housing2.set_stroke(color=WHITE, width=1.5, opacity=0.3)
        housing2.set_fill(color=BLUE_E, opacity=0.05)
        housing2.move_to(housing1.get_bottom())
        housing2.shift(UP * 0.5)

        housing3 = Prism(dimensions=[3.0, 0.5, 3.0])
        housing3.set_stroke(color=WHITE, width=1.5, opacity=0.3)
        housing3.set_fill(color=BLUE_E, opacity=0.05)
        housing3.move_to(housing1.get_top())
        housing3.shift(UP * 1.5)

        housing3_copy = housing3.copy()

        wave2 = ParametricFunction(
            left_circular_polarized,
            t_range=[1.75, 2.75],
            stroke_width=4.5,
            color=GOLD
        ).shift(DOWN)
        wave2_copy = wave2.copy()
        wave6 = ParametricFunction(
            right_circular_polarized,
            t_range=[1.75, 2.75],
            stroke_width=4.5,
            color=GOLD
        ).shift(DOWN)
        group0 = VGroup(housing2, housing3)

        self.play(ReplacementTransform(group[0], group0), ReplacementTransform(wave1, wave2))
        self.wait(2)
        off = CrystalOff(housing=housing3_copy).scale(0.75).shift(UP * 1.5)
        off_copy = off.copy()
        on = CrystalOn(housing=housing3_copy).scale(0.75).shift(UP * 1.5)
        on_copy = on.copy()
        
        self.play(FadeIn(off), run_time=0.8)
        self.wait(1.5)

        self.play(
            ReplacementTransform(off, on),
            Transform(wave2, wave6),
            run_time=2,
            rate_func=exponential_decay
        )
        self.wait(2)
        self.play(
            ReplacementTransform(on, off_copy),
            Transform(wave2, wave2_copy),
            run_time=2,
            rate_func=exponential_decay
        )
        self.wait(2)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=65 * DEGREES, theta=0 * DEGREES, run_time=2)

        wave3 = wave.copy().shift(UP * 2)
        wave4 = ParametricFunction(
            linear_wave_func,
            t_range=[0.1, 0.4, 0.01],
            stroke_width=3.5,
            color=BLUE_A
        ).rotate(90 * DEGREES, UP).scale(2).rotate(90 * DEGREES, UP).shift(RIGHT * 0.5, UP * 2, DOWN * 0.2)
        wave5 = wave3.copy().rotate(90 * DEGREES, UP).shift(RIGHT * 0.5)

        self.play(Create(wave3), Create(wave4))
        self.wait()
        self.move_camera(phi=30 * DEGREES, theta=0 * DEGREES, run_time=2)
        self.wait()
        self.move_camera(phi=65 * DEGREES, theta=0 * DEGREES, run_time=2)
        self.wait()
        self.play(
            ReplacementTransform(off_copy, on_copy),
            ReplacementTransform(wave4, wave5),
            ReplacementTransform(wave2, wave6)
        )
        self.wait()
        self.move_camera(phi=30 * DEGREES, theta=0 * DEGREES, run_time=2)
        self.wait()
        self.move_camera(phi=65 * DEGREES, theta=0 * DEGREES, run_time=2)

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "fourk_quality", "preview": True, "disable_caching": True}):
        scene = CrystalScene()
        scene.render()
