import pygame
import random
import time

pygame.init()

app = pygame.display.set_mode((500, 500))

joystick1 = pygame.joystick.get_count()
if joystick1 == 0:
    print("Sorry, Game has found that no joystick is attached.")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

#Windowed Title
pygame.display.set_caption("Driving Sim")

#Images
bg = pygame.image.load(
    '/Users/kev/Desktop/Driving Sim/road.png')
blue_car = pygame.image.load(
    '/Users/kev/Desktop/Driving Sim/blue.png')
red_car = pygame.image.load(
    '/Users/kev/Desktop/Driving Sim/red.png')
yellow_car = pygame.image.load(
    '/Users/kev/Desktop/Driving Sim/yellow.png')
white_car = pygame.image.load(
    '/Users/kev/Desktop/Driving Sim/white.png')
strip = pygame.image.load(
    '/Users/kev/Desktop/Driving Sim/strip.png')
boom = pygame.image.load(
    '/Users/kev/Desktop/Driving Sim/boom.png')
tree = pygame.image.load(
    '/Users/kev/Desktop/Driving Sim/tree.png')

#Sampled Music
music = pygame.mixer.music.load(
    '/Users/kev/Desktop/Driving Sim/music.mp3')
pygame.mixer.music.play(-1)

#Crash Sound
crash = pygame.mixer.Sound(
    '/Users/kev/Desktop/Driving Sim/crash.wav')

#Main Car
x = 160
y = 400
speed = 5
score = 0
car_speed = 0

#Oncoming Cars
a1 = 0
b1 = 350
c1 = 175
a = random.randint(370, 375)
b = random.randint(370, 375)
c = random.randint(370, 375)

#Road
d = 250
d1 = 0
d2 = 100
d3 = 200
d4 = 300
d5 = 400

#Tree
t = 25
tr = 450
t1 = 0
t2 = 100
t3 = 250
t4 = 350


def images():

  app.blit(bg, (0, 0))


  app.blit(strip, (d, d1))
  app.blit(strip, (d, d2))
  app.blit(strip, (d, d3))
  app.blit(strip, (d, d4))
  app.blit(strip, (d, d5))

  app.blit(tree, (t, t1))
  app.blit(tree, (tr, t2))
  app.blit(tree, (t, t3))
  app.blit(tree, (tr, t4))

  app.blit(red_car, (x, y))
  app.blit(yellow_car, (a, a1))
  app.blit(blue_car, (c, c1))
  app.blit(white_car, (b, b1))

#Score
  font = pygame.font.Font(None, 50)
  text = font.render("Score: "+str(score), 1, (255, 255, 255))
  app.blit(text, (75, 10))

  pygame.display.update()
#-------------------------------------------------------

#Crash
def accident(x, y):
  crash.play()
  app.blit(boom, (x, y))
  pygame.display.update()
  pygame.time.delay(500)

#Game Over Screen

def game_over_screen():
  app.blit(bg, (0, 0))
  font = pygame.font.Font(None, 75)
  text = font.render("Game Over", 1, (255, 255, 255))
  app.blit(text, (100, 100))

  font = pygame.font.Font(None, 50)
  text = font.render("Your score: "+str(score), 1, (255, 255, 255))
  app.blit(text, (140, 250))

  text = font.render("Press A key to Restart", 1, (255, 255, 255))
  app.blit(text, (70, 375))

  pygame.display.update()

  waiting = True
  while waiting:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 0:
                        pygame.quit()

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    waiting = False
              

#Game Start Screen
def game_Start_screen():
  app.blit(bg, (0, 0))
  font = pygame.font.Font(None, 40)
  text = font.render("Welcome to Driving Sim", 1, (255, 255, 255))
  app.blit(text, (90, 100))

  text = font.render("Press A to Start", 1, (255, 255, 255))
  app.blit(text, (90, 350))
  
  text = font.render("Press B to Quit", 1, (255, 255, 255))
  app.blit(text, (90, 400))

  pygame.display.update()

#Waiting for Input (loop)
  waiting1 = True
  while waiting1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    pygame.quit()

            
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 1:
                    waiting1 = False
              

runtime = True
game_over = False
start_game = True
while runtime:
  print (time.perf_counter())

#Start Logic
  if start_game:
    game_Start_screen()
    start_game = False

#Game Over Logic
  if game_over:
    game_over_screen()
    game_over = False
    a1 = 0
    b1 = 350
    c1 = 175
    a = random.randint(370, 375)
    b = random.randint(370, 375)
    c = random.randint(370, 375)
    x = 160
    y = 400
    score = 1
    speed = 3

#Safe Exit
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        runtime = False
    elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    runtime = False

#Movement
  keys_pressed = pygame.key.get_pressed()

#Right
  if keys_pressed[pygame.K_RIGHT]:
    if x < 375:
      x = x + speed

#Left
  if keys_pressed[pygame.K_LEFT]:
    if x > 70:
      x = x - speed

#Down
  if keys_pressed[pygame.K_DOWN]:
    if y < 400:
      y = y + speed

#Up
  if keys_pressed[pygame.K_UP]:
    if y > 0:
      y = y - speed

#If the axis isn't a whole number it will return either 1 or 0
  if joystick != 0:
    horiz_axis_pos = joystick.get_axis(0)
    vert_axis_pos = joystick.get_axis(1)

# Multiplying x according to axis and multiplying by speed for movement
    qw = int(horiz_axis_pos * speed)
    er = int(vert_axis_pos * speed)
    if qw < 0:
      if x >= 70:
        x = x + qw
    else:
      if x <= 375:
        x = x + qw

    if er < 0:
      if y >= 0:
        y = y + er
    else:
     if y <= 400:
      y = y + er

#Random Cars
  if a1 >= 500:
    a1 = 0
    a = random.randint(70, 170) #Random spawns
    score = score+1

#Movement acceleration based on joystick input
    if score % 10 == 0:
      speed = speed+1

    if score % 20 == 0:
      car_speed = car_speed+1

  if c1 >= 500:
    c1 = 0
    c = random.randint(180, 270)
    score = score+1

#Movement acceleration based on joystick input
    if score % 10 == 0:
      speed = speed+1

    if score % 20 == 0:
      car_speed = car_speed+1

  if b1 >= 500:
    b1 = 0
    b = random.randint(280, 375)
    score = score+1

#Movement acceleration based on joystick input
    if score % 10 == 0:
      speed = speed+1

    if score % 20 == 0:
      car_speed = car_speed+1

#Continuing road after image leaves screen
  if d1 >= 500:
    d1 = 0
  if d2 >= 500:
    d2 = 0
  if d3 >= 500:
    d3 = 0
  if d4 >= 500:
    d4 = 0
  if d5 >= 500:
    d5 = 0

#Reloading trees
  if t1 >= 500:
    t1 = 0
  if t2 >= 500:
    t2 = 0
  if t3 >= 500:
    t3 = 0
  if t4 >= 500:
    t4 = 0
    
#Matching background with car speed
  a1 = a1+speed+car_speed
  c1 = c1+speed+car_speed
  b1 = b1+speed+car_speed
  d1 = d1+speed
  d2 = d2+speed
  d3 = d3+speed
  d4 = d4+speed
  d5 = d5+speed
  t1 = t1+speed
  t2 = t2+speed
  t3 = t3+speed
  t4 = t4+speed

#Car hitboxes
  for k in (x, x+50):
    for l in (y, y+100):

      for i in range(a1, a1+100):
        for j in range(a, a+45):
          #Oncoming car hitboxes
          if k == j and l == i:
            accident(x, y)
            game_over = True

      for i in range(b1, b1+100):
        for j in range(b, b+45):
          if k == j and l == i:
            accident(x, y)
            game_over = True

      for i in range(c1, c1+100):
        for j in range(c, c+45):
          if k == j and l == i:
            accident(x, y)
            game_over = True

  images()