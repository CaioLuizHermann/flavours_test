import pygame

pygame.init()
info = pygame.display.Info()
WIDTH = info.current_w
HEIGHT = info.current_h
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Meu Jogo")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    screen.fill((255, 229, 204))
    start_btn_w = 350
    start_btn_h = 100
    start_btn_x = WIDTH/2 - start_btn_w/2
    start_btn_y = HEIGHT/2 - start_btn_h/2 + 150
    start_btn = pygame.draw.rect(screen, (255,255,255), (start_btn_x, start_btn_y, 350, 100))
    pygame.display.flip()

pygame.quit()
