import pygame
from Config import Config
from alumno import Alumno
from game_functionalities import game_events
import game_functionalities
from laptop import Laptop
from pygame.sprite import Group

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

    # Crear grupos
    laptops_group = Group()

    running = True
    while running:
        game_functionalities.game_events(esc_alumno_config, screen, esc_alumno_personaje, laptops_group)

        # Se actualizan los elementos de la pantalla en la función screen_refresh que recibe
        game_functionalities.screen_refresh(esc_alumno_config, screen, esc_alumno_personaje, laptops_group, screen_size)

# Código a nivel de módulo
if __name__ == "__main__":
    run_game()
