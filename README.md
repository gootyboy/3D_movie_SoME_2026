# 3D_movie_SoME_2026

A collection of Manim (3D) scenes, helper modules, and assets used to produce a short visual explanation about how 3D movies and stereoscopic rendering work. The project demonstrates stereoscopic concepts (eyes, cameras, disparity, depth) using procedural 3D tree fractals, camera rigs, and annotated math.

Video (SoME 2026 submission): (https://www.youtube.com/watch?v=OuoVlWlmYdk)

SoME competition link: (https://some.3b1b.co/)

---

## Quick overview

- Primary language: Python (Manim Community Edition)
- Purpose: Render and animate 3D scenes that illustrate stereoscopic concepts for a short educational video
- Entry points: scene files in `main_code/`; reusable primitives in `main_code/helper_files/`

---

## Repository structure

```
main_code/
  intro_scene.py
  camera_scene.py
  eye_scene.py
  one_eye_scene.py
  glasses_scene.py
  crystal_scene.py
  github_scene.py
  conclusion_text.py
  thank_you_scene.py
  empty_scene.py
  helper_files/
    camera.py
    tree.py
    eye.py
    eye3D.py
    glasses.py
    crystal.py
    wave_funcs.py

images/
videos/
.gitignore
README.md
```

How it fits together: Each scene defines a Manim Scene class which composes primitives from `helper_files/` and image assets from `images/`. Use Manim CLI to render a scene (examples below). Procedural objects like `Tree3D` are used across scenes to demonstrate depth cues and stereo disparities.

---

## Stack

- Language: Python 3.8+ (Python 3.10+ recommended)
- Framework: Manim Community Edition (3D support)
- Notable libraries: manim, numpy, pillow (for image handling)

---

## How to render scenes

From the repository root, use the Manim CLI. Example commands:

```bash
# Preview intro scene (low quality + preview)
manim -pql main_code/intro_scene.py IntroScene

# Render camera scene in higher quality
manim -pqk main_code/camera_scene.py CameraScene
```

Notes:
- Several scene files use `tempconfig(...)` with presets (e.g., `low_quality`, `fourk_quality`). You can override these by removing the preset or by passing CLI flags.
- Some scenes reference absolute image paths (e.g., `/Volumes/...`) — replace these with repository-relative paths (for example `images/sky.png`) so renders work on other machines. Search for `/Volumes/` and update as needed.

---

