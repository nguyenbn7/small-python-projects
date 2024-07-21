import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
PADDLE_SPEED = 200


class Ball:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # these variables are for keeping track of our velocity on both the
        # X and Y axis, since the ball can move in two dimensions
        self.dy = 0
        self.dy = 0

    def collides(self, paddle):
        # first, check to see if the left edge of either is farther to the right
        # than the right edge of the other
        if self.x > paddle.x + paddle.width or paddle.x > self.x + self.width:
            return False

        # then check to see if the bottom edge of either is higher than the top
        # edge of the other
        if self.y > paddle.y + paddle.height or paddle.y > self.y + self.height:
            return False

        return True

    def reset(self):
        self.x = WINDOW_WIDTH / 2 - 2
        self.y = WINDOW_HEIGHT / 2 - 2
        self.dx = 0
        self.dy = 0


class Paddle:

    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = 0

    def update(self, dt: float):
        self.y = (
            max(0, self.y + self.dy * dt)
            if self.y < 0
            else min(WINDOW_HEIGHT - self.height, self.y + self.dy * dt)
        )

    def render(self, screen: pygame.surface.Surface):
        pygame.draw.rect(
            screen, "white", pygame.Rect(self.x, self.y, self.width, self.height)
        )


pygame.init()
pygame.display.set_caption("Pong")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Fonts
small_font = pygame.font.Font("font.ttf", 8)
large_font = pygame.font.Font("font.ttf", 16)
score_font = pygame.font.Font("font.ttf", 70)

# Sounds
sounds = {
    "paddle hit": pygame.mixer.Sound("sounds/paddle_hit.wav"),
    "score": pygame.mixer.Sound("sounds/score.wav"),
    "wall hit": pygame.mixer.Sound("sounds/wall_hit.wav"),
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
