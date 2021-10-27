from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import TwoLineAvatarListItem,  ImageLeftWidget
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior,RecycleDataAdapter
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior



class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''

class SelectableLabel(RecycleDataViewBehavior, TwoLineAvatarListItem, ImageLeftWidget, RecycleDataAdapter):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    


           
    def pressed_view(self,*args):
        print(self.parent.get_view_index_at(self.center))


class Recycleview(RecycleView):
    def __init__(self, **kwargs):
        super(Recycleview,self).__init__(**kwargs)

        

    def add_items(self):

        pass