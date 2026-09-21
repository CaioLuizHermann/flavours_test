import pygame
from PIL import Image
import PIL
class MenuScreen:
    def __init__(self, width, height, script_dir):
        self.width = width
        self.height = height
        self.script_dir = script_dir
        self.background = pygame.image.load(script_dir / "assets/menu_background.png")
        self.frames_start_btn = []
        self.current_frame_start_btn = 0
        self.frame_counter_start_btn = 0
        self.frame_delay = 50
        self.background = pygame.transform.scale(self.background, (width, height))
        self.start_btn_img = Image.open(script_dir / "assets/start_button.gif")
        self.n_frames_start_btn = self.start_btn_img.n_frames
        for i in range(0, self.n_frames_start_btn):
            try:
                self.start_btn_img.seek(i)
                start_btn_RGBA = self.start_btn_img.convert("RGBA")
                start_btn_frame_data = start_btn_RGBA.tobytes()
                self.start_btn_frame_surface = pygame.image.frombytes(start_btn_frame_data, start_btn_RGBA.size, "RGBA")
                self.start_btn_frame_surface = pygame.transform.scale(self.start_btn_frame_surface, (self.width / 4, (self.height / 5)))
                self.frames_start_btn.append(self.start_btn_frame_surface)
            except EOFError:
                break
        self.start_btn_rect = self.start_btn_frame_surface.get_rect()
        self.start_btn_rect.center = (self.width/2, (self.height/2) * 1.4)
        self.title = pygame.image.load(script_dir / "assets/title.png")
        self.title = pygame.transform.scale(self.title, (width/2, height/5)) 
        self.titlebox = pygame.image.load(script_dir / "assets/titlebox.png")
        self.titlebox = pygame.transform.scale(self.titlebox, ((width/2) * 1.1,(height/5) * 1.1))
        self.titlebox_rect = self.titlebox.get_rect()
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (width/2, (height/2) * 0.6)
        self.titlebox_rect.center = self.title_rect.center
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
        self.frame_counter_start_btn += 1
        if self.frame_counter_start_btn >= self.frame_delay:
            self.current_frame_start_btn += 1
            self.frame_counter_start_btn = 0
            if self.current_frame_start_btn >= len(self.frames_start_btn):
                self.current_frame_start_btn = 0
    def draw(self, screen):
        screen.fill((255, 229, 204))
        if self.start_btn_rect.collidepoint(self.mouse_pos_virtual):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        screen.blit(self.background, (0, 0))
        screen.blit(self.frames_start_btn[self.current_frame_start_btn], (self.start_btn_rect))
        screen.blit(self.titlebox, self.titlebox_rect)
        screen.blit(self.title, self.title_rect)
