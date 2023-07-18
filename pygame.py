import pygame
from pygame.locals import *

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Арканоид")

# Определение размеров и положения платформы
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 10
platform_x = (SCREEN_WIDTH - PLATFORM_WIDTH) // 2
platform_y = SCREEN_HEIGHT - 50

# Определение скорости и направления мяча
ball_radius = 10
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dx = 3
ball_dy = 3

# Определение размеров и положения кирпичей
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
brick_rows = 5
brick_cols = SCREEN_WIDTH // BRICK_WIDTH
brick_color = [BLUE, RED]
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * BRICK_WIDTH
        brick_y = 75 + row * BRICK_HEIGHT
        bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)  # Ограничение FPS до 60

    # Обработка событий
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Движение платформы влево/вправо при нажатии клавиш
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        platform_x -= 5
    if keys[K_RIGHT]:
        platform_x += 5

    # Обновление позиции мяча
    ball_x += ball_dx
    ball_y += ball_dy

    # Отскок мяча от границ экрана
    if ball_x < ball_radius or ball_x > SCREEN_WIDTH - ball_radius:
        ball_dx *= -1
    if ball_y < ball_radius:
        ball_dy *= -1

    # Отскок мяча от платформы
    if ball_y > platform_y - ball_radius and platform_x - ball_radius < ball_x < platform_x + PLATFORM_WIDTH + ball_radius:
        ball_dy *= -1

    # Проверка столкновений с кирпичами
    for brick in bricks:
        if brick.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
            ball_dy *= -1
            bricks.remove(brick)
            break

    # Очистка экрана
    screen.fill(BLACK)

    # Рисование платформы
    pygame.draw.rect(screen, WHITE, (platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT))

    # Рисование мяча
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

    # Рисование кирпичей
    for brick in bricks:
        brick_color_index = bricks.index(brick) % len(brick_color)  # Исправлено здесь
        pygame.draw.rect(screen, brick_color[brick_color_index], brick)

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
