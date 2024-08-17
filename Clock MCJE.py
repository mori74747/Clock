from mcje.minecraft import Minecraft
import param_MCJE as param
import time
import datetime


from seven_seg_pg import Seven_seg
from lcd_font_pg import LCD_font


mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('This is a clock made with LCDfont and transferred to mincraft world')

mc.setBlock(5, 70, 5,  param.GOLD_BLOCK)

LCD_0 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 1, 1,
         1, 0, 1, 0, 1,
         1, 1, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0)

LCD_1 = (0, 0, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 0, 1, 0, 0,
         0, 1, 1, 1, 0)

LCD_2 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         1, 1, 1, 1, 1)

LCD_3 = (1, 1, 1, 1, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 0, 0, 1, 0,
         0, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1 ,1, 0,)

LCD_4 = (0, 0, 0, 1, 0,
         0, 0, 1, 1, 0,
         0, 1, 0, 1, 0,
         1, 0, 0, 1, 0,
         1, 1, 1, 1, 1,
         0, 0, 0, 1, 0,
         0, 0, 0, 1, 0,)

LCD_5 = (1, 1, 1, 1, 1,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         0, 0, 0, 0, 1,
         0, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,)

lCD_6 = (0, 0, 1, 1, 0,
         0, 1, 0, 0, 0,
         1, 0, 0, 0, 0,
         1, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,)

LCD_7 = (1, 1, 1, 1, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 0, 1, 0, 0,
         0, 1, 0, 0, 0,
         0, 1, 0, 0, 0,
         0, 1, 0, 0, 0,)

LCD_8 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 0,)

LCD_9 = (0, 1, 1, 1, 0,
         1, 0, 0, 0, 1,
         1, 0, 0, 0, 1,
         0, 1, 1, 1, 1,
         0, 0, 0, 0, 1,
         0, 0, 0, 1, 0,
         0, 1, 1, 0, 0,)

LCD_10 = (0, 0, 0, 0, 0,
         0, 1, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 0, 0, 0,
         0, 1, 1, 0, 0,
         0, 1, 1, 0, 0,
         0, 0, 0, 0, 0,)

LCD_11 = (0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         1, 1, 1, 1, 1,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,
         0, 0, 0, 0, 0,)


LCD_font_styles = (LCD_0, LCD_1, LCD_2, LCD_3, LCD_4, LCD_5, lCD_6, LCD_7, LCD_8, LCD_9, LCD_10, LCD_11)

mc.setBlocks (-7,49,5,75,17,5,param.SEA_LANTERN_BLOCK)
mc.setBlocks (-5,47,5,73,19,5,param.IRON_BLOCK)

def update_col( col=0, code=2):
    i = 34
    for y in range(7):
        for x in range(5):
            if  LCD_font_styles[int(code)][i]  == 1:
                mc.setBlock(-x + col*8, y+40, 5,  param.GOLD_BLOCK)
            else:
                mc.setBlock(-x + col*8, y+40, 5,  param.IRON_BLOCK)
            i -= 1

def update_col1( col=0, code=2):
    i = 34
    for y in range(7):
        for x in range(5):
            if  LCD_font_styles[int(code)][i]  == 1:
                mc.setBlock(-x + col*8, y+30, 5,  param.GOLD_BLOCK)
            else:
                mc.setBlock(-x + col*8, y+30, 5,  param.IRON_BLOCK)
            i -= 1

running = True
while running:
        
    date = datetime.datetime.now()
    update_col(col= 0, code= date.hour//10)
    update_col(col= 1, code= date.hour%10)
    update_col(col= 2, code= 11)
    update_col(col= 3, code= date.minute//10)
    update_col(col= 4, code= date.minute%10)
    update_col(col= 5, code= 11)
    update_col(col= 6, code= date.second//10)
    update_col(col= 7, code= date.second%10)
    update_col1(col= 0, code= date.year//1000%10)
    update_col1(col= 1, code= date.year//100%10)
    update_col1(col= 2, code= date.year//10%10)
    update_col1(col= 3, code= date.year%10)
    update_col1(col= 4, code= 10)
    update_col1(col= 5, code= date.month//10)
    update_col1(col= 6, code= date.month%10)
    update_col1(col= 7, code= 10)
    update_col1(col= 8, code= date.day//10)
    update_col1(col= 9, code= date.day%10)

    time.sleep(0.1)

from datetime import datetime
import pygame

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([500, 320])
pygame.display.set_caption("pygame 7-segment display simulation")
pygame.display.set_caption("LCD font")
screen.fill(DARK_GRAY)

display5 = Seven_seg(screen)
display5.init_col(BLOCK_SIZE=9, BLOCK_INTV=9, COLOR_ON=CYAN, COLOR_OFF=GRAY)
display5.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

lcd1 = LCD_font(screen)
lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
lcd1.init_row(X_ORG=1, Y_ORG=20, COL_INTV=6)

lcd2 = LCD_font(screen)
lcd2.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=RED, COLOR_OFF=GRAY)
lcd2.init_row(X_ORG=1, Y_ORG=12, COL_INTV=6)

running = True
# infinite loop top ----
while running:
    for count in range(16 ** 4):  # 0から65535まで
        # press ctrl-c or close the window to stop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if not running:
            break

        dt_now = datetime.now()
        time_now = (dt_now.hour * 10000
                    + dt_now.minute * 100
                    + dt_now.second)
        display5.disp_num2(zfil=True, rjust=0, num=time_now, base=10)

   
        lcd1.update_col(col=0, code=dt_now.hour // 10)
        lcd1.update_col(col=1, code=dt_now.hour % 10)
        lcd1.update_col(col=2, code=10)
        lcd1.update_col(col=3, code=dt_now.minute // 10)
        lcd1.update_col(col=4, code=dt_now.minute % 10)
        lcd1.update_col(col=5, code=10)
        lcd1.update_col(col=6, code=dt_now.second // 10)
        lcd1.update_col(col=7, code=dt_now.second % 10)

        lcd2.update_col(col=0, code=int(str(dt_now.year)[0]))
        lcd2.update_col(col=1, code=int(str(dt_now.year)[1]))
        lcd2.update_col(col=2, code=int(str(dt_now.year)[2]))
        lcd2.update_col(col=3, code=int(str(dt_now.year)[3]))
        lcd2.update_col(col=4, code=11)
        
        lcd2.update_col(col=5, code=0)
        lcd2.update_col(col=6, code=int(str(dt_now.month)[0]))
        
        lcd2.update_col(col=7, code=11)
        
        lcd2.update_col(col=8, code=int(str(dt_now.day)[0]))
        lcd2.update_col(col=9, code=int(str(dt_now.day)[1]))

        pygame.display.flip()  # update_col
        clock.tick(20)  # FPS, Frame Per Second
    
    screen.fill(DARK_GRAY)

# infinit loop bottom ----

pygame.quit()