import pygame
from pygame.sprite import Sprite

class Laptop (Sprite):

    def __init__(self, esc_alumno_config, screen, esc_alumno_personaje): # Objeto de las configuraciones, screen y alumno.
        super(Laptop, self).__init__()

        # Atributos
        self.esc_alumno_config = esc_alumno_config
        self.esc_alumno_personaje = esc_alumno_personaje
        self.screen = screen

        # Se carga la imagen y obtiene el rectángulo
        self.image = pygame.image.load("Media/laptop.png")
        self.image_laptop_rect = self.image.get_rect() # Rectángulo de la imagen
        self.screen_rect = screen.get_rect() # Obtiene el rectángulo de la pantalla

        # Inicializar posición a partir de la imagen del jugador
        self.image_laptop_rect.centerx = self.esc_alumno_personaje.image_rect.centerx
        self.image_laptop_rect.top = self.esc_alumno_personaje.image_rect.top

        # Centros del rectángulo utilizando variables flotantes. Esto permite controlar la velocidad.
        self.image_laptop_rect_centerx = float(self.image_laptop_rect.centerx)
        self.image_laptop_rect_centery = float(self.image_laptop_rect.centery)

        # Velocidad de la laptop obtenida de las configuraciones
        self.laptop_speed = self.esc_alumno_config.laptop_speed  # Variable para la velocidad.

    # Métod0 que dibuja el arma laptop.
    def dibujar_laptop(self):
        self.screen.blit(self.image, self.image_laptop_rect)

    def update_laptop(self):
        # Se actualiza el valor decimal de la posición.
        self.image_laptop_rect_centery -= self.laptop_speed

        # Se actualiza el valor de la posición del Rect de la laptop.
        self.image_laptop_rect.centery = self.image_laptop_rect_centery