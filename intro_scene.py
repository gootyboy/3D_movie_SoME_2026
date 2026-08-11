from glasses import *
from tree import *
from eye import *
from camera import *

class IntroScene(ThreeDScene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        config.max_files_cached = 10

        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        camera_shift_mob = Mobject().to_edge()
        camera_shift = (UP) + RIGHT * 0.35
        left_camera = FilmCamera().shift(camera_shift, LEFT * 1.05).rotate(90 * DEGREES, DOWN)
        right_camera = FilmCamera().shift(RIGHT * 0.525, camera_shift).rotate(90 * DEGREES, DOWN)
        cameras = VGroup(left_camera, right_camera)
        camera_text = Paragraph("My Own", "3D Movie", alignment="center").next_to(camera_box, DOWN)
        def rotate_func(mob, dt):
            return mob.rotate(dt, DOWN)

        self.play(Create(cameras))
        self.wait()
        cameras.add_updater(rotate_func)
        self.play(Write(camera_text))
        self.wait(10)

        self.play(FadeOut(camera_text, cameras))
        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "low_quality", "preview": True, "disable_caching": True}):
        scene = IntroScene()
        scene.render()
