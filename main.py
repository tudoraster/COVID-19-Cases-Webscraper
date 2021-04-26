import logic

from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.button import Button

#Window.fullscreen = 'auto'

class MyLayout(Widget):
    def spinner_clicked(self, value):
        actual, total = logic.get_country_covid_cases(value.upper())
        self.ids.actual.text = actual
        self.ids.total.text = total

    def load_saves(self):
        with open("saves.txt", "r") as f:
            saves = f.read()

        saves = saves.split()
        self.ids.spinner_id.values = saves

    def save(self):
        actual, total = logic.get_country_covid_cases(self.country.text.upper())
        if actual != "" and total != "":
            with open('saves.txt', 'a') as file:
                file.write(self.country.text.capitalize() + "\n")


class MyGui(App):
    def build(self):
        self.title = 'COVID-19 Cases'
        self.icon = 'icon.png'

        return MyLayout()


if __name__ == "__main__":
    MyGui().run()
