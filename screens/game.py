import pygame
from PIL import Image
import PIL
import random
class GameScreen:
    def __init__(self, width, height, script_dir):
        self.screen_n = 0
        self.points = 0
        self.texts = [
    "*Walks through the front door*",
    "What a long day.",
    "*Drags feet toward the bedroom*",
    "*Closes the door behind him*",
    "*Freezes* ...Wait. Something's moving on my desk.",
    "*Steps closer, squinting* Are those... my papers? Why are they shuffling on their own?",
    "And what is that blob?",
    "*Wobbles nervously* O-oh! You're home! Please don't scream!",
    "*Jumps back* You talked! You're a slime?!",
    "*Bounces slightly* I know this looks strange, but it's me. Marina.",
    "Marina? My English teacher, Marina?",
    "*Drips a little from embarrassment* The one and only. Or... what's left of her.",
    "What happened to you and why are you in my house?!",
    "*Shrinks a bit* A mad scientist ambushed me after class yesterday.",
    "He said I was \"the perfect test subject\" and turned me into this slime.",
    "That's insane. There has to be a way to reverse it, right?",
    "*Perks up, bouncing hopefully* There is! But I need your help.",
    "My help? What can I do?",
    "The scientist left behind an English assignment. He said if all the questions are answered correctly, we will gain the antidote.",
    "*Wobbles toward the papers on the desk* These papers... they're the assignment. Will you help me, please?",
    "*Sits down at the desk* Of course I will. Let's get you back to normal.",
    "*Bounces happily, leaving a tiny trail of goo* Thank you! Let's start right away!",
    "*Hops onto the desk, papers rustling beneath her* Alright! Let's begin with question one.",
    "\"Which of these words describes the sea-scent the best?\" a) Pungent b) Briny c) Salty d) Earthy",
    "*Bounces excitedly* Correct! \"Briny\" is magnificent for describing that salty ocean scent!",
    "Question two! \"Which of these flavors is tangy most similar to?\" a) Sour b) Salty c) Sickly Sweet d) Umami",
    "*Wiggles happily* Yes! Tangy and sour go hand in hand.",
    "Question three! \"Which of these is flaky?\" a) Croissant b) Pão de Queijo c) Pepperoni Pizza d) A Wooden Plank",
    "Exactly! Croissants are definitely flaky!",
    "Question four! \"Which of these has a pungent odor?\" a) A Snowflake b) A Raw Potato c) Lasagna d) Gorgonzola Cheese",
    "Yes, that's correct!",
    "Question five! \"Which of these can be considered earthy?\" a) French fries and a burger b) A mop and a broom c) Mushrooms and tubers d) Pasta with ground beef",
    "*Smiles in approval* Wonderful! You're really getting the hang of this!",
    "Question six! \"What does 'couch potato' mean?\" a) A potato sitting in the couch b) A person that lies down on the couch all day c) Kids that like couches and potatoes d) None of the options",
    "That's it! You're really getting the hang of this!",
    "*Takes a deep, nervous breath* This is it... the last question",
    "What is the correct scale of \"crunchiness\" from more crunchy to less crunchy? a) Crunchy, Crispy, Flaky b) Crispy, Snowflaky, Crunchy, Oyster c) Crunchy, Flaky, Radiant, Crispy d) Crunchy, Crispy, Flaky, Smiley",
    "That's... that's correct!!",
    "The antidote... it's ready!",
    "*Shields eyes as the vial begins to fizz and glow faintly* Marina?! Are you okay?!",
    "*Voice slightly muffled as she absorbs the liquid* I'm fine! Just... hold on!",
    "*The glow fades, revealing her human form once more* ...I— I'm back.",
    "*Looks down at her own hands, flexing her fingers* Hands. Actual hands!",
    "*Stunned* You're... you're really you again.",
    "*Smiles warmly, eyes glistening* Thanks to you. I don't know how to repay this.",
    "Final Points: "
        ]
        self.question_n = (23, 25, 27, 29, 31, 33, 36)
        self.marina = False
        self.displayed_points = 0
        self.counter_points = 0
        self.points_delay = 5
        self.wrong_active = False
        self.correct_answers = {23: 1, 25: 0, 27: 0, 29: 3, 31: 2, 33: 1, 36: 0}
        self.wrong_answer = "Darn it, let's try again!"
        self.script_dir = script_dir
        self.slime_active = False
        self.font_clock = pygame.font.Font(None, 70)
        self.font_mouse = pygame.font.Font(None, 30)
        self.font_speech = pygame.font.Font(script_dir / "assets/deltarune.ttf", 40)
        self.current_text_str = self.texts[0]
        self.type_speed = 0.5
        self.script_dir = script_dir
        self.width = width
        self.debug_mode = False
        self.question_active = False
        self.height = height
        self.current_frame_text_box = 0
        self.current_frame_slime = 0
        self.frame_counter_slime = 0
        self.current_frame_clock = 0
        self.frame_counter_clock = 0
        self.frame_counter_text_box = 0
        self.current_frame_background = 0
        self.frame_counter_background = 0
        self.frame_delay = 20
        self.counter = 60
        self.frames_textbox = []
        self.frames_clock = []
        self.frames_slime = []
        self.frames_background = []
        self.frames_question = []
        self.answer_selected = 0
        self.marina_human = pygame.image.load(script_dir / "assets/marina_human.png")
        self.marina_human = pygame.transform.scale(self.marina_human, (self.marina_human.get_width()*2, self.marina_human.get_height()*2))
        self.slime = Image.open(script_dir / "assets/slime.gif")
        self.clock = Image.open(script_dir / "assets/clock.gif")
        self.background = Image.open(script_dir / "assets/background_game.gif")
        self.HUD_clock = pygame.image.load(script_dir / "assets/HUD_clock.png")
        self.txt_box = Image.open(self.script_dir / "assets/textbox_player.gif")
        self.num_frames_slime = self.slime.n_frames
        self.num_frames_clock = self.clock.n_frames
        self.num_frames_background = self.background.n_frames
        self.num_frames_txtbox = self.txt_box.n_frames
        self.slime_screens = [11,13,14,16,18,19,21,22,37,39,40,41,43]
        self.player_screens = [0,1,2,3,4,5,6,8,10,12,15,17,20,38,42]
        self.unknown_screens = [7,9]
        self.typed_chars = 0.0
        self.talking()
        self.load_textbox()
        self.current_frame_question = 0
        self.frame_counter_question = 0
        self.frames_question = []
        for letter in "ABCD":
            img = Image.open(self.script_dir / f"assets/question_{letter}.gif")
            frames = []
            for i in range(img.n_frames):
                try:
                    img.seek(i)
                    question_RGBA = img.convert("RGBA")
                    question_frame_data = question_RGBA.tobytes()
                    question_frame_surface = pygame.image.frombytes(question_frame_data, question_RGBA.size, "RGBA")
                    question_frame_surface = pygame.transform.scale(question_frame_surface, (self.width / 5, (self.height / 3)* 1.3))
                    frames.append(question_frame_surface)
                except EOFError:
                    break
            self.frames_question.append(frames)
        for i in range(0, self.num_frames_txtbox):
            try:
                self.txt_box.seek(i)
                txt_box_RGBA = self.txt_box.convert("RGBA")
                txt_box_frame_data = txt_box_RGBA.tobytes()
                txt_box_frame_surface = pygame.image.frombytes(txt_box_frame_data, txt_box_RGBA.size, "RGBA")
                txt_box_frame_surface = pygame.transform.scale(txt_box_frame_surface, (self.width, (self.height / 3) * 1.3))
                self.frames_textbox.append(txt_box_frame_surface)
            except EOFError:
                break
        for i in range(0, self.num_frames_clock):
            try:
                self.clock.seek(i)
                clock_RGBA = self.clock.convert("RGBA")
                clock_frame_data = clock_RGBA.tobytes()
                clock_frame_surface = pygame.image.frombytes(clock_frame_data, clock_RGBA.size, "RGBA")
                clock_frame_surface = pygame.transform.scale(clock_frame_surface, (100,100))
                self.frames_clock.append(clock_frame_surface)
            except EOFError:
                break

        for i in range(0, self.num_frames_slime):
            try:
                self.slime.seek(i)
                slime_RGBA = self.slime.convert("RGBA")
                slime_frames_data = slime_RGBA.tobytes()
                slime_frame_surface = pygame.image.frombytes(slime_frames_data, slime_RGBA.size, "RGBA")
                slime_frame_surface = pygame.transform.scale(slime_frame_surface, (250, 250))
                self.frames_slime.append(slime_frame_surface)
            except EOFError:
                break
        for i in range(0, self.num_frames_background):
            try:
                self.background.seek(i)
                background_RGBA = self.background.convert("RGBA")
                background_frames_data = background_RGBA.tobytes()
                background_frame_surface = pygame.image.frombytes(background_frames_data, background_RGBA.size, "RGBA")
                background_frame_surface = pygame.transform.scale(background_frame_surface, (self.width, self.height))
                self.frames_background.append(background_frame_surface)
            except EOFError:
                break

    def talking(self):
        if self.screen_n in self.slime_screens or (self.screen_n >= 23 and self.screen_n <= 37):
            self.speaker = "slime"
            self.txt_box = Image.open(self.script_dir / "assets/textbox_marina.gif")
            self.question_active = False
        elif self.screen_n in self.player_screens:
            self.speaker = "player"
            self.txt_box = Image.open(self.script_dir / "assets/textbox_player.gif")
            self.question_active = False
        elif self.screen_n in self.unknown_screens:
            self.speaker = "unknown"
            self.txt_box = Image.open(self.script_dir / "assets/textbox.gif")
            self.question_active = False
        self.question_active = self.screen_n in self.correct_answers
            
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"
            if event.key == pygame.K_F6:
                if self.debug_mode == False:
                    self.debug_mode = True
                else:
                    self.debug_mode = False
            if event.key == pygame.K_RETURN:
                if self.counter <= 0:
                    self.go_to(self.screen_n + 2)     # o tempo acabou enquanto lia o erro
                else:
                    if self.wrong_active:
                        self.wrong_active = False
                        self.current_text_str = self.texts[self.screen_n]
                        self.typed_chars = 0.0
                        self.question_active = True
                    elif self.question_active:
                        if self.answer_selected == self.correct_answers[self.screen_n]:
                            self.points += self.counter * 100
                            self.next_screen()
                        else:
                            if self.counter >= 21:
                                self.counter = self.counter - 20
                            else:
                                self.counter = 0
                            self.wrong_active = True
                            self.question_active = False
                            self.current_text_str = self.wrong_answer
                            self.typed_chars = 0.0
                    else:
                        self.next_screen()
            if self.question_active == True and (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                self.answer_selected += 1
                if self.answer_selected >= 4:
                    self.answer_selected = 0
            if self.question_active == True and (event.key == pygame.K_w or event.key == pygame.K_UP):
                self.answer_selected -= 1
                if self.answer_selected <= -1:
                    self.answer_selected = 3

    def update(self):
        if self.screen_n >= 41:
            self.marina = True
        if self.screen_n in self.question_n:
            self.question_active = True
        else:
            self.question_active = False
        if self.question_active == True:
            self.frame_counter_question += 1
            if self.frame_counter_question >= self.frame_delay:
                self.current_frame_question += 1
                self.frame_counter_question = 0
                if self.current_frame_question >= len(self.frames_question[self.answer_selected]):
                    self.current_frame_question = 0
        if self.screen_n >= 7 and self.screen_n < 41:
            self.slime_active = True
        else:
            self.slime_active = False
        self.frame_counter_text_box += 1
        if self.frame_counter_text_box >= self.frame_delay:
            self.current_frame_text_box += 1
            self.frame_counter_text_box= 0
            if self.current_frame_text_box >= len(self.frames_textbox):
                self.current_frame_text_box = 0
        if self.question_active == True:
            self.frame_counter_clock += 1
            if self.frame_counter_clock >= self.frame_delay:
                self.current_frame_clock += 1
                self.frame_counter_clock= 0
                if self.current_frame_clock >= len(self.frames_clock):
                    self.current_frame_clock = 0
        if self.slime_active == True:            
            self.frame_counter_slime += 1
            if self.frame_counter_slime >= self.frame_delay:
                self.current_frame_slime += 1
                self.frame_counter_slime = 0
                if self.current_frame_slime >= len(self.frames_slime):
                    self.current_frame_slime = 0
        self.frame_counter_background += 1
        if self.frame_counter_background >= self.frame_delay:
            self.frame_counter_background = 0
            self.current_frame_background += 1
            if self.current_frame_background >= len(self.frames_background):
                self.current_frame_background = 0
        if self.typed_chars < len(self.current_text_str):
            self.typed_chars += self.type_speed
            if not self.wrong_active:
                self.current_text_str = self.texts[self.screen_n]
        if self.question_active and not self.wrong_active and self.counter <= 0:
            self.go_to(self.screen_n + 2)
        if self.screen_n == len(self.texts) -1:
            if self.displayed_points < self.points:
                self.displayed_points += 100
            self.texts[self.screen_n] = f"Final Points: {self.displayed_points}"
            self.current_text_str = f"Final Points: {self.displayed_points}"
            self.typed_chars = len(self.current_text_str)

    def draw(self, screen):
        screen.blit(self.frames_background[self.current_frame_background], (0, 0))
        if self.debug_mode == True:
            self.mouse_pos_original = pygame.mouse.get_pos()
            self.mouse_pos = (self.mouse_pos_original[0] / 2, self.mouse_pos_original[1] /2)
            self.mouse_pos_txt = self.font_mouse.render(str(self.mouse_pos), True, color = (255, 255, 255))
            self.rect_mouse = self.mouse_pos_txt.get_rect()
            self.rect_mouse.topright = (self.width - 10, 10)
            screen.blit(self.mouse_pos_txt, self.rect_mouse)
        self.text_render = self.font_clock.render(str(self.counter), True, color= (255, 255, 255))
        text_rect = self.text_render.get_rect()
        if self.marina:
            marina_rect = self.marina_human.get_rect()
            marina_rect.bottomleft = (50, self.height - 50)
            screen.blit(self.marina_human, marina_rect)
        screen.blit(self.frames_textbox[self.current_frame_text_box], (0, 300))

        if self.question_active == True:
            screen.blit(self.HUD_clock, (0, 0))
            clock_frame = self.frames_clock[self.current_frame_clock]
            clock_rect = clock_frame.get_rect()
            HUD_clock_rect = self.HUD_clock.get_rect()
            HUD_clock_rect.center = (70, 70)
            HUD_clock_center = HUD_clock_rect.center
            clock_rect.center = (HUD_clock_center)
            text_rect.center = HUD_clock_center
            screen.blit(self.frames_clock[self.current_frame_clock], clock_rect)
            screen.blit(self.text_render, text_rect)
            self.frame_question = self.frames_question[self.answer_selected][self.current_frame_question]
            self.question_rect = self.frame_question.get_rect(bottomright=(self.width - 10, 300))
            screen.blit(self.frame_question, self.question_rect)
        if self.slime_active == True:
            screen.blit(self.frames_slime[self.current_frame_slime], (10,73))
            
    def draw_text(self, screen):
        words = self.current_text_str.split(" ")
        lines = []
        present_line = ""
        for word in words:
            if len(present_line + word) < 47:
                present_line += word + " "
            else:
                lines.append(present_line)
                present_line = word + " "
        lines.append(present_line)
        remaining = int(self.typed_chars)    
        for i, line in enumerate(lines):
            if remaining <= 0:
                break
            line_render = self.font_speech.render(line[:remaining], True, color=(255, 255, 255))
            y = 340 + (i * 50)
            screen.blit(line_render, (20, y))

    def reset(self):
        self.typed_chars = 0.0
        self.question_active = False
        self.slime_active = False
        self.screen_n = 0
        self.counter = 60
        self.screen_n = 0
        self.typed_chars = 0.0
        self.answer_selected = 0
        self.wrong_active = False

    def get_current_screen(self):
        return self.screen_n
    
    def load_textbox(self):
        self.frames_textbox = []
        self.current_frame_text_box = 0
        for i in range(0, self.num_frames_txtbox):
            try:
                self.txt_box.seek(i)
                txt_box_RGBA = self.txt_box.convert("RGBA")
                txt_box_frame_data = txt_box_RGBA.tobytes()
                txt_box_frame_surface = pygame.image.frombytes(txt_box_frame_data, txt_box_RGBA.size, "RGBA")
                txt_box_frame_surface = pygame.transform.scale(txt_box_frame_surface, (self.width, (self.height / 3) * 1.3))
                self.frames_textbox.append(txt_box_frame_surface)
            except EOFError:
                break
    def next_screen(self):
        self.counter = 60
        if self.screen_n + 1 < len(self.texts):
            self.screen_n += 1
            self.typed_chars = 0.0
            self.talking()
            self.load_textbox()
    def go_to(self, n):
        self.screen_n = n
        self.typed_chars = 0.0
        self.counter = 60
        self.wrong_active = False
        self.answer_selected = 0
        self.current_text_str = self.texts[n]
        if n == len(self.texts) - 1:
            self.displayed_points = 0
        self.talking()
        self.load_textbox()
    def next_screen(self):
        if self.screen_n + 1 < len(self.texts):
            self.go_to(self.screen_n + 1)
