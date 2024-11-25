import pygame

# Aquí se configuran parámetros que no se van a modificar.

class Config:
    def __init__(self):
        self.screen_width = 1080
        self.screen_height = 720
        self.game_title = "Escape de Alumnos"
        self.background_image = pygame.image.load("Media/compu.png")