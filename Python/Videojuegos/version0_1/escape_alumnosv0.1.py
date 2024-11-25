import sys
import pygame

# Función para inicializar el juego
def run_game():
    pygame.init()
    screen = (1080,720) # Inicializar la pantalla
    display = pygame.display.set_mode(screen)
    game_title = "Escape de Alumnos" # Definir el título del juego.
    pygame.display.set_caption(game_title) # Muestra el título del juego.
    running = True
    while running:
        for event in pygame.event.get(): # Evento que realiza el usuario (mouse, teclado).
            if event.type == pygame.QUIT:
                sys.exit()
            background_color = (255, 87, 51) # Asignar color al fondo.
            display.fill (background_color)
            pygame.display.flip() # Actualiza la pantalla con los cambios realizados (ilusión de movimientos).

# Código a nivel de módulo.
run_game()
