import pygame

# Aquí se configuran parámetros que no se van a modificar.

class Config:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 500
        self.game_title = "MTX Racing"
        self.background_image = pygame.image.load("Media/fondo_bucle.png")
        self.mototaxi_speed = 17.0 # Velocidad de la moto (flotante).
        self.scroll = 0
        self.background_speed = 1.0  # Velocidad inicial del fondo
        self.escalar_cono = 0.3 # Aumenta el tamaño del cono
        self.FPS = 60  # Velocidad a la que se mueve el fondo
        self.RELOJ = pygame.time.Clock()  # Inicializar el reloj como atributo de instancia
        self.enemy_speed = 10.0
