
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '250')

Config.set('graphics', 'resizable', False)

class Container(BoxLayout):
    def __init__(self, **kwargs):
        super(BoxLayout, self).__init__(**kwargs)
        self.guess = 500
        self.lower = 0
        self.higher = 1000
    def Button_high(self):

        self.lower = self.guess
        self.guess = int((self.higher + self.lower)/2)
        text =  'is your number is ' + str(self.guess)
        self.ids.mylabel.text = text
        print(self.guess)
    def Button_low(self):

        self.higher = self.guess
        self.guess = int((self.higher + self.lower)/2)
        text =  'is your number is ' + str(self.guess)
        self.ids.mylabel.text = text
        print(self.guess)

    def Button_yes(self):
            self.guess = 500
            self.lower = 0
            self.higher = 1000
            text =  'is your number is ' + str(self.guess)+ '?'
            self.ids.mylabel.text = text
class NumberGuesser(App):

    def build(self):
        self.title = 'Number Guesser'
        return Container()


if __name__ == '__main__':
    NumberGusser().run()
