from helper_files.glasses import *
from helper_files.tree import *
from helper_files.eye import *
from helper_files.camera import *

class IntroScene(ThreeDScene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        config.max_files_cached = 10

        img_path = r"/Volumes/Samsung 990 1TB/projects/3D_movie_SoME_2026/photos/sky.png"
        blur_img_path = r"/Volumes/Samsung 990 1TB/projects/3D_movie_SoME_2026/photos/blurred_sky.png"
        image = ImageMobject(img_path)
        blurred_image = ImageMobject(blur_img_path)
        rotated_image = image.rotate(90 * DEGREES, UP).rotate(90 * DEGREES, RIGHT)
        blurred = blurred_image.rotate(90 * DEGREES, UP).rotate(90 * DEGREES, RIGHT)

        self.set_camera_orientation(phi=90 * DEGREES, theta=90 * DEGREES)
        self.move_camera(theta=0 * DEGREES, run_time=3, added_anims=[FadeIn(rotated_image, run_time=3)])
        self.wait(10)
        self.play(Transform(rotated_image, blurred, run_time=2))
        self.wait(5)

        question = Paragraph(
            "How do", "3D Movies", "Work?", 
            alignment="center",
            t2c={"3D Movies": YELLOW}, 
            font_size=DEFAULT_FONT_SIZE * 1.5
        ).center().set_opacity(0)

        self.add_fixed_in_frame_mobjects(question)
        self.play(Write(question.set_opacity(1)))
        self.wait(3)
        self.play(FadeOut(question), run_time=2)
        self.wait()
        self.play(FadeOut(blurred, rotated_image), run_time=2)
        self.wait()
        self.set_camera_orientation(phi=70 * DEGREES, theta=-135 * DEGREES)

        eye_box = Rectangle().to_corner(UL, buff=0.5).shift(DOWN)
        camera_box = Rectangle().to_edge(UP, buff=0.5).shift(DOWN)
        glasses_box = Rectangle().to_corner(UR, buff=0.5).shift(DOWN)

        eye_shift = eye_box.get_center()
        left_eye = Eye().scale(0.7).shift(eye_shift)
        right_eye = Eye().shift(RIGHT * 1.05, eye_shift).scale(0.35)
        eye_text = Paragraph("How Do", "Eyes Perceive", "Depth?", alignment="center").next_to(eye_box, DOWN)
        left_eye.pupil.timer = 0
        right_eye.pupil.timer = 0
        def blink(mob, dt):
            mob.timer += dt

            hidden_duration = 0.1
            visible_duration = 1.0
            total_cycle = hidden_duration + visible_duration
            cycle_time = mob.timer % total_cycle
            opacity = 0.0 if cycle_time < hidden_duration else 1.0
            
            mob.set_style(fill_opacity=opacity, stroke_opacity=opacity)

        self.play(Create(eye_box), run_time=2)
        self.wait()
        self.play(AnimateEye(left_eye))
        self.wait()
        self.play(LaggedStart(left_eye.animate.scale(0.5).shift(LEFT * 1.05), AnimateEye(right_eye), lag_ratio=0.3), Write(eye_text), run_time=2)
        left_eye.pupil.add_updater(blink)
        right_eye.pupil.add_updater(blink)
        self.wait()

        camera_shift = camera_box.get_edge_center(UP) + RIGHT * 0.35
        left_camera = FilmCamera().scale(0.35).shift(camera_shift, LEFT * 1.05).rotate(90 * DEGREES, DOWN)
        right_camera = FilmCamera().scale(0.35).shift(RIGHT * 0.525, camera_shift).rotate(90 * DEGREES, DOWN)
        cameras = VGroup(left_camera, right_camera)
        camera_text = Paragraph("How To", "Record A", "3D Movie?", alignment="center").next_to(camera_box, DOWN) 

        def rotate_func(mob, dt):
            return mob.rotate(dt, DOWN)

        self.play(Create(camera_box), run_time=2)
        self.wait()

        self.play(Create(cameras))
        self.wait()

        cameras.add_updater(rotate_func)
        self.play(Write(camera_text))

        glasses = Glasses().move_to(glasses_box).match_width(glasses_box).scale(0.85)
        glasses_text = Paragraph("How Do", "3D Glasses", "Work?").next_to(glasses_box, DOWN)

        self.play(Create(glasses_box), run_time=2)
        self.wait()
        self.play(Create(glasses))
        self.wait()
        glasses.add_updater(lambda mob, dt: mob.rotate(dt, DOWN))
        self.play(Write(glasses_text))
        self.wait()
        self.play(FadeOut(eye_text))
        self.wait()
        self.play(FadeOut(camera_text))
        self.wait()
        self.play(FadeOut(glasses_text))
        self.wait()
        self.play(FadeOut(eye_box))
        self.wait()
        self.play(FadeOut(camera_box))
        self.wait()
        self.play(FadeOut())

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "low_quality", "preview": True, "disable_caching": True}):
        scene = IntroScene()
        scene.render()
