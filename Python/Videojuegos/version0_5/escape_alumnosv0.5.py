import pygame
from Config import Config
from alumno import Alumno
from game_functionalities import game_events

def run_game():
    pygame.init()

    # Crear configuración del juego
    esc_alumnos_config = Config()

    # Configuración de la pantalla
    screen_size = (esc_alumnos_config.screen_width, esc_alumnos_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    # Creamos el objeto de la clase Alumno.
    esc_alumno_personaje = Alumno(screen, esc_alumnos_config)

    # Título del juego
    pygame.display.set_caption(esc_alumnos_config.game_title)

    # Escalar la imagen de fondo al tamaño de la pantalla
    background_image = pygame.transform.scale(esc_alumnos_config.background_image, screen_size)

    running = True
    while running:

        # Dibujar el fondo
        screen.blit(background_image, (0, 0))

        # Llamar a la función de funcionalidades
        game_events(esc_alumno_personaje)

        # Mover al alumno
        esc_alumno_personaje.update()

        # Llamamos al constructor dibujar
        esc_alumno_personaje.dibujar()

        # Actualizar la pantalla
        pygame.display.flip()

# Código a nivel de módulo
if __name__ == "__main__":
    run_game()
