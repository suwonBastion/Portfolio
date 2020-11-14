import pygame as pg
import os

pg.init() #파이게임 초기화

#화면 크기 설정
screen_width = 640
screen_height = 480
screen = pg.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pg.display.set_caption("Portfolio")

#FPS
clock = pg.time.Clock()

#설정
current_path = os.path.dirname(__file__) #현재 파일위치 반환
image_path = os.path.join(current_path,"image") #image폴더위치 설정

#배경
background = pg.image.load(os.path.join(image_path,"background.png"))
#스테이지
stage = pg.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지 높이 위에 캐릭터를 두기 위해 사용

#캐릭터(스프라이트)
character = pg.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size 
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width /2) - (character_width/2)
character_y_pos = screen_height-character_height-stage_height

#무기 만들기
weapon = pg.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기 여러발발사 가능
weapons = []

#무기 이속
weapon_speed = 10

# 공만들기
ball_images = [
    pg.image.load(os.path.join(image_path,"balloon1.png")),
    pg.image.load(os.path.join(image_path,"balloon2.png")),
    pg.image.load(os.path.join(image_path,"balloon3.png")),
    pg.image.load(os.path.join(image_path,"balloon4.png"))]
# 공 스피드
ball_speed_y = [-18,-15,-12,-9] #idx 0,1,2,3

#공들
balls = []
balls.append({
    "pos_x":50, #공의 x좌표
    "pos_y":50, #공의 y좌표
    "img_idx":0, #공의 이미지 인덱스
    "to_x":3, #공의 x축 이동방향 -3왼 +3오
    "to_y": -6, #y축 이동방향
    "init_spd_y": ball_speed_y[0]}) #y최초속도추가

#무기 공 쓰레기통
weapon_to_remove = -1
ball_to_remove = -1

#폰트 정의
game_font = pg.font.Font(None,40)
total_time = 100
start_ticks = pg.time.get_ticks() #시작시간정의

game_result = "Game Over"


#이동할 좌표
to_x = 0
to_y = 0

#이속
character_speed = 0.6

#이벤트 루프
running = True #게임진행중
while running:
    dt = clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN: #방향키 눌러짐
            if event.key == pg.K_LEFT: #왼쪽방향키
                to_x -= character_speed
            elif event.key == pg.K_RIGHT: #오른쪽방향키
                to_x += character_speed
            elif event.key == pg.K_SPACE:
                weapon_x_pos = character_x_pos+(character_width/2)-(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                to_x = 0
          

    character_x_pos += to_x * dt           

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width
    
    #무기 발사
    weapons = [[w[0],w[1] - weapon_speed] for w in weapons if w[1] > 0]

    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #벽에 닿으면 튕김
        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] *-1
        #세로위치
        if ball_pos_y >= screen_height-stage_height-ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5 
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    #충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        #공rect업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        
        #공과 캐릭터 충돌처리
        if character_rect.colliderect(ball_rect):            
            running = False
            break
        #공과 무기들 충돌처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_x_pos = weapon_val[0]
            weapon_y_pos =  weapon_val[1]

            #무기 rect 정보 업데이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos

            #충돌체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당무기 없애기위한 값 설정
                ball_to_remove = ball_idx
                
                #가장 작은공이 아니라면 두개로 쪼개기
                if ball_img_idx < 3:
                    #현재 공크기정보
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    #나눠진 공 정보
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]
                    #왼쪽으로 쪼개지는공
                    balls.append({
                        "pos_x":ball_pos_x + (ball_width /2)-(small_ball_width/2), #공의 x좌표
                        "pos_y":ball_pos_y+(ball_height/2)-(small_ball_height/2), #공의 y좌표
                        "img_idx":ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x":-3, #공의 x축 이동방향 -3왼 +3오
                        "to_y": -6, #y축 이동방향
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]})
                    #오른쪽으로 쪼개지는 공
                    balls.append({
                        "pos_x":ball_pos_x + (ball_width /2)-(small_ball_width/2), #공의 x좌표
                        "pos_y":ball_pos_y+(ball_height/2)-(small_ball_height/2), #공의 y좌표
                        "img_idx":ball_img_idx + 1, #공의 이미지 인덱스
                        "to_x":3, #공의 x축 이동방향 -3왼 +3오
                        "to_y": -6, #y축 이동방향
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]})
                break
        else:
            continue
        break
    # 충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
       
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    for idx,val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    
    #시간계산 
    elapsed_time = (pg.time.get_ticks() - start_ticks) / 1000 
    timer = game_font.render("Time : {}".format(int(total_time-elapsed_time)),True,(255,255,255))
    screen.blit(timer,(10,10))
    
    #시간 초과했다면
    if total_time - elapsed_time <=0:
        game_result = "Time Over"
        running = False
    
    #게임깸
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False
    pg.display.update()
msg = game_font.render(game_result,True,(255,255,0))
msg_rect = msg.get_rect(center=(int(screen_width/2),int(screen_height/2)))
screen.blit(msg,msg_rect)
pg.display.update()
pg.time.delay(2000)

pg.quit()


     
    