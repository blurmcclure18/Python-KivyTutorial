from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton,MDIconButton, MDFloatingActionButton

 
class MyApp(MDApp):
    def build(self):
        screen = MDScreen()
        #UI Widgets go here
        btn_flat = MDRectangleFlatButton(
            text='Hello World', 
            pos_hint={'center_x':0.5,'center_y': 0.5},
            )
        icon_btn = MDIconButton(
            icon='language-python', 
            pos_hint={'center_x':0.4, 'center_y':0.5},
        )
        floating_btn =MDFloatingActionButton(
            icon='language-python', 
            pos_hint={'center_x':0.6, 'center_y':0.5},
        )
        screen.add_widget(btn_flat)
        screen.add_widget(icon_btn)
        screen.add_widget(floating_btn)
        return screen
 
if __name__ == '__main__':
    MyApp().run()