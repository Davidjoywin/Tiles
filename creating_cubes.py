'''A program the draw cubes across the screen that changes color every second'''
import sys, random, time
import pygame
class Mcube:
    '''Moveable cube, it moves round across the screen and down the screen'''
    def __init__(self, screen, settings):
        self.screen = screen
        self.movement_y = 45
        self.screen_rect = screen.get_rect()
        self.setting = settings
        self.rect = pygame.Rect(35,45,40,40)
    
    def update_cube_pos(self):
        '''Moves the cube through the block and down the block
            return to the beginning at the end of the cube'''
        number_box_x = get_available_space_x(self.screen, self.setting)
        number_box_y = get_available_space_y(self.screen, self.setting)
        if self.rect.x < (number_box_x-1)*60:
            self.rect.x += 60
        elif self.rect.x >= (number_box_x-1)*60:
            self.rect.y += 60
            if self.rect.x != 35:
                self.rect.x = 35
        if self.rect.x < 35 + (number_box_x-1)*60 and self.rect.y == 45 + (number_box_y)*60:
            self.rect.x, self.rect.y = 35, 45
        

    def draw_moving_cube(self):
        '''draw the moving cube'''
        pygame.draw.rect(self.screen, self.setting.moveable_cube_color, self.rect)
    
class Setting:
    '''A class for the settings of the program'''
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 720
        self.moveable_cube_color =(255,0,0)
        self.rect_wall_thickness = 10
        self.margin_left = 30
        self.margin_top = 40
        self.FPS = 60


def get_available_space_x(screen, settings):
    '''returns the number of cubes in a row'''
    screen_rect = screen.get_rect()
    available_space_x = screen_rect.width - (10*2)
    number_x = int(available_space_x // 60)
    return number_x

def get_available_space_y(screen, setting):
    '''returns the number of rows'''
    screen_rect = screen.get_rect()
    available_space_y = screen_rect.height-(10*2)
    number_row_x = int(available_space_y // 60)
    return number_row_x

def create_cube(screen, settings, row_number, number_x, rect_color):
    '''Create a single cube'''
    pos_x = settings.margin_left + 60 * row_number
    pos_y = settings.margin_top + 60 * number_x
    rect = pygame.Rect((pos_x, pos_y),(50,50))
    pygame.draw.rect(screen, rect_color, rect, settings.rect_wall_thickness)

def check_screen_cube(random_screen_color, rect_color):
    pass
    
def create_cubes(screen, settings, rect_color):
    '''create cubes across the screen'''
    number_x = get_available_space_x(screen,settings)
    number_row_x = get_available_space_y(screen, settings)
    for row_number in range(number_x):
        for number_x in range(number_row_x):
            create_cube(screen, settings, row_number, number_x, rect_color)
def loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def run_main():
    '''the main function the run the main program'''
    pygame.init()
    settings = Setting()
    pygame.display.set_caption('Cubes')
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    screen_rect = screen.get_rect()
    cube = Mcube(screen, settings)

    rect_color = [(255,255,0), (255,255,255)]#yellow
    color = [(0,0,0), (0,0,255), (0,255,255), (255, 255,255), (255, 255,0), (255,0,255)]
    slp = pygame.time.Clock()


    while True:
        slp.tick(settings.FPS)
        random_screen_color = random.choice(color)
        '''conditional statement to change the color of the 
        cube when it equals the color of the screen'''
        if random_screen_color != rect_color:
            rect_color = (255,255,0)
        else:
            rect_color = (255,0,0)
        loop()
        screen.fill(random_screen_color)
        time.sleep(1)
        create_cubes(screen, settings, rect_color)
        cube.draw_moving_cube()
        cube.update_cube_pos()
        pygame.display.flip()

run_main()
