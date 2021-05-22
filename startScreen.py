import pygame, sys,levelSelect,scoreBoard
from context import *
from pygame.locals import *

class startScreen():
    
    def __init__(self, screen):
        #화면 크기
        self.WINDOWWIDTH = 500
        self.WINDOWHEIGHT = 700

        #색상
        self.WHITE = (255,255,255 )
        self.BLACK = (0,0,0)
        self.BROWN = (180,120,40)

        #메인 화면 배경이미지
        self.BGIMAGE = pygame.image.load("images/startScreen/introbg.png")
        self.BGIMAGE = pygame.transform.scale(self.BGIMAGE, (500, 700))

        #메인 화면 타이틀 이미지
        self.TITLE = pygame.image.load("images/startScreen/title.png")
        self.TITLE = pygame.transform.scale(self.TITLE, (300, 100))

        #버튼 속성(색상)
        self.BUTTONTEXTCOLOR = self.WHITE
        
        #메인화면 배경음악
        self.startSOUND = pygame.mixer.Sound("Audio/Laid Back LOOP.wav")
        
        #메인화면 선택 버튼
        self.START_SURF, self.START_RECT = self.makeText('게임 시작', self.BUTTONTEXTCOLOR, 40, self.WINDOWWIDTH/2, 400)
        self.SCOREBOARD_SURF, self.SCOREBOARD_RECT = self.makeText('랭킹 점수', self.BUTTONTEXTCOLOR, 40, self.WINDOWWIDTH/2, 450)
        self.EXIT_SURF, self.EXIT_RECT = self.makeText('게임 종료', self.BUTTONTEXTCOLOR, 40, self.WINDOWWIDTH/2, 500)
        self.startSOUND.play()
        
        self.screen = screen
        
    #이벤트 루프
    def update(self, dt):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                if self.START_RECT.collidepoint(event.pos): #사용자가 게임 시작 버튼을 눌렀을 시
                    #레벨 선택
                    push(levelSelect.levelSelect())
                elif self.SCOREBOARD_RECT.collidepoint(event.pos):#랭킹 점수를 눌렀을 시
                    push(scoreBoard.scoreBoard())
                elif self.EXIT_RECT.collidepoint(event.pos):
                    if top() is self:
                        pop()
            
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    if top() is self:
                        pop()
            
            elif event.type == QUIT:
                sys.exit()
        
    #화면에 그리기
    def draw(self, dt): 
        self.screen.blit(self.BGIMAGE, (0, 0))
        self.screen.blit(self.TITLE, (100, 100))
        self.screen.blit(self.START_SURF, self.START_RECT)
        self.screen.blit(self.SCOREBOARD_SURF, self.SCOREBOARD_RECT)
        self.screen.blit(self.EXIT_SURF, self.EXIT_RECT)
        
        pygame.display.flip()      
    
    #게임 함수
    def think(self, dt):
        self.update(dt)
        self.draw(dt)
            
    def makeText(self, text, color, size, centerx, height):
        font = pygame.font.SysFont("malgungothic", size, bold=True)
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect()
        textRect.midbottom = (centerx, height)
        return (textSurf, textRect)
