import kivy

from kivy.app import App
from kivy.uix.button import Label

class HelloKivy(App):
    
    def build(self):
        return Label(text= "Hello!")
    
helloKivy = HelloKivy()
helloKivy.run()