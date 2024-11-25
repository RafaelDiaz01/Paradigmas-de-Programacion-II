import sys
import pygame

def game_events(alumno):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Verificar si el evento (presionar tecla) se ha ejecutado
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = True
            elif event.key == pygame.K_LEFT:
                alumno.is_moving_left = True
            elif event.key == pygame.K_UP:
                alumno.is_moving_up = True
            elif event.key == pygame.K_DOWN:
                alumno.is_moving_down = True

        # Verificar si el evento (soltar tecla) se ha ejecutado
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = False
            elif event.key == pygame.K_LEFT:
                alumno.is_moving_left = False
            elif event.key == pygame.K_UP:
                alumno.is_moving_up = False
            elif event.key == pygame.K_DOWN:
                alumno.is_moving_down = False

def screen_refresh():
    pygame.display.flip()