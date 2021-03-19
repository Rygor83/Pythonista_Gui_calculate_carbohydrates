import ui
from datetime import datetime
import requests, json

#################################
# Views
#################################

screen_width = ui.get_screen_size().width

# Label: гр. углеводов в 100 г
lb_carb_per_100 = ui.Label()
lb_carb_per_100.text = ' 1. гр. углеводов в 100 г продукта:'
lb_carb_per_100.x = 0
lb_carb_per_100.y = 0
lb_carb_per_100.height = 35
lb_carb_per_100.width = screen_width
lb_carb_per_100.alignment = ui.ALIGN_LEFT
lb_carb_per_100.border_width = 1

# TextField: гр. углеводов в 100 г
tf_carb_per_100 = ui.TextField()
tf_carb_per_100.x = 0
tf_carb_per_100.y = 35
tf_carb_per_100.width = screen_width
tf_carb_per_100.height = 35
tf_carb_per_100.keyboard_type = ui.KEYBOARD_NUMBERS
tf_carb_per_100.border_width = 1


# Label: выбор расчета
lb_option = ui.Label()
lb_option.text = ' 2. Выберите расчет:'
lb_option.x = 0
lb_option.y = 75
lb_option.height = 35
lb_option.width = screen_width
lb_option.alignment = ui.ALIGN_LEFT
lb_option.border_width = 1

# SegmentedControl: выбор расчета
sc_option = ui.SegmentedControl()
sc_option.enable = True
sc_option.x = 0
sc_option.y = 110
sc_option.width = screen_width
sc_option.height = 50
sc_option.segments = 'Сколько ХЕ в Х грамм?','Сколько гр.прод. на Х ХЕ?'
sc_option.border_width = 1


# Label: во что пересчитываем
lb_param_to = ui.Label()
lb_param_to.text = ' 3. '
lb_param_to.x = 0
lb_param_to.y = 160
lb_param_to.height = 35
lb_param_to.width = screen_width
lb_param_to.alignment = ui.ALIGN_LEFT
lb_param_to.border_width = 1

# TextField: во что пересчитываем
tf_param_to = ui.TextField()
tf_param_to.x = 0
tf_param_to.y = 195
tf_param_to.width = screen_width
tf_param_to.height = 35
tf_param_to.keyboard_type = ui.KEYBOARD_NUMBERS
tf_param_to.border_width = 1


# Button: convert
bt_convert = ui.Button()
bt_convert.border_width = 4
bt_convert.title = 'Расчитать'
bt_convert.x = 0
bt_convert.y = 250
bt_convert.width = screen_width
bt_convert.height = 50
bt_convert.font = ('verdana',25)
bt_convert.corner_radius = 20

# TextView: результат перерасчета
txtv_info = ui.TextView()
txtv_info.x = 0
txtv_info.y = 305
txtv_info.width = screen_width
txtv_info.height = 300
txtv_info.editable = False
txtv_info.font = ('verdana', 18)
txtv_info.border_width = 1

#################################
# Global class
#################################

class MyClass(ui.View):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.table1_selection = None
		self.bg_color = 'lightyellow'
		self.make_view()
		
	def make_view(self):
		# self.add_subview(dp_rep_date)
		self.add_subview(sc_option)
		self.add_subview(lb_option)
		self.add_subview(lb_carb_per_100)
		self.add_subview(tf_carb_per_100)
		self.add_subview(lb_param_to)
		self.add_subview(tf_param_to)
		
		self.add_subview(bt_convert)
		self.add_subview(txtv_info)
		
		# Actions
		
		tf_carb_per_100.action = self.fn_carb_per_100_entered
		
		sc_option.action = self.fn_segment_select
		
		bt_convert.action = self.fn_convert
		
	def fn_carb_per_100_entered(self, sender):
		p = sender.text
		
	def fn_segment_select(self, sender):
		if sc_option.selected_index == 0:
			lb_param_to.text = " 3. Сколько грамм продукта даем:"
		elif sc_option.selected_index == 1:
			lb_param_to.text = " 3. Сколько ХЕ нужно дать:"
		
	def fn_convert(self, sender):
		
		if tf_carb_per_100.text == '':
			txtv_info.text = '1. Заполните сколько гр. углеводов в 100 г продукта'
		elif sc_option.selected_index ==  -1:
			txtv_info.text = '2. Выберите расчет'
		elif  tf_param_to.text == '':
			txtv_info.text = '3. Заполните сколько даем грамм / ХЕ продукта'
		else:
			# Сколько грамм продукта даем
			if sc_option.selected_index == 0:
				
				amount = int(tf_param_to.text) * int(tf_carb_per_100.text) / 100 / 12
				
				txtv_info.text = f'{round(amount,2)} ХЕ в {tf_param_to.text} грамм(а) продукта'
				
			# Сколько ХЕ нужно дать
			elif sc_option.selected_index == 1:
				
				amount = int(tf_param_to.text) * 12 * 100 / int(tf_carb_per_100.text)
				
				txtv_info.text = f'{round(amount,2)} грамм(а) продукта даём на {tf_param_to.text} ХЕ'
		
##################
# Зауск
##################
v = MyClass(name='Carbohydrate converter')
v.present('full_screen')
