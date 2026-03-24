"""
06_combined_scene.py
====================
A more complete scene that combines shapes, text, graphs, and smooth camera
movement to tell a short "story" about the sine function.  This is a good
template to copy and adapt for your own animations.

Run with:
    manim -pql 06_combined_scene.py CombinedScene
"""

import math

from manim import (
    Scene,
    Axes,
    Circle,
    Dot,
    Line,
    MathTex,
    Text,
    VGroup,
    Create,
    Write,
    FadeIn,
    FadeOut,
    Transform,
    MoveAlongPath,
    UpdateFromFunc,
    always_redraw,
    TracedPath,
    WHITE,
    YELLOW,
    GREEN,
    RED,
    BLUE,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    TAU,
    PI,
    ValueTracker,
)


class CombinedScene(Scene):
    """
    Visualizes how the sine function is derived from the unit circle.

    Steps
    -----
    1. Show a title card.
    2. Draw the unit circle and the axes side by side.
    3. Animate a point travelling around the circle while a corresponding
       dot traces sin(θ) on the right-hand graph.
    4. Fade everything out with a closing message.
    """

    def construct(self):
        # ------------------------------------------------------------------
        # 1. Title card
        # ------------------------------------------------------------------
        title = Text("The Sine Function", font_size=56)
        subtitle = Text("from the unit circle", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.4)

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(0.3)

        # ------------------------------------------------------------------
        # 2. Layout: unit circle on the left, axes on the right
        # ------------------------------------------------------------------
        circle = Circle(radius=1.5, color=WHITE)
        circle.shift(LEFT * 3.5)

        axes = Axes(
            x_range=[0, TAU + 0.2, PI / 2],
            y_range=[-1.6, 1.6, 0.5],
            x_length=5.5,
            y_length=3.2,
            axis_config={"color": WHITE},
        )
        axes.shift(RIGHT * 2)

        x_label = axes.get_x_axis_label(MathTex(r"\theta"))
        y_label = axes.get_y_axis_label(MathTex(r"\sin\theta"))

        self.play(Create(circle), Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)

        # ------------------------------------------------------------------
        # 3. Animated point + traced sine curve
        # ------------------------------------------------------------------
        tracker = ValueTracker(0)   # tracks the current angle θ

        # Point on the unit circle
        circle_dot = always_redraw(
            lambda: Dot(
                point=circle.get_center()
                + 1.5 * RIGHT * math.cos(tracker.get_value())
                + 1.5 * UP * math.sin(tracker.get_value()),
                color=RED,
                radius=0.08,
            )
        )

        # Horizontal dashed line from circle_dot to the graph dot
        connector = always_redraw(
            lambda: Line(
                start=circle_dot.get_center(),
                end=axes.c2p(tracker.get_value(), math.sin(tracker.get_value())),
                color=YELLOW,
                stroke_width=1.5,
            )
        )

        # Point on the graph that follows sin(θ)
        graph_dot = always_redraw(
            lambda: Dot(
                point=axes.c2p(tracker.get_value(), math.sin(tracker.get_value())),
                color=GREEN,
                radius=0.08,
            )
        )

        # The traced sine curve builds up as θ increases
        sine_curve = axes.plot(
            lambda x: math.sin(x),
            x_range=[0, TAU],
            color=GREEN,
        )

        self.add(circle_dot, connector, graph_dot)
        self.wait(0.3)

        # Animate θ from 0 to 2π while simultaneously drawing the curve
        self.play(
            tracker.animate.set_value(TAU),
            Create(sine_curve),
            run_time=6,
            rate_func=lambda t: t,   # linear
        )
        self.wait(1)

        # ------------------------------------------------------------------
        # 4. Label the curve and close
        # ------------------------------------------------------------------
        curve_label = MathTex(r"y = \sin(\theta)", color=GREEN, font_size=36)
        curve_label.next_to(axes, UP, buff=0.3)
        self.play(FadeIn(curve_label))
        self.wait(1)

        closing = Text("And that's the sine wave!", font_size=40)
        self.play(
            FadeOut(circle, axes, x_label, y_label, circle_dot, connector, graph_dot, sine_curve, curve_label),
            FadeIn(closing),
        )
        self.wait(2)
        self.play(FadeOut(closing))
        self.wait(0.5)
