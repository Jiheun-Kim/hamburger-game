import pygame, sys, highScore
from context import *
from pygame.locals import *

class submitScore():
    
    def __init__(self, score, puz):
        self.WINDOWWIDTH = 1100
        self.WINDOWHEIGHT = 700

        #색상
        self.WHITE = (255, 255, 255)
        self.BLACK = 0, 0, 0
    
        #폰트
        self.BASICFONTSIZE = 20
         
        self.BASICFONT = pygame.font.SysFont("malgungothic", self.BASICFONTSIZE, bold=True, italic = True)
        
        #버튼 속성
        self.BUTTONTEXTCOLOR = self.WHITE
        
        self.screen = pygame.display.get_surface()
        
        self.__playerName = ""
        self.score = score
        self.puz = puz
        
    #이벤트 루프 함수
    def update(self, dt):
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                pass
            
            elif event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    highScore.Highscore(self.puz).add(self.__playerName, self.score)

                    if top() is self:
                        pop()
                        
                elif event.key >= 65 and event.key <= 122:
                    self.__playerName += chr(event.key)
                if event.key == K_ESCAPE:
                    if top() is self:
                        pop()
            
            elif event.type == QUIT:
                sys.exit()
        
    #화면에 그리기
    def draw(self, dt):
        pygame.draw.rect(self.screen, self.BLACK, (0, 180, self.WINDOWWIDTH, 300))
        
        self.TITLE = self.BASICFONT.render('랭킹에 등록할 이름을 입력하세요.', 1, self.WHITE)
        self.askNameText = self.BASICFONT.render('이름:', 1, self.WHITE)
        self.askName = self.BASICFONT.render(self.__playerName, 1, self.WHITE)
        
        self.screen.blit(self.TITLE, (20, 205))
        self.screen.blit(self.askNameText, (100, 305))        
        self.screen.blit(self.askName, (200, 305)) 
        
        pygame.display.flip()

    #게임 함수 
    def think(self, dt):
        self.update(dt)
        self.draw(dt)
