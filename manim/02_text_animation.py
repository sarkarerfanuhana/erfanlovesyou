"""
02_text_animation.py
====================
Shows how to display text on screen, animate it letter-by-letter with Write,
change its colour, scale it, and finally fade it out.

Run with:
    manim -pql 02_text_animation.py TextAnimation
"""

from manim import (
    Scene,
    Text,
    Write,
    FadeIn,
    FadeOut,
    Transform,
    YELLOW,
    BLUE,
    UP,
    DOWN,
)


class TextAnimation(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Write a title on screen
        # ------------------------------------------------------------------
        title = Text("Welcome to Manim!", font_size=64)
        self.play(Write(title))
        self.wait(1)

        # ------------------------------------------------------------------
        # 2. Move the title up and show a subtitle below it
        # ------------------------------------------------------------------
        subtitle = Text("Let's animate the world of math.", font_size=36, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(title.animate.shift(UP), FadeIn(subtitle))
        self.wait(1)

        # ------------------------------------------------------------------
        # 3. Change the colour of the title
        # ------------------------------------------------------------------
        self.play(title.animate.set_color(BLUE))
        self.wait(0.5)

        # ------------------------------------------------------------------
        # 4. Scale the subtitle up and back to its original size
        # ------------------------------------------------------------------
        self.play(subtitle.animate.scale(1.4))
        self.wait(0.3)
        self.play(subtitle.animate.scale(1 / 1.4))
        self.wait(1)

        # ------------------------------------------------------------------
        # 5. Replace the subtitle with a new line of text
        # ------------------------------------------------------------------
        new_text = Text("The animations are just getting started!", font_size=32, color=YELLOW)
        new_text.next_to(title, DOWN, buff=0.5)

        self.play(Transform(subtitle, new_text))
        self.wait(1)

        # ------------------------------------------------------------------
        # 6. Fade everything out
        # ------------------------------------------------------------------
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(0.5)
