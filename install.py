import pygame

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
score = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
color = (100, 100, 100)
colorone = (50, 50, 50)
colore = (200, 200, 200)
coler = (105, 64, 104)
score_add = +1
player_me = 1
player_more = +1
apple = 1
"Draw"

background = (105, 64, 104)























RADIUS = 1
CENTER = (50, 50)
display_surface.fill(YELLOW)
pygame.draw.circle(display_surface, colore, CENTER, RADIUS)


loop_count = 1
my_sum = 0
while loop_count <=10:
    my_sum +=loop_count
    loop_count += 1
    print(f"The sum is {my_sum}")



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    "if press w display_surface.fill(color)"