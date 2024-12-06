import pygame
from pygame.sprite import Sprite

# Clase para controlar al hacker (funciona como enemigo)
class Hacker(Sprite):
    # Define el constructor del Hacker que hereda del constructor del Sprite
    def __init__(self, esc_alumno_config, screen):
        # Se llama al constructor de la clase Sprite
        super(Hacker, self).__init__()

        # Se crean los objetos de la pantalla y de las configuraciones del juego
        super().__init__()
        self.config = esc_alumno_config
        self.screen = screen
