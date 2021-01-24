import pygame


class Menu():
    def __init__(self, virtuavelo):
        self.virtuavelo = virtuavelo
        self.mid_w, self.mid_h = self.virtuavelo.DISPLAY_W / 2, self.virtuavelo.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 40, 40)
        self.offset = - 200
        self.font_size = round((self.virtuavelo.DISPLAY_H + self.virtuavelo.DISPLAY_W) / 60)

    def draw_cursor(self):
        self.virtuavelo.draw_text('*', self.font_size - 5, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.virtuavelo.window.blit(self.virtuavelo.display, (0, 0))
        pygame.display.update()
        self.virtuavelo.reset_keys()


class MainMenu(Menu):
    def __init__(self, virtuavelo):
        Menu.__init__(self, virtuavelo)
        self.state = "Start"
        self.startx, self.starty = self.mid_w / 1.5, self.mid_h / 1.25
        self.statsx, self.statsy = self.mid_w * 1.5, self.mid_h / 1.25
        self.confx, self.confy = self.mid_w / 1.63, self.mid_h * 1.25
        self.helpx, self.helpy = self.mid_w * 1.60, self.mid_h * 1.65
        self.exitx, self.exity = self.mid_w * 1.75, self.mid_h * 1.65

        self.cursor_rect.midtop = ((self.startx + self.offset) / 1.1, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.virtuavelo.check_events()
            self.check_input()
            self.virtuavelo.display.fill(self.virtuavelo.BLACK)
            self.virtuavelo.draw_text('Main Menu', self.font_size, self.mid_w, self.mid_h - 300)
            self.virtuavelo.draw_text("Choisir un parcour", self.font_size, self.startx, self.starty)
            self.virtuavelo.draw_text("Statistiques", self.font_size, self.statsx, self.statsy)
            self.virtuavelo.draw_text("Configuration", self.font_size, self.confx, self.confy - 5)
            self.virtuavelo.draw_text("Exit", self.font_size, self.exitx, self.exity - 5)
            self.virtuavelo.draw_text("Help", self.font_size, self.helpx, self.helpy - 5)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.virtuavelo.DOWN_KEY:
            if self.state in ['Start', 'Stats']:
                self.cursor_rect.midtop = ((self.confx + self.offset)*1.07, self.confy*1.01)
                self.state = 'Conf'
            elif self.state == 'Conf':
                self.cursor_rect.midtop = ((self.helpx + self.offset)/0.9, self.helpy*1.005)
                self.state = 'Help'
            elif self.state in ['Exit', 'Help']:
                self.cursor_rect.midtop = ((self.startx + self.offset)/1.05, self.starty*1.02)
                self.state = 'Start'

        elif self.virtuavelo.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = ((self.exitx + self.offset)/0.907, self.exity*1.005)
                self.state = 'Exit'
            elif self.state in ['Exit', 'Help']:
                self.cursor_rect.midtop = ((self.confx + self.offset)*1.07, self.confy*1.01)
                self.state = 'Conf'
            elif self.state in ['Conf', 'Stats']:
                self.cursor_rect.midtop = ((self.startx + self.offset) / 1.05, self.starty * 1.02)
                self.state = 'Start'

        elif self.virtuavelo.RIGHT_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = ((self.statsx + self.offset)*1.04, self.statsy*1.02)
                self.state = 'Stats'
            elif self.state == 'Stats':
                self.cursor_rect.midtop = ((self.confx + self.offset)*1.07, self.confy*1.01)
                self.state = 'Conf'
            elif self.state == 'Conf':
                self.cursor_rect.midtop = ((self.helpx + self.offset)/0.9, self.helpy*1.005)
                self.state = 'Help'
            elif self.state == 'Help':
                self.cursor_rect.midtop = ((self.exitx + self.offset)/0.907, self.exity*1.005)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = ((self.startx + self.offset)/1.05, self.starty*1.02)
                self.state = 'Start'

        elif self.virtuavelo.LEFT_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = ((self.exitx + self.offset)/0.907, self.exity*1.005)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = ((self.helpx + self.offset)/0.9, self.helpy*1.005)
                self.state = 'Help'
            elif self.state == 'Help':
                self.cursor_rect.midtop = ((self.confx + self.offset)*1.07, self.confy*1.01)
                self.state = 'Conf'
            elif self.state == 'Conf':
                self.cursor_rect.midtop = ((self.statsx + self.offset)*1.04, self.statsy*1.02)
                self.state = 'Stats'
            elif self.state == 'Stats':
                self.cursor_rect.midtop = ((self.startx + self.offset)/1.05, self.starty*1.02)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.virtuavelo.START_KEY:
            if self.state == 'Start':
                self.virtuavelo.playing = True
            elif self.state == 'Stats':
                self.virtuavelo.curr_menu = self.virtuavelo.stats
            elif self.state == 'Conf':
                self.virtuavelo.curr_menu = self.virtuavelo.conf
            # TO DO : elif pour les autres fonctions HELP et EXIT
            self.run_display = False


class StatsMenu(Menu):
    def __init__(self, virtuavelo):
        Menu.__init__(self, virtuavelo)
        self.state = 'statistics'
        self.volx, self.voly = self.mid_w, self.mid_h
        self.controlsx, self.controlsy = self.mid_w, self.mid_h
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.virtuavelo.check_events()
            self.check_input()
            self.virtuavelo.display.fill((0, 0, 0))
            self.virtuavelo.draw_text('Options', self.font_size, self.mid_w, self.mid_h - 30)
            self.virtuavelo.draw_text("Volume", self.font_size, self.volx, self.voly)
            self.virtuavelo.draw_text("Controls", self.font_size, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.virtuavelo.BACK_KEY:
            self.virtuavelo.curr_menu = self.virtuavelo.main_menu
            self.run_display = False
        elif self.virtuavelo.UP_KEY or self.virtuavelo.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.virtuavelo.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass


class ConfMenu(Menu):
    def __init__(self, virtuavelo):
        Menu.__init__(self, virtuavelo)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.virtuavelo.check_events()
            if self.virtuavelo.START_KEY or self.virtuavelo.BACK_KEY:
                self.virtuavelo.curr_menu = self.virtuavelo.main_menu
                self.run_display = False
            self.virtuavelo.display.fill(self.virtuavelo.BLACK)
            self.virtuavelo.draw_text('Credits', self.font_size, self.mid_w, self.mid_h / 1.2)
            self.virtuavelo.draw_text('Made by me', self.font_size, self.mid_w, self.mid_h / 1.1)
            self.blit_screen()
