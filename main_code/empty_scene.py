from manim import *

class EmptyScene(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "fourk_quality", "preview": True, "disable_caching": True}):
        scene = EmptyScene()
        scene.render()
