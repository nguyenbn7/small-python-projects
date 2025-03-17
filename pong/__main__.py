import pygame

from __init__ import PADDLE_SPEED, WINDOW_HEIGHT, WINDOW_WIDTH
from classes import Paddle


pygame.init()
pygame.display.set_caption("Pong")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Fonts
small_font = pygame.font.Font("pong/font.ttf", 8)
large_font = pygame.font.Font("pong/font.ttf", 16)
score_font = pygame.font.Font("pong/font.ttf", 70)

# Sounds
sounds = {
    "paddle hit": pygame.mixer.Sound("pong/sounds/paddle_hit.wav"),
    "score": pygame.mixer.Sound("pong/sounds/score.wav"),
    "wall hit": pygame.mixer.Sound("pong/sounds/wall_hit.wav"),
}

# objects
player1 = Paddle(5, WINDOW_HEIGHT / 2, 15, 60)
player1_score = 0

player2 = Paddle(WINDOW_WIDTH - 20, WINDOW_HEIGHT / 2, 15, 60)
player2_score = 0

running = True
dt = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((40, 45, 52, 255))

    screen.blit(
        score_font.render(f"{player1_score}", False, (255, 255, 255)),
        (WINDOW_WIDTH / 2 - 130, WINDOW_HEIGHT / 3),
    )

    screen.blit(
        score_font.render(f"{player2_score}", False, (255, 255, 255)),
        (WINDOW_WIDTH / 2 + 130, WINDOW_HEIGHT / 3),
    )

    player1.render(screen)
    player2.render(screen)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player1.dy = -PADDLE_SPEED
    elif keys[pygame.K_s]:
        player1.dy = PADDLE_SPEED
    else:
        player1.dy = 0

    if keys[pygame.K_UP]:
        player2.dy = -PADDLE_SPEED
    elif keys[pygame.K_DOWN]:
        player2.dy = PADDLE_SPEED
    else:
        player2.dy = 0

    player1.update(dt)
    player2.update(dt)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
