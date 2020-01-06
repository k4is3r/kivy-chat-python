import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import os

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        
        if os.path.isfile('prev_details.txt'):
            with open('prev_details.txt','r') as f:
                d = f.read().split(',')
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]
        else:
            prev_ip = ''
            prev_port = ''
            prev_username = ''
        
        self.add_widget(Label(text='IP: '))
        self.ip = TextInput(text=prev_ip ,multiline=False)
        self.add_widget(self.ip)
        
        self.add_widget(Label(text='Port: '))
        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)

        self.add_widget(Label(text='Username: '))
        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)
        
        self.join = Button(text='Join')
        self.join.bind(on_press = self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)
        
    def join_button(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text
        print(f' Attemting to join {ip}:{port} as {username}')
        
        with open('prev_details.txt','w') as f:
            f.write(f'{ip},{port},{username}')


class ChatIpApp(App):
    title = 'Chat IP'
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')        
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name='InfoPage')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    ChatIpApp().run()

