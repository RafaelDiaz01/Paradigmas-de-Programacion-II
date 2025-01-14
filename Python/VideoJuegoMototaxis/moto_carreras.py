import sys
import pygame
from Config import Config
from mototaxi import Mototaxi
from cono import Cono
import game_functionalities

def show_start_screen(screen, moto_config):
    # Inicializar el mezclador de música
    pygame.mixer.init()

    # Cargar música para la pantalla de inicio
    pygame.mixer.music.load("Media/musica_inicio.mp3")  # Ruta al archivo de música
    pygame.mixer.music.set_volume(0.2)  # Ajustar volumen
    pygame.mixer.music.play(-1)  # Reproducir en bucle

    # Cargar la imagen de fondo
    background_image = pygame.image.load("Media/base.png")
    background_image = pygame.transform.scale(background_image, (moto_config.screen_width, moto_config.screen_height))

    # Cargar la fuente
    font_path = "Media/LetraRetro.ttf"  # Ruta al archivo de la fuente
    font = pygame.font.Font(font_path, 50)  # Tamaño 50

    # Renderizar texto
    # title_text = font.render("MTX RACING", True, (235, 8, 8))  # Texto blanco
    # screen.blit(title_text, (100, 100)) # Dibujar en la posición (100, 100)

    # Fuente y colores para texto y botón
    button_font = pygame.font.Font(font_path, 25)
    text_color = (255, 255, 255)  # Blanco
    button_color = (0, 128, 0)    # Verde oscuro
    button_hover_color = (0, 200, 0)  # Verde claro

    # Coordenadas del botón
    button_rect = pygame.Rect(0, 0, 200, 80)
    button_rect.center = (moto_config.screen_width // 2, moto_config.screen_height // 2)

    running = True
    while running:
        # Dibujar la imagen de fondo
        screen.blit(background_image, (0, 0))

        # Mostrar el título
        #screen.blit(title_text, (moto_config.screen_width // 2 - title_text.get_width() // 2, 15))

        # Dibujar el botón
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, button_hover_color, button_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)

        # Agregar texto al botón
        button_text = button_font.render("Start", True, text_color)
        screen.blit(button_text, (button_rect.centerx - button_text.get_width() // 2,
                                  button_rect.centery - button_text.get_height() // 2))

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                # Detener música actual
                pygame.mixer.music.stop()
                running = False  # Sale de la pantalla de inicio

        pygame.display.flip()
        pygame.time.Clock().tick(moto_config.FPS)

def show_gameOver_screen(screen, moto_config):
    # Establecer el fondo negro
    screen.fill((0, 0, 0))  # Color negro de fondo

    # Cargar imagen encima del texto (reemplaza 'Media/gameover_image.png' con la ruta de tu imagen)
    game_over_image = pygame.image.load("Media/game_over.png")
    game_over_image = pygame.transform.scale(game_over_image, (600, 400))  # Imagen más grande
    screen.blit(game_over_image, (moto_config.screen_width // 2 - game_over_image.get_width() // 2, -150))  # Posición más arriba y centrada

    # Cambiar tamaño de la fuente para "GAME OVER" y establecer color blanco con estilo vintage
    font_path = "Media/LetraRetro.ttf"  # Ruta al archivo de la fuente
    font = pygame.font.Font(font_path, 60)  # Tamaño más grande para el texto
    game_over_text = font.render("GAME OVER", True, (255, 255, 255))  # Texto blanco
    screen.blit(game_over_text, (moto_config.screen_width // 2 - game_over_text.get_width() // 2, 200))  # Posición debajo de la imagen

    # Mostrar el texto "Play Again"
    play_again_font = pygame.font.Font(font_path, 30)
    play_again_text = play_again_font.render("Play Again", True, (255, 255, 255))
    screen.blit(play_again_text, (moto_config.screen_width // 2 - play_again_text.get_width() // 2, 300))

    # Actualizar la pantalla
    pygame.display.flip()
    pygame.time.Clock().tick(moto_config.FPS)

def run_game():
    pygame.init()

    # Crear configuración del juego
    moto_config = Config()

    # Configuración de la pantalla
    screen_size = (moto_config.screen_width, moto_config.screen_height)
    screen = pygame.display.set_mode(screen_size)

    # Título del juego
    pygame.display.set_caption(moto_config.game_title)

    # Mostrar pantalla de inicio
    show_start_screen(screen, moto_config)

    # Reproducir música de fondo
    pygame.mixer.music.load("Media/musica_fondo.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # Música en bucle infinito

    # Creamos el objeto de la clase Mototaxi.
    mototaxi = Mototaxi(screen, moto_config)

    # Inicializar enemigos y puntuación
    enemies = []  # Lista vacía para los enemigos
    score = {"points": 0}  # Diccionario para manejar la puntuación

    # Creamos el objeto de la clase cono
    cono = Cono(screen, moto_config, score, enemies, mototaxi)

    running = True
    while running:
        game_functionalities.game_events(moto_config, screen, mototaxi)
        game_functionalities.screen_refresh(moto_config, screen, mototaxi, score, cono)

        # Comprobar si el juego ha terminado
        if game_functionalities.check_game_over(moto_config, screen, mototaxi, enemies, cono):
            show_gameOver_screen(screen, moto_config)
            break  # Fin del juego, esperar a que el jugador reinicie

# Código a nivel de módulo
if __name__ == "__main__":
    run_game()
