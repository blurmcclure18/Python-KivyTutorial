from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
 
username_helper= """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "of click on forgot username"
    helper_text_mode:"on_focus"
    icon_right: "language-python"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x':0.5, 'center_y':0.5}
    size_hint_x:None
    width:300

"""

class MyApp(MDApp):

    def build(self):
        screen = MDScreen()
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.theme_style="Dark"
        #UI Widgets go here
        username = Builder.load_string(username_helper)
        # MDTextField(
        #    text='Enter Username', 
        #    pos_hint={'center_x':0.5, 'center_y':0.5},
        #    size_hint_x=None, #<-- Prevents auto resizing
        #    width=300, #<-- in pixels
        #    )

        screen.add_widget(username)
        return screen
 
if __name__ == '__main__':
    MyApp().run()