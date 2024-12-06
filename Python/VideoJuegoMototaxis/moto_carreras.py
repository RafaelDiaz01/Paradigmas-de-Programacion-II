import pygame
from Config import Config
from mototaxi import Mototaxi
from game_functionalities import game_events
import game_functionalities

def run_game():
    pygame.init()

    # Crear configuración del juego
    moto_config = Config()

    # Configuración de la pantalla
    screen_size = (moto_config.screen_width, moto_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    # Título del juego
    pygame.display.set_caption(moto_config.game_title)

    # Creamos el objeto de la clase Mototaxi.
    mototaxi = Mototaxi(screen, moto_config)

    running = True
    while running:
        game_functionalities.game_events(moto_config, screen, mototaxi)

        # Se actualizan los elementos de la pantalla en la función screen_refresh que recibe
        game_functionalities.screen_refresh(moto_config, screen, mototaxi, screen_size)

# Código a nivel de módulo
if __name__ == "__main__":
    run_game()
