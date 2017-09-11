import pygame
from pygame.sprite import Sprite
from settings import Settings

class Bullet(Sprite):
	
	def __init__(self, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen
		self.settings = Settings()
		
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
			self.settings.bullet_height)
		
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		self.y = self.rect.y
		
		self.color = self.settings.bullet_color

	def update(self):
		self.rect.y -= int(self.settings.bullet_speed_factor)
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		
			
		
		
