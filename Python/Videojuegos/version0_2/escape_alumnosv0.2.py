import sys
import pygame
from Config import Config


def run_game():
    pygame.init()

    # Crear configuración del juego
    esc_alumnos_config = Config()

    # Configuración de la pantalla
    screen_size = (esc_alumnos_config.screen_width, esc_alumnos_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    # Título del juego
    pygame.display.set_caption(esc_alumnos_config.game_title)

    # Escalar la imagen de fondo al tamaño de la pantalla
    background_image = pygame.transform.scale(esc_alumnos_config.background_image, screen_size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Dibujar el fondo
        screen.blit(background_image, (0, 0))

        # Actualizar la pantalla
        pygame.display.flip()


# Código a nivel de módulo
if __name__ == "__main__":
    run_game()
