import pygame

# Aquí se configuran parámetros que no se van a modificar.

class Config:
    def __init__(self):
        self.screen_width = 626
        self.screen_height = 423
        self.game_title = "Moto Carreras"
        self.background_image = pygame.image.load("Media/carretera.jpeg")
        self.mototaxi_speed = 2.0 # Velocidad de la mototaxi (flotante).