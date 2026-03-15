from manim import *
from manim_slides import Slide
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class VoiceoverExample(VoiceoverScene, Slide):
    def construct(self):
        self.set_speech_service(GTTSService())

        title = Text("Manim Voiceover Example").to_edge(UP)

        with self.voiceover("Welcome to this example of Manim with voiceover."):
            self.play(Write(title))

        self.pause()

        equation = Text("e^(i*pi) + 1 = 0").scale(2)

        with self.voiceover("This is Euler's identity, one of the most beautiful equations in mathematics."):
            self.play(Write(equation))

        self.pause()

        with self.voiceover("The animation automatically waits for the voiceover to finish before moving on."):
            self.play(equation.animate.set_color(YELLOW))

        self.pause()
        self.wait()
