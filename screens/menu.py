import pygame
class MenuScreen:
    def __init__(self, width, height, script_dir):
        self.width = width
        self.height = height
        self.script_dir = script_dir

        self.start_btn_w = 350
        self.start_btn_h = 100
        self.start_btn_img = pygame.image.load(script_dir / "start_btn.png")
        self.start_btn_img = pygame.transform.scale(self.start_btn_img, (self.start_btn_w, self.start_btn_h))
        self.start_btn_x = width/2 - self.start_btn_w/2
        self.start_btn_y = height/2 - self.start_btn_h/2 + 150
        self.start_btn_rect = pygame.Rect(self.start_btn_x, self.start_btn_y, self.start_btn_w, self.start_btn_h)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                if self.start_btn_rect.collidepoint(mouse_pos):
                    return "game"
        return None

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((255, 229, 204))
        mouse_pos = pygame.mouse.get_pos()
        if self.start_btn_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(self.start_btn_img, (self.start_btn_x, self.start_btn_y))