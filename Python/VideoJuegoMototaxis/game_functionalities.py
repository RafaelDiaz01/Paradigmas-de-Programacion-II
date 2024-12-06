import sys
import pygame

def game_events(moto_config, screen, mototaxi):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Verificar si el evento (presionar tecla) se ha ejecutado
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, moto_config, screen, mototaxi)

        # Verificar si el evento (soltar tecla) se ha ejecutado
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, mototaxi)

def game_events_keydown(event, moto_config, screen, mototaxi):
    if event.key == pygame.K_RIGHT:
        mototaxi.is_moving_right = True  # Actualiza la bandera.
    elif event.key == pygame.K_LEFT:
        mototaxi.is_moving_left = True
    elif event.key == pygame.K_UP:
        mototaxi.is_moving_up = True
    elif event.key == pygame.K_DOWN:
        mototaxi.is_moving_down = True

def game_events_keyup(event, mototaxi):
    if event.key == pygame.K_RIGHT:
        mototaxi.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        mototaxi.is_moving_left = False
    elif event.key == pygame.K_UP:
        mototaxi.is_moving_up = False
    elif event.key == pygame.K_DOWN:
        mototaxi.is_moving_down = False

def screen_refresh(moto_config, screen, mototaxi, screen_size):
    # Se muestra el fondo
    # Escalar la imagen de fondo al tamaño de la pantalla
    background_image = pygame.transform.scale(moto_config.background_image, screen_size)
    screen.blit(background_image, (0, 0))

    # Se actualiza la posición del alumno.
    mototaxi.update()

    # Se muestra el objeto alumno en pantalla.
    mototaxi.dibujar()

    # Se actualiza la pantalla, dando la impresión visual de movimiento.
    pygame.display.update() # Actualiza la pantalla.