"""
05_math_equations.py
====================
Shows how to render LaTeX math expressions using MathTex and Tex,
and how to highlight individual parts of an equation.

Requirements: a working LaTeX installation (e.g. MiKTeX or TeX Live).

Run with:
    manim -pql 05_math_equations.py MathEquations
"""

from manim import (
    Scene,
    MathTex,
    Tex,
    Write,
    FadeIn,
    FadeOut,
    Transform,
    Indicate,
    SurroundingRectangle,
    Create,
    YELLOW,
    BLUE,
    RED,
    GREEN,
    UP,
    DOWN,
)


class MathEquations(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Display the quadratic formula
        # ------------------------------------------------------------------
        quadratic = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=64,
        )
        self.play(Write(quadratic))
        self.wait(1)

        # ------------------------------------------------------------------
        # 2. Colour individual sub-expressions
        #    Break the formula into separately colourable parts by splitting
        #    the LaTeX string at the tex_to_color_map boundaries.
        # ------------------------------------------------------------------
        coloured_quadratic = MathTex(
            r"x = \frac{",
            r"-b",
            r" \pm \sqrt{",
            r"b^2 - 4ac",
            r"}}{2a}",
            font_size=64,
        )
        coloured_quadratic[1].set_color(RED)       # -b
        coloured_quadratic[3].set_color(BLUE)      # discriminant

        self.play(Transform(quadratic, coloured_quadratic))
        self.wait(1)

        # ------------------------------------------------------------------
        # 3. Highlight (pulse) the discriminant part
        # ------------------------------------------------------------------
        discriminant_box = SurroundingRectangle(coloured_quadratic[3], color=YELLOW)
        self.play(Create(discriminant_box))
        self.play(Indicate(coloured_quadratic[3], color=YELLOW))
        self.wait(0.5)

        label = Tex(r"Discriminant: $b^2 - 4ac$", font_size=36, color=YELLOW)
        label.next_to(quadratic, DOWN, buff=0.8)
        self.play(FadeIn(label))
        self.wait(1)

        # ------------------------------------------------------------------
        # 4. Euler's identity
        # ------------------------------------------------------------------
        self.play(FadeOut(quadratic, discriminant_box, label))
        self.wait(0.3)

        euler = MathTex(r"e^{i\pi} + 1 = 0", font_size=96)
        self.play(Write(euler))
        self.wait(0.5)

        euler_label = Tex(r"Euler's Identity", font_size=40, color=GREEN)
        euler_label.next_to(euler, UP, buff=0.6)
        self.play(FadeIn(euler_label))
        self.wait(1.5)

        self.play(FadeOut(euler, euler_label))
        self.wait(0.5)
