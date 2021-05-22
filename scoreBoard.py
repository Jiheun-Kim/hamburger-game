import pygame, sys, highScore
from context import *
from pygame.locals import *

class scoreBoard():

    def __init__(self):
        self.WINDOWWIDTH = 500
        self.WINDOWHEIGHT = 700
        
        #색상
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BROWN = (80, 120, 40)
        
        #Set In Game colors and assets
        self.BGCOLOR = self.BLACK
        self.BGIMAGE = pygame.image.load("images/game/gamebg1.png")
        self.BGIMAGE = pygame.transform.scale(self.BGIMAGE, (500, 700))
        self.BORDERCOLOR = self.BROWN
        
        #버튼 속성
        self.BUTTONTEXTCOLOR = self.BLACK
        
        #뒤로가기
        self.BACK_SURF, self.BACK_RECT = self.makeText('뒤로가기', self.BUTTONTEXTCOLOR, 20, 10, self.WINDOWHEIGHT - 40)
    
        self.screen = pygame.display.get_surface() 

    #이벤트 루프 함수
    def update(self, dt):
        for event in pygame.event.get():
            
            if event.type == MOUSEBUTTONUP:
                if self.BACK_RECT.collidepoint(event.pos):
                    if top() is self:
                        pop()
            
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    if top() is self:
                        pop()
    
            elif event.type == QUIT:
                sys.exit()

    #/화면에 그리기             
    def draw(self, dt): 

        self.screen.blit(self.BGIMAGE, (0, 0))
        pygame.draw.rect(self.screen, self.BROWN, (100,100, (self.WINDOWWIDTH - 200), (self.WINDOWHEIGHT) - 200), 9)
        pygame.draw.rect(self.screen, self.WHITE, (108,108, (self.WINDOWWIDTH - 217), (self.WINDOWHEIGHT - 217)))
        
        TITLE, TITLERECT = self.makeText('랭킹', self.BLACK, 20, 230, 110)
        self.screen.blit(TITLE, TITLERECT)
        
        puzHighScoreObj = highScore.Highscore("puz")
         
        x = 150
        y = 210
        
        for score in puzHighScoreObj.getScores():         
            
            puzPlayerName, puzPlayerRect = self.makeText(score[0], self.BLACK, 30, x, y)
            self.screen.blit(puzPlayerName, puzPlayerRect)        

            puzPlayerScore, puzPlayerScoreRect = self.makeText(str(score[1]), self.BLACK, 30, x + 250, y)
            self.screen.blit(puzPlayerScore, puzPlayerScoreRect) 
            
            y += 30

        self.screen.blit(self.BACK_SURF,self.BACK_RECT)
        pygame.display.flip()
            
    #게임 함수
    def think(self, dt):
        self.update(dt)
        self.draw(dt)

    def makeText(self, text, color, size, top, left, ):
        font = pygame.font.SysFont("malgungothic", size, bold=True)
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect()
        textRect.topleft = (top, left)
        return (textSurf, textRect)
