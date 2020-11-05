import pygame              # ❶ 파이게임 모듈 임포트하기
import time
from datetime import datetime
from datetime import timedelta
import random

SCREEN_WIDTH = 400         # ❷ 게임 화면의 너비
SCREEN_HEIGHT = 400         #   게임 화면의 높이

pygame.init()              # ❸ 파이게임을 사용하기 전에 초기화한다.

# ❹ 지정한 크기의 게임 화면 창을 연다.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RED = 255, 0, 0        # 적색:   적 255, 녹   0, 청   0
GREEN = 0, 255, 0      # 녹색:   적   0, 녹 255, 청   0
BLUE = 0, 0, 255       # 청색:   적   0, 녹   0, 청 255
PURPLE = 127, 0, 127   # 보라색: 적 127, 녹   0, 청 127
BLACK = 0, 0, 0        # 검은색: 적   0, 녹   0, 청   0
GRAY = 127, 127, 127   # 회색:   적 127, 녹 127, 청 127
WHITE = 255, 255, 255  # 하얀색: 적 255, 녹 255, 청 255

# 화면 전체에 하얀 사각형 그리기
rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))  # ❶
pygame.draw.rect(screen, WHITE, rect)  # ❷

# 화면 왼쪽 위에 녹색 정사각형 그리기
rect = pygame.Rect((0, 0), (40, 40))
pygame.draw.rect(screen, GREEN, rect)

# 화면 오른쪽 아래에 적색 직사각형 그리기
rect = pygame.Rect((340, 60), (60, 20))
pygame.draw.rect(screen, RED, rect)

pygame.display.update()  # ❸ 화면 새로고침

# time.sleep(3)
# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

def draw_background(screen):
    """게임의 배경을 그린다."""
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)

def draw_block(screen, color, position):
    """position 위치에 color 색깔의 블록을 그린다."""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

pygame.init()  
    
# draw_background(screen)
# draw_block(screen, RED, (1, 1))
# draw_block(screen, RED, (3, 1))
# draw_block(screen, RED, (5, 1))
# draw_block(screen, RED, (7, 1))
# draw_block(screen, GREEN, (12, 10))
# draw_block(screen, GREEN, (12, 11))
# draw_block(screen, GREEN, (12, 12))
# draw_block(screen, GREEN, (12, 13))
# pygame.display.update()


block_position = [0, 0]  # ❶ 블록의 위치 (y, x)
DIRECTION_ON_KEY = {
    pygame.K_UP: 'north',
    pygame.K_DOWN: 'south',
    pygame.K_LEFT: 'west',
    pygame.K_RIGHT: 'east',
}
block_direction = 'east'




# while True:
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             exit()
#         if event.type == pygame.KEYDOWN:
#             # ❸ 입력된 키가 화살표 키면,
#             if event.key in DIRECTION_ON_KEY:
#                 # ❹ 블록의 방향을 화살표 키에 맞게 바꾼다 
#                 block_direction = DIRECTION_ON_KEY[event.key]

#     if timedelta(seconds=1) <= datetime.now() - last_moved_time:
#         if block_direction == 'north':    # ❺ 1초가 지날 때마다
#             block_position[0] -= 1        # 블록의 방향에 따라
#         elif block_direction == 'south':  # 블록의 위치를 변경한다
#             block_position[0] += 1
#         elif block_direction == 'west':
#             block_position[1] -= 1
#         elif block_direction == 'east':
#             block_position[1] += 1
#         last_moved_time = datetime.now()

#     draw_background(screen)
#     draw_block(screen, GREEN, block_position)
#     pygame.display.update()

class Snake:
    """뱀 클래스"""
    color = GREEN  # 뱀의 색
    

    def __init__(self):
        self.positions = [(9, 6), (9, 7), (9, 8), (9, 9)]  # 뱀의 위치
        self.direction = 'north'  # 뱀의 방향
    def draw(self, screen):
        """뱀을 화면에 그린다."""
        for position in self.positions:  # ❶ 뱀의 몸 블록들을 순회하며
            draw_block(screen, self.color, position)  # 각 블록을 그린다
    def crawl(self):
        """뱀이 현재 방향으로 한 칸 기어간다."""
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'south':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'west':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'east':
            self.positions = [(y, x + 1)] + self.positions[:-1]
    def turn(self, direction):  # ❶
        """뱀의 방향을 바꾼다."""
        self.direction = direction
    def grow(self):
        """뱀이 한 칸 자라나게 한다."""
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'north':
            self.positions.append((y - 1, x))
        elif self.direction == 'south':
            self.positions.append((y + 1, x))
        elif self.direction == 'west':
            self.positions.append((y, x - 1))
        elif self.direction == 'east':
            self.positions.append((y, x + 1))
   

class Apple:
    """사과 클래스"""
    color = RED  # 사과의 색

    def __init__(self, position=(random.randint(0, 19), random.randint(0, 19))):
        self.position = position  # 사과의 위치
    def draw(self, screen):
        """사과를 화면에 그린다."""
        draw_block(screen, self.color, self.position)  # ❷


class GameBoard:
    """게임판 클래스"""
    width = 20   # 게임판의 너비
    height = 20  # 게임판의 높이

    def __init__(self):
        self.snake = Snake()  # 게임판 위의 뱀
        self.apple = Apple()  # 게임판 위의 사과
        self.apple2 = Apple()  # 게임판 위의 사과
    def draw(self, screen):
        """화면에 게임판의 구성요소를 그린다."""
        self.apple.draw(screen)  # ❸ 게임판 위의 사과를 그린다
        self.apple2.draw(screen)
        self.snake.draw(screen)  # 게임판 위의 뱀을 그린다
    def process_turn(self):
        """게임을 한 차례 진행한다."""
        
        self.snake.crawl()  # 뱀이 한 칸 기어간다.
        head = self.snake.positions[0]
        y, x = head
        if self.snake.positions[0] == self.apple.position:
            self.snake.grow()     # 뱀을 한 칸 자라게 한다  
            self.put_new_apple()  # 사과를 새로 놓는다
        if self.snake.positions[0] == self.apple2.position:
            self.snake.grow()     # 뱀을 한 칸 자라게 한다  
            self.put_new_apple2()  # 사과를 새로 놓는다
        # 뱀의 머리가 뱀의 몸과 부딛혔으면
        if self.snake.positions[0] in self.snake.positions[1:]:
            raise SnakeCollisionException()  # 뱀 충돌 예외를 일으킨다
        if (x>19 or x<0 or y>19 or y<0):
            raise SnakeCollisionException()  # 뱀 충돌 예외를 일으킨다
        if len(self.snake.positions)>7:
            self.snake.color = PURPLE
        if len(self.snake.positions)>11:
            self.snake.color = BLACK
            TURN_INTERVAL = timedelta(seconds=0.05)

        
        

    
    def put_new_apple(self):
        """게임판에 새 사과를 놓는다."""
        self.apple = Apple((random.randint(0, 19), random.randint(0, 19)))  # ❷
        for position in self.snake.positions:    # ❸ 뱀 블록을 순회하면서
            if self.apple.position == position:  # 사과가 뱀 위치에 놓인 경우를 확인해
                self.put_new_apple()             # 사과를 새로 놓는다
                break
    def put_new_apple2(self):
        """게임판에 새 사과를 놓는다."""
        self.apple2 = Apple((random.randint(0, 19), random.randint(0, 19)))  # ❷
        for position in self.snake.positions:    # ❸ 뱀 블록을 순회하면서
            if self.apple2.position == position:  # 사과가 뱀 위치에 놓인 경우를 확인해
                self.put_new_apple()             # 사과를 새로 놓는다
                break

class SnakeCollisionException(Exception):
    """뱀 충돌 예외"""
    pass

game_board = GameBoard()  # ❶ 게임판 인스턴스를 생성한다

TURN_INTERVAL = timedelta(seconds=0.2)  # ❶ 게임 진행 간격을 0.3초로 정의한다

last_turn_time = datetime.now()  # ❶ 마지막으로 블록을 움직인 때

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:  # ❷ 화살표 키가 입력되면 뱀의 방향을 바꾼다
            if event.key in DIRECTION_ON_KEY:
                game_board.snake.turn(DIRECTION_ON_KEY[event.key])
        
    

    # ❷ 시간이 TURN_INTERVAL만큼 지날 때마다 게임을 한 차례씩 진행한다
    if TURN_INTERVAL < datetime.now() - last_turn_time:
              
        try:
            game_board.process_turn()
        except SnakeCollisionException:
            exit()
        last_turn_time = datetime.now()
    
        

    draw_background(screen)
    game_board.draw(screen)
    pygame.display.update()





