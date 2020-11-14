import pygame as pg
import random

pg.init() #파이게임 초기화

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pg.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pg.display.set_caption("Portfolio")

#FPS
clock = pg.time.Clock()

game_font = pg.font.Font(None,40)

start_ticks = pg.time.get_ticks()

#배경이미지 불러오기
background = pg.image.load("C:/Users/Bastion/Documents/Portfolio/background.png")
#캐릭터(스프라이트)
character = pg.image.load("C:/Users/Bastion/Documents/Portfolio/character.png")
character_size = character.get_rect().size #이미지 크기 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width/2)
character_y_pos = screen_height-character_height

to_x = 0
character_speed = 0.6
#똥
ddong = pg.image.load("C:/Users/Bastion/Documents/Portfolio/enemy.png")
ddong_size = ddong.get_rect().size #이미지 크기 구해옴
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0,screen_width-ddong_width)
ddong_y_pos = 0
ddong_speed = 10

ddong1 = pg.image.load("C:/Users/Bastion/Documents/Portfolio/enemy.png")
ddong1_size = ddong1.get_rect().size #이미지 크기 구해옴
ddong1_width = ddong1_size[0]
ddong1_height = ddong1_size[1]
ddong1_x_pos = random.randint(0,screen_width-ddong_width)
ddong1_y_pos = 0
ddong1_speed = 8

ddong2 = pg.image.load("C:/Users/Bastion/Documents/Portfolio/enemy.png")
ddong2_size = ddong2.get_rect().size #이미지 크기 구해옴
ddong2_width = ddong2_size[0]
ddong2_height = ddong2_size[1]
ddong2_x_pos = random.randint(0,screen_width-ddong_width)
ddong2_y_pos = 0
ddong2_speed = 6

ddong3 = pg.image.load("C:/Users/Bastion/Documents/Portfolio/enemy.png")
ddong3_size = ddong3.get_rect().size #이미지 크기 구해옴
ddong3_width = ddong3_size[0]
ddong3_height = ddong3_size[1]
ddong3_x_pos = random.randint(0,screen_width-ddong_width)
ddong3_y_pos = 0
ddong3_speed = 5

#이벤트 루프
running = True #게임진행중
while running:
    dt = clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN: #방향키 눌러짐
            if event.key == pg.K_LEFT: #왼쪽방향키
                to_x -= character_speed
            elif event.key == pg.K_RIGHT: #오른쪽방향키
                to_x += character_speed
            
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                to_x = 0
            
    character_x_pos += to_x * dt               

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width
    
    ddong_y_pos += ddong_speed
    ddong1_y_pos += ddong1_speed
    ddong2_y_pos += ddong2_speed
    ddong3_y_pos += ddong3_speed

    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0,screen_width-ddong_width)
    if ddong1_y_pos > screen_height:
        ddong1_y_pos = 0
        ddong1_x_pos = random.randint(0,screen_width-ddong_width)
    if ddong2_y_pos > screen_height:
        ddong2_y_pos = 0
        ddong2_x_pos = random.randint(0,screen_width-ddong_width)
    if ddong3_y_pos > screen_height:
        ddong3_y_pos = 0
        ddong3_x_pos = random.randint(0,screen_width-ddong_width)
    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    ddong1_rect = ddong1.get_rect()
    ddong1_rect.left = ddong1_x_pos
    ddong1_rect.top = ddong1_y_pos

    ddong2_rect = ddong2.get_rect()
    ddong2_rect.left = ddong2_x_pos
    ddong2_rect.top = ddong2_y_pos
    
    ddong3_rect = ddong3.get_rect()
    ddong3_rect.left = ddong3_x_pos
    ddong3_rect.top = ddong3_y_pos
    
    result = "Game Over"
    end = game_font.render(result,True,(255,0,255))
    end_rect = end.get_rect(center=(int(screen_width/2),int(screen_height/2)))

    if character_rect.colliderect(ddong_rect):
        screen.blit(end,end_rect)
        pg.display.update()
        running = False
        pg.time.delay(2000)
    if character_rect.colliderect(ddong1_rect):
        screen.blit(end,end_rect)
        pg.display.update()  
        running = False
        pg.time.delay(2000)
    if character_rect.colliderect(ddong2_rect):
        screen.blit(end,end_rect)
        pg.display.update()     
        running = False
        pg.time.delay(2000)
    if character_rect.colliderect(ddong3_rect):
        screen.blit(end,end_rect)
        pg.display.update()     
        running = False
        pg.time.delay(2000)
    elapsed_time = game_font.render(str(int((pg.time.get_ticks() - start_ticks) / 1000)),True,(255,255,255)) 

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(ddong,(ddong_x_pos,ddong_y_pos))
    screen.blit(ddong1,(ddong1_x_pos,ddong1_y_pos))
    screen.blit(ddong2,(ddong2_x_pos,ddong2_y_pos))
    screen.blit(ddong3,(ddong3_x_pos,ddong3_y_pos))
    screen.blit(elapsed_time,(10,10))
    pg.display.update() #게임화면 업데이트