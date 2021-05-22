import pygame, sys, game
from context import *
from pygame.locals import *

class levelSelect():

    def __init__(self):
        self.WINDOWWIDTH = 500
        self.WINDOWHEIGHT = 700
        
        #색상
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        #배경 화면        
        self.BGIMAGE = pygame.image.load("images/startScreen/introbg.png")
        self.BGIMAGE = pygame.transform.scale(self.BGIMAGE, (500, 700))

        #뒤로가기 
        self.BACK_SURF, self.BACK_RECT = self.makeText('뒤로가기', self.WHITE, 20, 10, self.WINDOWHEIGHT - 40)
        
        self.screen = pygame.display.get_surface()
        
    #이벤트 루프 함수
    def update(self, dt):
        for event in pygame.event.get(): 
            if event.type == MOUSEBUTTONUP:
                if self.easyRect.collidepoint(event.pos):
                    push(game.game(80, 4, 4))
                if self.hardRect.collidepoint(event.pos):
                    push(game.game(64, 5, 5))
                    
            if event.type == MOUSEBUTTONUP:
                if self.BACK_RECT.collidepoint(event.pos):
                    if top() is self:
                        pop()
                    
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    if top() is self:
                        pop()
                    
                if event.key == K_RETURN:
                    if top() is self:
                        pop()  
            
            elif event.type == QUIT:
                sys.exit()

    #화면에 그리기
    def draw(self, dt): 

        self.screen.blit(self.BGIMAGE, (0, 0))
        pygame.draw.rect(self.screen, self.BLACK, (0, 0, 500, 700))
        
        titleText0, titleRect0 = self.makeTextCenter("하...집에 가고싶다...", self.WHITE, 20, 250, 230)
        titleText1, titleRect1 = self.makeTextCenter("안녕? 나는 햄버거가게 알바생이야", self.WHITE, 20, 250, 260)
        titleText2, titleRect2 = self.makeTextCenter("집에 가고 싶은데 손님이 아직 3명이나 남았어", self.WHITE, 20, 250, 290)
        titleText3, titleRect3 = self.makeTextCenter("키보드 'w''s''a''d'를 눌러서 햄버거 퍼즐을 맞춰줘", self.WHITE, 20, 250, 320)
        titleText4, titleRect4 = self.makeTextCenter("너만 믿을게..?", self.WHITE, 20, 250, 350)
        self.easyText, self.easyRect = self.makeTextCenter("쉬운 모드", self.WHITE, 30, 120, 460)
        self.hardText, self.hardRect = self.makeTextCenter("어려운 모드", self.WHITE, 30, 360, 460)
            
        self.screen.blit(titleText0, titleRect0)
        self.screen.blit(titleText1, titleRect1)
        self.screen.blit(titleText2, titleRect2)
        self.screen.blit(titleText3, titleRect3)
        self.screen.blit(titleText4, titleRect4)
        self.screen.blit(self.easyText, self.easyRect)
        self.screen.blit(self.hardText, self.hardRect)

        self.screen.blit(self.BACK_SURF,self.BACK_RECT)
            
        pygame.display.flip()      
            
    #게임 함수
    def think(self, dt):
        self.update(dt)
        self.draw(dt)

    def makeTextCenter(self,  text, color, size, centerx, height):
        font = pygame.font.SysFont("malgungothic", size, bold=True, italic = False)
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect()
        textRect.center = (centerx, height)
        return (textSurf, textRect)
    
    def makeText(self, text, color, size, top, left, ):
        font = pygame.font.SysFont("malgungothic", size, bold=True)
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect()
        textRect.topleft = (top, left)
        return (textSurf, textRect)
