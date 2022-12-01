import pygame
import sys
import win
 

pygame.init()

# Sound
pygame.mixer.music.load('Sound_08421.mp3')

# Screen
margin = 5
size_block = 110
width = heigth = size_block * 4 + margin * 5

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("ИГРА - Крестики нолики")

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

mas = [[0] * 4 for i in range(4)]
k = 0
game_over = False
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit(0)
      elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
         x_mouse, y_mouse = pygame.mouse.get_pos()
         col = x_mouse // (size_block + margin)
         row = y_mouse // (size_block + margin)
         if mas[row][col] == 0:
            if k % 2 == 0:
               mas[row][col] = 'x'
            else:
               mas[row][col] = 'o'
            k += 1
      elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
         game_over = False
         mas = [[0] * 4 for i in range(4)]
         k = 0
         screen.fill(black)
         
   if not game_over:        
      for row in range(4):
         for col in range(4):
            if mas[row][col] == 'x':
               color = red
            elif mas[row][col] == 'o':
               color = blue
            else:
               color = white            
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            if color == red:
               pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
               pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 5)
            elif color == blue:
               pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2, 5)
   if (k - 1) % 2 == 0:
      game_over = win.check_win(mas, 'x')
   else:
      game_over = win.check_win(mas, 'o')
      
      
   if game_over:
      pygame.mixer.music.play()
      pygame.time.delay(5)
      screen.fill(black)
      font = pygame.font.SysFont('arial', 80)
      text1 = font.render(game_over, True, white)
      text_rect = text1.get_rect()
      text_x = screen.get_width() / 2 - text_rect.width / 2
      text_y = screen.get_width() / 2 - text_rect.width / 2
      screen.blit(text1, [text_x, text_y])
   pygame.display.update()
   
         



