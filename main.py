##this script creates a usable customisable button with set background images that change on clicking the button

import kivy

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App


class NiceButton(Button):
    pass
#the code for our nicer button is in the .kv file

class YourFloatLayout(FloatLayout):
    pass
#the code for the layout you will use the button in is also in the .kv file


class YourApp(App):
    def build(self):
        return YourFloatLayout()

if __name__ == "__main__":
    YourApp().run()

#A simple way of running the app, but you can also use builder. to run the app this way you MUST
#name the .kv file your.kv (or whatever you have called the app)
