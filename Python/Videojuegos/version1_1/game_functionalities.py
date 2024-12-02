import sys
import pygame

from laptop import Laptop

def game_events(esc_alumno_config, screen, alumno, laptops_group):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Verificar si el evento (presionar tecla) se ha ejecutado
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, esc_alumno_config, screen, alumno, laptops_group)

        # Verificar si el evento (soltar tecla) se ha ejecutado
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, alumno)

def game_events_keydown(event, esc_alumno_config, screen, alumno, laptops_group):
    if event.key == pygame.K_RIGHT:
        alumno.is_moving_right = True  # Actualiza la bandera.
    elif event.key == pygame.K_LEFT:
        alumno.is_moving_left = True
    elif event.key == pygame.K_UP:
        alumno.is_moving_up = True
    elif event.key == pygame.K_DOWN:
        alumno.is_moving_down = True
    elif event.key == pygame.K_SPACE:
        new_laptop = Laptop(esc_alumno_config, screen, alumno)
        laptops_group.add(new_laptop)

def game_events_keyup(event, alumno):
    if event.key == pygame.K_RIGHT:
        alumno.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        alumno.is_moving_left = False
    elif event.key == pygame.K_UP:
        alumno.is_moving_up = False
    elif event.key == pygame.K_DOWN:
        alumno.is_moving_down = False

def screen_refresh(esc_alumno_config, screen, esc_alumno_personaje, laptops_group, screen_size):
    # Se muestra el fondo
    # Escalar la imagen de fondo al tamaño de la pantalla
    background_image = pygame.transform.scale(esc_alumno_config.background_image, screen_size)
    screen.blit(background_image, (0, 0))

    # Se actualiza la posición del alumno.
    esc_alumno_personaje.update()

    # Se muestra el objeto alumno en pantalla.
    esc_alumno_personaje.dibujar()

    # Se actualiza la posición y se muestra el grupo de laptops en la pantalla.
    for laptop in laptops_group.sprites():
        laptop.update_laptop()
        laptop.dibujar_laptop()

    # Se actualiza la pantalla, dando la impresión visual de movimiento.
    pygame.display.update() # Actualiza la pantalla.