"""
04_graphs.py
============
Shows how to use Axes to plot mathematical functions and label them.
Topics covered: Axes, plot(), get_graph_label(), and area_under_curve.

Run with:
    manim -pql 04_graphs.py GraphExample
"""

import math

from manim import (
    Scene,
    Axes,
    Text,
    Create,
    Write,
    FadeIn,
    FadeOut,
    GREEN,
    BLUE,
    YELLOW,
    RED,
    WHITE,
    UP,
    DR,
    PI,
)


class GraphExample(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Set up coordinate axes
        # ------------------------------------------------------------------
        axes = Axes(
            x_range=[-1, 7, 1],          # [min, max, step]
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=5,
            axis_config={"color": WHITE},
            tips=True,                    # draw arrow tips on axes
        )
        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")

        self.play(Create(axes), Write(axis_labels))
        self.wait(0.5)

        # ------------------------------------------------------------------
        # 2. Plot sin(x)
        # ------------------------------------------------------------------
        sin_graph = axes.plot(lambda x: math.sin(x), color=GREEN, x_range=[0, 6.5])
        sin_label = axes.get_graph_label(sin_graph, label="\\sin(x)", x_val=5, direction=UP)

        self.play(Create(sin_graph), Write(sin_label))
        self.wait(0.5)

        # ------------------------------------------------------------------
        # 3. Plot cos(x) on the same axes
        # ------------------------------------------------------------------
        cos_graph = axes.plot(lambda x: math.cos(x), color=BLUE, x_range=[0, 6.5])
        cos_label = axes.get_graph_label(cos_graph, label="\\cos(x)", x_val=5, direction=DR)

        self.play(Create(cos_graph), Write(cos_label))
        self.wait(0.5)

        # ------------------------------------------------------------------
        # 4. Shade the area under sin(x) between 0 and π
        # ------------------------------------------------------------------
        area = axes.get_area(
            sin_graph,
            x_range=(0, PI),
            color=(GREEN, YELLOW),
            opacity=0.4,
        )
        area_label = Text("Area under sin(x)\nfrom 0 to π", font_size=24, color=YELLOW)
        area_label.to_corner(DR)

        self.play(FadeIn(area), Write(area_label))
        self.wait(2)

        self.play(FadeOut(axes, axis_labels, sin_graph, sin_label, cos_graph, cos_label, area, area_label))
        self.wait(0.5)
