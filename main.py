import pygame
from pathlib import Path
from screens.menu import MenuScreen
from screens.game import GameScreen

pygame.init()
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Meu Jogo")
script_dir = Path(__file__).parent
clock = pygame.time.Clock()

menu_screen = MenuScreen(WIDTH, HEIGHT, script_dir)
game_screen = GameScreen(WIDTH, HEIGHT)

current_screen = "menu"
running = True

while running:
    clock.tick(FPS)
    fps_counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if current_screen == "menu":
        result = menu_screen.handle_event(event)
        if result == "game":
            current_screen = "game"
        elif result == "quit":
            pygame.quit()
    elif current_screen == "game":
        result = game_screen.handle_event(event)
        if result == "menu":
            current_screen = "menu"
    if current_screen == "menu":
        menu_screen.update()
        menu_screen.draw(screen)
    elif current_screen == "game":
        game_screen.draw(screen)
        game_screen.update()
    if fps_counter % 60 == 0 and current_screen == "game":
        game_screen.text = game_screen.text - 1
    
    pygame.display.flip()
pygame.quit()