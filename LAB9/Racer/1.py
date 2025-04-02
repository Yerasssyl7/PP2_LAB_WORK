import pygame
import random
import time
import os

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

image_background = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\PP2_LABS\LABS\LAB8\Racer\resources\AnimatedStreet.png")
image_player = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\PP2_LABS\LABS\LAB8\Racer\resources\Player.png")
image_enemy = pygame.image.load(r"C:\Users\Ерасыл\OneDrive\Desktop\PP2_LABS\LABS\LAB8\Racer\resources\Enemy.png")
image_coin = pygame.image.load(r"C:\Users\Ерасыл\Downloads\coin1.jpg")
image_coin = pygame.transform.scale(image_coin, (60, 60))

pygame.mixer.music.load(r"C:\Users\Ерасыл\OneDrive\Desktop\PP2_LABS\LABS\LAB8\Racer\resources\background.wav")
pygame.mixer.music.play(-1)

sound_crash = pygame.mixer.Sound(r"C:\Users\Ерасыл\OneDrive\Desktop\PP2_LABS\LABS\LAB8\Racer\resources\crash.wav")

font = pygame.font.SysFont("Verdana", 30)
game_over_font = pygame.font.SysFont("Verdana", 60)
image_game_over = game_over_font.render("Game Over", True, "black")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WIDTH: self.rect.right = WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 5

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = -self.rect.height

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.reset_position()
        self.speed = 5

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-150, -40)


clock = pygame.time.Clock()
FPS = 60
score = 0

player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemy_sprites = pygame.sprite.Group(enemy)
coin_sprites = pygame.sprite.Group(coin)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.move()
    enemy.move()
    coin.move()


    screen.blit(image_background, (0, 0))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        screen.fill("red")
        screen.blit(image_game_over, (100, 250))
        pygame.display.flip()
        time.sleep(2)
        running = False

    if pygame.sprite.spritecollideany(player, coin_sprites):
        score += 1
        coin.reset_position()

        if score % 10 == 0:
            FPS = int(FPS * 1.5)  # увеличение FPS каждый раз на 10 монет


    score_text = font.render(f"Coins: {score}", True, "black")
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()