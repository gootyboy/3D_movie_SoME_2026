# 3D_movie_SoME_2026

A collection of Manim (3D) scenes, helper modules, and assets used to produce a short visual explanation about how 3D movies and stereoscopic rendering work. The project demonstrates stereoscopic concepts (eyes, cameras, disparity, depth) using procedural 3D tree fractals, camera rigs, and annotated math.

Video (SoME 2026 submission): LINK_HERE

---

## Quick overview

- Primary language: Python (Manim Community Edition)
- Purpose: Render and animate 3D scenes that illustrate stereoscopic concepts for a short educational video
- Entry points: scene files in `main_code/`; reusable primitives in `main_code/helper_files/`

---

## Repository structure

```
main_code/                       # Scene entry points and scripts
  intro_scene.py                 # Title + visual introduction (eyes, cameras, glasses)
  camera_scene.py                # Stereo camera demo and disparity/depth derivations
  eye_scene.py                   # Eye-focused demonstrations
  one_eye_scene.py               # Single-eye examples
  glasses_scene.py               # 3D glasses demos (anaglyph/polarization/crystal)
  crystal_scene.py               # Polarization/crystal examples
  github_scene.py                # Small supporting scene
  conclusion_text.py             # Text used in the conclusion
  thank_you_scene.py             # End screens / credits
  empty_scene.py                 # Minimal placeholder scene
  helper_files/                  # Reusable 3D primitives and utilities
    camera.py
    tree.py                      # Procedural Tree3D and AnimateTree
    eye.py
    eye3D.py
    glasses.py
    crystal.py
    wave_funcs.py

images/                           # Image assets used by scenes (sky, left/right eye, anaglyph examples)
videos/                           # (Optional) exported renders / intermediate video files
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

## Installation

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -U pip
pip install manim numpy pillow
```

(Optional) Create a requirements.txt or pin versions for reproducibility.

---

## How to render scenes

From the repository root, use the Manim CLI. Example commands:

```bash
# Preview intro scene (low quality + preview)
manim -pql main_code/intro_scene.py IntroScene

# Render camera scene in higher quality
manim -pqh main_code/camera_scene.py CameraScene
```

Notes:
- Several scene files use `tempconfig(...)` with presets (e.g., `low_quality`, `fourk_quality`). You can override these by removing the preset or by passing CLI flags.
- Some scenes reference absolute image paths (e.g., `/Volumes/...`) — replace these with repository-relative paths (for example `images/sky.png`) so renders work on other machines. Search for `/Volumes/` and update as needed.

---

## Important details & tips

- Large image assets increase render time and memory use. If you hit memory limits, try lower rendering quality or downsample images.
- Scene files follow the standard Manim pattern: define a Scene class and render it via the CLI.
- If you get unexpected caching behavior, use Manim flags to clear caches or set `disable_caching=True` in `tempconfig`.

---

## Scenes of particular interest

- CameraScene: Demonstrates stereo camera rigs, disparity math, and the derivation of depth (d) as a function of focal length and camera separation.
- IntroScene: Title and visual introduction covering eyes, cameras, and glasses.
- Tree3D (helper): A procedural 3D tree used to show depth and parallax.

---

## Contributing

Contributions are welcome. A few guidelines:
- Reference assets with relative paths (e.g., `images/...`) so scenes run out-of-the-box.
- Add or update a `requirements.txt` when new dependencies are introduced.
- Keep PRs small and focused; include a brief description of the change and rendering notes if applicable.

---

## License

No license file is currently included. If you intend to share or allow reuse, add a LICENSE (e.g., MIT) to make terms explicit.

---

## Contact & acknowledgements

- Author: gootyboy
- Built for: 3Blue1Brown SoME 2026 submission
- If you want, I can:
  - Add a LICENSE file (MIT recommended)
  - Replace absolute image paths with repository-relative paths
  - Add a pinned requirements.txt

---

(Updated README by GitHub Copilot assistant.)
