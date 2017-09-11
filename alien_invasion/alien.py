import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
	
	def __init__(self, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.alien_set = Settings()
		
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		
		if self.rect.right >= screen_rect.right:
			return True
			
		elif self.rect.left <= 0:
			return True
	
	def update(self):
		self.rect.x += int(self.alien_set.alien_speed_factor * self.alien_set.fleet_direction)
		
	
