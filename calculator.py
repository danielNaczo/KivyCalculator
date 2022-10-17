from kivy.app import App
from kivy.uix.widget import Widget


class CalculatorWidget(Widget):
    calculation = None

    def add_Value(self, value):
        self.ids.calculation.text += value

    def clear(self):
        self.ids.calculation.text = ""

    def delete(self):
        calc = self.ids.calculation.text
        self.ids.calculation.text = calc[:len(calc)-1]

    def evaluate(self):
        try:
            result = str(eval(self.ids.calculation.text))
            self.ids.calculation.text = result
        except:
            pass


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()
