from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
 
class MyApp(MDApp):
    def flip(self):
        print("working...")
    def build(self):
        screen = MDScreen()
        #UI Widgets go here

        # Create Top Toolbar
        self.toolbar = MDToolbar(title="TITLE")
        self.toolbar.pos_hint = {"top": 1}
        
        screen.add_widget(self.toolbar)

        # Logo

        screen.add_widget(Image(
            source="logo.png",
            pos_hint = {"center_x":0.5, "center_y": 0.7}
        ))

        return screen
 
if __name__ == '__main__':
    MyApp().run()