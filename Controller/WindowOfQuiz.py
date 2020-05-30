from kivy.uix.screenmanager import ScreenManager, Screen

class WindowOfQuiz(Screen):
    ListOfVerification = []
    ListQuest = []
    def RespostQuizInBD(self,valueAnswer):
        if valueAnswer == 'Sim':
            WindowOfQuiz.ListOfVerification.append(1)

            for i in self.ids:
                cont = 0
                l = list(i)
                if cont < 1:
                    WindowOfQuiz.ListQuest.append(int(l[9]))
                if WindowOfQuiz.ListQuest[cont] == int(l[9]) or cont < 1:
                    print("encontrado!!!")
                    break
                else:
                    print("n ppode entrar")
                cont += 1