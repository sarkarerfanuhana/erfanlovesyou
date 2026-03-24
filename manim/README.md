# Manim Code Examples for Beginners

[Manim](https://www.manim.community/) (Mathematical Animation Engine) is a Python library for creating precise, programmatic animations — popularised by the [3Blue1Brown](https://www.youtube.com/@3blue1brown) YouTube channel.

This folder contains small, focused example scripts that walk you through the most common things you will want to do in Manim.

---

## Installation

```bash
# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install Manim Community edition
pip install manim
```

You also need a working installation of **LaTeX** if you want to render `MathTex` / `Tex` objects (used in `05_math_equations.py`).  
A lightweight option is [MiKTeX](https://miktex.org/) (Windows/macOS/Linux) or `texlive-full` on Debian/Ubuntu.

---

## Running an example

Each file contains one or more `Scene` subclasses.  Pass the class name you want to render:

```bash
# Low quality (fast preview)
manim -pql 01_basic_shapes.py BasicShapes

# High quality (1080p)
manim -pqh 01_basic_shapes.py BasicShapes

# Flags:
#   -p   open the video when done
#   -ql  low quality  (480p, 15 fps)
#   -qm  medium quality (720p, 30 fps)
#   -qh  high quality  (1080p, 60 fps)
```

The rendered video will be saved under `media/videos/`.

---

## Examples overview

| File | Scene class | What it teaches |
|------|-------------|-----------------|
| `01_basic_shapes.py` | `BasicShapes` | Drawing circles, squares, and triangles |
| `02_text_animation.py` | `TextAnimation` | Writing text and animating it |
| `03_transformations.py` | `Transformations` | Morphing one shape into another |
| `04_graphs.py` | `GraphExample` | Plotting a function on axes |
| `05_math_equations.py` | `MathEquations` | Rendering LaTeX math expressions |
| `06_combined_scene.py` | `CombinedScene` | A more complex scene combining many techniques |
