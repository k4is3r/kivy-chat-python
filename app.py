import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class ChatIpApp(App):
    def build(self):
        return Label(text='Hi from kivy')



if __name__ == '__main__':
    ChatIpApp().run()

