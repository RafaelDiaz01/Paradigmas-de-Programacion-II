import pygame
from Config import Config
from alumno import Alumno
from game_functionalities import game_events
import game_functionalities
from laptop import Laptop

def run_game():
    pygame.init()

    # Crear configuración del juego
    esc_alumno_config = Config()

    # Configuración de la pantalla
    screen_size = (esc_alumno_config.screen_width, esc_alumno_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    # Título del juego
    pygame.display.set_caption(esc_alumno_config.game_title)

    # Creamos el objeto de la clase Alumno.
    esc_alumno_personaje = Alumno(screen, esc_alumno_config)

    # Escalar la imagen de fondo al tamaño de la pantalla
    background_image = pygame.transform.scale(esc_alumno_config.background_image, screen_size)

    # Se crea el objeto de la laptop
    laptop = Laptop(screen, esc_alumno_config, esc_alumno_personaje)

    running = True
    while running:
        # Llamar a la función de funcionalidades
        game_events(esc_alumno_personaje, laptop)

        # Dibujar el fondo
        screen.blit(background_image, (0, 0))

        # Mover al alumno
        esc_alumno_personaje.update()

        # Llamamos al constructor dibujar
        esc_alumno_personaje.dibujar()

        # Actualizar la pantalla
        pygame.display.flip()

        # Se actualizan los elementos de la pantalla en la función screen_refresh que recibe
        game_functionalities.screen_refresh(esc_alumno_config, screen, esc_alumno_personaje, laptop)

# Código a nivel de módulo
if __name__ == "__main__":
    run_game()
