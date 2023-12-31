import sys

import pygame

def check_events(ship):
    """Respond to keypressess and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship )
            
def check_keydown_events(event, ship):
        """Respond to keypresses.""" 
    
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True 
        


def check_keyup_events(event, ship):
        """Respond to key releases."""
    #elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
                ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                ship.moving_left = False
                    
                #Move ship to the right. pg250
                ship.rect.centerx += 1
            
def update_screen(ai_settings, screen, ship):
    """update images on the screen and flip to the new screen"""
    
    screen.fill(ai_settings.bg_color)
    ship.blitme()