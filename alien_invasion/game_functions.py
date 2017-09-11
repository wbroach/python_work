import sys
import pygame
from bullet import Bullet
from alien import Alien
from settings import Settings
from time import sleep


def check_events(screen, stats, play_button, ship, aliens, bullets, sb):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
				
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, screen, ship, bullets, aliens,
				stats, sb)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(screen, stats, play_button, ship, 
				aliens, bullets, mouse_x, mouse_y, sb)
			
def check_play_button(screen, stats, play_button, ship, 
		aliens, bullets, mouse_x, mouse_y, sb):
	
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	
	if button_clicked and not stats.game_active:
		start_game(screen, stats, aliens, bullets, ship, sb)
	
def check_keydown_events(event, screen, ship, bullets, aliens, stats, 
		sb):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True

	if event.key == pygame.K_LEFT:
		ship.moving_left = True
	
	if event.key == pygame.K_SPACE:
		fire_bullet(screen, ship, bullets)
		
	if event.key == pygame.K_p and not stats.game_active:
		start_game(screen, stats, aliens, bullets, ship, sb)
	
	if event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False
		
def start_game(screen, stats, aliens, bullets, ship, sb):
	ship.ship_set.initialize_dynamic_settings()

	pygame.mouse.set_visible(False)

	stats.reset_stats()
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()
	sb.prep_ships()
	sb.show_score()
	stats.game_active = True
	
	aliens.empty()
	bullets.empty()
	
	create_fleet(screen, ship, aliens)
	ship.center_ship()
	
def update_screen(ai_settings, screen, ship, bullets, aliens, 
		stats, play_button, sb):
	
	screen.fill(ai_settings.bg_color)
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
	aliens.draw(screen)
	sb.show_score()
		
	if not stats.game_active:
		play_button.draw_button()
		
	pygame.display.flip()
	
def remove_bullets(bullets):
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def update_bullets(bullets, aliens, screen, ship, stats, sb):
	bullets.update()
	remove_bullets(bullets)
	check_bullet_alien_collissions(screen, ship, bullets, aliens, stats, 
		sb)
		
def check_bullet_alien_collissions(screen, ship, bullets, aliens, stats, 
		sb):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += ship.ship_set.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)
		
	if len(aliens) == 0:
		bullets.empty()
		
		ship.ship_set.increase_speed()
		
		stats.level += 1
		sb.prep_level()
		
		create_fleet(screen, ship, aliens)
		for alien in aliens.sprites(): 
			alien.alien_set.alien_speed_factor = ship.ship_set.ship_speed_factor

def ship_hit(stats, screen, ship, aliens, bullets, sb):
		
	if stats.ships_left > 0:
		
		stats.ships_left -= 1
		sb.prep_ships()
		
		aliens.empty()
		bullets.empty()
		
		create_fleet(screen, ship, aliens)
		for alien in aliens.sprites():
			alien.alien_set.alien_speed_factor = ship.ship_set.ship_speed_factor

		ship.center_ship()
		
		sleep(0.5)
		
	else: 
		stats.game_active = False
		pygame.mouse.set_visible(True)
	
def check_aliens_bottom(stats, screen, ship, aliens, bullets, sb):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(stats, screen, ship, aliens, bullets, sb)
			break
	
def update_aliens(aliens, ship, bullets, stats, screen, sb):
	check_fleet_edges(aliens)
	aliens.update()
	
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(stats, screen, ship, aliens, bullets, sb)

	check_aliens_bottom(stats, screen, ship, aliens, bullets, sb)
	
def fire_bullet(screen, ship, bullets):
	new_bullet = Bullet(screen, ship)
	bullets.add(new_bullet)
	
def get_number_aliens_x(screen):
	alien = Alien(screen)
	alien_width = alien.rect.width
	available_space_x = alien.alien_set.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	
	return number_aliens_x
	
def get_number_rows(ship_height, alien_height):
	ai_settings = Settings()
	available_space_y = (ai_settings.screen_height -
		(3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	
	return number_rows

def create_alien(screen, aliens, alien_number, row_number):
	alien = Alien(screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def create_fleet(screen, ship, aliens):
	alien = Alien(screen)
	number_aliens_x = get_number_aliens_x(screen)
	number_rows = get_number_rows(ship.rect.height, alien.rect.height)
	
	for i in range(number_rows):
		for j in range(number_aliens_x):
			create_alien(screen, aliens, j, i)
			
def check_fleet_edges(aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(aliens)
			break
			
def change_fleet_direction(aliens):
	for alien in aliens.sprites():
		alien.rect.y += alien.alien_set.fleet_drop_speed
		alien.alien_set.fleet_direction *= -1
		
def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()


