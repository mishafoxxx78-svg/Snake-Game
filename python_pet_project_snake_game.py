# snake_game.py
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)


def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, CELL, CELL))


def draw_food(food):
    pygame.draw.rect(screen, (255, 0, 0), (*food, CELL, CELL))


def random_food():
    return [random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL)]


def game_loop():
    snake = [[100, 100]]
    direction = [CELL, 0]
    food = random_food()
    score = 0

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = [0, -CELL]
                elif event.key == pygame.K_DOWN:
                    direction = [0, CELL]
                elif event.key == pygame.K_LEFT:
                    direction = [-CELL, 0]
                elif event.key == pygame.K_RIGHT:
                    direction = [CELL, 0]

        head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

        if (
            head in snake
            or head[0] < 0
            or head[0] >= WIDTH
            or head[1] < 0
            or head[1] >= HEIGHT
        ):
            break

        snake.insert(0, head)

        if head == food:
            food = random_food()
            score += 1
        else:
            snake.pop()

        draw_snake(snake)
        draw_food(food)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    game_loop()



