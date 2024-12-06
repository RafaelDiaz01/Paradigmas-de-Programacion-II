import pygame

# Clase para manipular al personaje alumno.
class Alumno:
    def __init__(self, screen, esc_alumno_config):
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

        # Velocidad
        self.esc_alumno_config = esc_alumno_config # Se crea el objeto
        self.alumno_speed = self.esc_alumno_config.mototaxi_speed # Se crea la variable para la velocidad.
        self.image_rect_centerx = float(self.image_rect.centerx) # Hacemos un cast a flotante.
        self.image_rect_centery = float(self.image_rect.centery) # Cast a flotante

    # Métod0 que dibuja al alumno en su ubicación.
    def dibujar (self):
        self.screen.blit (self.image, self.image_rect)

    # Métod0 que actualiza la posición del personaje.
    def update(self):
        if self.is_moving_right and (self.image_rect.right < self.screen_rect.right):
            self.image_rect_centerx += self.alumno_speed # Velocidad a la derecha en flotante.
        if self.is_moving_left and (self.image_rect.left > self.screen_rect.left):
            self.image_rect_centerx -= self.alumno_speed # Velocidad a la izquierda en flotante.
        if self.is_moving_up and (self.image_rect.top > self.screen_rect.top):
            self.image_rect_centery -= self.alumno_speed # Velocidad hacia arriba.
        if self.is_moving_down and (self.image_rect.bottom < self.screen_rect.bottom):
            self.image_rect_centery += self.alumno_speed # Velocidad hacia abajo.

        self.image_rect.centerx = self.image_rect_centerx # Asignamos el flotante al entero.
        self.image_rect.centery = self.image_rect_centery # Asignamos el flotante al entero.