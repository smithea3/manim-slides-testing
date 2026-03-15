from manim import *
from manim_slides import Slide


class Precalc11FunctionsAndNotation(Slide):
    def construct(self):

        # ── helpers ──────────────────────────────────────────────────────────
        def fade_all(self):
            self.play(*[FadeOut(mob) for mob in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 1 — Title
        # ════════════════════════════════════════════════════════════════════
        title = Title("Functions and Function Notation")
        subtitle = Text(
            "OpenStax Precalculus 2e — Section 1.1", font_size=32, color=GRAY
        ).next_to(title, DOWN, buff=0.4)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 2 — What is a Relation?
        # ════════════════════════════════════════════════════════════════════
        heading = Text("What is a Relation?", font_size=40, color=YELLOW).to_edge(UP)
        definition = MathTex(
            r"\text{A relation is a set of ordered pairs } (x,\, y)",
            font_size=36,
        ).next_to(heading, DOWN, buff=0.6)
        example = MathTex(
            r"\{(1,4),\ (2,5),\ (3,6),\ (2,7)\}", font_size=36
        ).next_to(definition, DOWN, buff=0.5)

        self.play(Write(heading))
        self.pause()
        self.play(Write(definition))
        self.pause()
        self.play(Write(example))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 3 — Mapping Diagram for a Relation
        # ════════════════════════════════════════════════════════════════════
        heading3 = Text("Mapping Diagram", font_size=40, color=YELLOW).to_edge(UP)

        # ellipses
        in_ellipse = Ellipse(width=2.2, height=3.2, color=BLUE).shift(LEFT * 3)
        out_ellipse = Ellipse(width=2.2, height=3.2, color=GREEN).shift(RIGHT * 3)
        in_label = Text("Input", font_size=28, color=BLUE).next_to(
            in_ellipse, UP, buff=0.15
        )
        out_label = Text("Output", font_size=28, color=GREEN).next_to(
            out_ellipse, UP, buff=0.15
        )

        # input values
        x_vals = [1, 2, 3]
        y_vals = [4, 5, 6, 7]
        x_dots = VGroup(
            *[
                Text(str(v), font_size=28).move_to(in_ellipse.get_center() + UP * (1 - i))
                for i, v in enumerate(x_vals)
            ]
        )
        # highlight "2" in yellow
        x_dots[1].set_color(YELLOW)

        y_dots = VGroup(
            *[
                Text(str(v), font_size=28).move_to(
                    out_ellipse.get_center() + UP * (1.5 - i)
                )
                for i, v in enumerate(y_vals)
            ]
        )

        # arrows: 1→4, 2→5, 3→6, 2→7
        arrow_pairs = [(0, 0), (1, 1), (2, 2), (1, 3)]
        arrows = VGroup(
            *[
                CurvedArrow(
                    x_dots[i].get_right() + RIGHT * 0.05,
                    y_dots[j].get_left() + LEFT * 0.05,
                    angle=-0.3 if (i, j) != (1, 3) else 0.5,
                    color=YELLOW if i == 1 else WHITE,
                    stroke_width=2,
                )
                for i, j in arrow_pairs
            ]
        )

        diagram = VGroup(
            in_ellipse, out_ellipse, in_label, out_label, x_dots, y_dots
        ).shift(DOWN * 0.3)

        self.play(Write(heading3))
        self.play(
            Create(in_ellipse),
            Create(out_ellipse),
            Write(in_label),
            Write(out_label),
        )
        self.play(Write(x_dots), Write(y_dots))
        self.play(LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.3))

        note = Text(
            'Input "2" maps to both 5 and 7', font_size=28, color=YELLOW
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 4 — What is a Function? (Definition)
        # ════════════════════════════════════════════════════════════════════
        heading4 = Text("What is a Function?", font_size=40, color=YELLOW).to_edge(UP)

        defn_text = Text(
            "A function is a relation in which\neach input has exactly one output.",
            font_size=32,
        )
        defn_box = SurroundingRectangle(defn_text, color=BLUE, buff=0.3)
        defn_group = VGroup(defn_text, defn_box).next_to(heading4, DOWN, buff=0.7)

        clarifier = MathTex(
            r"\text{Each } x \text{ maps to exactly one } y", font_size=34
        ).next_to(defn_group, DOWN, buff=0.6)

        self.play(Write(heading4))
        self.play(Write(defn_text), Create(defn_box))
        self.pause()
        self.play(Write(clarifier))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 5 — Function vs. Not a Function (side-by-side)
        # ════════════════════════════════════════════════════════════════════
        heading5 = Text(
            "Function vs. Not a Function", font_size=40, color=YELLOW
        ).to_edge(UP)

        # Left: function mapping
        left_in = Ellipse(width=1.8, height=2.8, color=BLUE).shift(LEFT * 4 + DOWN * 0.3)
        left_out = Ellipse(width=1.8, height=2.8, color=GREEN).shift(LEFT * 1.5 + DOWN * 0.3)
        l_x1 = Text("1", font_size=26).move_to(left_in.get_center() + UP * 0.6)
        l_x2 = Text("2", font_size=26).move_to(left_in.get_center())
        l_x3 = Text("3", font_size=26).move_to(left_in.get_center() + DOWN * 0.6)
        l_y1 = Text("a", font_size=26).move_to(left_out.get_center() + UP * 0.6)
        l_y2 = Text("b", font_size=26).move_to(left_out.get_center())
        l_y3 = Text("c", font_size=26).move_to(left_out.get_center() + DOWN * 0.6)
        l_arrows = VGroup(
            CurvedArrow(l_x1.get_right(), l_y1.get_left(), angle=-0.2, stroke_width=2),
            CurvedArrow(l_x2.get_right(), l_y2.get_left(), angle=-0.2, stroke_width=2),
            CurvedArrow(l_x3.get_right(), l_y3.get_left(), angle=-0.2, stroke_width=2),
        )
        fn_label = Text("Function", font_size=28, color=GREEN).next_to(
            left_out, DOWN, buff=0.25
        )
        left_group = VGroup(
            left_in, left_out, l_x1, l_x2, l_x3, l_y1, l_y2, l_y3, l_arrows
        )

        # Right: not-a-function mapping
        right_in = Ellipse(width=1.8, height=2.8, color=BLUE).shift(RIGHT * 1.5 + DOWN * 0.3)
        right_out = Ellipse(width=1.8, height=2.8, color=GREEN).shift(RIGHT * 4 + DOWN * 0.3)
        r_x1 = Text("1", font_size=26).move_to(right_in.get_center() + UP * 0.6)
        r_x2 = Text("2", font_size=26, color=YELLOW).move_to(right_in.get_center())
        r_x3 = Text("3", font_size=26).move_to(right_in.get_center() + DOWN * 0.6)
        r_y1 = Text("a", font_size=26).move_to(right_out.get_center() + UP * 0.8)
        r_y2 = Text("b", font_size=26).move_to(right_out.get_center() + UP * 0.1)
        r_y3 = Text("c", font_size=26).move_to(right_out.get_center() + DOWN * 0.6)
        r_arrows = VGroup(
            CurvedArrow(r_x1.get_right(), r_y1.get_left(), angle=-0.2, stroke_width=2),
            CurvedArrow(
                r_x2.get_right(), r_y1.get_left(), angle=0.4, stroke_width=2, color=RED
            ),
            CurvedArrow(
                r_x2.get_right(), r_y2.get_left(), angle=-0.4, stroke_width=2, color=RED
            ),
            CurvedArrow(r_x3.get_right(), r_y3.get_left(), angle=-0.2, stroke_width=2),
        )
        not_fn_label = Text("Not a Function", font_size=28, color=RED).next_to(
            right_out, DOWN, buff=0.25
        )
        right_group = VGroup(
            right_in, right_out, r_x1, r_x2, r_x3, r_y1, r_y2, r_y3, r_arrows
        )

        divider = DashedLine(UP * 2.5, DOWN * 2.5, color=GRAY)

        self.play(Write(heading5))
        self.play(Create(left_group), Create(right_group), Create(divider))
        self.pause()
        self.play(Write(fn_label), Write(not_fn_label))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 6 — Domain and Range
        # ════════════════════════════════════════════════════════════════════
        heading6 = Text("Domain and Range", font_size=40, color=YELLOW).to_edge(UP)

        d_ellipse = Ellipse(width=2.2, height=3.2, color=BLUE).shift(LEFT * 3 + DOWN * 0.3)
        r_ellipse = Ellipse(width=2.2, height=3.2, color=ORANGE).shift(RIGHT * 3 + DOWN * 0.3)
        d_vals = VGroup(
            Text("1", font_size=28).move_to(d_ellipse.get_center() + UP * 0.7),
            Text("2", font_size=28).move_to(d_ellipse.get_center()),
            Text("3", font_size=28).move_to(d_ellipse.get_center() + DOWN * 0.7),
        )
        r_vals = VGroup(
            Text("4", font_size=28).move_to(r_ellipse.get_center() + UP * 0.7),
            Text("5", font_size=28).move_to(r_ellipse.get_center()),
            Text("6", font_size=28).move_to(r_ellipse.get_center() + DOWN * 0.7),
        )
        map_arrows = VGroup(
            *[
                CurvedArrow(
                    d_vals[i].get_right() + RIGHT * 0.05,
                    r_vals[i].get_left() + LEFT * 0.05,
                    angle=-0.2,
                    stroke_width=2,
                )
                for i in range(3)
            ]
        )

        d_brace = Brace(d_ellipse, direction=LEFT, color=BLUE)
        d_brace_label = Text("Domain", font_size=26, color=BLUE).next_to(
            d_brace, LEFT, buff=0.15
        )
        r_brace = Brace(r_ellipse, direction=RIGHT, color=ORANGE)
        r_brace_label = Text("Range", font_size=26, color=ORANGE).next_to(
            r_brace, RIGHT, buff=0.15
        )

        d_def = MathTex(
            r"\text{Domain: all possible } x\text{-values (inputs)}",
            font_size=28,
            color=BLUE,
        ).to_edge(DOWN, buff=0.9)
        r_def = MathTex(
            r"\text{Range: all possible } y\text{-values (outputs)}",
            font_size=28,
            color=ORANGE,
        ).next_to(d_def, DOWN, buff=0.25)

        self.play(Write(heading6))
        self.play(
            Create(d_ellipse),
            Create(r_ellipse),
            Write(d_vals),
            Write(r_vals),
            LaggedStart(*[Create(a) for a in map_arrows], lag_ratio=0.3),
        )
        self.play(Create(d_brace), Write(d_brace_label))
        self.pause()
        self.play(Create(r_brace), Write(r_brace_label))
        self.pause()
        self.play(Write(d_def), Write(r_def))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 7 — Function Notation: Introducing f(x)
        # ════════════════════════════════════════════════════════════════════
        heading7 = Text("Function Notation", font_size=40, color=YELLOW).to_edge(UP)

        eq_y = MathTex(r"y = 2x + 3", font_size=48)
        eq_f = MathTex(r"f", r"(", r"x", r")", r" = 2x + 3", font_size=48)
        eq_f[0].set_color(YELLOW)
        eq_f[2].set_color(GREEN)

        eq_y.next_to(heading7, DOWN, buff=0.8)
        eq_f.move_to(eq_y)

        self.play(Write(heading7))
        self.play(Write(eq_y))
        self.pause()
        self.play(ReplacementTransform(eq_y, eq_f))
        self.pause()

        # annotations
        fn_name_arrow = CurvedArrow(
            eq_f[0].get_top() + UP * 0.05,
            eq_f[0].get_top() + UP * 1.0 + LEFT * 0.5,
            angle=0.5,
            color=YELLOW,
            stroke_width=2,
        )
        fn_name_lbl = Text("function name", font_size=24, color=YELLOW).next_to(
            fn_name_arrow.get_end(), UP, buff=0.05
        )
        self.play(Create(fn_name_arrow), Write(fn_name_lbl))
        self.pause()

        input_arrow = CurvedArrow(
            eq_f[2].get_bottom() + DOWN * 0.05,
            eq_f[2].get_bottom() + DOWN * 1.0 + LEFT * 0.3,
            angle=-0.5,
            color=GREEN,
            stroke_width=2,
        )
        input_lbl = Text("input variable", font_size=24, color=GREEN).next_to(
            input_arrow.get_end(), DOWN, buff=0.05
        )
        self.play(Create(input_arrow), Write(input_lbl))
        self.pause()

        output_arrow = CurvedArrow(
            eq_f[4].get_bottom() + DOWN * 0.05,
            eq_f[4].get_bottom() + DOWN * 1.0 + RIGHT * 0.5,
            angle=0.5,
            color=WHITE,
            stroke_width=2,
        )
        output_lbl = Text("rule / output", font_size=24).next_to(
            output_arrow.get_end(), DOWN, buff=0.05
        )
        self.play(Create(output_arrow), Write(output_lbl))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 8 — Evaluating Functions: Numeric Input
        # ════════════════════════════════════════════════════════════════════
        heading8 = Text(
            "Evaluating Functions: f(5)", font_size=40, color=YELLOW
        ).to_edge(UP)

        step0 = MathTex(r"f(x) = 2x + 3", font_size=40)
        step1 = MathTex(r"f(5) = 2(5) + 3", font_size=40)
        step2 = MathTex(r"f(5) = 10 + 3", font_size=40)
        step3 = MathTex(r"f(5) = 13", font_size=40)

        steps = VGroup(step0, step1, step2, step3).arrange(
            DOWN, buff=0.45, aligned_edge=LEFT
        ).next_to(heading8, DOWN, buff=0.6)

        self.play(Write(heading8))
        self.play(Write(step0))
        self.pause()
        self.play(Write(step1))
        self.pause()
        self.play(Write(step2))
        self.pause()
        self.play(Write(step3))
        self.play(step3.animate.set_color(YELLOW).scale(1.2))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 9 — Evaluating Functions: Algebraic Input
        # ════════════════════════════════════════════════════════════════════
        heading9 = Text(
            r"Evaluating Functions: f(a+1)", font_size=40, color=YELLOW
        ).to_edge(UP)

        a0 = MathTex(r"f(x) = x^2 - 4", font_size=40)
        a1 = MathTex(r"f(a+1) = (a+1)^2 - 4", font_size=40)
        a2 = MathTex(r"= a^2 + 2a + 1 - 4", font_size=40)
        a3 = MathTex(r"= a^2 + 2a - 3", font_size=40)

        alg_steps = VGroup(a0, a1, a2, a3).arrange(
            DOWN, buff=0.45, aligned_edge=LEFT
        ).next_to(heading9, DOWN, buff=0.6)

        self.play(Write(heading9))
        self.play(Write(a0))
        self.pause()
        self.play(Write(a1))
        self.pause()
        self.play(Write(a2))
        self.pause()
        self.play(Write(a3))
        self.play(a3.animate.set_color(YELLOW))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 10 — Representing Functions: Table
        # ════════════════════════════════════════════════════════════════════
        heading10 = Text(
            "Representing Functions: Table", font_size=40, color=YELLOW
        ).to_edge(UP)

        eq_table = MathTex(r"f(x) = 3x - 1", font_size=40).next_to(
            heading10, DOWN, buff=0.5
        )

        x_data = [-1, 0, 1, 2, 3]
        fx_data = [3 * x - 1 for x in x_data]

        table = Table(
            [["x", "f(x)"], *[[str(x), str(y)] for x, y in zip(x_data, fx_data)]],
            include_outer_lines=True,
        ).scale(0.65).next_to(eq_table, DOWN, buff=0.5)

        self.play(Write(heading10))
        self.play(Write(eq_table))
        self.play(Create(table))
        # highlight x=0 row (row index 2, 0-based header=1)
        row_highlight = table.get_rows()[2]  # x=0 row
        self.play(row_highlight.animate.set_color(YELLOW))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 11 — Representing Functions: Graph
        # ════════════════════════════════════════════════════════════════════
        heading11 = Text(
            "Representing Functions: Graph", font_size=36, color=YELLOW
        ).to_edge(UP)

        axes11 = Axes(
            x_range=[-2, 4, 1],
            y_range=[-6, 10, 2],
            x_length=7,
            y_length=5.5,
            axis_config={"include_numbers": True},
        ).next_to(heading11, DOWN, buff=0.3)
        ax_labels11 = axes11.get_axis_labels(x_label="x", y_label="f(x)")

        graph11 = axes11.plot(lambda x: 3 * x - 1, color=BLUE)

        table_dots = VGroup(
            *[
                Dot(axes11.coords_to_point(x, 3 * x - 1), color=YELLOW)
                for x in x_data
            ]
        )

        self.play(Write(heading11))
        self.play(Create(axes11), Write(ax_labels11))
        self.play(Create(graph11))
        self.pause()
        self.play(LaggedStart(*[GrowFromCenter(d) for d in table_dots], lag_ratio=0.2))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 12 — Vertical Line Test: Concept
        # ════════════════════════════════════════════════════════════════════
        heading12 = Text(
            "The Vertical Line Test", font_size=40, color=YELLOW
        ).to_edge(UP)

        vlt_text = Text(
            "If any vertical line crosses a graph\nmore than once, the graph does\nNOT represent a function.",
            font_size=30,
            line_spacing=1.3,
        )
        vlt_box = SurroundingRectangle(vlt_text, color=BLUE, buff=0.35)
        vlt_group = VGroup(vlt_text, vlt_box).next_to(heading12, DOWN, buff=0.8)

        self.play(Write(heading12))
        self.play(Write(vlt_text), Create(vlt_box))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 13 — Vertical Line Test: Passes (Parabola)
        # ════════════════════════════════════════════════════════════════════
        heading13 = Text(
            "VLT: Parabola (Passes)", font_size=36, color=YELLOW
        ).to_edge(UP)

        axes13 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 6, 1],
            x_length=6,
            y_length=4.5,
        ).next_to(heading13, DOWN, buff=0.3)
        ax_labels13 = axes13.get_axis_labels(x_label="x", y_label="y")

        parabola = axes13.plot(lambda x: x ** 2, color=BLUE)

        x_tracker = ValueTracker(-2.5)

        vline13 = always_redraw(
            lambda: DashedLine(
                axes13.coords_to_point(x_tracker.get_value(), -0.5),
                axes13.coords_to_point(x_tracker.get_value(), 6),
                color=YELLOW,
                stroke_width=3,
            )
        )

        riding_dot = always_redraw(
            lambda: Dot(
                axes13.coords_to_point(
                    x_tracker.get_value(), x_tracker.get_value() ** 2
                ),
                color=RED,
                radius=0.1,
            )
        )

        self.play(Write(heading13))
        self.play(Create(axes13), Write(ax_labels13), Create(parabola))
        self.add(vline13, riding_dot)
        self.play(x_tracker.animate.set_value(2.5), run_time=4, rate_func=linear)
        self.pause()

        result13 = Text(
            "One intersection — IS a Function", font_size=28, color=GREEN
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(result13))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 14 — Vertical Line Test: Fails (Circle)
        # ════════════════════════════════════════════════════════════════════
        heading14 = Text(
            "VLT: Circle (Fails)", font_size=36, color=YELLOW
        ).to_edge(UP)

        axes14 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5.5,
            y_length=5.5,
        ).next_to(heading14, DOWN, buff=0.3)
        ax_labels14 = axes14.get_axis_labels(x_label="x", y_label="y")

        circle14 = Circle(radius=axes14.c2p(2, 0)[0] - axes14.c2p(0, 0)[0], color=BLUE)
        circle14.move_to(axes14.c2p(0, 0))

        # vertical line at x=1
        static_vline = DashedLine(
            axes14.coords_to_point(1, -2.5),
            axes14.coords_to_point(1, 2.5),
            color=YELLOW,
            stroke_width=3,
        )

        # intersection points on circle at x=1: y = ±sqrt(3)
        import math
        y_pos = math.sqrt(3)
        dot_top = Dot(axes14.coords_to_point(1, y_pos), color=RED, radius=0.12)
        dot_bot = Dot(axes14.coords_to_point(1, -y_pos), color=RED, radius=0.12)

        self.play(Write(heading14))
        self.play(Create(axes14), Write(ax_labels14), Create(circle14))
        self.play(Create(static_vline))
        self.play(GrowFromCenter(dot_top), GrowFromCenter(dot_bot))
        self.play(Indicate(dot_top), Indicate(dot_bot))

        result14 = Text(
            "Two intersections — NOT a Function", font_size=28, color=RED
        ).to_edge(DOWN, buff=0.4)
        self.play(Write(result14))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 15 — One-to-One Functions: Definition
        # ════════════════════════════════════════════════════════════════════
        heading15 = Text(
            "One-to-One Functions", font_size=40, color=YELLOW
        ).to_edge(UP)

        oto_text = Text(
            "A function is one-to-one if each output\ncorresponds to exactly one input.",
            font_size=30,
            line_spacing=1.3,
        )
        oto_box = SurroundingRectangle(oto_text, color=BLUE, buff=0.3)
        oto_group = VGroup(oto_text, oto_box).next_to(heading15, DOWN, buff=0.5)

        # Left mini diagram — NOT one-to-one (two inputs, same output)
        left_label15 = Text("NOT One-to-One", font_size=22, color=RED)
        l15_in = Ellipse(width=1.5, height=2.2, color=BLUE).shift(LEFT * 3.5 + DOWN * 1.5)
        l15_out = Ellipse(width=1.5, height=2.2, color=GREEN).shift(LEFT * 1.5 + DOWN * 1.5)
        l15_a = Text("a", font_size=22).move_to(l15_in.get_center() + UP * 0.4)
        l15_b = Text("b", font_size=22).move_to(l15_in.get_center() + DOWN * 0.4)
        l15_1 = Text("1", font_size=22).move_to(l15_out.get_center())
        l15_arrows = VGroup(
            CurvedArrow(l15_a.get_right(), l15_1.get_left(), angle=-0.3, stroke_width=2, color=RED),
            CurvedArrow(l15_b.get_right(), l15_1.get_left(), angle=0.3, stroke_width=2, color=RED),
        )
        left_label15.next_to(l15_out, DOWN, buff=0.2)
        left15 = VGroup(l15_in, l15_out, l15_a, l15_b, l15_1, l15_arrows, left_label15)

        # Right mini diagram — one-to-one
        right_label15 = Text("One-to-One", font_size=22, color=GREEN)
        r15_in = Ellipse(width=1.5, height=2.2, color=BLUE).shift(RIGHT * 1.5 + DOWN * 1.5)
        r15_out = Ellipse(width=1.5, height=2.2, color=GREEN).shift(RIGHT * 3.5 + DOWN * 1.5)
        r15_a = Text("a", font_size=22).move_to(r15_in.get_center() + UP * 0.4)
        r15_b = Text("b", font_size=22).move_to(r15_in.get_center() + DOWN * 0.4)
        r15_1 = Text("1", font_size=22).move_to(r15_out.get_center() + UP * 0.4)
        r15_2 = Text("2", font_size=22).move_to(r15_out.get_center() + DOWN * 0.4)
        r15_arrows = VGroup(
            CurvedArrow(r15_a.get_right(), r15_1.get_left(), angle=-0.2, stroke_width=2, color=GREEN),
            CurvedArrow(r15_b.get_right(), r15_2.get_left(), angle=-0.2, stroke_width=2, color=GREEN),
        )
        right_label15.next_to(r15_out, DOWN, buff=0.2)
        right15 = VGroup(r15_in, r15_out, r15_a, r15_b, r15_1, r15_2, r15_arrows, right_label15)

        self.play(Write(heading15))
        self.play(Write(oto_text), Create(oto_box))
        self.pause()
        self.play(Create(left15), Create(right15))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 16 — Horizontal Line Test: Concept
        # ════════════════════════════════════════════════════════════════════
        heading16 = Text(
            "The Horizontal Line Test", font_size=40, color=YELLOW
        ).to_edge(UP)

        hlt_text = Text(
            "If any horizontal line crosses a graph\nmore than once, the function is\nNOT one-to-one.",
            font_size=30,
            line_spacing=1.3,
        )
        hlt_box = SurroundingRectangle(hlt_text, color=ORANGE, buff=0.35)
        hlt_group = VGroup(hlt_text, hlt_box).next_to(heading16, DOWN, buff=0.8)

        self.play(Write(heading16))
        self.play(Write(hlt_text), Create(hlt_box))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 17 — Horizontal Line Test: Side-by-side
        # ════════════════════════════════════════════════════════════════════
        heading17 = Text(
            "HLT: Side-by-Side Comparison", font_size=36, color=YELLOW
        ).to_edge(UP)

        # Left: x^2 (fails HLT)
        axes_left = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 5, 1],
            x_length=4.5,
            y_length=4,
            axis_config={"include_numbers": False},
        ).shift(LEFT * 3.3 + DOWN * 0.5)
        graph_left = axes_left.plot(lambda x: x ** 2, color=BLUE)
        ax_lbl_left = axes_left.get_axis_labels(
            x_label=MathTex("x", font_size=24),
            y_label=MathTex("x^2", font_size=24),
        )

        # horizontal line at y=2 on left axes
        hline_left = DashedLine(
            axes_left.coords_to_point(-3, 2),
            axes_left.coords_to_point(3, 2),
            color=YELLOW,
            stroke_width=3,
        )
        # Two dots at intersections: x=±sqrt(2)
        left_dot1 = Dot(axes_left.coords_to_point(math.sqrt(2), 2), color=RED, radius=0.1)
        left_dot2 = Dot(axes_left.coords_to_point(-math.sqrt(2), 2), color=RED, radius=0.1)

        label_left = Text("Fails HLT\nNot One-to-One", font_size=22, color=RED).next_to(
            axes_left, DOWN, buff=0.2
        )

        # Right: x^3 (passes HLT)
        axes_right = Axes(
            x_range=[-2, 2, 1],
            y_range=[-5, 5, 2],
            x_length=4.5,
            y_length=4,
            axis_config={"include_numbers": False},
        ).shift(RIGHT * 3.3 + DOWN * 0.5)
        graph_right = axes_right.plot(lambda x: x ** 3, color=BLUE)
        ax_lbl_right = axes_right.get_axis_labels(
            x_label=MathTex("x", font_size=24),
            y_label=MathTex("x^3", font_size=24),
        )

        # horizontal line at y=2 on right axes
        hline_right = DashedLine(
            axes_right.coords_to_point(-2, 2),
            axes_right.coords_to_point(2, 2),
            color=YELLOW,
            stroke_width=3,
        )
        right_dot = Dot(
            axes_right.coords_to_point(2 ** (1 / 3), 2), color=GREEN, radius=0.1
        )

        label_right = Text("Passes HLT\nOne-to-One", font_size=22, color=GREEN).next_to(
            axes_right, DOWN, buff=0.2
        )

        divider17 = DashedLine(UP * 3, DOWN * 3, color=GRAY)

        self.play(Write(heading17))
        self.play(
            Create(axes_left),
            Write(ax_lbl_left),
            Create(graph_left),
            Create(axes_right),
            Write(ax_lbl_right),
            Create(graph_right),
            Create(divider17),
        )
        self.play(
            Create(hline_left),
            Create(hline_right),
            GrowFromCenter(left_dot1),
            GrowFromCenter(left_dot2),
            GrowFromCenter(right_dot),
        )
        self.pause()
        self.play(Write(label_left), Write(label_right))
        self.pause()

        self.play(*[FadeOut(m) for m in self.mobjects])

        # ════════════════════════════════════════════════════════════════════
        # SLIDE 18 — Summary
        # ════════════════════════════════════════════════════════════════════
        summary_title = Title("Section 1.1 Summary")
        self.play(Write(summary_title))

        bullets_text = [
            "Relation: a set of ordered pairs (x, y)",
            "Function: each input has exactly one output",
            "Domain: all possible input (x) values",
            "Range: all possible output (y) values",
            "f(x) notation: f is the name, x is the input",
            "Vertical Line Test: checks if graph is a function",
            "One-to-One: each output has exactly one input",
            "Horizontal Line Test: checks if function is one-to-one",
        ]

        bullets = VGroup(
            *[
                Text(f"• {t}", font_size=28).set_width(11)
                for t in bullets_text
            ]
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).next_to(summary_title, DOWN, buff=0.4)

        self.play(LaggedStart(*[Write(b) for b in bullets], lag_ratio=0.25))
        self.pause()
        self.wait()
