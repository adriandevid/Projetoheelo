from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.picker import MDDatePicker
from kivymd.toast import toast

class WindowOfCadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dictvalues = {}
    def ValidateData(self, Data):
        try:
            dia, mes, ano = map(int, Data.split('/'))
            if mes < 1 or mes > 12 or ano <= 0 or ano >= 2020:
                toast("Erro de data insira uma data valida!")
            else:
                if mes in (1, 3, 5, 7, 8, 10, 12):
                    ultimo_dia = 31
                elif mes == 2:
                    if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
                        ultimo_dia = 29
                    else:
                        ultimo_dia = 28
                else:
                    ultimo_dia = 30
                    if dia < 1 or dia > ultimo_dia:
                        toast("Data invalida!!")
                    else:
                        self.dictvalues['DatadeNascimento'] = Data
                        return True
        except ValueError:
            toast("O dado inserido não é valido")
    def ValidateEmail(self, Email):
        if Email[-25:] == '@academico.ifs.edu.com.br':
            self.dictvalues['Email'] = Email
        else:
            toast("E-mail incorreto")
    def ValidateSenha(self, senha, comfirmsenha):
        if senha == comfirmsenha:
            self.dictvalues['Senha'] = senha
        else:
            toast("senha incorreta!! Verifique se a senha e a comfirmação dela estão corretas!!")
    def ValidateTelefone(self, numero):
        if (numero[:3] == '079') or (numero[:2] == '79'):
            if (len(numero[3:]) == 9) or (len(numero[2:]) == 9):
                 self.dictvalues['Numero'] = numero
            else:
                toast("Digite um numero valido!")
        else:
            toast("Digite um numero valido!")
    def ValidateCategoria(self, categoria):
        if len(categoria) == 1:
            if categoria in ('S', "T", "A"):
                self.dictvalues['Categoria'] = categoria
            else:
                toast("Opção invalida!")
        else:
            print("error")
    def ValidateCampus(self, Campus):
        self.dictvalues['Campus'] = Campus
    def VerificationAnswersForm(self):
        self.ValidateEmail(self.ids['Email'].text)
        self.ValidateSenha(self.ids['Senha'].text, self.ids['ComfirmSenha'].text)
        self.ValidateTelefone(self.ids["Telefone"].text)
        self.ValidateData(self.ids['DtNascimento'].text)
        print(self.dictvalues)
        
        
        