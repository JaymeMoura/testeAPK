import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class ContadorApp(App):
    def build(self):
        self.contador = 0
        
        layout = BoxLayout(orientation='vertical', padding=20)
        
        self.label = Label(text=str(self.contador), font_size=80)
        
        btn_aumentar = Button(text='Aumentar', on_press=self.aumentar)
        btn_diminuir = Button(text='Diminuir', on_press=self.diminuir)
        
        layout.add_widget(self.label)
        layout.add_widget(btn_aumentar)
        layout.add_widget(btn_diminuir)
        
        return layout
    
    def aumentar(self, instance):
        self.contador += 1
        self.label.text = str(self.contador)
    
    def diminuir(self, instance):
        self.contador -= 1
        self.label.text = str(self.contador)

if __name__ == '__main__':
    ContadorApp().run()
