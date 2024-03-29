import pygame

import player
from button import Button
from avatar_selection import AvatarSelection
from text import Text
import background_mech
import pytmx
_INITIAL_BACKGROUD_WIDTH = 300
_INITIAL_BACKGROUD_HEIGHT = 300
BACKGROUND = 'backgrounds/practice.tmx'

## entity is item created in the map
## for example, walls, houses, field of grass
ENTITY = []





class Pokemon:
	def __init__(self, window, character: int):
		self._running = True
		self._pause = False
		self.keys = None
		self.player = None
		self._window = window
		self._charater = character
		self.avatarcell = 0

	def load(self):
		'''setting up the game before the game's main while loop '''

		##-------------setting up pygame window---------------
		# pygame.init()
		# self._window = pygame.display.set_mode((_INITIAL_BACKGROUD_WIDTH, _INITIAL_BACKGROUD_HEIGHT), pygame.RESIZABLE)
		# pygame.display.set_caption('Pokemon') # Sets the window name 
		##-------------setting up pygame window---------------
		try:
			## Since this is outside the main while loop to start the game, therefore self.quit() doesn't apply
			## if the user exit the window before the game starts,
			## we need to prevent other functions from calling


			# ##-------setting up character selection---------------
			# self.start_menu()
			# self.player = player.Player(_INITIAL_BACKGROUD_WIDTH/2, _INITIAL_BACKGROUD_HEIGHT/2)
			# character = self.avatar_selection() 
			# if character == None:
			# 	## temporary, maybe pit all of this under the start_menu
			# 	raise pygame.error()
			# self.player.avatar(character) ## CHOSE THE AVATAR from 1 - 5, Can put somewhere else
			# self.avatar = pygame.image.load(self.player.path).convert_alpha() # 
			# ##-------setting up character selection---------------
			self.player = player.Player(_INITIAL_BACKGROUD_WIDTH/2, _INITIAL_BACKGROUD_HEIGHT/2, self._charater)
			self.avatar = pygame.image.load(self.player.path).convert_alpha() # 
			## ----------setting up moving background-----------------
			self.map = background_mech.Tiledmap(BACKGROUND) ## load filename
			self.map_image = self.map.make_map() ## blit tiles to screen, return a surface with the tiles
			self.map_rect = self.map_image.get_rect() 

			self.camera = background_mech.camera(self.map.width, self.map.height,self._window)
			## ----------setting up moving background-----------------
		except pygame.error:
			self.quit()
			
	def start_menu(self):

		start = True
		w, h = self._window.get_size()
		
		start_logo = Text('Comic Sans MS', 50, 'Pokemon', (0, 0, 0), self._window, w / 2, h - (h - 50))
		sample_text = Text('Comic Sans MS', 20, 'Test', (0, 0, 0), self._window, 25, 20)
		new_game = Button(self._window, (25, 150, 100, 50),(0, 0, 0), 'New Game', 15, 'Comic Sans MS',
						 (255, 255, 255))
		load_game = Button(self._window, (150, 150, 100, 50), (0, 0, 0), 'Load Game', 15, 'Comic Sans MS',
						 (255, 255, 255))		

		# While user is in the start menu	
		while start == True:

			self._window.fill((255, 255, 255))

			start_logo.create()
			new_game.create()
			load_game.create()

			if new_game.clicked():
				start = False
			if load_game.clicked():
				pass

			new_game.hover()
			load_game.hover()

			pygame.display.update()

			for event in pygame.event.get():
				mouse_pos = pygame.mouse.get_pos()

				if event.type == pygame.QUIT:
					start = False
					pygame.quit()

	
	def avatar_selection(self):
		selection = True
		w, h = self._window.get_size()

		a1_button = Button(self._window, (w - (w - 25), h / 2 + 25, 75, 40), (0, 0, 0), 'Avtar 1', 10, 'Comic Sans MS',
			              (255, 255, 255))
		a2_button = Button(self._window, (w - (w - 120), h / 2 + 25, 75, 40), (0, 0, 0), 'Avatar 2', 10, 'Comic Sans MS',
	                      (255, 255, 255))
		a3_button = Button(self._window, (w - (w - 200), h / 2 + 25, 75, 40), (0, 0, 0), 'Avatar 3', 10, 'Comic Sans MS',
			              (255, 255, 255))

		# While the user is selecting their character
		while selection:
			self._window.fill((255, 255, 255))

			a1 = AvatarSelection('backgrounds/character1/bd.png', 1, 4, 0, 0, 200, 300, self._window).create_avatar_selection()
			a1_button.create()

			a2 = AvatarSelection('backgrounds/character1/gd.png', 1, 4, 0, 0, 300, 300, self._window).create_avatar_selection()
			a2_button.create()

			a3 = AvatarSelection('backgrounds/avatars/3.png', 4, 3, 0, 1, 400, 297, self._window).create_avatar_selection()
			a3_button.create()

			pygame.display.update()

			for event in pygame.event.get():
				mouse_pos = pygame.mouse.get_pos()

				if event.type == pygame.QUIT:
					selection = False
					self.quit()
					

	def play(self):
		'''if the game is in the playing state'''
	
		## TESTING AREA -------------------------
		## AREA FOR SPAWNING OBSTACLES
		## iterate all the objects in the .tmx file 
		## and check if it is stored in our obstacle dict
		## and if it is, call the value of the dict, and pass it the arguments
		## Need to keep track of when the maps change
		dic = {'water', 'grass', 'wall'}
		for tile_object in self.map.tmxdata.objects:
			if tile_object.name in dic:
				print(tile_object.name)
			

		## TESTING AREA -------------------------

		while self._running:
			# print("Game is running")

			if self.player._avatar <= 2:
				## since if we choose avatar 1, 2 then 
				## we are loading different pictures since movements are croped
				## to different pictures
				self.avatar = pygame.image.load(self.player.path).convert_alpha()

			pygame.time.delay(100)
			# Just checks to see if user clicked the "X" on the top
			# right of the window

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				if event.type == pygame.VIDEORESIZE:
					### NEED MORE WORK, MAKE SURE TO SEPARATE TO ANOTHER FILE

					self._window = pygame.display.set_mode((event.w, event.h),
															pygame.RESIZABLE)
					self.player.x = event.w // 2
					self.player.y = event.h // 2
				elif event.type == pygame.MOUSEBUTTONDOWN:
					print("Mouse detected in play state")
					# if the user pressed the mouse
					### Not sure if we need this during the play state
					### Maybe if we click on something, we can get it's information??
					### Not sure, but doesn't need this
					self.handle_mouse()
			self.handle_play_events()

			### make a draw class
			self._window.fill((0, 0, 0))
			self.draw()
			
			# self._window.blit(self.avatar, 
			# 	(self.player.x, self.player.y), 
			# 	(self.player.current_col()*sprite_width,self.player.current_row() * sprite_height, 
			# 	sprite_width, sprite_height))
			
			# pygame.display.update()
	def draw(self):
		'''draw the avatar when it moves '''

		## draws the map
		self._window.blit(self.map_image, self.camera.apply_rect(self.map_rect))

		## avatar can move if the scrolling backgound is not moving
		# self.draw_avatar(self.player.x, self.player.y)
		# self.camera.update(self.player)
		# self.tilemap.camera(self.player, self._window)
		self.draw_avatar(_INITIAL_BACKGROUD_WIDTH/2, _INITIAL_BACKGROUD_HEIGHT/2)
		# self.tilemap.camera(self.player, self._window)
		
		pygame.display.update()


	def draw_avatar(self, x, y):
		''' draws the avatar on screen '''
		##---------------------------------------------------------##
		## Avatar animation, chooses the coordinate of the avatar's
		## movement in the .png file
		##---------------------------------------------------------##

		area = self.avatar.get_width(), self.avatar.get_height() # get the dimension of the entire image
		sprite_width, sprite_height = area[0]/self.player.sprite_col(), area[1]/self.player.sprite_row() 

		## blit the screen once we got the avatar
		self._window.blit(self.avatar, 
			(x, y), 
			(self.player.current_col()*sprite_width,self.player.current_row() * sprite_height, 
			sprite_width, sprite_height))

		self.camera.update(self.player)
	

	def pause(self):
		''' the pause state brings up the settings.
			So far, the setting includes exit, save, Pokedex(?), 
			Pokemon, Personal info (badges,etc), bags (items)'''

		### PROBLEM SO FAR IS THAT WHEN WE EXIT PLAY STATE WITH X
		### PAUSE FUNCTION IS CALLED BEFORE IT EXIT. 
		### NOT A MAJOR PROBLEM BUT PAUSE SHOULDN'T BE CALLED AT ALL
		### PUT IF ELSE STATEMENTS
		print("self.pause: pause state")

		setting = pygame.image.load('backgrounds/settings.png')
		self._window.blit(setting, (50,100))
		while self._pause == True:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						'''
						if user pressed esc again, then exit
						pause state and resume the play state. The time wait prevent
						the game from registering the key too fast  
						'''
						self._pause = False
						self._running = True
						pygame.time.wait(250)
					elif event.key == pygame.K_DOWN:
						pass
					elif event.key == pygame.K_UP:
						pass
				if event.type == pygame.MOUSEBUTTONDOWN:
					### If we use mouse instead of keyboard
					### Checks to see the mouse click is within range of the option
					### make sure to draw the options
					self.handle_mouse()
					# pass 
			# self.handle_setting()
			pygame.display.update()

	def run(self):

		## DO NOT UNCOMMENT, SECTION MOVE TO load()
		# ## UNCOMENT THIS SECTION
		# pygame.init()

		# self._window = pygame.display.set_mode((_INITIAL_BACKGROUD_WIDTH, _INITIAL_BACKGROUD_HEIGHT), pygame.RESIZABLE)

		# pygame.display.set_caption('Pokemon') # Sets the window name 

		# ##---------------------------set up characters -----------------##
		# ## let player choose types of avatar
		# self.start_menu()
		# self.player = player.Player(_INITIAL_BACKGROUD_WIDTH/2, _INITIAL_BACKGROUD_HEIGHT/2)
		# character = self.avatar_selection()
		# self.player.avatar(character) ## CHOSE THE AVATAR from 1 - 5, Can put somewhere else
		# self.avatar = pygame.image.load(self.player.path).convert_alpha() # 
		# self.load()
		# ##--------------------------------------------------------------##
		# ## UNCOMENT SECTION

		
		# ##---------------TESTING---------------##
		# self.player = player.Player(_INITIAL_BACKGROUD_WIDTH/2, _INITIAL_BACKGROUD_HEIGHT/2)
		self.load()
		# self.player.avatar(1) ## CHOSE THE AVATAR from 1 - 5, Can put somewhere else
		# self.avatar = pygame.image.load(self.player.path).convert_alpha() # 
		# # self.tilemap = background_mech.Tiledmap(BACKGROUND)
		# # self.camera(0,0)
		# ##---------------END TESTING CODE -----##

		while not (self._running == False and self._pause == False):
			
			self.play()
			self.pause()


		pygame.quit()


	def quit(self):
		'''kills the game'''

		self._running = False
		self._pause = False

	def handle_mouse (self):
		self._mousex, self._mousey = pygame.mouse.get_pos()
		print("mouse coordinate: x = ", self._mousex, " y = ", self._mousey)
		# print(self._mousex, self._mousey)



	def handle_play_events(self):
		# function to handle movements
		keys = pygame.key.get_pressed()
		
		'''
		player movements
		'''

		if keys[pygame.K_UP]:
			self.player.moveup()
		if keys[pygame.K_DOWN]:
			self.player.movedown()
		if keys[pygame.K_RIGHT]:
			self.player.moveright()
		if keys[pygame.K_LEFT]:
			self.player.moveleft()

		'''settings. Problem: holding any key shouldn't do anything'''
		
		if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
			print("Save option")
			f = open("SAVED_GAME.txt", "w+")
			### created a txt file for saved game, what what should be saved??

			f.write("%s\n", self.player._avatar) # Save the avatar

		if keys[pygame.K_ESCAPE]:
			# If user press esc, then bring up the setting option
			self._pause = True
			self._running = False
	

		

if __name__ == '__main__':
	# print("uncomment lines in Pokemon.run()")
	print("=============================debugging purposes=================================================")
	pygame.init()
	pygame.display.set_caption('Pokemon')
	CHARACTER = 1
	WINDOW = pygame.display.set_mode((_INITIAL_BACKGROUD_WIDTH, _INITIAL_BACKGROUD_HEIGHT), pygame.RESIZABLE)
	Pokemon(WINDOW, CHARACTER).run()
	print("=============================debugging purposes=================================================")
    
