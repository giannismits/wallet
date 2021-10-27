# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.theming import ThemeManager
from welcome import Welcome
from kivy.clock import Clock
from mainscreen import MainScreen
from categories import Categories, RecycleCatExcpences
from contentnavigationdrwer import ContentNavigationDrawer
from kivy.properties import StringProperty, ObjectProperty
from dbconnection import Dbconnection




from kivy.core.window import Window
Window.size = (300, 600)




class MainMenuApp(MDApp):
    #theme_cls = ThemeManager()

    def __init__(self,**kwargs):
        super(MainMenuApp,self).__init__(**kwargs)
        dbconn = Dbconnection()
        dbconn.get_cat_from_db()
        self.cats = dbconn.get_categories()




    def popup(self):
        layout = GridLayout(cols = 1, padding = 10)

        popupLabel = MDLabel(text= "Hello!")
        layout.add_widget(popupLabel)
        popup = Popup(title='Test popup',
        content=layout,
        size_hint=(None, None), size=(400, 400))
        print("popup")
        return popup.open()


if __name__== "__main__":
    MainMenuApp().run()
