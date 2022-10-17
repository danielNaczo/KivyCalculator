from kivy.app import App
from kivy.uix.widget import Widget


class CalculatorWidget(Widget):
    calculation = None

    def add_Value(self, value):
        self.ids.calculation.text += value

    def clear(self):
        self.ids.calculation.text = ""

    def evaluate(self):
        result = str(eval(self.ids.calculation.text))
        self.ids.calculation.text = result


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()
