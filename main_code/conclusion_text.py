from manim import *

class ConclusionTextScene(Scene):
    def construct(self):
        config.max_files_cached = 10
        self.camera.background_color = DARKER_GRAY

        text = Text("Conclusion").scale(4)

        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "fourk_quality", "preview": True, "disable_caching": True}):
        scene = ConclusionTextScene()
        scene.render()
