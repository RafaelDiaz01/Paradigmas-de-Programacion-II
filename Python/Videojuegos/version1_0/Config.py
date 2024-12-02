import pygame

# Aquí se configuran parámetros que no se van a modificar.

class Config:
    def __init__(self):
        self.screen_width = 1080
        self.screen_height = 520
        self.game_title = "Escape de Alumnos"
        self.background_image = pygame.image.load("Media/espacio.png")
        self.alumno_speed = 5.0 # Velocidad del personaje (flotante).
        self.laptop_speed = 5.0 # Velocidad del arma laptop.