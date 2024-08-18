# デジタル時計を表示するAPI
「Clock_MCJE」マイクラ世界に表示

「Clock_pygame」pygameにて表示

どちらもコードを書き換えることによって素材、大きさを変更可

「Clock_MCJE」...115,116行目と118~136行目から値を変更
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

![2024-08-18_04 45 12](https://github.com/user-attachments/assets/a2e0933a-b30a-4689-92c0-13ec96758cd8)
