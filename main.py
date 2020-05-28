from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from Controllers import WindowOfQuiz, WindowOfLogin, WindowOfCadastro

Window.size = (360, 640)

class Test(MDApp):
    def build(self):
        return  Builder.load_string(open("C:/Users/PC/Documents/ProjetoHeelo/Screens/ViewMaster.kv", encoding="utf-8").read(), rulesonly=False)

Test().run()