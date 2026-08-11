from manim import *
from helper_files.tree import *
from helper_files.camera import *

class CameraScene(ThreeDScene):
    def construct(self):
        config.max_files_cached = 10
        self.camera.background_color = DARKER_GRAY

        self.set_camera_orientation(phi=90 * DEGREES)

        camera = FilmCamera().rotate(90 * DEGREES, RIGHT)
        self.play(AnimateCamera(camera), run_time=2)
        self.wait()

        tree = Tree3D().move_to(camera.get_center()).move_to(LEFT * 10).shift(DOWN)
        self.play(AnimateTree(tree), run_time=2)
        self.move_camera(theta=0 * DEGREES, run_time=3)
        self.wait(1)
        midpoint = (tree.get_center() + camera.get_center()) / 2

        self.move_camera(phi=0 * DEGREES, run_time=3, zoom=0.5, frame_center=midpoint)

        line = Line3D(start=camera.get_center() + LEFT, end=camera.get_center() + LEFT * 9, color=YELLOW).shift(OUT * 1.5).shift(DOWN * 0.2)
        self.play(Write(line), run_time=2)
        self.wait(2)
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, zoom=0.75, run_time=3)

        self.wait()
        self.play(Unwrite(line), run_time=2)
        self.wait()

        camera1 = camera.copy().shift(DOWN)
        camera2 = camera.copy().shift(UP)

        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, run_time=3, zoom=0.5, frame_center=midpoint, added_anims=[Succession(FadeOut(camera), AnimationGroup(AnimateCamera(camera1, run_time=2), AnimateCamera(camera2, run_time=2)), lag_ratio=2)])

        line1 = Line3D(start=camera1.get_center() + LEFT, end=camera1.get_center() + LEFT * 9, color=YELLOW).shift(OUT * 1.5).shift(DOWN * 0.2)
        line2 = Line3D(start=camera2.get_center() + LEFT, end=camera2.get_center() + LEFT * 9, color=YELLOW).shift(OUT * 1.5).shift(DOWN * 0.2)
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, run_time=3, zoom=0.4, frame_center=midpoint)
        self.play(Write(line1), Write(line2), run_time=2)

        camera1_group = VGroup(camera1, line1)
        camera2_group = VGroup(camera2, line2)

        self.play(AnimationGroup(AnimateCamera(camera1, run_time=2), AnimateCamera(camera2, run_time=2)), run_time=2)

        def get_brace(text, sharp=2, width=6, mob1=camera1, mob2=camera2, points=None):
            if points != None:
                mob1 = Dot(point=points[0])
                mob2 = Dot(point=points[1])

            p1 = mob1.get_center()
            p2 = mob2.get_center()
            brace = BraceBetweenPoints(p1, p2, stroke_width=width, sharpness=sharp)
            label = text
            label.next_to(brace, RIGHT, buff=0.1)

            group = VGroup(brace, label)

            def update_brace_and_label(mob):
                current_p1 = mob1.get_center()
                current_p2 = mob2.get_center()

                new_brace = BraceBetweenPoints(current_p1, current_p2, stroke_width=width, sharpness=sharp)
                mob[0].become(new_brace)

                mob[1].next_to(mob[0], RIGHT, buff=0.1)

            group.add_updater(update_brace_and_label)
            return group

        brace = always_redraw(lambda: get_brace(Text("Distance?").rotate(90 * DEGREES, OUT)))

        self.wait(2)
        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, zoom=0.75, run_time=3)
        self.wait()

        self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES, run_time=3, zoom=0.4, frame_center=midpoint)
        self.play(Write(brace), run_time=2)

        self.play(camera1_group.animate.shift(DOWN * 2), camera2_group.animate.shift(UP * 2))
        self.wait()
        self.play(camera1_group.animate.shift(UP * 2), camera2_group.animate.shift(DOWN * 2))
        self.wait()
        brace2 = always_redraw(lambda: get_brace(Text("d").rotate(90 * DEGREES, OUT)))
        self.play(FadeOut(brace), FadeIn(brace2), run_time=2)

        self.wait()
        self.play(FadeOut(line1, line2), run_time=2)

        far_line = Line3D(start=camera1.get_center() + LEFT, end=camera1.get_center() + LEFT * 12, color=YELLOW).shift(OUT * 1.5).shift(DOWN * 0.2)
        far_brace = Brace(far_line, sharpness=0.5, stroke_width=2)
        far_text = MathTex(r"D_{far}", stroke_width=2).next_to(far_brace, DOWN).rotate(90 * DEGREES).scale(2).shift(DOWN * 0.5)
        d_far = VGroup(far_line, far_brace, far_text).shift(DOWN)

        self.wait()
        self.play(Write(d_far), run_time=2)

        near_line = Line3D(start=camera2.get_center() + LEFT, end=camera2.get_center() + LEFT * 8, color=YELLOW).shift(OUT * 1.5).shift(DOWN * 0.2)
        near_brace = Brace(near_line, UP, sharpness=0.5, stroke_width=2)
        near_text = MathTex(r"D_{near}", stroke_width=2).next_to(near_brace, UP).rotate(90 * DEGREES).scale(2).shift(UP * 0.75)
        d_near = VGroup(near_line, near_brace, near_text).shift(UP)

        self.wait()
        self.play(Write(d_near), run_time=2)

        self.wait()
        self.play(tree.animate.set_opacity(0.1))

        center_point = (camera1.get_center() + camera2.get_center()) / 2
        center_line = Line3D(start=center_point + LEFT, end=center_point + LEFT * 10, color=BLUE).shift(DOWN * 0.2, LEFT, OUT * 5)

        self.wait()
        self.play(Write(center_line), run_time=2)

        camera1_copy1 = camera1.copy().shift(UP * 0.5).shift(LEFT)
        camera1_copy2 = camera1.copy().shift(DOWN * 0.5).shift(UP * 0.2).shift(LEFT)
        near_point = center_point + (LEFT * 8)
        far_point = center_point + (LEFT * 10.5)
        left_d_near_line = Line3D(start=camera1_copy1.get_center() + LEFT, end=near_point, color=RED_C).shift(DOWN * 0.2, OUT * 5)
        left_d_near_points = VGroup(Dot3D(left_d_near_line.get_start(), color=YELLOW, radius=0.15).shift(OUT * 5, DOWN * 0.2), Dot3D(left_d_near_line.get_end(), color=YELLOW, radius=0.15).shift(OUT * 5, DOWN * 0.2))
        left_d_near_anim = AnimationGroup(GrowFromCenter(left_d_near_line), GrowFromCenter(left_d_near_points[0]), GrowFromCenter(left_d_near_points[1]))
        left_d_far_line = Line3D(start=camera1_copy2.get_center() + LEFT, end=far_point, color=RED_C).shift(DOWN * 0.2).shift(OUT * 5)
        left_d_far_points = VGroup(Dot3D(left_d_far_line.get_start(), color=YELLOW, radius=0.15).shift(OUT * 5, DOWN * 0.2), Dot3D(left_d_far_line.get_end(), color=YELLOW, radius=0.15).shift(OUT * 5, DOWN * 0.2))
        left_d_far_anim = AnimationGroup(GrowFromCenter(left_d_far_line), GrowFromCenter(left_d_far_points[0]), GrowFromCenter(left_d_far_points[1]))
        left_d_anim = AnimationGroup(left_d_far_anim, left_d_near_anim)

        near_point += DOWN * 0.4
        far_point += DOWN * 0.4
        camera2_copy1 = camera2.copy().shift(DOWN * 0.5).shift(LEFT, UP * 0.2, DOWN * 0.4)
        camera2_copy2 = camera2.copy().shift(UP * 0.5).shift(LEFT, DOWN * 0.4)
        right_d_near_line = Line3D(start=camera2_copy1.get_center() + LEFT, end=near_point, color=RED_C).shift(UP * 0.2, OUT * 5)
        right_d_near_points = VGroup(Dot3D(right_d_near_line.get_start(), color=YELLOW, radius=0.15).shift(OUT * 5, UP * 0.2), Dot3D(right_d_near_line.get_end(), color=YELLOW, radius=0.15).shift(OUT * 5, UP * 0.2))
        right_d_near_anim = AnimationGroup(GrowFromCenter(right_d_near_line), GrowFromCenter(right_d_near_points[0]), GrowFromCenter(right_d_near_points[1]))
        right_d_far_line = Line3D(start=camera2_copy2.get_center() + LEFT, end=far_point, color=RED_C).shift(UP * 0.2).shift(OUT * 5)
        right_d_far_points = VGroup(Dot3D(right_d_far_line.get_start(), color=YELLOW, radius=0.15).shift(OUT * 5, UP * 0.2), Dot3D(right_d_far_line.get_end(), color=YELLOW, radius=0.15).shift(OUT * 5, UP * 0.2))
        right_d_far_anim = AnimationGroup(GrowFromCenter(right_d_far_line), GrowFromCenter(right_d_far_points[0]), GrowFromCenter(right_d_far_points[1]))
        right_d_anim = AnimationGroup(right_d_far_anim, right_d_near_anim)


        self.wait()
        self.play(Succession(left_d_anim, right_d_anim), run_time=2)
        self.wait(7.5)

        all_mobjects = VGroup(camera1, camera2, tree, d_far, d_near, left_d_near_line, left_d_far_line, right_d_near_line, right_d_far_line, right_d_near_points, left_d_near_points, left_d_far_points, right_d_far_points, center_line, brace, brace2)
        self.play(FadeOut(all_mobjects), run_time=3)
        self.wait(2)

        eq1 = MathTex(r"\frac{x_{l}}{f}=\frac{X}{Z}").rotate(90 * DEGREES).scale(4).shift(UP * 7.5, LEFT * 10)
        eq2 = MathTex(r"x_{l}=\frac{f \cdot X}{Z}").rotate(90 * DEGREES).scale(4).move_to(eq1)

        self.play(Write(eq1), run_time=2)
        self.wait(5)
        self.play(ReplacementTransform(eq1, eq2), run_time=2)
        self.wait()

        eq3 = MathTex(r"\frac{x_{r}}{f}=\frac{X-d}{Z}").rotate(90 * DEGREES).scale(4).move_to(eq1).shift(DOWN * 15)
        eq4 = MathTex(r"x_{r}=\frac{f\cdot (X-d)}{Z}").rotate(90 * DEGREES).scale(4).move_to(eq3)
        self.play(Write(eq3), run_time=2)
        self.wait(5)
        self.play(ReplacementTransform(eq3, eq4), run_time = 2)
        self.wait()

        eq5 = MathTex(r"P=x_{l} - x_{r}").rotate(90 * DEGREES).scale(4)
        eq6 = MathTex(r"P=\left(\frac{f\cdot X}{Z}\right)-\left(\frac{f\cdot (X-d)}{Z}\right)").scale(4).rotate(90 * DEGREES)
        self.play(Write(eq5), run_time=2)
        self.wait(3)
        self.play(ReplacementTransform(eq5, eq6), run_time = 2)
        self.wait()

        eq7 = MathTex(r"P=\frac{f\cdot X-f\cdot X+f\cdot d}{Z}").rotate(90 * DEGREES).scale(4)
        eq8 = MathTex(r"P=\frac{f\cdot d}{Z}").rotate(90 * DEGREES).scale(4)
        eq9 = MathTex(r"P_{\text{max}}=P_{\text{near}}-P_{\text{far}}").rotate(90 * DEGREES).scale(4)
        eq0 = MathTex(r"P_{\text{max}}=\frac{f\cdot d}{D_{\text{near}}}-\frac{f\cdot d}{D_{\text{far}}}").rotate(90 * DEGREES).scale(4)
        eq10 = MathTex(r"P_{\text{max}}=\frac{f\cdot d\cdot D_{\text{far}}}{D_{\text{near}}\cdot D_{\text{far}}}-\frac{f\cdot d\cdot D_{\text{near}}}{D_{\text{far}}\cdot D_{\text{near}}}").rotate(90 * DEGREES).scale(4)
        eq11 = MathTex(r"P_{\text{max}}=\frac{f\cdot d\cdot D_{\text{far}} - f\cdot d\cdot D_{\text{near}}}{D_{\text{near}}\cdot D_{\text{far}}}").rotate(90 * DEGREES).scale(4)
        eq12 = MathTex(r"P_{\text{max}} = \frac{f \cdot d \cdot \left(D_{\text{far}} - D_{\text{near}}\right)}{D_{\text{near}} \cdot D_{\text{far}}}").rotate(90 * DEGREES).scale(4)
        eq13 = MathTex(r"P_{\text{max}} \cdot \left(D_{\text{near}} \cdot D_{\text{far}}\right) = f \cdot d \cdot \left(D_{\text{far}} - D_{\text{near}}\right)").rotate(90 * DEGREES).scale(3.5)
        eq14 = MathTex(r"d = \frac{P_{\text{max}} \cdot D_{\text{near}} \cdot D_{\text{far}}}{f \cdot \left(D_{\text{far}} - D_{\text{near}}\right)}").scale(4).rotate(90 * DEGREES)
        eq15 = MathTex(r"d = \frac{P_{\text{max}} \cdot D_{\text{near}} \cdot D_{\text{far}}}{f \cdot \left(D_{\text{far}} - D_{\text{near}}\right)}").scale(5).rotate(90 * DEGREES).shift(LEFT * 5)

        self.play(ReplacementTransform(eq6, eq7), run_time=2)
        self.wait()
        self.play(ReplacementTransform(eq7, eq8), run_time = 2)
        self.wait()
        self.play(FadeOut(eq8), FadeIn(eq9), run_time=2)
        self.wait(5)
        self.play(FadeOut(eq9), FadeIn(eq0), run_time=2)
        self.wait(3)
        self.play(ReplacementTransform(eq0, eq10), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(eq10, eq11), run_time=2)
        self.wait()
        self.play(ReplacementTransform(eq11, eq12), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(eq12, eq13), run_time=2)
        self.wait(2)
        self.play(ReplacementTransform(eq13, eq14), run_time=2)
        self.wait()
        self.play(FadeOut(eq2, eq4), run_time=2)
        self.wait()
        self.play(ReplacementTransform(eq14, eq15, run_time=2))
        self.wait(10)
        self.play(FadeOut(eq15), run_time=2)

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "fourk_quality", "preview": True, "disable_caching": True}):
        scene = CameraScene()
        scene.render()
