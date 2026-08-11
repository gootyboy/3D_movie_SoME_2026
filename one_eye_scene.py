from tree import *
from eye import *

class OneEyeScene(ThreeDScene):
    def construct(self):
        self.camera.background_color = DARKER_GREY

        tree = Tree3D().scale(0.9).shift(UP * 2 + IN * 6, RIGHT).shift(RIGHT * 3).shift(DOWN).scale(1.25)

        eyes = Eye3D()
        left_eye = eyes.left_eye.copy()
        right_eye = eyes.right_eye.copy()
        left_pupil = eyes.left_pupil
        right_pupil = eyes.right_pupil
        left_eye_group = VGroup(left_eye, left_pupil).set_opacity(0)
        right_eye_group = VGroup(right_eye, right_pupil).set_opacity(0)
        draw_left_eye = VGroup(left_eye.copy().set_opacity(0.5).rotate(90 * DEGREES, RIGHT))
        draw_right_eye = draw_left_eye.copy().shift(RIGHT * 4)

        eye_line = Line(start=left_eye.get_center(), end=right_eye.get_center(), color=RED)

        left_ray = Line(start=left_eye.get_center(), end=tree.get_center() + LEFT * 0.25, color=YELLOW)
        right_ray = always_redraw(lambda: Line(start=right_eye.get_center(), end=tree.get_center() + LEFT * 0.25, color=BLUE))

        brace = Brace(eye_line, stroke_width=4, sharpness=4, color=YELLOW)
        text = MathTex("B", color=PINK).next_to(brace, DOWN)

        alpha = MathTex(r"\alpha").next_to(tree, DOWN).shift(UP * 1.75, LEFT * 0.3)

        equation0 = MathTex(r"\tan (").shift(LEFT * 5).scale(2)
        equation1 = MathTex(r") = ").scale(2).next_to(equation0, buff=0.4)
        equation = MathTex(r"Z \approx \dfrac{B}{\alpha}").scale(2).move_to(equation1)

        self.add(equation, eye_line, tree, draw_left_eye, draw_right_eye, left_ray, right_ray, brace, text, alpha)
        self.wait(3)
        self.play(FadeOut(brace, text, draw_left_eye, left_ray, equation, eye_line, alpha))
        self.wait()
        self.play(draw_right_eye.animate.shift(LEFT * 2), right_eye.animate.shift(LEFT * 2))
        self.wait()
        self.play(tree.animate.shift(LEFT * 4), draw_right_eye.animate.shift(LEFT * 3), right_eye.animate.shift(LEFT * 3))

        vibration_amplitude = 0.05
        number_of_shakes = 35
        run_time_per_shake = 0.04

        for i in range(number_of_shakes):
            self.play(
                draw_right_eye.animate.shift(RIGHT * vibration_amplitude),
                right_eye.animate.shift(RIGHT * vibration_amplitude),
                run_time=run_time_per_shake,
                rate_func=linear
            )
            self.play(
                draw_right_eye.animate.shift(LEFT * vibration_amplitude),
                right_eye.animate.shift(LEFT * vibration_amplitude),
                run_time=run_time_per_shake,
                rate_func=linear
            )

        self.wait()
        center = self.camera.frame_center
        self.move_camera(zoom=15, frame_center=right_eye.get_left(), run_time=3)
        self.wait()
        right_eye2 = draw_right_eye.copy().shift(LEFT * vibration_amplitude)
        self.play(draw_right_eye.animate.set_opacity(0.75), Write(right_eye2), right_eye2.animate.set_opacity(0.25))
        line = Line3D(draw_right_eye.get_left(), right_eye2.get_left(), 0.01)
        line_brace = Brace(line, color=YELLOW).stretch_to_fit_height(0.05).next_to(line, DOWN, buff=0.02)
        line_text = Text("B", color=PINK).scale(0.1).next_to(line_brace, DOWN, buff=0.05)
        self.wait()
        self.play(GrowFromCenter(line), Write(line_brace), Write(line_text))
        self.wait(2)
        right_ray2 = always_redraw(lambda: Line(start=right_eye2.get_center(), end=tree.get_center() + LEFT * 0.25, color=YELLOW))
        self.move_camera(zoom=1, frame_center=center, run_time=3, added_anims=[FadeOut(line, line_brace, line_text)])
        self.add(right_ray2)
        self.wait(2)
        eye_line2 = always_redraw(lambda: Line(start=left_eye.get_center(), end=right_eye.get_center(), color=RED))
        eye_line3 = always_redraw(lambda: Line(start=eye_line2.get_start(), end=eye_line2.get_start() + LEFT * 2, color=RED))
        brace2 = always_redraw(lambda: Brace(eye_line2, color=YELLOW))
        text2 = always_redraw(lambda: Text("B", color=PINK).next_to(brace2, DOWN))
        self.play(FadeIn(eye_line2, brace2, text2, eye_line3))
        self.play(draw_right_eye.animate.shift(RIGHT * 3), right_eye2.animate.shift(RIGHT), right_eye.animate.shift(RIGHT * 3), run_time=3)
        self.wait()

        beta = MathTex(r"\beta").move_to(eye_line2.get_start() + LEFT * 0.5 + UP * 0.3)
        gamma = MathTex(r"\gamma").move_to(beta).shift(RIGHT * 1.8)
        self.play(Write(beta), Write(gamma))
        alpha2 = MathTex(r"\alpha").next_to(tree, DOWN).shift(UP * 1.75, RIGHT * 0.3)
        beta_180 = MathTex(r"180^\circ - \beta").scale(0.5).next_to(beta, RIGHT, buff=0.25)
        self.wait()
        self.play(Write(alpha2), Write(beta_180))
        self.wait()
        eq = MathTex(r"\alpha = ?").scale(2).to_corner(UL)
        eq0 = MathTex(r"= 180^\circ - \left(\gamma + 180^\circ - \beta\right)").to_corner(UL).shift(DOWN)
        eq1 = MathTex(r"= 180^\circ - \gamma - 180^\circ + \beta").to_corner(UL).shift(DOWN * 2)
        eq2 = MathTex(r"= \beta - \gamma").scale(2).to_corner(UL).shift(DOWN * 3)
        eqs = VGroup(eq, eq0, eq1, eq2)
        eq3 = MathTex(r"\alpha = \beta - \gamma").scale(2).to_edge(LEFT)

        self.play(Write(eq))
        self.wait()
        self.play(TransformFromCopy(eq, eq0))
        self.wait()
        self.add(eq0)
        self.play(TransformFromCopy(eq0, eq1))
        self.wait()
        self.add(eq1)
        self.play(TransformFromCopy(eq1, eq2))
        self.wait()
        self.add(eqs)
        self.remove(eq0, eq1, eq2)
        self.play(ReplacementTransform(eqs, eq3))
        self.wait()
        self.play(FadeOut(eq3))

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "fourk_quality", "preview": True, "disable_caching": True}):
        scene = OneEyeScene()
        scene.render()
