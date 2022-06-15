from turtle import screensize
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
import glob
from pathlib import Path
import random

Builder.load_file("design.kv")


class LoginScreen(Screen):

    def sign_up(self):
        self.manager.current = "Signup_screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
            if (uname in users) and (users[uname]['password'] == pword):
                self.manager.current = "LoginSuccess"
            else:
                self.ids.login_wrong.text = "Incorrect Username Or Password"


class SignUp_Screen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
            users[uname] = {"username": uname,
                            "password": pword, "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")}

            print(users)

        with open("users.json", 'w') as file:
            json.dump(users, file)

        self.manager.current = "backTologin"


class ContinueLogin(Screen):
    def backTologin(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "Login_screen"


class LoginScreenSuccess(Screen):
    def logOut(self):
        self.manager.transition.direction = "right"
        self.manager.current = "Login_screen"

    def showQoute(self, mood):
        available_mood = glob.glob("quotes/*.txt")

        available_mood = [Path(filename).stem for filename in available_mood]

        if mood in available_mood:
            with open(f"quotes/{mood}.txt", encoding="utf8") as file:
                quotes = file.readlines()
                self.ids.quote.text = random.choice(quotes)

        else:
            self.ids.quote.text = 'try another feeling'


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
