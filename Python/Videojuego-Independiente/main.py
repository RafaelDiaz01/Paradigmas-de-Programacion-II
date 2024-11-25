import pygame
import sys
from Config import Config
from personaje import Personaje

jugador = Personaje(350,350)

def run_game():
    pygame.init()

    # Crear configuración del juego.
    juego_unsij_config = Config()

    # Configuración de la pantalla.
    screen_size = (juego_unsij_config.screen_width, juego_unsij_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    # Título del juego.
    pygame.display.set_caption(juego_unsij_config.game_title)

    # Escalar la imagen de fondo al tamaño de la pantalla.
    background_image = pygame.transform.scale(juego_unsij_config.background_image, screen_size)

    running = True
    while running:

        # Dibujar el fondo.
        screen.blit(background_image, (0, 0))

        # Dibuja al personaje encima del fondo.
        jugador.dibujar(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Reconocer si se presiona una tecla.
            if event.type == pygame.KEYDOWN:
                # Cuando se pulsa la letra "a" del teclado imprime "Izquierda" en consola.
                if event.key == pygame.K_a:
                    print("Izquierda")

                # Cuando se pulsa la letra "d" del teclado imprime "Derecha" en consola.
                if event.key == pygame.K_d:
                    print("Derecha")

                # Cuando se pulsa la letra "a" del teclado imprime "Arriba" en consola.
                if event.key == pygame.K_w:
                    print("Arriba")

                # Cuando se pulsa la letra "s" del teclado imprime "Abajo" en consola.
                if event.key == pygame.K_s:
                    print("Abajo")


        # Actualizar la pantalla.
        pygame.display.update()

if __name__ == "__main__":
    run_game()