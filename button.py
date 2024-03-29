import pygame

class Button:
	def __init__(self, surface, button_info, button_color, text, text_size, font, text_color):
		self.surface = surface
		self.x_pos = button_info[0]
		self.y_pos = button_info[1]
		self.w = button_info[2]
		self.h = button_info[3]
		self.button_color = button_color
		self.text = text
		self.text_size = int(text_size)
		self.font = font
		self.color = text_color
		self.text_color = text_color

	def create(self):
		button = pygame.draw.rect(self.surface, self.button_color, (self.x_pos, self.y_pos, self.w, self.h))
		button_text = pygame.font.SysFont(self.font, self.text_size, bold=True)
		bt_surface = button_text.render(self.text, True, self.text_color)
		bt_rect = bt_surface.get_rect(center = (self.x_pos + self.w / 2, self.y_pos + self.h / 2))
		self.surface.blit(bt_surface, bt_rect)

	def hover(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.x_pos + self.w > mouse_pos[0] > self.x_pos and self.y_pos + self.h > mouse_pos[1] > self.y_pos:
			self.button_color = (255, 0, 0)
			return True
		self.button_color = (0, 0, 0)
		return False

	def clicked(self):
		mouse_pos = pygame.mouse.get_pressed()
		return mouse_pos[0] == 1 and self.hover()

	def change_box_color(self, color):
		''' change the color of the rectangle'''
		pass

class Box:
	def __init__(self, surface, box_area, box_pos, box_color = (0,0,0), text = None, font = 'Comic Sans MS', text_color = None):
		self._window = surface
		self._width, self._height = box_area	
		self._x , self._y = box_pos
		self._text = text
		self._font = font
		self._text_color = text_color
	def draw(self):
		pass
	def change_box_color(self, color):
		'''change the color of the rectangle box'''
		pass
	def add_text(self, text: str, font: int):
		''' replace the old text with new text '''
		pass
	def within(self, coord: tuple):
		''' checks if the coordinate is inside the box'''
		pass