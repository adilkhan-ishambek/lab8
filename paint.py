import pygame

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

game_over = False

prev, cur = None, None
screen.fill(WHITE)

mode= 'pen'
while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if mode=='pen':  
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if prev:
            pygame.draw.line(screen, RED, prev, cur, 1)
            prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    if mode=='rectangle':
         if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
         if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
         if prev:
             pygame.draw.rect(screen,RED,(min(prev[0],cur[0]),min(prev[1],cur[1]),abs(prev[0]-cur[0]),abs(prev[1]-cur[1])),3)
             screen.blit(screen,(0,0))
         if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    if mode=='eraser':
         if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
         if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
         if prev:
             pygame.draw.line(screen,WHITE,prev,cur,1)
         if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    if mode=='circle':
         if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
         if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
         if prev:
              pygame.draw.polygon(screen,RED,(min(prev[0],cur[0]),min(prev[1],cur[1]),abs(prev[0]-cur[0]),abs(prev[1]-cur[1])))
         if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
          mode='rectangle'
      if event.key==pygame.K_LEFT:
          mode='eraser'
      if event.key==pygame.K_UP:
          mode='circle'
    if mode=='circle':
         if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
         if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
         if prev:
              pygame.draw.ellipse(screen,RED,(min(prev[0],cur[0]),min(prev[1],cur[1]),abs(prev[0]-cur[0])))
         if event.type == pygame.MOUSEBUTTONUP:
            prev = None


  pygame.display.flip()

  clock.tick(30)


pygame.quit()