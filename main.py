import os
import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class CalcFloatLayout(FloatLayout):
	def calculate(self,all):
		try:
			self.display.text = (str(eval(all)))
		except:
			self.display.text = ('error')

class RootApp(App):
	def build(self):
		return CalcFloatLayout()

if __name__ == '__main__':
	RootApp().run()
