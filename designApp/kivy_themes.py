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
                
        # Color Options in primary_palette - Available options are: ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, ‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’, ‘Green’, ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’, ‘Brown’, ‘Gray’, ‘BlueGray’
        self.theme_cls.primary_palette = 'Amber'
        
        # Primary hue option - ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’, ‘A400’, ‘A700’.
        self.theme_cls.primary_hue='200'
        
        # Theme Styles 'Dark' or 'Light'
        self.theme_cls.theme_style='Dark'

        btn = MDFillRoundFlatButton(
            text='Hello World',
            pos_hint={'center_x':0.5,'center_y':0.5}
            )
        screen.add_widget(btn)

        return screen
 
if __name__ == '__main__':
    MyApp().run()