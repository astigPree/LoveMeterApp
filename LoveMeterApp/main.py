
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.lang.builder import Builder
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty, BooleanProperty , StringProperty
from kivy.animation import Animation
from kivy.clock import Clock

import random 

class Information(Label):
	pass


class NamePlaceholder(FloatLayout):
	name : TextInput= ObjectProperty(None)
	

class ProgressPercentage(Label):
	pass
	

class CustomProgressBar(FloatLayout):
	bar : BoxLayout = ObjectProperty()
	
	def animate(self , percentage : float , times : int ):
		greater_than_0 = True
		animations = None
		for divider in range( 1 , times):
			if animations:
				animations += Animation( 
					size_hint = (0 , 1) if greater_than_0 else (1 , 1) ,
					duration= 1 / divider if not greater_than_0 else 0)
				greater_than_0 = not greater_than_0
			else:
				animations = Animation(size_hint= (1 , 1), duration = 1)
		
		if greater_than_0 :
			animations += Animation(size_hint=(0,1) , duration = 0)
			
		animations += Animation(size_hint_x = percentage , duration= 1 / 2)
		animations.start(self.bar)


class CheckLove(Button):
	
	default_text : str = StringProperty("Let's Check Your Love")
	animate_text_1 : str = StringProperty("Checking")
	animate_text_2 : str = StringProperty("Checking .")
	animate_text_3 : str = StringProperty("Checking . .")
	animate_text_4 : str = StringProperty("Checking . . .")
	
	def on_release(self , *args):
		
		times = random.randint(40 , 60)
		progress = random.randint(20 , 100) / 100
		for _ in range(len(self.parent.name.name.text)):
			progress = random.randint(20 , 100) / 100
		duration = sum([ 1 / divider for divider in range(1 , times)])
		
		checking_button_delay = duration / 9
		animate_duration = 0
		for i in range(10):
			animate_duration = checking_button_delay * i
			Clock.schedule_once(self.animate , animate_duration)
		Clock.schedule_once(self.resetText, animate_duration)
		
		self.parent.progress.animate(progress ,times)
	
	def resetText(self , interval):
		self.text = self.default_text
	
	def animate(self , interval):
		if self.text == self.default_text:
			self.text = self.animate_text_1
		
		if self.text == self.animate_text_1:
			self.text = self.animate_text_2
		elif self.text == self.animate_text_2:
			self.text = self.animate_text_3
		elif self.text == self.animate_text_3:
			self.text = self.animate_text_4
		elif self.text == self.animate_text_4:
			self.text = self.animate_text_1
		
		
class MainWindow(FloatLayout):
	
	is_checking : bool = BooleanProperty(False)


class LoveMeterApp(App):
	
	def build(self):
		return Builder.load_file("design.kv")

LabelBase.register( name = "lobster" , fn_regular="Lobster-Regular.ttf")
LoveMeterApp().run()

