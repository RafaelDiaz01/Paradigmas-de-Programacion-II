import sys
import pygame

def game_events(alumno, laptop):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Verificar si el evento (presionar tecla) se ha ejecutado
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = True # Bandera del alumno
            elif event.key == pygame.K_LEFT:
                alumno.is_moving_left = True
            elif event.key == pygame.K_UP:
                alumno.is_moving_up = True
            elif event.key == pygame.K_DOWN:
                alumno.is_moving_down = True
            elif event.key == pygame.K_SPACE:
                laptop.is_shoot = True

        # Verificar si el evento (soltar tecla) se ha ejecutado
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                alumno.is_moving_right = False
                laptop.is_moving_right = False
            elif event.key == pygame.K_LEFT:
                alumno.is_moving_left = False
                laptop.is_moving_left = False
            elif event.key == pygame.K_UP:
                alumno.is_moving_up = False
                laptop.is_moving_up = False
            elif event.key == pygame.K_DOWN:
                alumno.is_moving_down = False
                laptop.is_moving_down = False

def screen_refresh(esc_alumno_config, screen, esc_alumno_personaje, laptop):
    # Se muestra el fondo
    pygame.display.flip()

    # Se actualiza la posición del alumno y la laptop.
    esc_alumno_personaje.update()
    laptop.update_laptop()

    # Se muestra el objeto del alumno y la laptop en la pantalla.
    esc_alumno_personaje.dibujar()
    laptop.dibujar_laptop()

    # Se actualiza la pantalla, dando la impresión visual de movimiento.
    pygame.display.update() # Actualiza la pantalla.