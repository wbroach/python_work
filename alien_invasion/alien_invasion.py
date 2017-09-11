#!/usr/bin/env python3

import game_functions as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	play_button = Button(ai_settings, screen, "Play")
	
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	ship = Ship(screen)
	bullets = Group()
	aliens = Group()
	
	gf.create_fleet(screen, ship, aliens)
	
	# main game loop begins here
	while True:
		gf.check_events(screen, stats, play_button, ship, 
			aliens, bullets, sb)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, screen, ship, stats, sb)
			gf.update_aliens(aliens, ship, bullets, stats, screen, sb)
		
		gf.update_screen(ai_settings, screen, ship, bullets, aliens,
			stats, play_button, sb)
				
run_game()

				
				
		

