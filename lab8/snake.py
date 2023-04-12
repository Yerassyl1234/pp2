import pygame
import random
pygame.init()
gameover=pygame.display.set_mode((200,100))
W = 600
blocksize = 25
screen = pygame.display.set_mode((W, W))
caption = pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
fps = 8
lev = 0
SCORE = 0
LEVEL = 0
running = True
level_font = pygame.font.SysFont("Verdana", 30)
score_font = pygame.font.SysFont("Verdana", 30)
# food
class Apple:
   def __init__(self):
      self.x = int(random.randint(0, W)/ blocksize) * blocksize
      self.y = int(random.randint(0, W)/ blocksize) * blocksize
      self.rect = pygame.Rect(self.x, self.y, blocksize, blocksize)
   
   def update(self):
      pygame.draw.rect(screen, 'red', self.rect)

# snake
class Snake:
   def __init__(self):
      self.x, self.y = blocksize, blocksize
      self.xdir, self.ydir = 1, 0
      self.body = [pygame.Rect(self.x, self.y, blocksize, blocksize)]
      self.head = self.body[0]
      self.dead = False
   def update(self):
      global apple
      global LEVEL
      global SCORE
      # collision
      for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, W) or self.head.y not in range(0, W):
                self.dead = True
      # restart
      if self.dead:
            self.x, self.y = blocksize, blocksize
            self.head = pygame.Rect(self.x, self.y, blocksize, blocksize)
            self.body = [pygame.Rect(self.x, self.y, blocksize, blocksize)]
            self.xdir = 1
            self.ydir = 0
            self.dead = False
            apple = Apple()
            SCORE = 0
            LEVEL = 0
      # move
      self.body.append(self.head)
      for i in range(len(self.body) - 1):
         self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
      self.head.x += self.xdir * blocksize
      self.head.y += self.ydir * blocksize 
      self.body.remove(self.head)

# setka
def drawgrid():
   for x in range(0, W, blocksize):
      for y in range(0, W, blocksize):
         rect = pygame.Rect(x, y, blocksize, blocksize)
         pygame.draw.rect(screen, (255, 255, 255), rect, 1)
      

apple = Apple()
snake = Snake()
# game loop
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_UP:
            snake.xdir, snake.ydir = 0, -1
         elif event.key == pygame.K_DOWN:
            snake.xdir, snake.ydir = 0, 1
         elif event.key == pygame.K_LEFT:
            snake.xdir, snake.ydir = -1, 0
         elif event.key == pygame.K_RIGHT:
            snake.xdir, snake.ydir = 1, 0
   
   snake.update()
   screen.fill('black')
   
   score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 255))
   screen.blit(score, (0, 0))
   level = level_font.render(f"Your level: {LEVEL}", True, (0, 0, 255))
   screen.blit(level, (W - 200, 0))
   apple.update()
   pygame.draw.rect(screen, 'green', snake.head)

   for body in snake.body:
      pygame.draw.rect(screen, 'green', body)
   # eating 
   if snake.head.x == apple.x and snake.head.y == apple.y:
      snake.body.append(pygame.Rect(body.x, body.y,blocksize, blocksize))
      apple = Apple()
      SCORE += 1
      if SCORE % 2 == 0:
         fps += 1
         LEVEL += 1
         
   
   clock.tick(fps)
   pygame.display.update()