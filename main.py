import time

import pygame, sys, random


random.seed(int(time.time()))
pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode(((1200, 800)))
clock = pygame.time.Clock()
player = pygame.Rect(100, 350, 10, 90)
enemy = pygame.Rect(1100, 350, 10, 90)
ball = pygame.Rect(600, 350, 30, 30)
x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
player_score, enemy_score = 0, 0
FONT = pygame.font.SysFont("Consolas", 50)
run = True
while run:
    mouse_y = pygame.mouse.get_pos()[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    player.y = mouse_y
    if player.x - ball.width <= ball.x <= player.x and ball.y in range(player.top-ball.width, player.bottom+ball.width):
        x_speed = 1
        y_speed = random.choice([1, -1])
    if enemy.x - ball.width <= ball.x <= enemy.x and ball.y in range(enemy.top-ball.width, enemy.bottom+ball.width):
        x_speed = -1
        y_speed = random.choice([1, -1])

    if ball.y <= 0:
        y_speed = 1
    if ball.y >= 800:
        y_speed = -1
    if ball.x <= 0:
        enemy_score += 1
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
        ball.center = (600, 350)
    if ball.x >= 1200:
        player_score += 1
        x_speed, y_speed = random.choice([1, -1]), random.choice([1, -1])
        ball.center = (600, 350)
    if enemy.y < ball.y:
        enemy.top += 2
    if enemy.y > ball.y:
        enemy.bottom -= 2
    player_score_font = FONT.render(str(player_score), True, "green")
    enemy_score_font = FONT.render(str(enemy_score), True, "green")
    ball.x += x_speed * 2
    ball.y += y_speed * 2
    screen.fill("black")

    pygame.draw.rect(screen, "blue", player)
    pygame.draw.rect(screen, "red", enemy)
    pygame.draw.circle(screen, "white", ball.center, 15)
    screen.blit(player_score_font, (600, 100))
    screen.blit(enemy_score_font, (550, 100))
    pygame.display.update()
    clock.tick(300)

pygame.quit()