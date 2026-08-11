from manim import *

class GitHubScene(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GRAY
        text = Text(r"https://github.com/gootyboy/3D_movie_SoME_2026")
        self.play(Write(text), run_time=3)

        self.wait(5)

if __name__ == "__main__":
    with tempconfig({"quality": "fourk_quality", "preview": True, "disable_caching": True}):
        scene = GitHubScene()
        scene.render()
