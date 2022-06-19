from imaplib import Int2AP
import string
import sys
#from kivymd.app import MDApp
#from kivymd.uix.screen import Screen
#from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import sys
#Window.fullscreen = True

#budget planner tracker
#ask how much money monthly then callback should trigger a new question to be 
# asked where a table perhaps pops up which allowed user to enter their monthly 
# spendings which can then be used to create a graph showing monthly spendings, 
# investing advise should pop up indicating how much they would have to save to 
# earn x amount or should tell them how much they will take home after taxes maybe ask if they get any bonuses
#make it save recorded data while asking at the start if they want to continue or start again
#take student finance and their different plans into account
#note how much national insurance and tax they are paying
#look online on how much to invest depending on salary then output how much they will fget after example 5 year

class SayHello(App):
    def build(self):
        self.window = GridLayout() 
        self.window.cols = 1 
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}
 
        self.window.add_widget(Image(source = 'images.png', allow_stretch=True, keep_ratio=False))
        
        #add widgets to window
        self.greeting = Label(text = 'How much money do you earn monthly before taxes')
        self.window.add_widget(self.greeting)

        self.user = TextInput(
                     multiline=False,
                     padding_y = (20,20), 
                     size_hint = (1, 0.5),
                     input_filter = "float"        
                     )
        self.window.add_widget(self.user)

        self.button = Button(
                       text = "ADD",
                       size_hint = (1, 0.5)
                       )
        self.button.bind(on_press=self.NI)
        self.window.add_widget(self.button)

        return self.window


    def NI(self, instance):   #this function works out national insurance tax
#        self.greeting.text = ('you earn annually after taxes')
        inp = float(self.user.text)
        if inp < 9568:
           # self.greeting.text = ('you earn annually after taxes')
                                 
            self.inp1 = inp           
            Tax = self.IncomeTax(self)
        elif inp < 50270:
            self.NI1 = 0.12 * inp
            self.inp1 = inp - self.NI1  
            self.IncomeTax(self)
        else:
            self.inp2 = inp - 50270 
            self.NI1 = (self.inp2 * 0.02) + 4884
            self.inp1 = inp - self.NI1
            self.IncomeTax(self) 

         

    def IncomeTax(self, instance):  #this function works out the income tax

        inp = self.inp1
        if inp < 12570:
            self.income = self.inp1


        elif inp > 12571 and inp < 50270 :
            self.tax1 = self.inp1 - 12570
            self.tax2 = self.tax1 * 0.2
            self.income = self.inp1 - self.tax2


        elif inp > 50271 and inp < 150000 :
            self.tax1 = self.inp1 - 50271
            self.tax2 = self.tax1 * 0.4
            self.income = self.inp1 - self.tax2 - 7540

    
        else :
            self.tax1 = self.inp1 - 150000
            self.tax2 = self.tax1 * 0.45
            self.income = self.inp1 - self.tax2 - 47432
        output = str(self.income)
        self.greeting.text = ('you earn ' + output + ' annually after taxes')
        self.Spending(self)

    def Spending(self, instance):
          self.spend = Label(text = 'How much does your monthly spendings amount to?')
          self.window.add_widget(self.spend)
          self.window.remove_widget(self.button)      
          #self.window.remove_widget(self.user)        
          self.user1 = TextInput(
                     multiline=False,
                     padding_y = (20,20), 
                     size_hint = (1, 0.5),
                     input_filter = "float"        
                     )
          self.window.add_widget(self.user1)

          self.button1 = Button(
                       text = "ADD",
                       size_hint = (1, 0.5)
                       )
          self.button1.bind(on_press=self.Investment)
          self.window.add_widget(self.button1)
          

    def Investment(self, instance):
         inp = float(self.user1.text)
         if inp > (self.income*0.8) :
           self.spend = Label(text = 'Your monthly expenses are too high reduce discretionary spending if possible')
         else :
           self.spend = Label(text = 'Your monthly expenses are in check')
         
         amount = (self.income*0.2)/12
         monthlyrate = 12.1/12
         inp1 = amount([(1+0.121/12)^(12*10)-1]/(0.121/12))
         inp2 = amount([(1+0.121/12)^(12*20)-1]/(0.121/12))
         inp3 = amount([(1+0.121/12)^(12*30)-1]/(0.121/12))
         self.advice = Label(text = 'if you invest monthly 20% of your salary post-tax in the S&P500 after 10 years you will have' + inp1 + 'after 20 years you will have' + inp2 +'after 30 years you will have' + inp3 ) 
         self.window.add_widget(self.advice)

         
         
#search for investment advice based on salary or monthly remainings then tell them how much they 
#can invest monthly and how much they will end uop with after investing in the vangguard. also package as mobile app to see
if __name__ == "__main__":
    SayHello().run()