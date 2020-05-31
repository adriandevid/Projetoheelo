from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
class Efectskv:
    def EfectDialog():
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(halign= "center",text='Deseja confirmar sua resposta?', color=[0,0,0,1],font_size=11))
        box.add_widget(MDFillRoundFlatIconButton(text= "Confirmar", icon="check", md_bg_color = [0,0,1,1], pos_hint={"center_x": .5, "center_y": .5}))
        pop = Popup(content=box, size_hint=(None, None), size=(200, 200), background= 'white')
        pop.open()
    def EfectDialogResultQuiz():
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(halign= "center",text='Suas respostas foram computadas!!', color=[0,0,0,1],font_size=11))
        pop = Popup(content=box, size_hint=(None, None), size=(200, 200), background= 'white')
        pop.open()