import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Grid dimensions
GRID_SIZE = 4
BLOCK_SIZE = WIDTH // GRID_SIZE

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Obstacle Game")

# Fonts
font = pygame.font.Font(None, 36)
def render_text(text, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

# Game variables
score = 0
level = 1
obstacle_blocks = []
user_selected = []
time_to_memorize = 3

def generate_obstacles():
    num_obstacles = max(1, GRID_SIZE * GRID_SIZE - level * 2)
    obstacles = random.sample([(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE)], num_obstacles)
    return obstacles

def draw_grid():
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if (x, y) in user_selected:
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

# Main loop variables
running = True
memorization_phase = True
start_time = None
obstacle_blocks = generate_obstacles()

while running:
    screen.fill(BLACK)
    draw_grid()

    if memorization_phase:
        for x, y in obstacle_blocks:
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, RED, rect)
        if start_time is None:
            start_time = time.time()
        elif time.time() - start_time > time_to_memorize:
            memorization_phase = False
            user_selected = []
    else:
        render_text(f"Level: {level} | Score: {score}", BLUE, 10, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                level = 1
                score = 0
                obstacle_blocks = generate_obstacles()
                memorization_phase = True
                start_time = None
            elif event.key == pygame.K_r:
                level = 1
                score = 0
                obstacle_blocks = generate_obstacles()
                memorization_phase = True
                start_time = None
            elif event.key == pygame.K_e:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not memorization_phase:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x, grid_y = mouse_x // BLOCK_SIZE, mouse_y // BLOCK_SIZE
            if (grid_x, grid_y) not in user_selected:
                user_selected.append((grid_x, grid_y))
                if (grid_x, grid_y) in obstacle_blocks:
                    render_text("Game Over!", RED, WIDTH // 2 - 100, HEIGHT // 2)
                    pygame.display.flip()
                    time.sleep(2)
                    level = 1
                    score = 0
                    obstacle_blocks = generate_obstacles()
                    memorization_phase = True
                    start_time = None
                elif len(user_selected) == GRID_SIZE * GRID_SIZE - len(obstacle_blocks):
                    score += 1
                    level += 1
                    obstacle_blocks = generate_obstacles()
                    memorization_phase = True
                    start_time = None

    pygame.display.flip()

pygame.quit()
