from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class DemoApp(MDApp):
    def build(self):
        screen = MDScreen()
        label = MDLabel(
            text='Hello World!', 
            halign='center', 
            theme_text_color='Custom',
            text_color=(236/255,98/255,81/255,1),
            font_style= 'Caption',
            )

        icon_label = MDIcon(icon='language-python', halign='left')

        screen.add_widget(label,icon_label)

        return screen


if __name__ == "__main__":
    DemoApp().run()