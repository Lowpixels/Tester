# Pygame Final Project – Collect & Survive (Enhanced Edition)
# New Features: Bigger map, more blocks, health system with damage, coin counter, visual health bar

import random

import pygame

# -------------------- CONSTANTS --------------------
WIDTH, HEIGHT = 1200, 800  # Bigger map
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 200, 50)
BLUE = (50, 100, 220)
GREY = (140, 140, 140)
YELLOW = (255, 215, 0)
DARK_RED = (139, 0, 0)

PLAYER_SIZE = 40
BLOCK_SIZE = 25
ENEMY_SIZE = 30

START_TIME = 60  # seconds
TARGET_SCORE = 50  # increased for bigger map
ENEMY_DAMAGE = 5  # damage per hit
DAMAGE_COOLDOWN = 1000  # milliseconds between damage


# -------------------- CLASSES --------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 6
        self.coins = 0
        self.health = 100
        self.last_damage_time = 0

    def update(self, keys):
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # keep on screen
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def take_damage(self, amount, current_time):
        """Apply damage with cooldown to prevent instant death"""
        if current_time - self.last_damage_time >= DAMAGE_COOLDOWN:
            self.health -= amount
            self.last_damage_time = current_time
            if self.health < 0:
                self.health = 0
            print(f"Damage taken! Health: {self.health}%")  # Debug
            return True
        return False


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(
            center=(random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))
        )


class Coin(pygame.sprite.Sprite):
    """Special yellow collectible coins"""

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(
            center=(random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))
        )


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(
            center=(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        )
        self.vx = random.choice([-speed, speed])
        self.vy = random.choice([-speed, speed])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy *= -1


def draw_health_bar(screen, x, y, width, height, health_percent):
    """Draw a visual health bar with percentage"""
    # Border
    pygame.draw.rect(screen, BLACK, (x - 2, y - 2, width + 4, height + 4), 2)

    # Background (empty health)
    pygame.draw.rect(screen, DARK_RED, (x, y, width, height))

    # Foreground (current health)
    health_width = int(width * (health_percent / 100))

    # Color changes based on health level
    if health_percent > 60:
        health_color = GREEN
    elif health_percent > 30:
        health_color = YELLOW
    else:
        health_color = RED

    pygame.draw.rect(screen, health_color, (x, y, health_width, height))


# -------------------- GAME FUNCTION --------------------
def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Collect & Survive - Enhanced Edition")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 32)
    big_font = pygame.font.SysFont(None, 64)

    # Game state
    state = "menu"  # menu, play, win, lose

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()

    # Timing
    start_ticks = 0

    # Difficulty scaling values
    block_spawn = 10  # More blocks for bigger map
    coin_spawn = 5
    enemy_speed = 3

    def reset_game():
        nonlocal start_ticks, block_spawn, enemy_speed
        all_sprites.empty()
        blocks.empty()
        coins.empty()
        enemies.empty()

        player.rect.center = (WIDTH // 2, HEIGHT // 2)
        player.coins = 0
        player.health = 100
        player.last_damage_time = 0

        all_sprites.add(player)

        # Spawn more blocks
        for _ in range(block_spawn):
            b = Block()
            blocks.add(b)
            all_sprites.add(b)

        # Spawn coins
        for _ in range(coin_spawn):
            c = Coin()
            coins.add(c)
            all_sprites.add(c)

        # Spawn enemies
        for _ in range(2):
            e = Enemy(enemy_speed)
            enemies.add(e)
            all_sprites.add(e)

        start_ticks = pygame.time.get_ticks()

    running = True
    while running:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if state == "menu" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                    state = "play"

            if state in ("win", "lose") and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    state = "menu"

        screen.fill(GREY)

        # -------------------- MENU --------------------
        if state == "menu":
            title = big_font.render("COLLECT & SURVIVE", True, BLACK)
            msg1 = font.render("Move with WASD or Arrow Keys", True, BLACK)
            msg2 = font.render("Collect green blocks and yellow coins", True, BLACK)
            msg3 = font.render(
                "Avoid red enemies - they damage your health!", True, BLACK
            )
            msg4 = font.render(
                f"Goal: Collect {TARGET_SCORE} blocks before time runs out", True, BLACK
            )
            msg5 = font.render("Press SPACE to start", True, BLACK)

            screen.blit(title, title.get_rect(center=(WIDTH // 2, 200)))
            screen.blit(msg1, msg1.get_rect(center=(WIDTH // 2, 300)))
            screen.blit(msg2, msg2.get_rect(center=(WIDTH // 2, 340)))
            screen.blit(msg3, msg3.get_rect(center=(WIDTH // 2, 380)))
            screen.blit(msg4, msg4.get_rect(center=(WIDTH // 2, 420)))
            screen.blit(msg5, msg5.get_rect(center=(WIDTH // 2, 480)))

        # -------------------- PLAY --------------------
        elif state == "play":
            keys = pygame.key.get_pressed()
            player.update(keys)
            enemies.update()

            # Collect blocks
            block_hits = pygame.sprite.spritecollide(player, blocks, True)
            if block_hits:
                player.coins += len(block_hits)

                # Difficulty scaling
                if player.coins % 10 == 0 and player.coins > 0:
                    enemy_speed += 0.5
                    e = Enemy(enemy_speed)
                    enemies.add(e)
                    all_sprites.add(e)

                # Respawn blocks
                for _ in block_hits:
                    b = Block()
                    blocks.add(b)
                    all_sprites.add(b)

            # Collect coins
            coin_hits = pygame.sprite.spritecollide(player, coins, True)
            if coin_hits:
                player.coins += len(coin_hits) * 2  # Coins worth 2 points

                # Respawn coins
                for _ in coin_hits:
                    c = Coin()
                    coins.add(c)
                    all_sprites.add(c)

            # Enemy collision - now damages instead of instant death
            enemy_hits = pygame.sprite.spritecollide(player, enemies, False)
            if enemy_hits:
                player.take_damage(ENEMY_DAMAGE, current_time)

            # Check if health depleted
            if player.health <= 0:
                state = "lose"

            # Timer
            seconds = (current_time - start_ticks) / 1000
            time_left = max(0, int(START_TIME - seconds))
            if time_left <= 0:
                state = "lose"

            # Win condition
            if player.coins >= TARGET_SCORE:
                state = "win"

            all_sprites.draw(screen)

            # HUD - Score and Timer
            hud = font.render(
                f"Score: {player.coins}/{TARGET_SCORE}   Time: {time_left}s",
                True,
                BLACK,
            )
            screen.blit(hud, (10, 10))

            # Visual Health Bar
            health_bar_x = 10
            health_bar_y = 50
            health_bar_width = 300
            health_bar_height = 30

            draw_health_bar(
                screen,
                health_bar_x,
                health_bar_y,
                health_bar_width,
                health_bar_height,
                player.health,
            )

            # Health percentage text
            health_text = font.render(f"Health: {player.health}%", True, BLACK)
            screen.blit(
                health_text, (health_bar_x + health_bar_width + 20, health_bar_y)
            )

        # -------------------- WIN / LOSE --------------------
        elif state == "win":
            msg = big_font.render("YOU WIN!", True, GREEN)
            score = font.render(f"Final Score: {player.coins}", True, BLACK)
            health_left = font.render(
                f"Health Remaining: {player.health}%", True, BLACK
            )
            sub = font.render("Press R to return to menu", True, BLACK)

            screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))
            screen.blit(score, score.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            screen.blit(
                health_left, health_left.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
            )
            screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80)))

        elif state == "lose":
            msg = big_font.render("GAME OVER", True, RED)
            score = font.render(
                f"Final Score: {player.coins}/{TARGET_SCORE}", True, BLACK
            )

            if player.health <= 0:
                reason = font.render("You ran out of health!", True, BLACK)
            else:
                reason = font.render("You ran out of time!", True, BLACK)

            sub = font.render("Press R to return to menu", True, BLACK)

            screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60)))
            screen.blit(score, score.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
            screen.blit(reason, reason.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40)))
            screen.blit(sub, sub.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80)))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    game()
