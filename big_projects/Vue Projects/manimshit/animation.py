from manim import *


class OpeningManim(Scene):
    def construct(self):
        title = Text("Today's equation")
        basel = MathTex(r"\int (x+2)^{2}dx")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            FadeIn(title),
            Write(basel, shift=UP),
        )
        self.wait()

    transform_title = Tex("That was a transform")
    transform_title.to_corner(UP + LEFT)
    self.play(
        Transform(title, transform_title),
        LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
    )
    self.wait()
