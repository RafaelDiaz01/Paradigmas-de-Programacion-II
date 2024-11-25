import pygame

# Clase para manipular al personaje alumno.
class Alumno:
    def __init__(self, screen):
        self.screen = screen
        # Se carga la imagen y se obtiene el Rect.
        self.image = pygame.image.load("Media/estudiante.png")
        self.image_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializar la posición
        self.image_rect.centerx = self.screen_rect.centerx # Eje x
        self.image_rect.bottom = self.screen_rect.bottom # Eje y

        # Bandera
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

    # Métod0 que dibuja al alumno en su ubicación.
    def dibujar (self):
        self.screen.blit (self.image, self.image_rect)

    # Métod0 que actualiza la posición del personaje.
    def update(self):
        if self.is_moving_right:
            self.image_rect.centerx += 10
        elif self.is_moving_left:
            self.image_rect.centerx -= 10
        elif self.is_moving_up:
            self.image_rect.centery -= 10
        elif self.is_moving_down:
            self.image_rect.centery += 10