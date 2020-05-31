from kivy.uix.screenmanager import ScreenManager, Screen
from Screens.EfectsKv import Efectskv
from kivy.uix.label import Label

class WindowOfQuiz(Screen):
    ListOfResp = [0,0,0,0,0,0,0,0,0]
    ListOfVerification = [0,0,0,0,0,0,0,0,0]
    contador = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def RespostQuizInBD(self, MDId, valueAnswer):
        NumberPosition = int(MDId[8])
        if valueAnswer == 'Sim':
            if self.ListOfResp.count(0) != 0:
                self.contador += 1
                if self.ListOfVerification[NumberPosition] != 1: 
                    self.ListOfVerification[NumberPosition] = 1
                    self.ListOfResp[NumberPosition] = 1
                    Efectskv.EfectDialog()
                else:
                    print("ErrorException: Essa pergunta ja foi respondida!!")
            else:
                if (self.ListOfResp[NumberPosition] != 2) and (self.ListOfResp[NumberPosition] == 0):
                    self.ListOfResp[NumberPosition] = 1
                Efectskv.EfectDialogResultQuiz()
        elif valueAnswer == 'Não':
            if self.ListOfResp.count(0) != 0:
                self.contador += 1
                if self.ListOfVerification[NumberPosition] != 1: 
                    self.ListOfVerification[NumberPosition] = 1
                    self.ListOfResp[NumberPosition] = 2
                    Efectskv.EfectDialog()
                else:
                    print("ErrorException: Essa pergunta ja foi respondida!!")
            else:
                if (self.ListOfResp[NumberPosition] != 1) and (self.ListOfResp[NumberPosition] == 0):
                    self.ListOfResp[NumberPosition] = 2
                Efectskv.EfectDialogResultQuiz()
        print(self.ListOfResp)
