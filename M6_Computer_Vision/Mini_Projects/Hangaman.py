from kivymd.app import MDApp 
from kivy.lang import Builder
from kivy.core.window import  Window





class HangmanApp(MDApp):
	def build(self):
		self.theme_cls.theme_style='Light'
		self.theme_cls.primary_palette = 'DeepPurple'
		return Builder.load_file('hangman.kv')


if __name__ == '__main__':
	HangmanApp().run()