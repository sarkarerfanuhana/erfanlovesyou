"""
01_basic_shapes.py
==================
Introduces the fundamental building blocks of Manim: geometric mobjects
(Circle, Square, Triangle), positioning, colour, and basic animations
(Create, FadeIn, FadeOut).

Run with:
    manim -pql 01_basic_shapes.py BasicShapes
"""

from manim import (
    Scene,
    Circle,
    Square,
    Triangle,
    Create,
    FadeIn,
    FadeOut,
    RED,
    BLUE,
    GREEN,
    LEFT,
    RIGHT,
    UP,
    DOWN,
    WHITE,
)


class BasicShapes(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Create three shapes and arrange them side by side
        # ------------------------------------------------------------------
        circle = Circle(radius=1, color=RED)
        square = Square(side_length=2, color=BLUE)
        triangle = Triangle(color=GREEN)

        # shift() moves a mobject relative to its current position
        circle.shift(LEFT * 3)
        triangle.shift(RIGHT * 3)

        # ------------------------------------------------------------------
        # 2. Draw each shape with the Create animation
        # ------------------------------------------------------------------
        self.play(Create(circle))
        self.play(Create(square))
        self.play(Create(triangle))
        self.wait(1)

        # ------------------------------------------------------------------
        # 3. Fill the shapes with colour (opacity 0.4 = semi-transparent)
        # ------------------------------------------------------------------
        self.play(
            circle.animate.set_fill(RED, opacity=0.4),
            square.animate.set_fill(BLUE, opacity=0.4),
            triangle.animate.set_fill(GREEN, opacity=0.4),
        )
        self.wait(1)

        # ------------------------------------------------------------------
        # 4. Move the shapes around
        # ------------------------------------------------------------------
        self.play(
            circle.animate.shift(UP),
            square.animate.shift(DOWN),
            triangle.animate.shift(UP),
        )
        self.wait(0.5)

        # ------------------------------------------------------------------
        # 5. Fade everything out
        # ------------------------------------------------------------------
        self.play(FadeOut(circle), FadeOut(square), FadeOut(triangle))
        self.wait(0.5)
