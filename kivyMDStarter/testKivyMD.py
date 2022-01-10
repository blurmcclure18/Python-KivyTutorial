from kivymd.uix.behaviors import backgroundcolor_behavior
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
 
class MyApp(MDApp):
    def build(self):
        screen = MDScreen()
        #UI Widgets go here

        # Create Top Toolbar
        self.toolbar = MDToolbar(title="ScrapeBay")
        self.toolbar.pos_hint = {"top": 1}
        
        screen.add_widget(self.toolbar)

        # Create Search Bar
        # text input widget
        self.search = MDTextField(
            multiline = False,
            
            )
        self.search.pos_hint = {"top": 10}
        screen.add_widget(self.search)


        return screen
 
if __name__ == '__main__':
    MyApp().run()