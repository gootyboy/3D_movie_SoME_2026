from manim import *
from eye import *
from tree import *

class EyeScene(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        left_eye = Eye().scale(2)
        right_eye = Eye().shift(RIGHT * 3)
        self.play(AnimateEye(left_eye))
        self.wait()
        self.play(LaggedStart(left_eye.animate.scale(1 / 2).shift(LEFT * 3), AnimateEye(right_eye), lag_ratio=0.3), run_time=2)

        line = Line(start=LEFT * 3, end=RIGHT * 3, color=RED)
        left_endpoint = Dot(LEFT * 3, color=YELLOW)
        right_endpoint = Dot(RIGHT * 3, color=YELLOW)
        self.play(Create(line))
        self.play(GrowFromCenter(left_endpoint), run_time = 0.5)
        self.play(GrowFromCenter(right_endpoint), run_time = 0.5)

        self.wait()

        brace = Brace(line, direction=DOWN, color=GREEN)
        brace_text = Text("≈6-7 cm").next_to(brace, DOWN)
        inches_text = Text("≈2.5 in").next_to(brace_text, DOWN)

        self.play(GrowFromCenter(brace))
        self.play(Write(brace_text))
        self.wait()
        self.play(Write(inches_text))
        self.wait(2)
        self.play(FadeOut(brace_text, inches_text), brace.animate.scale(0))
        self.wait()
        self.play(line.animate.scale(0), left_endpoint.animate.scale(0), right_endpoint.animate.scale(0))
        self.wait(2)
        self.play(FadeOut(left_eye, right_eye))

        img_path = r"SoME/files/tree.png"
        tree = ImageMobject(img_path)
        tree.scale_to_fit_width(config.frame_width)
        tree.scale_to_fit_height(config.frame_height)
        tree.scale(1.25)

        both_eye_text = Text("Both Eyes", font_size=DEFAULT_FONT_SIZE * 2, gradient=[RED_C, RED_E]).to_edge(UP)
        left_eye_text = Text("Left Eye", font_size=DEFAULT_FONT_SIZE * 2, gradient=[RED_C, RED_E]).to_edge(UP)
        right_eye_text = Text("Right Eye", font_size=DEFAULT_FONT_SIZE * 2, gradient=[RED_C, RED_E]).to_edge(UP)
        layered_eye_text = Text("Left + Right Eye", font_size=DEFAULT_FONT_SIZE * 2, gradient=[RED_C, RED_E]).to_edge(UP)

        left_tree = tree.copy().shift(LEFT / 6)
        right_tree = tree.copy().shift(RIGHT / 6)
        org_tree = tree.copy()

        self.play(FadeIn(tree))
        self.wait()
        self.play(Write(both_eye_text))
        self.wait()
        self.play(FadeOut(both_eye_text))
        self.wait()
        self.play(Transform(tree, left_tree))
        self.wait()
        self.play(Write(left_eye_text))
        self.wait()
        self.play(FadeOut(left_eye_text))
        self.wait()
        self.play(Transform(tree, right_tree))
        self.wait()
        self.play(Write(right_eye_text))
        self.wait()
        self.play(FadeOut(right_eye_text))
        self.wait(2)
        self.play(FadeIn(left_tree), left_tree.animate.set_opacity(0.25), tree.animate.set_opacity(0.75))
        self.wait()
        self.add_foreground_mobject(layered_eye_text)
        self.play(Write(layered_eye_text))
        self.wait(2)
        self.play(FadeOut(layered_eye_text))
        self.wait()
        self.play(left_tree.animate.move_to(org_tree.get_center()).set_opacity(0), left_tree.animate.move_to(org_tree.get_center()).set_opacity(0), FadeIn(org_tree))
        self.wait()
        self.play(FadeOut(left_tree, right_tree, tree, org_tree))
        self.wait(2)

        tree = Tree3D().scale(0.9).shift(UP * 2 + IN * 6).shift(RIGHT * 3).shift(DOWN).scale(1.25)

        eyes = Eye3D()
        left_eye = eyes.left_eye.copy()
        right_eye = eyes.right_eye.copy()
        left_pupil = eyes.left_pupil
        right_pupil = eyes.right_pupil
        left_eye_group = VGroup(left_eye, left_pupil).set_opacity(0)
        right_eye_group = VGroup(right_eye, right_pupil).set_opacity(0)
        draw_left_eye = VGroup(left_eye.copy().set_opacity(0.5).rotate(90 * DEGREES, RIGHT))
        draw_right_eye = draw_left_eye.copy().shift(RIGHT * 4)

        self.play(AnimateTree(tree))

        self.play(
            Create(draw_left_eye),
            Create(draw_right_eye)
        )

        self.wait()

        eye_line = always_redraw(lambda: Line(
            start=left_eye.get_center(),
            end=right_eye.get_center(),
            color=RED
        ))

        self.play(Create(eye_line))
        self.wait()

        left_ray = always_redraw(lambda: Line(start=left_eye.get_center(), end=tree.get_center() + LEFT * 0.25, color=YELLOW))
        center = (left_eye.get_center() + right_eye.get_center()) / 2
        center_ray = Line(start=center, end=center + UP * 3.1)
        right_ray = always_redraw(lambda: Line(start=right_eye.get_center(), end=tree.get_center() + LEFT * 0.25, color=BLUE))

        self.play(Create(left_ray), Create(right_ray), Create(center_ray))

        left_right_angle = RightAngle(eye_line, center_ray, color=PURPLE).scale(2 / 3)
        right_right_angle = RightAngle(eye_line, center_ray, color=PURPLE).scale(2 / 3)

        self.wait()
        self.play(Write(left_right_angle), Write(right_right_angle))
        self.wait(3)

        brace = always_redraw(lambda: Brace(eye_line, stroke_width=4, sharpness=4, color=YELLOW))
        text = MathTex("B", color=PINK).next_to(brace, DOWN)
        self.play(Write(brace))
        self.play(Write(text))

        b_2_text = MathTex(r"B/2", color=GREEN).next_to(eye_line, UP).shift(LEFT * 0.5, DOWN * 0.2)
        self.wait()
        self.play(Write(b_2_text))
        self.wait(3)

        z_text = MathTex("Z", color=YELLOW).next_to(center_ray).shift(DOWN * 0.2, LEFT * 0.2)
        self.play(Write(z_text))
        self.wait(5)

        theta = MathTex(r"\theta", color=BLUE).move_to(tree).shift(DOWN * 0.5, LEFT * 0.4)
        self.play(Write(theta))
        self.wait(2)

        equation = MathTex(r"\tan (\quad) = \dfrac{\text{opposite}}{\text{adjacent}}").shift(LEFT * 3).scale(2)
        equation0 = MathTex(r"\tan (").shift(LEFT * 5).scale(2)
        equation1 = MathTex(r") = ").scale(2).next_to(equation0, buff=0.4)
        equation2 = MathTex(r"\dfrac{\quad\quad}{\quad\quad}").scale(2).next_to(equation1)
        theta_copy0 = theta.copy()
        theta_copy = theta.copy()
        b_2_text_copy = b_2_text.copy()
        z_text_copy = z_text.copy()
        equations = VGroup(equation0, equation1, equation2)

        self.play(Succession(Write(equation), theta_copy0.animate.scale(2).move_to(equation.get_left() + RIGHT * 2)))
        self.wait()

        self.play(
            ReplacementTransform(VGroup(equation, theta_copy0), equations),
            theta_copy.animate.scale(2).move_to(equation0.get_right() + RIGHT * 0.3),
            b_2_text_copy.animate.scale(1.75).move_to(equation2.get_top() + UP * 0.4),
            z_text_copy.animate.scale(1.75).move_to(equation2.get_bottom() + DOWN * 0.4),
            run_time=3,
            rate_func=smooth
        )
        self.wait(2)

        target_equation0 = MathTex(r"\tan (").shift(LEFT * 5).scale(2)
        target_equation1 = MathTex(r") = ").scale(2).next_to(equation0, buff=0.4)
        target_equation2 = MathTex(r"\dfrac{\quad\quad}{\quad\quad}").scale(2).next_to(equation1)
        target_equations = VGroup(target_equation0, target_equation1, target_equation2)
        current_group = VGroup(equation0, theta_copy, equation1, equation2, b_2_text_copy, z_text_copy)
        theta_copy2 = theta.copy()
        text_copy = text.copy()
        z_copy = z_text.copy()
        text2 = MathTex("2").scale(2).move_to(equation2.get_bottom() + DOWN * 0.4 + LEFT * 0.3)
        tan_equation = VGroup(target_equations, theta_copy2, text_copy, z_copy, text2)

        self.play(
            ReplacementTransform(current_group, target_equations),
            theta_copy2.animate.scale(2).move_to(target_equation0.get_right() + RIGHT * 0.3),
            text_copy.animate.scale(1.75).move_to(equation2.get_top() + UP * 0.4),
            z_copy.animate.scale(1.75).move_to(equation2.get_bottom() + DOWN * 0.4 + RIGHT * 0.3),
            FadeIn(text2),
            run_time=3,
            rate_func=smooth,
        )
        self.wait(2)

        self.play(FadeOut(theta_copy0, tan_equation, tree, center_ray, left_ray, right_ray, eye_line, draw_right_eye, draw_left_eye, theta, text, b_2_text, brace, right_right_angle, left_right_angle, z_text), run_time=3)
        self.wait()

        x_values = {
            0: r"$0$",
            np.pi / 12: r"$\dfrac{\pi}{12}$",
            np.pi / 6: r"$\dfrac{\pi}{6}$",
            np.pi / 4: r"$\dfrac{\pi}{4}$",
            np.pi / 3: r"$\dfrac{\pi}{3}$",
            5 * np.pi / 12: r"$\dfrac{5\pi}{12}$",
            np.pi / 2: r"$\dfrac{\pi}{2}$"
        }

        plane = NumberPlane(
            x_range=[0, np.pi / 2 + 0.05, np.pi / 12],  
            y_range=[0, 4.1, 1],  
            x_length=10, 
            y_length=5,
            axis_config={"include_numbers": False} 
        ).shift(UP * 1.25)
        plane.x_axis.add_labels(x_values)
        plane.y_axis.add_numbers([1, 2, 3, 4])

        shared_x_range = [0, np.pi / 2 - 0.2]

        tan_curve = plane.plot(
            lambda x: np.tan(x), 
            x_range=shared_x_range, 
            color=YELLOW
        )

        linear_curve = plane.plot(
            lambda x: x,
            x_range=shared_x_range,
            color=BLUE
        )

        tan_label = MathTex(r"y", r" = \tan(", r"x", r")", tex_to_color_map={r"x": YELLOW, r"y": PINK}).next_to(tan_curve, RIGHT, buff=0.1).shift(UP * 0.5)
        linear_label = MathTex(r"y", r"=", r"x", tex_to_color_map={r"x": YELLOW, r"y": PINK}).next_to(linear_curve, RIGHT, buff=0.1)

        self.play(Create(plane), run_time=2)
        self.wait()
        
        self.play(
            Create(tan_curve),
            Create(linear_curve),
            run_time=3,
            rate_func=linear
        )
        
        self.play(Write(tan_label), Write(linear_label), run_time=2.5)
        self.wait(2)

        new_x_vals = {
            0: r"$0^{\circ}$",
            np.pi / 36: r"$\dfrac{\pi}{36}$",
            np.pi / 18: r"$\dfrac{\pi}{18}$",
            np.pi / 12: r"$\dfrac{\pi}{12}$",
            np.pi / 9: r"$\dfrac{\pi}{9}$",
            5 * np.pi / 36: r"$\dfrac{5\pi}{36}$",
            np.pi / 6: r"$\dfrac{\pi}{6}$"
        }

        new_plane = NumberPlane(
            x_range=[0, np.pi / 6 + 0.05, np.pi / 36],  
            y_range=[0, 4.1, 1],  
            x_length=10, 
            y_length=5,
            axis_config={"include_numbers": False} 
        ).shift(UP * 1.25)
        new_plane.x_axis.add_labels(new_x_vals)
        new_plane.y_axis.add_numbers([1, 2, 3, 4])

        new_shared_x_range = [0, np.pi / 6 - 1 / 36]

        new_tan_curve = new_plane.plot(
            lambda x: np.tan(x), 
            x_range=new_shared_x_range, 
            color=YELLOW
        )

        new_linear_curve = new_plane.plot(
            lambda x: x,
            x_range=new_shared_x_range,
            color=BLUE
        )

        new_tan_label = MathTex(r"y", r"= \tan(", r"x", r")", tex_to_color_map={r"x": YELLOW, r"y": PINK}).next_to(new_tan_curve, RIGHT, buff=0.1).shift(UP * 0.5)
        new_linear_label = MathTex(r"y", r"=", r"x", tex_to_color_map={r"x": YELLOW, r"y": PINK}).next_to(new_linear_curve, RIGHT, buff=0.1)
        zoom_text = Tex("Zoom ", r"$3$", "x").scale(1.5).shift(UP * 2)
        zoom_text.set_color_by_tex(r"$3$", RED_C)

        self.play(ReplacementTransform(tan_curve, new_tan_curve), ReplacementTransform(linear_curve, new_linear_curve), ReplacementTransform(plane, new_plane), ReplacementTransform(tan_label, new_tan_label), ReplacementTransform(linear_label, new_linear_label), Write(zoom_text), run_time=2)
        self.wait(2)

        tanx_x_eq0 = (
            Tex(
                r"$\tan($", r"$x$", r"$)\approx$", r"$x$",
                color=BLUE
            )
            .set_color_by_tex(r"$x$", YELLOW)
            .scale(2)
            .next_to(new_plane, DOWN)
        )
        tanx_x_eq1 = Tex("for small values of ", r"$x$").next_to(tanx_x_eq0, DOWN)
        tanx_x_eq1.set_color_by_tex(r"$x$", YELLOW)
        tanx_x_eq1.set_color_by_tex("for small values of ", BLUE)

        self.play(Write(tanx_x_eq0))
        self.play(Write(tanx_x_eq1))
        self.wait(2)

        self.play(FadeOut(tanx_x_eq0, tanx_x_eq1, new_plane, new_tan_curve, new_tan_label, new_linear_curve, new_linear_label, zoom_text), run_time=2)
        self.play(FadeIn(tan_equation, tree, center_ray, left_ray, right_ray, eye_line, draw_right_eye, draw_left_eye, theta, text, b_2_text, brace, right_right_angle, left_right_angle, z_text), run_time=3)

        new_equation = MathTex(r"\theta \approx \dfrac{B}{2Z}").scale(2).move_to(equation1)
        alpha = always_redraw(lambda: MathTex(r"\alpha").next_to(tree, DOWN).shift(UP * 1.75, LEFT * 0.3))
        new_equation1 = MathTex(r"Z \approx \dfrac{B}{\alpha}").scale(2).move_to(equation1)
        new_equation2 = MathTex(r"\theta \cdot Z \approx \dfrac{B}{2}").scale(2).move_to(equation1)
        new_equation3 = MathTex(r"Z \approx \dfrac{B}{2\theta}").scale(2).move_to(equation1)

        self.play(ReplacementTransform(tan_equation, new_equation))
        self.wait()
        self.play(ReplacementTransform(new_equation, new_equation2))
        self.wait()
        self.play(ReplacementTransform(new_equation2, new_equation3))
        self.wait(2)
        self.play(FadeOut(center_ray, theta, b_2_text, z_text, left_right_angle, right_right_angle), run_time=2.5)
        self.play(Write(alpha), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(new_equation3, new_equation1))
        self.wait(7.5)

        self.play(tree.animate.shift(UP * 2))
        self.wait(6.5)
        self.play(tree.animate.shift(DOWN * 4))
        self.wait(6.5)
        self.play(tree.animate.shift(UP * 2))
        self.wait(6.5)
        self.play(draw_left_eye.animate.shift(LEFT * 1.75), draw_right_eye.animate.shift(RIGHT * 1.75), left_eye_group.animate.shift(LEFT * 1.75), right_eye_group.animate.shift(RIGHT * 1.75))
        self.wait(7.5)
        self.play(draw_left_eye.animate.shift(RIGHT * 3), draw_right_eye.animate.shift(LEFT * 3), left_eye_group.animate.shift(RIGHT * 3), right_eye_group.animate.shift(LEFT * 3))
        self.wait(7.5)
        self.play(draw_left_eye.animate.shift(LEFT * 1.75), draw_right_eye.animate.shift(RIGHT * 1.75), left_eye_group.animate.shift(LEFT * 1.75), right_eye_group.animate.shift(RIGHT * 1.75))
        self.wait(5)
        self.play(FadeOut(alpha, text, brace, eye_line, draw_left_eye, draw_right_eye, new_equation1, tree, left_ray, right_ray))

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "fourk_quality", "preview": True, "disable_caching": True}):
        scene = EyeScene()
        scene.render()
