from manim import *
# or: from manimlib import *
from manim_slides import Slide

class CalculusOneReview(Slide):
    def construct(self):
        diffy_formulas = [
            "\\frac{d}{dx}(x)=1", 
            "\\frac{d}{dx}(ax)=a", 
            "\\frac{d}{dx}\\left(x^n\\right)=nx^{n-1}",
            "\\frac{d}{dx}\\left( \\sin(x) \\right)=\\cos(x)",
            "\\frac{d}{dx}\\left( \\cos(x) \\right) = -\\sin(x)",
            "\\frac{d}{dx}\\left( \\tan(x) \\right) = \sec^2(x)",
            "\\frac{d}{dx}\\left( \\sec(x) \\right) = \\sec(x)\\tan(x)",
            "\\frac{d}{dx}\\left( \\csc(x) \\right) = -\\csc(x)\\cot(x)",
            "\\frac{d}{dx}\\left( \\ln(x) \\right) = \\frac{1}{x}",
            "\\frac{d}{dx}\\left( e^x \\right) = e^x",
            "\\frac{d}{dx}\\left( a^x \\right) = (\\ln a)a^x",
            "\\frac{d}{dx}\\left( \\arcsin(x) \\right) = \\frac{1}{\\sqrt{1-x^2}}",
            "\\frac{d}{dx}\\left( \\arctan(x) \\right) = \\frac{1}{1+x^2}",
            "\\frac{d}{dx}\\left( \\text{arcsec}(x) \\right) = \\frac{1}{|x|\\sqrt{x^2-1}}",
        ]

        integration_formuals =[
            "\\int\\left( 1 \\right)\\,dx = x + C",
            "\\int\\left( a \\right)\\,dx = ax + C",
            "\\int\\left( x^n \\right)\\,dx =\\frac{x^{n+1}}{n+1} + C",
            "\\int\\left( \\sin(x) \\right)\\,dx = -\\cos(x) + C",
            "\\int\\left( \\cos(x) \\right)\\,dx = \\sin(x) + C",
            "\\int\\left( \\sec^2(x) \\right)\\,dx = \\tan(x) + C",
            "\\int\\left( \\sec(x)\\tan(x) \\right)\\,dx = \\sec(x) + C",
            "\\int\\left( \\csc(x)\\cot(x) \\right)\\,dx = -\\csc(x) + C",
            "\\int\\left( \\frac{1}{x} \\right)\\,dx = \\ln|x| + C",
            "\\int\\left( e^x \\right)\\,dx = e^x + C",
            "\\int\\left( a^x \\right)\\,dx = \\frac{a^x}{\\ln a} + C, \\, a>0,\\, a\\neq1",
            "\\int\\left( \\frac{1}{\\sqrt{1-x^2}} \\right)\\,dx = \\arcsin(x) + C",
            "\\int\\left( \\frac{1}{1+x^2} \\right)\\,dx = \\arctan(x) + C",
            "\\int\\left( \\frac{1}{|x|\\sqrt{x^2-1}} \\right)\\,dx = \\text{arcsec}(x) + C",
        ]

        title1 = Title("Calculus 1 Review: Differenation Formulas")

        #self.add(title)

        self.play(Write(title1))

        self.pause()
        
        current_text = MathTex(diffy_formulas[0]).scale(1.5)
        self.play(Write(current_text))
        self.pause()

        for i in list(range(1, 14)):
            next_text = MathTex(diffy_formulas[i]).scale(1.5)
            self.play(ReplacementTransform(current_text, next_text))
            current_text=next_text
            self.pause()
        
        title2 = Title("Calculus 1 Review: Integration Formulas")
        self.play(Unwrite(current_text))
        self.play(ReplacementTransform(title1, title2))

        current_text = MathTex(integration_formuals[0]).scale(1.5)
        self.play(Write(current_text))
        self.pause()

        for i in list(range(1, 14)):
            next_text = MathTex(integration_formuals[i]).scale(1.5)
            self.play(ReplacementTransform(current_text, next_text))
            current_text=next_text
            self.pause()

        self.wait()

class HyperbolicEquations(Slide):
    def construct(self):
         title = Title("Hyperbolic Functions (Section 5.9)")

         self.play(Write(title))

         self.pause()

         self.play(Write(
            Text("Lorem Isupum").next_to(title, DOWN)
         ))

class CalculusOneReviewActivity(Slide):
    def construct(self):
        diffy_formulas_wo_answers = [
            "\\frac{d}{dx}(x)", 
            "\\frac{d}{dx}(ax)=a", 
            "\\frac{d}{dx}\\left(x^n\\right)",
            "\\frac{d}{dx}\\left( \\sin(x) \\right)",
            "\\frac{d}{dx}\\left( \\cos(x) \\right)",
            "\\frac{d}{dx}\\left( \\tan(x) \\right)",
            "\\frac{d}{dx}\\left( \\sec(x) \\right)",
            "\\frac{d}{dx}\\left( \\csc(x) \\right)",
            "\\frac{d}{dx}\\left( \\ln(x) \\right)",
            "\\frac{d}{dx}\\left( e^x \\right)",
            "\\frac{d}{dx}\\left( a^x \\right)",
            "\\frac{d}{dx}\\left( \\arcsin(x) \\right)",
            "\\frac{d}{dx}\\left( \\arctan(x) \\right)",
            "\\frac{d}{dx}\\left( \\text{arcsec}(x) \\right)",
        ]

        integration_formuals_wo_answers =[
            "\\int\\left( 1 \\right)\\,dx",
            "\\int\\left( a \\right)\\,dx",
            "\\int\\left( x^n \\right)\\,dx",
            "\\int\\left( \\sin(x) \\right)\\,dx",
            "\\int\\left( \\cos(x) \\right)\\,dx",
            "\\int\\left( \\sec^2(x) \\right)\\,dx",
            "\\int\\left( \\sec(x)\\tan(x) \\right)\\,dx",
            "\\int\\left( \\csc(x)\\cot(x) \\right)\\,dx",
            "\\int\\left( \\frac{1}{x} \\right)\\,dx",
            "\\int\\left( e^x \\right)\\,dx",
            "\\int\\left( a^x \\right)\\,dx",
            "\\int\\left( \\frac{1}{\\sqrt{1-x^2}} \\right)\\,dx",
            "\\int\\left( \\frac{1}{1+x^2} \\right)\\,dx",
            "\\int\\left( \\frac{1}{|x|\\sqrt{x^2-1}} \\right)\\,dx",
        ]

        diffy_formulas_with_answers = [
            "\\frac{d}{dx}(x)=1", 
            "\\frac{d}{dx}(ax)=a", 
            "\\frac{d}{dx}\\left(x^n\\right)=nx^{n-1}",
            "\\frac{d}{dx}\\left( \\sin(x) \\right)=\\cos(x)",
            "\\frac{d}{dx}\\left( \\cos(x) \\right) = -\\sin(x)",
            "\\frac{d}{dx}\\left( \\tan(x) \\right) = \sec^2(x)",
            "\\frac{d}{dx}\\left( \\sec(x) \\right) = \\sec(x)\\tan(x)",
            "\\frac{d}{dx}\\left( \\csc(x) \\right) = -\\csc(x)\\cot(x)",
            "\\frac{d}{dx}\\left( \\ln(x) \\right) = \\frac{1}{x}",
            "\\frac{d}{dx}\\left( e^x \\right) = e^x",
            "\\frac{d}{dx}\\left( a^x \\right) = (\\ln a)a^x",
            "\\frac{d}{dx}\\left( \\arcsin(x) \\right) = \\frac{1}{\\sqrt{1-x^2}}",
            "\\frac{d}{dx}\\left( \\arctan(x) \\right) = \\frac{1}{1+x^2}",
            "\\frac{d}{dx}\\left( \\text{arcsec}(x) \\right) = \\frac{1}{|x|\\sqrt{x^2-1}}",
        ]

        integration_formuals_with_answers =[
            "\\int\\left( 1 \\right)\\,dx = x + C",
            "\\int\\left( a \\right)\\,dx = ax + C",
            "\\int\\left( x^n \\right)\\,dx =\\frac{x^{n+1}}{n+1} + C",
            "\\int\\left( \\sin(x) \\right)\\,dx = -\\cos(x) + C",
            "\\int\\left( \\cos(x) \\right)\\,dx = \\sin(x) + C",
            "\\int\\left( \\sec^2(x) \\right)\\,dx = \\tan(x) + C",
            "\\int\\left( \\sec(x)\\tan(x) \\right)\\,dx = \\sec(x) + C",
            "\\int\\left( \\csc(x)\\cot(x) \\right)\\,dx = -\\csc(x) + C",
            "\\int\\left( \\frac{1}{x} \\right)\\,dx = \\ln|x| + C",
            "\\int\\left( e^x \\right)\\,dx = e^x + C",
            "\\int\\left( a^x \\right)\\,dx = \\frac{a^x}{\\ln a} + C, \\, a>0,\\, a\\neq1",
            "\\int\\left( \\frac{1}{ \\sqrt{1-x^2} } \\right)\\,dx = \\arcsin(x) + C",
            "\\int\\left( \\frac{1}{1+x^2} \\right)\\,dx = \\arctan(x) + C",
            "\\int\\left( \\frac{1}{|x|\\sqrt{x^2-1}} \\right)\\,dx = \\text{arcsec}(x) + C",
        ]

        # Create title for diffy activity.
        title1 = Title("Calculus 1 Review Activity: Differenation Formulas")

        #self.add(title)

        #Animate the previous title.
        self.play(Write(title1))

        self.pause()
        
        #define the first diffy formula in activity and write it on screen
        current_text = MathTex(diffy_formulas_wo_answers[0]).scale(1.5)
        self.play(Write(current_text))
        self.pause()

        # Loop through diffy formuals and write them on screen.
        for i in list(range(1, 14)):
            next_text = MathTex(diffy_formulas_wo_answers[i]).scale(1.5)
            self.play(ReplacementTransform(current_text, next_text))
            current_text=next_text
            self.pause()

        # Unwrite the current diffy formula on screen.
        self.play(Unwrite(current_text))
        self.pause()

        # Start the diffy answers activity.
        current_text = MathTex(diffy_formulas_with_answers[0]).scale(1.5)
        self.play(Write(current_text))
        self.pause()
        
        # Loop through diffy answers and write them on screen.
        for i in list(range(1, 14)):
            next_text = MathTex(diffy_formulas_with_answers[i]).scale(1.5)
            self.play(ReplacementTransform(current_text, next_text))
            current_text=next_text
            self.pause()
        
        title2 = Title("Calculus 1 Review Activity: Integration Formulas")
        self.play(Unwrite(current_text))
        self.play(ReplacementTransform(title1, title2))

        current_text = MathTex(integration_formuals_wo_answers[0]).scale(1.5)
        self.play(Write(current_text))
        self.pause()

        for i in list(range(1, 14)):
            next_text = MathTex(integration_formuals_wo_answers[i]).scale(1.5)
            self.play(ReplacementTransform(current_text, next_text))
            current_text=next_text
            self.pause()

         # Unwrite the current diffy formula on screen.
        self.play(Unwrite(current_text))
        self.pause()

        # Start the diffy answers activity.
        current_text = MathTex(integration_formuals_with_answers[0]).scale(1.5)
        self.play(Write(current_text))
        self.pause()

        for i in list(range(1, 14)):
            next_text = MathTex(integration_formuals_with_answers[i]).scale(1.5)
            self.play(ReplacementTransform(current_text, next_text))
            current_text=next_text
            self.pause()

        self.wait()