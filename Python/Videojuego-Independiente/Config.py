import pygame

# Aquí se configuran parámetros que no se van a modificar.

class Config:
    def __init__(self):
        self.screen_width = 626
        self.screen_height = 417
        self.game_title = "BACK ROOM UNSIJ"
        self.background_image = pygame.image.load("/home/diaz/Descargas/bosque.jpg")