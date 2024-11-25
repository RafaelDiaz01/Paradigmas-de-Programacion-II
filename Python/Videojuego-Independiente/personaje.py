import pygame

class Personaje:
    def __init__(self,x ,y):
        # Definimos la forma del personaje como rectángulo y tamaño de 20 x 20.
        self.forma = pygame.Rect(0, 0, 70, 70)
        self.forma.center = (x,y)

    def dibujar (self, interfaz):
        pygame.draw.rect(interfaz, (255, 255, 0), self.forma)