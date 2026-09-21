import pygame
class MenuScreen:
    def __init__(self, width, height, script_dir):
        self.width = width
        self.height = height
        self.script_dir = script_dir
        self.background = pygame.image.load(script_dir / "assets/menu_background.png")
        self.background = pygame.transform.scale(self.background, (width, height))
        self.start_btn_w = 250
        self.start_btn_h = 100
        self.start_btn_img = pygame.image.load(script_dir / "start_btn.png")
        self.start_btn_img = pygame.transform.scale(self.start_btn_img, (self.start_btn_w, self.start_btn_h))
        self.start_btn_x = width/2 - self.start_btn_w/2
        self.start_btn_y = height/2 - self.start_btn_h/2 + 150
        self.start_btn_rect = pygame.Rect(self.start_btn_x, self.start_btn_y, self.start_btn_w, self.start_btn_h)
        self.title = pygame.image.load(script_dir / "assets/title.png")
        self.title = pygame.transform.scale(self.title, (550, 125)) 
        self.titlebox = pygame.image.load(script_dir / "assets/titlebox.png")
        self.titlebox = pygame.transform.scale(self.titlebox, (600, 250))
        self.titlebox_rect = self.titlebox.get_rect()
        self.title_rect = self.titlebox.get_rect()
        self.title_rect.center = (525, 350)
        self.titlebox_rect.center = (500, 235)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.start_btn_rect.collidepoint(self.mouse_pos_virtual):
                    return "game"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "quit"
        return None

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos_virtual = (self.mouse_pos[0] / 2, self.mouse_pos[1] / 2)
    def draw(self, screen):
        screen.fill((255, 229, 204))
        if self.start_btn_rect.collidepoint(self.mouse_pos_virtual):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(self.background, (0, 0))
        screen.blit(self.start_btn_img, (self.start_btn_x, self.start_btn_y))
        screen.blit(self.titlebox, self.titlebox_rect)
        screen.blit(self.title, self.title_rect)
