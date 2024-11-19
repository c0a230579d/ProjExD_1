import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像を描画
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png") #3.pngを読み込み
    kk_img = pg.transform.flip(kk_img, True, False) #こうかとん反転
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0) # 10度反時計回りに回転

    screen.blit(kk_img, (300, 200)) # こうかとんを描画
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr%3200)
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        j=0
        j += -1
        y = 0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            y += -1
        if key_lst[pg.K_DOWN]:
            y += 1
        if key_lst[pg.K_LEFT]:
            j += -1
        if key_lst[pg.K_RIGHT]:
            j += 2
        kk_rct.move_ip((j,y))
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()