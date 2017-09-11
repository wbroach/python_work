import pygame
from settings import Settings
from pygame.sprite import Sprite

class Ship(Sprite):
	
	def __init__(self, screen):
		super(Ship, self).__init__()
		
		self.screen = screen
		
		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
 
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		
		#initialize Settings object
		self.ship_set = Settings()
		
		
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += int(self.ship_set.ship_speed_factor)

		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= int(self.ship_set.ship_speed_factor)

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.rect.centerx = self.screen_rect.centerx
