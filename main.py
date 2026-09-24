import pygame
from pathlib import Path
from screens.menu import MenuScreen
from screens.game import GameScreen

pygame.init()
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
VIRTUAL_WIDTH = int(WIDTH/2)
VIRTUAL_HEIGHT = int(HEIGHT/2)
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Flavours Test")
script_dir = Path(__file__).parent
clock = pygame.time.Clock()

menu_screen = MenuScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, script_dir)
from music import Music
music = Music(script_dir)
game_screen = GameScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, script_dir, music)
virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
current_screen_n = ""
current_screen = "menu"
running = True

fps_counter = 0
from music import Music
music = Music(script_dir)
music.play("menu")

while running:
    clock.tick(FPS)
    fps_counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_screen == "menu":
            result = menu_screen.handle_event(event)
            if result == "game":
                game_screen.reset()
                current_screen = "game"
                continue
            elif result == "quit":
                running = False
        elif current_screen == "game":
            result = game_screen.handle_event(event)
            if result == "menu":
                current_screen = "menu"
                music.play("menu")
                continue
    if current_screen == "menu":
        menu_screen.update()
        menu_screen.draw(virtual_screen)
    elif current_screen == "game":

        game_screen.draw(virtual_screen)
        game_screen.update()
        game_screen.draw_text(virtual_screen)
    if fps_counter % 60 == 0 and current_screen == "game":
        if game_screen.counter <= 0:
            pass
        elif game_screen.typed_chars >= len(game_screen.current_text_str) and game_screen.counter > 0:
            game_screen.counter = game_screen.counter - 1
    expanded = pygame.transform.scale(virtual_screen, (WIDTH, HEIGHT))
    screen.blit(expanded, (0, 0))
    pygame.display.flip()
pygame.quit()

