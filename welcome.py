from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.properties  import ListProperty
from kivymd.theming import ThemeManager


class Welcome(BoxLayout):
    theme_cls = ThemeManager()

    def ch(self):
        self.theme_cls.primary_hue = "100"
