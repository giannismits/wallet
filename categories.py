from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.tab import MDTabsBase
from kivy.properties import StringProperty, ObjectProperty
from recycleview import Recycleview,SelectableLabel,SelectableRecycleBoxLayout
from dbconnection import Dbconnection


class Categories(BoxLayout):
    def add_category(self, value):
        print(value)
        #dbconn = Dbconnection()
        #dbconn.add_category(value)
        pass
    

class Tab(BoxLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    content_text = StringProperty("")

class SelectableLabelexp(SelectableLabel):
    
    def pressed_view(self,*args):
        print("args:", *args)
        print(self.parent.get_view_index_at(self.center))

class RecycleCatExcpences(Recycleview,SelectableRecycleBoxLayout):
    def __init__(self, **kwargs):
        super(RecycleCatExcpences,self).__init__(**kwargs)
        dbconn = Dbconnection()
        self.cats = dbconn.get_categories()
        self.add_items()

        



    def add_items(self):
        self.data = [{'text':c,'secondary_text':"category"} for c in self.cats]
    
    

        