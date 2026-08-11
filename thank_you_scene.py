from manim import *

class ThankYouScene(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        text = Paragraph("Thanks for", "Watching!", alignment="center").scale(3)
        self.play(Write(text), run_time=3)

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "fourk_quality", "preview": True, "disable_caching": True}):
        scene = ThankYouScene()
        scene.render()
