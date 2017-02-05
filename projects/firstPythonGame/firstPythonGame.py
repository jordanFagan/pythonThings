import pygame
import time
import random
pygame.init()
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
grey = (100, 100, 100)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A Little Racey')
clock = pygame.time.Clock()

line_img = pygame.image.load('White_Line.png')
lineHeight = 300

carImg = pygame.image.load('racecar.png')
car_width = 73
car_height = 82
carRect = 0
obRect = 0

badImg = pygame.image.load('obstacle.png')
noOfBadGuys = 5

bulletImg = pygame.image.load('bullet.png')

powerupImg0 = pygame.image.load('powerup0.png')
powerupImg1 = pygame.image.load('powerup1.png')
powerupImg2 = pygame.image.load('powerup2.png')
powerupImg3 = pygame.image.load('powerup3.png')
powerupImg4 = pygame.image.load('powerup4.png')

currentHighscore = 0

def car(x, y):
  gameDisplay.blit(carImg, (x, y))
  return pygame.Rect(x + 6, y + 6, car_width - 12, car_height - 12)
  
def bullet(x, y):
  gameDisplay.blit(bulletImg, (x, y))
  return pygame.Rect(x, y, 3, 5)
  
def powerup(x, y, powerUpType):
  # 0 - speed up, 1 - slow down, 2 - add 10 points, 3 - remove 20 points, 4 add random(5-20) bullets
  if powerUpType == 0:
    powerupImg = powerupImg0
  elif powerUpType == 1:
    powerupImg = powerupImg1
  elif powerUpType == 2:
    powerupImg = powerupImg2
  elif powerUpType == 3:
    powerupImg = powerupImg3
  elif powerUpType == 4:
    powerupImg = powerupImg4
  gameDisplay.blit(powerupImg, (x, y))
  return pygame.Rect(x, y, 50, 50)

def obstacle(x, y):
  gameDisplay.blit(badImg, (x, y))
  return pygame.Rect(x, y, car_width, car_height)
    
def line(y):
  line2Y = y + lineHeight
  line3Y = line2Y + lineHeight
  line4Y = line3Y + lineHeight
  x = display_width * 0.5 - 6
  gameDisplay.blit(line_img, (x, y))
  gameDisplay.blit(line_img, (x, line2Y))
  gameDisplay.blit(line_img, (x, line3Y))
  gameDisplay.blit(line_img, (x, line4Y))
  x = display_width * 0.25 - 6
  gameDisplay.blit(line_img, (x, y))
  gameDisplay.blit(line_img, (x, line2Y))
  gameDisplay.blit(line_img, (x, line3Y))
  gameDisplay.blit(line_img, (x, line4Y))
  x = display_width * 0.75 - 6
  gameDisplay.blit(line_img, (x, y))
  gameDisplay.blit(line_img, (x, line2Y))
  gameDisplay.blit(line_img, (x, line3Y))
  gameDisplay.blit(line_img, (x, line4Y))

def text_objects(text, font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect()

def endGame(carsPassed):
  largeText = pygame.font.Font('freesansbold.ttf', 115)
  TextSurf, TextRect = text_objects("You crashed!", largeText)
  TextRect.center = ((display_width / 2), (display_height / 2 - 120))
  gameDisplay.blit(TextSurf, TextRect)
  smallerText = pygame.font.Font('freesansbold.ttf', 70)
  TextSurf, TextRect = text_objects( "You passed " + str(carsPassed) + " cars.", smallerText)
  TextRect.center = ((display_width / 2), (display_height / 2))
  gameDisplay.blit(TextSurf, TextRect)
  pygame.display.update()

def score(cars):
  smallText = pygame.font.Font('freesansbold.ttf', 16)
  TextSurf, TextRect = text_objects("Cars Passed: " + str(cars), smallText)
  TextRect.x = 5
  TextRect.y = 5
  gameDisplay.blit(TextSurf, TextRect)
  
def presentScore(score):
  smallText = pygame.font.Font('freesansbold.ttf', 16)
  TextSurf, TextRect = text_objects("Current Score: " + str(score), smallText)
  TextRect.x = 5
  TextRect.y = 20
  gameDisplay.blit(TextSurf, TextRect)
  
def highscore(highestScore):
  smallText = pygame.font.Font('freesansbold.ttf', 16)
  TextSurf, TextRect = text_objects("Highscore: " + str(highestScore), smallText)
  TextRect.x = 5
  TextRect.y = 35
  gameDisplay.blit(TextSurf, TextRect)
  
def speedo(speed):
  smallText = pygame.font.Font('freesansbold.ttf', 16)
  TextSurf, TextRect = text_objects("Speed: " + str(speed * 5) + "mph", smallText)
  TextRect.x = display_width - TextRect.width - 5
  TextRect.y = 5
  gameDisplay.blit(TextSurf, TextRect)

def showBullets(bullets):
  smallText = pygame.font.Font('freesansbold.ttf', 16)
  TextSurf, TextRect = text_objects("Bullets: " + str(bullets), smallText)
  TextRect.x = display_width - TextRect.width - 5
  TextRect.y = 20
  gameDisplay.blit(TextSurf, TextRect)

def checkUnsafe(obRect, otherBadGuys):
  unsafe = False;
  for i in otherBadGuys:
    badGuyRect = pygame.Rect(i[0], i[1], car_width, car_height)
    if detectCrash(obRect, badGuyRect):
      unsafe = True
  return unsafe

def detectCrash(carRect, obRect):
  return carRect.x > display_width - car_width or carRect.x < 0 or carRect.colliderect(obRect)
   
def game_loop(currentHighscore):
  
  x = (display_width * 0.45)
  y = (display_height * 0.8)
  x_change = 0
  y_change = 0
  speed = 4
  carsPassed = 0
  currentScore = 0
  poRect = powerup(16, display_height, 0)
  powerUpType = 0  
  bullets = 10
  bulletsArray = list()

  badGuys = [(x, y)]*noOfBadGuys
  for i in range(noOfBadGuys):
    badGuys[i] = (random.randint(0, display_width - car_width), random.randint(0 - display_height, 0))
  
  lineY = 0 - lineHeight

  gameExit = False

  while not gameExit:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x_change = 0 - 5
        elif event.key == pygame.K_RIGHT:
          x_change = 5
        elif event.key == pygame.K_UP:
          y_change = -5
        elif event.key == pygame.K_DOWN:
          y_change = 5
          
          
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          x_change = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
          y_change = 0
        elif event.key == pygame.K_SPACE:
          if bullets > 0:
            bullets += -1
            bulletsArray.append([x - 1 + car_width / 2, y])

    x += x_change
    if y + y_change > display_height / 2 and y + y_change < display_height - car_height - 12:
      y += y_change

    if lineY < 0 - speed:
      lineY += speed
    else:
      lineY = 0 - lineHeight

    for i in range(noOfBadGuys):
      if badGuys[i][1] < display_height:
        badGuys[i] = (badGuys[i][0], badGuys[i][1] + speed / 2)
      else:
        badGuys[i] = (random.randint(0, display_width - car_width), random.randint(0 - 600, 0 - car_height))
        obRect = obstacle(badGuys[i][0], badGuys[i][1])
        otherBadGuys = list(badGuys)
        otherBadGuys.remove(otherBadGuys[i])
        unsafe = checkUnsafe(obRect, otherBadGuys)
		
        while unsafe:
          badGuys[i] = (random.randint(0, display_width - car_width), random.randint(0 - 600, 0 - car_height))
          obRect = obstacle(badGuys[i][0], badGuys[i][1])
          unsafe = checkUnsafe(obRect, otherBadGuys)
    
        carsPassed += 1
        currentScore += 1
        if carsPassed % 4 == 0:
          speed += 1
        if carsPassed % 16 == 0:
          powerUpType = random.randint(0,4)
          poRect = powerup(random.randint(0, display_width - 50), -50, powerUpType)
    for i in range(len(bulletsArray) ):
      bulletsArray[i] = [bulletsArray[i][0], bulletsArray[i][1] - speed]
    
    gameDisplay.fill(grey)
    line(lineY)
    poRect = powerup(poRect.x, poRect.y + speed / 4, powerUpType)
    carRect = car(x, y)
    if detectCrash(carRect, poRect):
      poRect = powerup(16, display_height, powerUpType)

      # 0 - speed up, 1 - slow down, 2 - add 10 points, 3 - remove 20 points, 4 add random(5-20) bullets
      if powerUpType == 0:
        speed += 2      
      elif powerUpType == 1:
        speed += -2      
      elif powerUpType == 2:
        currentScore += 10      
      elif powerUpType == 3:
        currentScore += -20      
      elif powerUpType == 4:
        bullets += random.randint(5,20)
      
    for i in range(noOfBadGuys):
      if currentScore > currentHighscore:
        currentHighscore = currentScore
      obRect = obstacle(badGuys[i][0], badGuys[i][1])
      score(carsPassed)
      highscore(currentHighscore)
      presentScore(currentScore)
      speedo(speed)
      showBullets(bullets)
      for shot in bulletsArray:
        bulletRect = bullet(shot[0], shot[1])
        if detectCrash(bulletRect, obRect):
          bulletsArray.remove(shot)
          badGuys[i] = (random.randint(0, display_width - car_width), random.randint(0 - 600, 0 - car_height))
          obRect = obstacle(badGuys[i][0], badGuys[i][1])
          currentScore += 2
      if detectCrash(carRect, obRect):
        endGame(carsPassed)
        time.sleep(2)
        game_loop(currentHighscore)
      
      
    pygame.display.update()
    clock.tick(60)

game_loop(currentHighscore)
pygame.quit()
quit()
