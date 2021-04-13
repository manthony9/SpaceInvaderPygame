import pygame
import random
import math
#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

running = True

#background
background = pygame.image.load('space-bg.jpg')


#game title and icon
pygame.display.set_caption("Space Attack")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#player
pImage = pygame.image.load('spaceship.png')
playerX = 370
playerY = 470
playerX_chg = 0


#enemy
eImage = []
enemyX = []
enemyY = []
enemyXChange = []
enemyYChange = []
countEnemy = 5

for i in range(countEnemy):
    eImage.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyXChange.append(0.3)
    enemyYChange.append(25)

#bullet
bImage = pygame.image.load('bomb.png')
bullX = 0
bullY = 470
bullXChange = 0
bullYChange = 1.0
bullet_state = "ready"


#score
scoreval = 0
font = pygame.font.Font('freesansbold.ttf',32)


textX = 10
textY = 10

def dspScore(x,y):
    score = font.render("Score:" + str(scoreval),True,(255,255,255))
    screen.blit(score, (x, y))
def player(x,y):
    screen.blit(pImage, (x,y))

score = 0
def player(x,y):
    screen.blit(pImage,(x, y))

def enemy(x,y,i):
    screen.blit(eImage[i],(x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bImage,(x+15,y+10))

def collision(enmX, enmY, btX, btY):
    distance = math.sqrt(math.pow(enmX-btX,2)+ math.pow(enmY - btY,2))

    if distance < 27:
        return True
    else:
        return False


#Window loop
while running:

    screen.fill((112, 112, 112))
    #bg image
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_chg = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_chg = +0.2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullX = playerX
                    fire_bullet(bullX,bullY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_chg = 0

    playerX += playerX_chg

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #ufo movement
    for i in range(countEnemy):
        enemyX[i] += enemyXChange[i]
        if enemyX[i] <= 0:
            enemyXChange[i] = 0.3;
            enemyY[i] += enemyYChange[i]
        elif enemyX[i] >= 736:
            enemyXChange[i] = -0.3;
            enemyY[i] += enemyYChange[i]
        # collision
        coll = collision(enemyX[i], enemyY[i], bullX, bullY)
        if coll:
            bullY = 480
            bullet_state = "ready"
            scoreval += 1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i],i)

     #bullet movement
    if bullY <= 0 :
        bullY = 480
        bullet_state = "ready"


    if bullet_state == "fire":
        fire_bullet (bullX,bullY)
        bullY -= bullYChange






    player(playerX,playerY)
    dspScore(textX,textY)
    pygame.display.update()