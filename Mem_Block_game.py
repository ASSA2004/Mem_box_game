import pygame
import random
import time

# Initialize
pygame.init()

# Screen Setup
WIDTH, HEIGHT = 600, 700
GRID_SIZE = 4
BLOCK_SIZE = WIDTH // GRID_SIZE
TOP_BAR = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮PLAYBLOCK -Memory Obstacle Game")

# Fonts
FONT = pygame.font.SysFont("segoeui", 28)
BIG_FONT = pygame.font.SysFont("segoeui", 60, bold=True)

# Colors – modern tones
COLORS = {
    "bg": (30, 30, 45),
    "tile": (230, 230, 245),
    "obstacle": (239, 83, 80),
    "safe": (129, 199, 132),
    "text": (255, 255, 255),
    "shadow": (200, 200, 200),
    "bar_bg": (70, 70, 90),
    "bar_fg": (100, 200, 255),
}


def draw_text(text, font, color, center):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=center)
    screen.blit(surface, rect)


def draw_block(x, y, color, radius=12, shadow=True):
    rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE + TOP_BAR, BLOCK_SIZE, BLOCK_SIZE)
    if shadow:
        shadow_rect = rect.move(3, 3)
        pygame.draw.rect(screen, COLORS["shadow"], shadow_rect, border_radius=radius)
    pygame.draw.rect(screen, color, rect, border_radius=radius)


def generate_obstacles(level):
    count = min(4 + level, GRID_SIZE * GRID_SIZE - 1)
    all_positions = [(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE)]
    return random.sample(all_positions, count)


def draw_top_bar(level, score, remaining_time, max_time):
    pygame.draw.rect(screen, COLORS["bar_bg"], (0, 0, WIDTH, TOP_BAR))
    draw_text(f"Level: {level}", FONT, COLORS["text"], (100, 30))
    draw_text(f"Score: {score}", FONT, COLORS["text"], (WIDTH - 100, 30))

    # Draw timer bar
    time_ratio = max(0, remaining_time / max_time)
    bar_width = int(WIDTH * time_ratio)
    pygame.draw.rect(screen, COLORS["bar_fg"], (0, 70, bar_width, 15))


def draw_grid(user_selected, obstacles=[], show_obstacles=False):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pos = (x, y)
            if show_obstacles and pos in obstacles:
                draw_block(x, y, COLORS["obstacle"])
            elif pos in user_selected:
                draw_block(x, y, COLORS["safe"])
            else:
                draw_block(x, y, COLORS["tile"])


def reset_game():
    return {
        "level": 1,
        "score": 0,
        "memorize_time": 4.5,
        "obstacles": generate_obstacles(1),
        "user_selected": [],
        "phase": "memorize",
        "start_time": time.time(),
        "click_start": None,
    }


# Game loop
clock = pygame.time.Clock()
game = reset_game()
running = True

while running:
    screen.fill(COLORS["bg"])
    now = time.time()
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and game["phase"] == "click":
            mx, my = pygame.mouse.get_pos()
            if my > TOP_BAR:
                gx, gy = mx // BLOCK_SIZE, (my - TOP_BAR) // BLOCK_SIZE
                pos = (gx, gy)
                if pos not in game["user_selected"]:
                    game["user_selected"].append(pos)

                    if pos in game["obstacles"]:
                        # Game Over
                        draw_grid(game["user_selected"], game["obstacles"], True)
                        draw_top_bar(game["level"], game["score"], 0, 10)
                        draw_text("GAME OVER", BIG_FONT, COLORS["obstacle"], (WIDTH // 2, HEIGHT // 2 - 40))
                        draw_text("Click to Restart", FONT, COLORS["text"], (WIDTH // 2, HEIGHT // 2 + 30))
                        pygame.display.flip()

                        waiting = True
                        while waiting:
                            for e in pygame.event.get():
                                if e.type == pygame.QUIT:
                                    running = False
                                    waiting = False
                                elif e.type == pygame.MOUSEBUTTONDOWN:
                                    game = reset_game()
                                    waiting = False

    # GAME PHASE HANDLING
    if game["phase"] == "memorize":
        elapsed = now - game["start_time"]
        draw_grid([], game["obstacles"], show_obstacles=True)
        draw_top_bar(game["level"], game["score"], game["memorize_time"] - elapsed, game["memorize_time"])
        if elapsed >= game["memorize_time"]:
            game["phase"] = "click"
            game["click_start"] = time.time()

    elif game["phase"] == "click":
        draw_grid(game["user_selected"], game["obstacles"], show_obstacles=False)
        elapsed = now - game["click_start"]
        draw_top_bar(game["level"], game["score"], 10 - elapsed, 10)

        if elapsed >= 10:
            draw_grid(game["user_selected"], game["obstacles"], True)
            draw_top_bar(game["level"], game["score"], 0, 10)
            draw_text("TIME'S UP!", BIG_FONT, COLORS["obstacle"], (WIDTH // 2, HEIGHT // 2 - 40))
            draw_text("Click to Restart", FONT, COLORS["text"], (WIDTH // 2, HEIGHT // 2 + 30))
            pygame.display.flip()
            waiting = True
            while waiting:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        running = False
                        waiting = False
                    elif e.type == pygame.MOUSEBUTTONDOWN:
                        game = reset_game()
                        waiting = False

        elif len(game["user_selected"]) == GRID_SIZE * GRID_SIZE - len(game["obstacles"]):
            # Advance to next level
            game["level"] += 1
            game["score"] += 1
            game["memorize_time"] = max(1.5, game["memorize_time"] - 0.3)
            game["obstacles"] = generate_obstacles(game["level"])
            game["user_selected"] = []
            game["phase"] = "memorize"
            game["start_time"] = time.time()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
