import pyxel
from enum import Enum

#import os           # タイムスタンプ
#import pathlib


# test no
TEST_COLOR = 0
TEST_IMG_LOAD = 1
TEST_RELOAD = 2
TEST_TILE = 3
TEST_END = 4

test_str = ["0:COLOR","1:IMG LOAD","2:RELOAD","3:TILE","END"]

class App:

    img_no = 0
    file_time = 0
    file_anim = "assets/img_re00.png"
    file_anim_time = 0
    test_mode = 0
    reload_text_time = 0
    reload_anim_time = 0
    reload_anim_no = 0

    #-----------------------------------------------------
    def __init__(self):
        pyxel.init(256, 240, title="Hello Pyxel",display_scale=3)

        self.deg = 0
        self.test_mode = 0

        pyxel.run(self.update, self.draw)

    #-----------------------------------------------------
    def update(self):
        # メニュー選択
        if pyxel.btnp(pyxel.KEY_UP) | pyxel.btnp(pyxel.KEY_DOWN):
            if pyxel.btnp(pyxel.KEY_UP):
                if self.test_mode > 0:
                    self.test_mode -= 1
            if pyxel.btnp(pyxel.KEY_DOWN):
                if self.test_mode < TEST_END - 1:
                    self.test_mode += 1
                    if self.test_mode == TEST_RELOAD:
                        self.file_anim_time = 0     # リロードさせる

        # Color
        if  self.test_mode == TEST_COLOR:
            pyxel.colors.from_list([0x000000,0x2B335F,0x7E2072,0x19959C,
                                    0x8B4852,0x395C98,0xA9C1FF,0xEEEEEE,
                                    0xD4186C,0xD38441,0xE9C35B,0x70C6A9,
                                    0x7696DE,0xA3A3A3,0xFF9798,0xEDC7B0])

        # イメージファイルのロード 
        # 左右で3枚目のみリロードする、パレットは変化しない
        if  self.test_mode == TEST_IMG_LOAD:
            pyxel.images[0].load(0, 0, "assets/img00.png", incl_colors=True)
            pyxel.images[1].load(0, 0, "assets/img01.png", incl_colors=True)
            pyxel.images[2].load(0, 0, "assets/img02.png", incl_colors=True)

        #イメージファイルのタイムスタンプを調べて変化したらリロードする
        if  self.test_mode == TEST_RELOAD:
#            self.file_anim_time = os.path.getmtime(self.file_anim)
            pass

        #タイル
        if  self.test_mode == TEST_TILE:
            pyxel.load("./assets/my_resource.pyxres")


        #---------------------------------------------
        # test main
        if  self.test_mode == TEST_COLOR:
            pass

        if  self.test_mode == TEST_IMG_LOAD:
            # img loadのテスト
            if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_LEFT):
                if pyxel.btnp(pyxel.KEY_RIGHT):
                    self.img_no += 1
                    if self.img_no > 2:
                        self.img_no = 0
                if pyxel.btnp(pyxel.KEY_LEFT):
                    self.img_no -= 1
                    if self.img_no < 0:
                        self.img_no = 2

                if self.img_no == 0:
                    pyxel.images[2].load(0, 0, "assets/img00.png", incl_colors=True)
                if self.img_no == 1:
                    pyxel.images[2].load(0, 0, "assets/img01.png", incl_colors=True)
                if self.img_no == 2:
                    pyxel.images[2].load(0, 0, "assets/img02.png", incl_colors=True)
        
        if  self.test_mode == TEST_RELOAD:
            # ファイルのタイムスタンプが更新されたらリロードする
#            t = os.path.getmtime(self.file_anim)
#            if self.file_anim_time != t:
#                self.file_anim_time = t
#                pyxel.images[2].load(0, 0, "assets/img_re00.png", incl_colors=True)
#                self.reload_text_time = 60
            pass

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        if  self.test_mode == TEST_COLOR:
            for i in range(16):
                rgb = pyxel.colors[i]
                hex = f"#{rgb:06X}"
                pyxel.rect(100, 50 + i * 10, 20, 8, i)
                pyxel.text(140, 50 + i * 10, hex, 7)

        if  self.test_mode == TEST_IMG_LOAD:
            pyxel.blt(30, 40, 0, 0, 0, 256, 256)
            pyxel.blt(30, 100, 1, 0, 0, 256, 256)
            pyxel.blt(30, 160, 2, 0, 0, 256, 256)

        if  self.test_mode == TEST_RELOAD:
            # テクスチャReload
            pyxel.blt(30, 40, 2, 0, 0, 256, 256)


            # anim
            pyxel.text(50, 150, str(self.reload_anim_no), 10)

            uu = 0 + self.reload_anim_no * 32
            vv = 64
            pyxel.blt(50, 160, 2, uu, vv, 32, 32)

            self.reload_anim_time -= 1
            if self.reload_anim_time < 0:
                self.reload_anim_time = 10
                self.reload_anim_no += 1
                if self.reload_anim_no > 3:
                    self.reload_anim_no = 0

            if self.reload_text_time > 0:
                self.reload_text_time -= 1
                pyxel.text(100, 60, "Reload", pyxel.frame_count % 16)

            pyxel.text(100, 40, str(self.file_anim_time), 10)

        if  self.test_mode == TEST_TILE:
            # bltm(x, y, tm, u, v, w, h, [colkey], [rotate], [scale])
            pyxel.bltm(0, 0, 0, 0, 256, 256, 240, 0)
            pyxel.bltm(0, 0, 0, 0, 0, 256, 240, 0)


        pyxel.text(100, 40, str(self.img_no), 10)

        # Color Bar
        for a in range(0,63, 1):
            col = str(a)
            pyxel.text(1, a * 4, col, a)
            pyxel.rect(10, a * 4, 10, 4, a)

        pyxel.text(100, 0, "Pixel", pyxel.frame_count % 16)

        y = 0
        for s in test_str:
            c = 1
            if self.test_mode == y:
                c = pyxel.frame_count % 16
            pyxel.text(50 ,10 + y * 10 ,s , c)
            y += 1
            if y == TEST_END:   break
     
App()
