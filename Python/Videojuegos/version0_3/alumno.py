import pygame

# Clase para manipular al personaje alumno.
class Alumno:
    def __init__(self, screen):
        self.screen = screen
        # Se carga la imagen y se obtiene el Rect.
        self.image = pygame.image.load("../Media/carro_verde.png")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializar la posición
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

    # Métod0 que dibuja al alumno en su ubicación.
    def dibujar (self):
        self.screen.blit (self.image, self.image_rect)
