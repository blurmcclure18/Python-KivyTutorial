from os import close
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton,MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.lang import Builder
from Helpers.helpers import username_helper
from kivymd.uix.dialog import MDDialog

class MyApp(MDApp):

    def build(self):
        screen = MDScreen()
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.theme_style="Dark"
        #UI Widgets go here
        self.username = Builder.load_string(username_helper)
        
        # MDTextField(
        #    text='Enter Username', 
        #    pos_hint={'center_x':0.5, 'center_y':0.5},
        #    size_hint_x=None, #<-- Prevents auto resizing
        #    width=300, #<-- in pixels
        #    )

        button = MDFillRoundFlatButton(
            text='Show',
            pos_hint={'center_x':0.5, 'center_y':0.4},
            on_release=self.show_data
            )

        screen.add_widget(self.username)
        screen.add_widget(button)
        
        return screen
    
    def show_data(self,obj):
        if self.username.text is '':
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + " does not exist!"
        
        close_btn=MDFlatButton(
            text='Close',
            on_release=self.close_dialog,
        )
        more_btn=MDFlatButton(
            text='More',
        )
        
        self.dialog = MDDialog(
            text=check_string,
            title='Username Check',
            size_hint=(0.7,1),
            buttons=[close_btn,more_btn],
        )
        self.dialog.open()
    
    def close_dialog(self,obj):
        self.dialog.dismiss()

 
if __name__ == '__main__':
    MyApp().run()