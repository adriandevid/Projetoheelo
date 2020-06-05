from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker
class WindowOfCadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dictvalues = {}
    def VerificationAnswersForm(self):
        if self.ids['Email'].text[-25:] == '@academico.ifs.edu.com.br':
            self.dictvalues['Email'] = self.ids['Email'].text
            print(self.dictvalues)
        else:
            print('error')
        if self.ids['Senha'].text == self.ids['ComfirmSenha'].text:
            self.dictvalues['Senha'] = self.ids['Senha'].text
            print(self.dictvalues)
        else:
            print("error")
        try:
            if (len(self.ids['Data'].text) == 10) and (int(self.ids['Data'].text[0:2]) <= 31) and (int(self.ids['Data'].text[3:4]) <= 12) and (int(self.ids['Data'].text[6:]) <= 2014):
                self.dictvalues['Data'] = self.ids['Data'].text
                print(self.dictvalues)
            else:
                print('incorreto')
        except ValueError:
            print("incorreto")
        