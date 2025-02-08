import pygame
import sys
import random
from math import sin, cos, radians

pygame.init()

width = 800
height = 600

display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Shooter")
clock = pygame.time.Clock()

margin = 100
lowerBound = 100
score = 0
missed_balloons = 0  
max_missed = 5  

""" Colors """
white = (230, 230, 230)
lightBlue = (174, 124, 241)
red = (231, 76, 60)
lightGreen = (25, 111, 61)
darkGray = (40, 55, 71)
darkBlue = (21, 67, 96)
green = (35, 155, 86)
yellow = (244, 208, 63)
blue = (46, 134, 193)
purple = (155, 89, 182)
orange = (243, 156, 18)

font = pygame.font.SysFont("snap ITC", 25)

class Balloon:
    def __init__(self, speed):
        self.reset(speed)

    def reset(self, speed=None):
        self.a = random.randint(30, 40)
        self.b = self.a + random.randint(0, 10)
        self.x = random.randrange(margin, width - self.a - margin)
        self.y = height - lowerBound
        self.angle = 90
        self.speed = -speed if speed else -random.choice([1, 2, 3, 4,5,6,8,9])
        self.probPool = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        self.length = random.randint(50, 100)
        self.color = random.choice([red, green, yellow, blue, darkBlue, darkGray, purple, orange, lightGreen, lightBlue, white])

    def move(self):
        direct = random.choice(self.probPool)
        self.angle += direct * 10

        # Calculating balloon movement
        rad_angle = radians(self.angle)
        self.y += self.speed * sin(rad_angle)
        self.x += self.speed * cos(rad_angle)

        # Handling balloon out-of-bounds
        if (self.x + self.a > width) or (self.x < 0):
            if self.y > height / 5:
                self.x -= self.speed * cos(rad_angle)
            else:
                self.reset()
        if self.y + self.b < 0:  # If balloon is missed (out of top boundary)
            global missed_balloons
            missed_balloons += 1  # Increase missed count
            self.reset()

    def show(self):
        # Drawing balloon and string
        pygame.draw.line(display, darkBlue, (self.x + self.a / 2, self.y + self.b), (self.x + self.a / 2, self.y + self.b + self.length))
        pygame.draw.ellipse(display, self.color, (self.x, self.y, self.a, self.b))
        pygame.draw.ellipse(display, self.color, (self.x + self.a / 2 - 5, self.y + self.b - 3, 10, 10))

    def burst(self, pos):
        global score
        if self.is_burst(pos):
            score += 1
            self.reset()

    def is_burst(self, pos):
        return self.x < pos[0] < self.x + self.a and self.y < pos[1] < self.y + self.b

balloons = [Balloon(random.choice([1, 2, 3, 4])) for _ in range(10)]

def pointer():
    pos = pygame.mouse.get_pos()
    r = 25
    l = 20
    color = lightGreen

    for balloon in balloons:
        if balloon.is_burst(pos):
            color = red
            break

    # Drawing the pointer (crosshair)
    pygame.draw.ellipse(display, color, (pos[0] - r / 2, pos[1] - r / 2, r, r), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] - l / 2), (pos[0], pos[1] - l), 4)
    pygame.draw.line(display, color, (pos[0] + l / 2, pos[1]), (pos[0] + l, pos[1]), 4)
    pygame.draw.line(display, color, (pos[0], pos[1] + l / 2), (pos[0], pos[1] + l), 4)
    pygame.draw.line(display, color, (pos[0] - l / 2, pos[1]), (pos[0] - l, pos[1]), 4)

def lowerPlatform():
    pygame.draw.rect(display, darkGray, (0, height - lowerBound, width, lowerBound))

def showScore():
    scoreText = font.render(f"Balloon Bursted: {score}", True, white)
    display.blit(scoreText, (150, height - lowerBound + 50))

def showMissedBalloons():
    missedText = font.render(f"Missed Balloons: {missed_balloons}/{max_missed}", True, white)
    display.blit(missedText, (500, height - lowerBound + 50))

def game_over():
    display.fill((0, 0, 0))
    gameOverText = font.render(f"Game Over! Final Score: {score}", True, red)
    display.blit(gameOverText, (width // 3, height // 2))
    pygame.display.update()
    pygame.time.wait(3000)
    close()

def close():
    pygame.quit()
    sys.exit()

def game():
    global score, missed_balloons
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                close()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                score = 0
                missed_balloons = 0  # Reset missed balloons
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for balloon in balloons:
                    balloon.burst(pos)

        display.fill((0, 0, 0))  # Clear the screen

        for balloon in balloons:
            balloon.move()
            balloon.show()

        pointer()
        lowerPlatform()
        showScore()
        showMissedBalloons()

        # Check if missed balloons reach the maximum allowed
        if missed_balloons >= max_missed:
            game_over()

        pygame.display.update()
        clock.tick(60)
def main():
    game()
