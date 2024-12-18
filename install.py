import pygame

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
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









player_image = pygame.image.load("red-box-background (1).jpg")
player_rect = player_image.get_rect()
player_rect.left = 0
player_rect.centery = WINDOW_HEIGHT // 2




"player_rect.y -= PLAYER_VELOCITY"







RADIUS = 1
CENTER = (50, 50)
display_surface.fill(YELLOW)
pygame.draw.circle(display_surface, colore, CENTER, RADIUS)


loop_count = 1
my_sum = 0
while loop_count <=2:
    my_sum +=loop_count
    loop_count += 1
    print(f"The sum is {my_sum}")



running = True
while running:
    display_surface.blit(player_image, player_rect)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_0] and running:
        running = False
    if keys[pygame.K_6] and player_more:
        player_rect.x += player_more
    if keys[pygame.K_5] and player_more:
        player_rect.x -= player_more
    if keys[pygame.K_4] and player_more:
        player_rect.y -= player_more
    if keys[pygame.K_3] and player_more:
        player_rect.y += player_more
    if keys[pygame.K_1] and display_surface:
        display_surface.fill(color)
        if keys[pygame.K_2] and display_surface:
            display_surface.fill(MAGENTA)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
