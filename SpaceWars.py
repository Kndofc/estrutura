#!/usr/bin/env python3
import turtle
import math
import random
import pygame

pygame.init()

laser_sound = pygame.mixer.Sound("laser.wav")
explosion_sound = pygame.mixer.Sound("explosion.wav")
gameover_sound = pygame.mixer.Sound("gameover.wav")

# ===============================================
# Configurações iniciais da tela
# ===============================================
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("8-bit SpaceWarS")
screen.bgpic("dp.gif")

# Registra as imagens dos sprites
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("missile.gif")

# ===============================================
# Criação do jogador
# ===============================================
player = turtle.Turtle()
player.color("blue")
player.speed(0)
player.shape("player.gif")
player.setheading(90)
player.penup()
player.goto(0, -250)

playerspeed = 20

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -340:
        x = -340
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 340:
        x = 340
    player.setx(x)

# ===============================================
# Criação dos inimigos
# ===============================================
enemies = []
for i in range(7):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.speed(0)
    enemy.turtlesize(1.2, 1.2)
    enemy.shape("enemy.gif")
    enemy.penup()
    enemy.setheading(90)
    x = random.randint(-300, 300)
    y = random.randint(180, 260)
    enemy.goto(x, y)

enemyspeed = 1.8

# ===============================================
# Criação do projétil
# ===============================================
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.speed(0)
bullet.shape("missile.gif")
bullet.turtlesize(0.5, 0.5)
bullet.penup()
bullet.hideturtle()
bullet.setheading(90)
bullet.goto(0, -240)

bulletspeed = 22
bulletstate = "Ready"

def firebullet():
    global bulletstate
    if bulletstate == "Ready":
        bulletstate = "Fire"
        # Toca som de tiro
        laser_sound.play()

        x = player.xcor()
        y = player.ycor() + 20
        bullet.goto(x, y)
        bullet.showturtle()

# ===============================================
# Sistema de pontuação
# ===============================================
Score = 0
scorepen = turtle.Turtle()
scorepen.pencolor("white")
scorepen.speed(0)
scorepen.up()
scorepen.setposition(-355, 280)
scorestring = f"Score: {Score}"
scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
scorepen.hideturtle()

# ===============================================
# Funções de colisão
# ===============================================
def collisionplay(a, b):
    distance = math.sqrt((a.xcor() - b.xcor()) ** 2 + (a.ycor() - b.ycor()) ** 2)
    if distance < 25:
        return True
    return False

def collision(a, b):
    distance = math.sqrt((a.xcor() - b.xcor()) ** 2 + (a.ycor() - b.ycor()) ** 2)
    if distance < 20:
        return True
    return False

# ===============================================
# Keybindings
# ===============================================
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(firebullet, "space")

# ===============================================
# Loop principal do jogo
# ===============================================
while True:
    print(enemy.ycor())

    for enemy in enemies:
        # Movimento do inimigo
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Checa se bateu na borda direita
        if enemy.xcor() > 325:
            for j in enemies:
                y = j.ycor()
                y -= 25
                j.sety(y)
            enemyspeed *= -1

        # Checa se bateu na borda esquerda
        if enemy.xcor() < -325:
            for j in enemies:
                y = j.ycor()
                y -= 25
                j.sety(y)
            enemyspeed *= -1

        # Colisão projétil-inimigo
        if collisionplay(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "Ready"
            # Som de explosão
            explosion_sound.play()
            bullet.setposition(0, -400)

            # Respawna o inimigo
            x = random.randint(-300, 300)
            y = random.randint(180, 280)
            enemy.setposition(x, y)

            # Atualiza pontuação
            Score += 10
            scorestring = f"Score: {Score}"
            scorepen.clear()
            scorepen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        # Colisão jogador-inimigo
        if collision(player, enemy):
            for e in enemies:
                e.hideturtle()
            player.hideturtle()
            # Som de game over
            gameover_sound.play()
            print("GAME OVER")
            break

        # Se o inimigo descer muito (y < -200), game over também
        if enemy.ycor() < -200:
            for j in enemies:
                j.hideturtle()
            player.hideturtle()
            print("GAME OVER")
            gameover_sound.play()
            break

    # Movimento do projétil
    if bulletstate == "Fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

        # Se atingir certa altura, considera que saiu da tela
        if bullet.ycor() > 300:
            bullet.hideturtle()
            bulletstate = "Ready"

    # Essa checagem faz o projétil ficar "Ready" ao passar de y=150
    # (mas você colocou outra checagem aos 300 px também)
    if bullet.ycor() > 150:
        bulletstate = "Ready"

delay = input()
