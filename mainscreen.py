from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.list import OneLineIconListItem,OneLineAvatarIconListItem,IRightBodyTouch
from kivy.metrics import dp
from kivy.properties import StringProperty, ObjectProperty, BooleanProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.theming import ThemeManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.menu import MDDropdownMenu
from dbconnection import Dbconnection
from recycleview import Recycleview,SelectableLabel,SelectableRecycleBoxLayout





class MainScreen(BoxLayout):
    print('mainscreen created')
    

    
    def __init__(self, **kwargs):
        super(MainScreen,self).__init__(**kwargs)
        self.dbconn = Dbconnection()
        self.cat = self.dbconn.get_categories()
        Clock.schedule_once(self.drop_down)


    def drop_down(self,dt):
        print(self.cat)
        menu_items = [{ "text": f"{i}"} for i in self.cat]
        self.menu = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4,
            )
        self.menu.bind(on_release=self.set_item)


    def set_item(self, instance_menu, instance_menu_item):
        self.ids.drop_item.set_item(instance_menu_item.text)
        self.menu.dismiss()



    
    def clicked(self,item, amount):
        print("clicked current:", item)
        print("amount",amount)
        
    


class Tab(BoxLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    content_text = StringProperty("")

class SelectableRecycleBoxLayout(SelectableRecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SelectableLabelMain(SelectableLabel):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def pressed_view(self,data, instance):
        index = self.parent.get_view_index_at(self.center)
        print(self.parent)
        root = self.parent
        root.remove_widget(self)
        print(data[index])
        data.pop(index)


    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)   

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))

class RvMain(Recycleview):
    
    def __init__(self,index = 0, **kwargs):
        super(RvMain,self).__init__(**kwargs)
        self.set_cont()
        self.index = index
        self.add_items()
    



    def set_cont(self):
        print("setting....")
        self.contacts = [
            ["Annie", "555-24235", "http://myphotos.com/annie.png"],
            ["Bob", "555-15423", "http://myphotos.com/bob.png"],
            ["Claire", "555-66098", "http://myphotos.com/claire.png"],
            ["Annie", "555-24235", "http://myphotos.com/annie.png"],
            ["Bob", "555-15423", "http://myphotos.com/bob.png"],
            ["Claire", "555-66098", "http://myphotos.com/claire.png"],
            ["Annie", "555-24235", "http://myphotos.com/annie.png"],
            ["Bob", "555-15423", "http://myphotos.com/bob.png"],
            ["Claire", "555-66098", "http://myphotos.com/claire.png"],
            ["Annie", "555-24235", "http://myphotos.com/annie.png"],
            ["Bob", "555-15423", "http://myphotos.com/bob.png"],
            ["Claire", "555-66098", "http://myphotos.com/claire.png"]
        ]
    
    def get_cont(self):
        print("getting...")
        return self.contacts
    
    def add_items(self):
        print(self.get_cont())
        self.data = [{'text':c[0],'secondary_text':c[1]} for c in self.get_cont()]

    
    
        