import pygame
class GameScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"
    def update(self):
        pass
    def draw(self, screen):
        screen.fill((255, 229, 204))