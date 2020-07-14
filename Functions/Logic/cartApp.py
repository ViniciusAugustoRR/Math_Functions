import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.config import Config
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Bezier
from math import pow

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

from kivy.core.window import Window


class MenuTab(GridLayout):

    def __init__(self, **kwargs):
        super(MenuTab, self).__init__(**kwargs)
        
        Clock.schedule_once(self._finish_init)
        

    def _finish_init(self, dt):
        self.exp = '_null_'
        self.xc = 0
        self.yc = 0


    def setFunction(self):
        self.exp = str(self.ids['function_ti'].text)


    def setCordinates(self):
        try:
            self.xc = float(self.ids['cordenates_ti'].text)
            self.calculate()
        except:
            pass

    def calculate(self):
        print( eval(self.exp, {'x': self.xc}) )

class FloatArea(FloatLayout):

    def __init__(self, **kwargs):
        super(FloatArea, self).__init__(**kwargs)
    
class MainPage(Screen):
    pass

class Tests(FloatLayout):
    
    def __init__ (self, **kwargs):
        super(Tests, self).__init__(**kwargs)

        self.size = Window.size
        self.center_z = (self.width/2, self.height/2)

        Clock.schedule_once(self._finish_init)


    def getPositiveX_list(self):
        ### ----->  2x + 3

        points = [self.center_z[0], self.center_z[1]]


        for x in range(-5, 100):
            points.append(self.center_z[0] + x)
            points.append(self.center_z[1] + ((2*x)+2))




        return points


    def _finish_init(self, dt):
        


        with self.canvas:

            Color(1, 1, 1, .5, mode='rgba') 
            Line(points=(self.x, self.center_z[1],
                self.width, self.center_z[1]))
            Line(points=(self.center_z[0], self.y,
                self.center_z[0], self.height))
            
            
            
            Color(1, 0, 0, .5, mode='rgba') 
            lista1 = self.getPositiveX_list()
            #listw = [self.center_z[0], self.center_z[1], self.center_z[0] + 100, self.center_z[1] + 150]
            Line(points=lista1, width=3)







class cartApp(App):

    def build(self):
        #return Builder.load_file('../View/cart.kv')
        return Builder.load_file('../View/test.kv')


if __name__ == '__main__':
    cartApp().run()



'''

-Farinha de pão 330g ------ 2,1/3 xicaras

-acuçar 30g ------- 1/8 xicaras

-sal 1 Colher de mesa

-leite em pó 10g ---------- 1.1/2 Colher de mesa

-leite 200ml mais ou menos

-gema 2

-fermento instantanêo 3g --------- 1 Colher de mesa 

-manteiga sem sal 25g ------------ 2 colheres de mesa

-tamanho da panela 28cm x 6cm x 20cm

- cozinhe a 170ºC ou 240ºF por 15-17 minutos

'''