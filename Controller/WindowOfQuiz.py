from kivy.uix.screenmanager import ScreenManager, Screen
from Screens.EfectsKv import Efectskv
from DAO.DbFactory import DbFactory
from kivymd.toast import toast


class WindowOfQuiz(Screen):
    ListOfResp = [0,0,0,0,0,0,0,0,0]
    contador = 0
    def RespostQuiz(self, MDId, valueAnswer):
        NumberPosition = int(MDId[8])
        if valueAnswer == 'Sim':
            self.contador += 1
            self.ListOfResp[NumberPosition] = 1
            toast("A resposta foi computada!!")
            if (self.ListOfResp[NumberPosition] != 2) and (self.ListOfResp[NumberPosition] == 0):
                self.ListOfResp[NumberPosition] = 1
        elif valueAnswer == 'Não':
            self.contador += 1
            self.ListOfResp[NumberPosition] = 2
            toast("A resposta foi computada!!")
            if (self.ListOfResp[NumberPosition] != 1) and (self.ListOfResp[NumberPosition] == 0):
                self.ListOfResp[NumberPosition] = 2
        print(self.ListOfResp)
    def SubmitRespostInDb(self):
        DbFactory.DataBase('SQLite').CreateConnector('ola.db').Connect()