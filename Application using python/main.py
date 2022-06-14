from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime
import json

Builder.load_file("design.kv")


class LoginScreen(Screen):

    def sign_up(self):
        self.manager.current = "Signup_screen"


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


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
