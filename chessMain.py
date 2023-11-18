import pygame as pg

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
PIECES = ['bp', 'br', 'bn', 'bb', 'bq', 'bk', 'wp', 'wr', 'wn', 'wb', 'wq', 'wk']

def engine(): 
  pg.init()
  screen = pg.display.set_mode((HEIGHT, WIDTH))
  clock = pg.time.Clock()
  running = True

  while running:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False

    screen.fill("white")

    draw_board(screen)

    pg.display.flip()
    clock.tick(60)

  pg.quit()

def draw_board(screen):
  colors = [pg.Color('white'),pg.Color('grey')]
  for row in range(DIMENSION):
    for col in range(DIMENSION):
      color = colors[(row + col) % 2]
      pg.draw.rect(screen, color, pg.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE ) )