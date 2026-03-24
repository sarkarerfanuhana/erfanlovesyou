"""
03_transformations.py
=====================
Demonstrates the Transform and ReplacementTransform animations, which morph
one mobject into another.  Also shows how to use AnimationGroup and
simultaneous animations.

Run with:
    manim -pql 03_transformations.py Transformations
"""

from manim import (
    Scene,
    Circle,
    Square,
    Star,
    Triangle,
    Transform,
    ReplacementTransform,
    AnimationGroup,
    Create,
    FadeOut,
    RED,
    BLUE,
    YELLOW,
    GREEN,
    LEFT,
    RIGHT,
)


class Transformations(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Draw a circle, then morph it into a square
        #    Transform keeps the *original* Python object alive (it just
        #    looks like the target); ReplacementTransform actually replaces it.
        # ------------------------------------------------------------------
        circle = Circle(radius=1.5, color=RED)
        self.play(Create(circle))
        self.wait(0.5)

        square = Square(side_length=3, color=BLUE)
        self.play(Transform(circle, square))
        self.wait(1)

        # ------------------------------------------------------------------
        # 2. Morph the square (still `circle` under the hood) into a triangle
        # ------------------------------------------------------------------
        triangle = Triangle(color=YELLOW).scale(2)
        self.play(Transform(circle, triangle))
        self.wait(1)

        # ------------------------------------------------------------------
        # 3. Fade out, then show a side-by-side morph with two objects
        # ------------------------------------------------------------------
        self.play(FadeOut(circle))
        self.wait(0.3)

        left_shape = Circle(radius=1, color=GREEN).shift(LEFT * 3)
        right_shape = Square(side_length=2, color=RED).shift(RIGHT * 3)

        self.play(
            AnimationGroup(
                Create(left_shape),
                Create(right_shape),
            )
        )
        self.wait(0.5)

        # ReplacementTransform — left_shape IS replaced by right_shape in the scene
        new_left = Square(side_length=2, color=GREEN).shift(LEFT * 3)
        new_right = Circle(radius=1, color=RED).shift(RIGHT * 3)

        self.play(
            ReplacementTransform(left_shape, new_left),
            ReplacementTransform(right_shape, new_right),
        )
        self.wait(1)

        self.play(FadeOut(new_left), FadeOut(new_right))
        self.wait(0.5)
