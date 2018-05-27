import winsound
import pygame
from pygame.locals import * 
x = 70
x1 = x+15
y = 80#Era pra ser "p1"
p2 = 200
oitava =  2
sup = pygame.Surface((720,320))
sup.fill((255,255,255))     
g = pygame.display.set_mode((800,400))
g.blit(sup,[40,40]) 
while True:
#========cores=======
         branco = (255,255,255)
         preto = (0,0,0)
#========cores=======
#========letras======
         do = [pygame.draw.rect(g,(preto),Rect((p2,y),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+5,y+5),(40,90)))]
         dos = [pygame.draw.rect(g,(preto),Rect((p2+60,y),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+65,y+5),(40,90)))]
         re = [pygame.draw.rect(g,(preto),Rect((p2+120,y),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+125,y+5),(40,90)))]
         res = [pygame.draw.rect(g,(preto),Rect((p2+180,y),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+185,y+5),(40,90)))]
         mi = [pygame.draw.rect(g,(preto),Rect((p2+240,y),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+245,y+5),(40,90)))]
         fa = [pygame.draw.rect(g,(preto),Rect((p2+300,y),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+305,y+5),(40,90)))]
         fas = [pygame.draw.rect(g,(preto),Rect((p2+360,y),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+365,y+5),(40,90)))]
#====================
         sol = [pygame.draw.rect(g,(preto),Rect((p2+30,y+155),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+35,y+160),(40,90)))]
         sols = [pygame.draw.rect(g,(preto),Rect((p2+90,y+155),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+95,y+160),(40,90)))]
         la = [pygame.draw.rect(g,(preto),Rect((p2+150,y+155),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+155,y+160),(40,90)))]
         las = [pygame.draw.rect(g,(preto),Rect((p2+210,y+155),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+215,y+160),(40,90)))]
         si = [pygame.draw.rect(g,(preto),Rect((p2+270,y+155),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+275,y+160),(40,90)))]
         do_a = [pygame.draw.rect(g,(preto),Rect((p2+330,y+155),(50,100))),pygame.draw.rect(g,(branco),Rect((p2+335,y+160),(40,90)))]
#========letras======
#========textos1======
         pygame.font.init()
         font_txt = pygame.font.SysFont(pygame.font.get_default_font(), 50)
#========i======
         i = ("oitava: " + str(oitava))  
#========blits1=====  
         g.blit(font_txt.render("q = do" ,1,preto),[62,x])
         g.blit(font_txt.render("w = do#" ,1,preto),[62,x+40])
         g.blit(font_txt.render("e = re" ,1 ,preto),[62,x+80])
         g.blit(font_txt.render("r = re#" ,1,preto),[62,x+120])
         g.blit(font_txt.render("t = mi" ,1 ,preto),[62,x+160])
         g.blit(font_txt.render("y = fa" ,1,preto),[62,x+200])
         g.blit(font_txt.render("u =fa#" ,1 ,preto),[62,x+240])
#========blits2=====
         g.blit(font_txt.render("a = sol" ,1 ,preto),[622,x1])
         g.blit(font_txt.render("s = sol#" ,1 ,preto),[622,x1+40])
         g.blit(font_txt.render("d = la" ,1 ,preto),[622,x1+80])
         g.blit(font_txt.render("f = la#" ,1 ,preto),[622,x1+120])
         g.blit(font_txt.render("g = si" ,1 ,preto),[622,x1+160])
         g.blit(font_txt.render("s = do_a" ,1 ,preto),[622,x1+200]) 
         g.blit(font_txt.render(i,1,branco),[0,0])
#========blits2=====         
         pygame.display.update()
#========textos======
#========gamb========
         pygame.time.wait(150)
         gamb = True
#========gamb========
         for event in pygame.event.get():
            if (event.type == KEYDOWN and gamb == True):
                if(event.key==pygame.K_q):
                    if(oitava == 2):
                       do = [pygame.draw.rect(g,(preto),Rect((p2,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+5,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(66,500)
                       gamb = False
                    if(oitava == 3):
                       do = [pygame.draw.rect(g,(preto),Rect((p2,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+5,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(132,500)
                       gamb = False
                    if(oitava == 4):
                       do = [pygame.draw.rect(g,(preto),Rect((p2,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+5,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(264,500)
                       gamb = False
                    if(oitava == 5):
                       do = [pygame.draw.rect(g,(preto),Rect((p2,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+5,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(528,500)
                       gamb = False
                    if(oitava == 6):
                       do = [pygame.draw.rect(g,(preto),Rect((p2,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+5,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(1056,500)
                       gamb = False
                    if(oitava == 7):
                       do = [pygame.draw.rect(g,(preto),Rect((p2,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+5,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(2112,500)
                       gamb = False
                    if(oitava == 8):
                       do = [pygame.draw.rect(g,(preto),Rect((p2,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+5,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(4224,500)
                       gamb = False
                    if(oitava == 9):
                       do = [pygame.draw.rect(g,(preto),Rect((p2,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+5,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(8448,500)
                       gamb = False       
                if(event.key==pygame.K_w):
                    if(oitava == 2):
                       dos = [pygame.draw.rect(g,(preto),Rect((p2+60,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+65,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(70,500)
                       gamb = False
                    if(oitava == 3):
                       dos = [pygame.draw.rect(g,(preto),Rect((p2+60,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+65,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(140,500)
                       gamb = False
                    if(oitava ==4):
                       dos = [pygame.draw.rect(g,(preto),Rect((p2+60,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+65,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(280,500)
                       gamb = False
                    if(oitava == 5):
                       dos = [pygame.draw.rect(g,(preto),Rect((p2+60,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+65,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(559,500)
                       gamb = False
                    if(oitava == 6):
                       dos = [pygame.draw.rect(g,(preto),Rect((p2+60,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+65,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(1118,500)
                       gamb = False
                    if(oitava == 7):
                       dos = [pygame.draw.rect(g,(preto),Rect((p2+60,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+65,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(2237,500)
                       gamb = False
                    if(oitava == 8):
                       dos = [pygame.draw.rect(g,(preto),Rect((p2+60,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+65,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(4473,500)
                       gamb = False
                    if(oitava == 9):
                       dos = [pygame.draw.rect(g,(preto),Rect((p2+60,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+65,y+5),(40,90)))]
                       pygame.display.update()
                       winsound.Beep(8946,500)
                       gamb = False
                if(event.key==pygame.K_e):
                    if(oitava == 2):
                        re = [pygame.draw.rect(g,(preto),Rect((p2+120,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+125,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(74,500)
                        gamb = False
                    if(oitava == 3):
                        re = [pygame.draw.rect(g,(preto),Rect((p2+120,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+125,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(148,500)
                        gamb = False
                    if(oitava == 4):
                        re = [pygame.draw.rect(g,(preto),Rect((p2+120,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+125,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(296,500)
                        gamb = False
                    if(oitava == 5):
                        re = [pygame.draw.rect(g,(preto),Rect((p2+120,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+125,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(592,500)
                        gamb = False
                    if(oitava == 6):
                        re = [pygame.draw.rect(g,(preto),Rect((p2+120,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+125,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(1184,500)
                        gamb = False
                    if(oitava == 7):
                        re = [pygame.draw.rect(g,(preto),Rect((p2+120,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+125,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(2370,500)
                        gamb = False
                    if(oitava == 8):
                        re = [pygame.draw.rect(g,(preto),Rect((p2+120,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+125,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(4739,500)
                        gamb = False
                    if(oitava == 9):
                        re = [pygame.draw.rect(g,(preto),Rect((p2+120,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+125,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(9479,500)
                        gamb = False
                if(event.key==pygame.K_r):
                     if(oitava == 2):
                        res = [pygame.draw.rect(g,(preto),Rect((p2+180,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+185,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(78,500)        
                        gamb = False
                     if(oitava == 3):
                        res = [pygame.draw.rect(g,(preto),Rect((p2+180,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+185,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(157,500)        
                        gamb = False
                     if(oitava == 4):
                        res = [pygame.draw.rect(g,(preto),Rect((p2+180,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+185,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(314,500)        
                        gamb = False
                     if(oitava == 5):
                        res = [pygame.draw.rect(g,(preto),Rect((p2+180,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+185,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(628,500)        
                        gamb = False
                     if(oitava == 6):
                        res = [pygame.draw.rect(g,(preto),Rect((p2+180,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+185,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(1256,500)        
                        gamb = False
                     if(oitava == 7):
                        res = [pygame.draw.rect(g,(preto),Rect((p2+180,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+185,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(2511,500)        
                        gamb = False
                     if(oitava == 8):
                        res = [pygame.draw.rect(g,(preto),Rect((p2+180,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+185,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(5022,500)        
                        gamb = False
                     if(oitava == 9):
                        res = [pygame.draw.rect(g,(preto),Rect((p2+180,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+185,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(10045,500)        
                        gamb = False
                if(event.key==pygame.K_t):
                     if(oitava == 2):
                         mi = [pygame.draw.rect(g,(preto),Rect((p2+240,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+245,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(83,500)        
                         gamb = False
                     if(oitava == 3):
                         mi = [pygame.draw.rect(g,(preto),Rect((p2+240,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+245,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(166,500)        
                         gamb = False
                     if(oitava == 4):
                         mi = [pygame.draw.rect(g,(preto),Rect((p2+240,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+245,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(333,500)        
                         gamb = False
                     if(oitava == 5):
                         mi = [pygame.draw.rect(g,(preto),Rect((p2+240,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+245,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(665,500)        
                         gamb = False
                     if(oitava == 6):
                         mi = [pygame.draw.rect(g,(preto),Rect((p2+240,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+245,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(1331,500)        
                         gamb = False
                     if(oitava == 7):
                         mi = [pygame.draw.rect(g,(preto),Rect((p2+240,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+245,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(2661,500)        
                         gamb = False
                     if(oitava == 8):
                         mi = [pygame.draw.rect(g,(preto),Rect((p2+240,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+245,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(5322,500)        
                         gamb = False
                     if(oitava == 9):
                         mi = [pygame.draw.rect(g,(preto),Rect((p2+240,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+245,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(10644,500)        
                         gamb = False
                if(event.key==pygame.K_y):
                    if(oitava == 2):
                         fa = [pygame.draw.rect(g,(preto),Rect((p2+300,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+305,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(88,500)        
                         gamb = False
                    if(oitava == 3):
                         fa = [pygame.draw.rect(g,(preto),Rect((p2+300,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+305,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(176,500)        
                         gamb = False
                    if(oitava == 4):
                         fa = [pygame.draw.rect(g,(preto),Rect((p2+300,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+305,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(352,500)        
                         gamb = False
                    if(oitava == 5):
                         fa = [pygame.draw.rect(g,(preto),Rect((p2+300,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+305,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(705,500)        
                         gamb = False
                    if(oitava == 6):
                         fa = [pygame.draw.rect(g,(preto),Rect((p2+300,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+305,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(1410,500)        
                         gamb = False
                    if(oitava == 7):
                         fa = [pygame.draw.rect(g,(preto),Rect((p2+300,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+305,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(2819,500)        
                         gamb = False
                    if(oitava == 8):
                         fa = [pygame.draw.rect(g,(preto),Rect((p2+300,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+305,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(5639,500)        
                         gamb = False
                    if(oitava == 9):
                         fa = [pygame.draw.rect(g,(preto),Rect((p2+300,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+305,y+5),(40,90)))]
                         pygame.display.update()
                         winsound.Beep(11278,500)        
                         gamb = False
                if(event.key==pygame.K_u):
                    if(oitava==2):
                        fas = [pygame.draw.rect(g,(preto),Rect((p2+360,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+365,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(93,500)        
                        gamb = False
                    if(oitava==3):
                        fas = [pygame.draw.rect(g,(preto),Rect((p2+360,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+365,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(187,500)        
                        gamb = False
                    if(oitava==4):
                        fas = [pygame.draw.rect(g,(preto),Rect((p2+360,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+365,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(373,500)        
                        gamb = False
                    if(oitava==5):
                        fas = [pygame.draw.rect(g,(preto),Rect((p2+360,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+365,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(746,500)        
                        gamb = False
                    if(oitava==6):
                        fas = [pygame.draw.rect(g,(preto),Rect((p2+360,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+365,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(1493,500)        
                        gamb = False
                    if(oitava==7):
                        fas = [pygame.draw.rect(g,(preto),Rect((p2+360,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+365,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(2986,500)        
                        gamb = False
                    if(oitava==8):
                        fas = [pygame.draw.rect(g,(preto),Rect((p2+360,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+365,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(5973,500)        
                        gamb = False
                    if(oitava==9):
                        fas = [pygame.draw.rect(g,(preto),Rect((p2+360,y),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+365,y+5),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(11945,500)        
                        gamb = False
                if(event.key==pygame.K_a):
                    if(oitava==2):
                        sol = [pygame.draw.rect(g,(preto),Rect((p2+30,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((225,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(99,500)
                        gamb = False
                    if(oitava==3):
                        sol = [pygame.draw.rect(g,(preto),Rect((p2+30,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((225,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(198,500)
                        gamb = False
                    if(oitava==4):
                        sol = [pygame.draw.rect(g,(preto),Rect((p2+30,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((225,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(395,500)
                        gamb = False
                    if(oitava==5):
                        sol = [pygame.draw.rect(g,(preto),Rect((p2+30,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((225,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(791,500)
                        gamb = False
                    if(oitava==6):
                        sol = [pygame.draw.rect(g,(preto),Rect((p2+30,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((225,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(1582,500)
                        gamb = False
                    if(oitava==7):
                        sol = [pygame.draw.rect(g,(preto),Rect((p2+30,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((225,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(3164,500)
                        gamb = False
                    if(oitava==8):
                        sol = [pygame.draw.rect(g,(preto),Rect((p2+30,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((225,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(6328,500)
                        gamb = False
                    if(oitava==9):
                        sol = [pygame.draw.rect(g,(preto),Rect((p2+30,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((225,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(12655,500)
                        gamb = False
                if(event.key==pygame.K_s):
                    if(oitava==2):
                        sols = [pygame.draw.rect(g,(0,0,0),Rect((p2+90,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+95,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(105,500)
                        gamb = False
                    if(oitava==3):
                        sols = [pygame.draw.rect(g,(0,0,0),Rect((p2+90,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+95,y+165),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(209,500)
                        gamb = False
                    if(oitava==4):
                        sols = [pygame.draw.rect(g,(0,0,0),Rect((p2+90,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+95,y+165),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(419,500)
                        gamb = False
                    if(oitava==5):
                        sols = [pygame.draw.rect(g,(0,0,0),Rect((p2+90,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+95,y+165),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(838,500)
                        gamb = False
                    if(oitava==6):
                        sols = [pygame.draw.rect(g,(0,0,0),Rect((p2+90,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+95,y+165),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(1676,500)
                        gamb = False
                    if(oitava==7):
                        sols = [pygame.draw.rect(g,(0,0,0),Rect((p2+90,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+95,y+165),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(3352,500)
                        gamb = False
                    if(oitava==8):
                        sols = [pygame.draw.rect(g,(0,0,0),Rect((p2+90,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+95,y+165),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(6704,500)
                        gamb = False
                    if(oitava==9):
                        sols = [pygame.draw.rect(g,(0,0,0),Rect((p2+90,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+95,y+165),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(13407,500)
                        gamb = False
                if(event.key==pygame.K_d):
                    if(oitava==2):
                        la = [pygame.draw.rect(g,(preto),Rect((p2+150,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+155,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(111,500)
                        gamb = False
                    if(oitava==3):
                        la = [pygame.draw.rect(g,(preto),Rect((p2+150,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+155,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(222,500)
                        gamb = False
                    if(oitava==4):
                        la = [pygame.draw.rect(g,(preto),Rect((p2+150,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+155,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(444,500)
                        gamb = False
                    if(oitava==5):
                        la = [pygame.draw.rect(g,(preto),Rect((p2+150,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+155,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(888,500)
                        gamb = False
                    if(oitava==6):
                        la = [pygame.draw.rect(g,(preto),Rect((p2+150,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+155,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(1776,500)
                        gamb = False
                    if(oitava==7):
                        la = [pygame.draw.rect(g,(preto),Rect((p2+150,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+155,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(3552,500)
                        gamb = False
                    if(oitava==8):
                        la = [pygame.draw.rect(g,(preto),Rect((p2+150,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+155,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(7104,500)
                        gamb = False
                    if(oitava==9):
                        la = [pygame.draw.rect(g,(preto),Rect((p2+150,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+155,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(14210,500)
                        gamb = False
                if(event.key==pygame.K_f):
                    if(oitava==2):
                        las = [pygame.draw.rect(g,(preto),Rect((p2+210,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+215,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(118, 500)
                        gamb = False
                    if(oitava==3):
                        las = [pygame.draw.rect(g,(preto),Rect((p2+210,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+215,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(235, 500)
                        gamb = False
                    if(oitava==4):
                        las = [pygame.draw.rect(g,(preto),Rect((p2+210,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+215,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(470, 500)
                        gamb = False
                    if(oitava==5):
                        las = [pygame.draw.rect(g,(preto),Rect((p2+210,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+215,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(941, 500)
                        gamb = False
                    if(oitava==6):
                        las = [pygame.draw.rect(g,(preto),Rect((p2+210,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+215,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(1882, 500)
                        gamb = False
                    if(oitava==7):
                        las = [pygame.draw.rect(g,(preto),Rect((p2+210,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+215,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(3764, 500)
                        gamb = False
                    if(oitava==8):
                        las = [pygame.draw.rect(g,(preto),Rect((p2+210,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+215,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(7527, 500)
                        gamb = False
                    if(oitava==9):
                        las = [pygame.draw.rect(g,(preto),Rect((p2+210,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+215,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(15054, 500)
                        gamb = False
                if(event.key==pygame.K_g):        
                    if(oitava==2):          
                        si = [pygame.draw.rect(g,(preto),Rect((p2+270,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+275,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(125,500)
                        gamb = False
                    if(oitava==3):          
                        si = [pygame.draw.rect(g,(preto),Rect((p2+270,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+275,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(249,500)
                        gamb = False
                    if(oitava==4):          
                        si = [pygame.draw.rect(g,(preto),Rect((p2+270,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+275,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(498,500)
                        gamb = False
                    if(oitava==5):          
                        si = [pygame.draw.rect(g,(preto),Rect((p2+270,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+275,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(997,500)
                        gamb = False
                    if(oitava==6):          
                        si = [pygame.draw.rect(g,(preto),Rect((p2+270,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+275,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(1994,500)
                        gamb = False
                    if(oitava==7):          
                        si = [pygame.draw.rect(g,(preto),Rect((p2+270,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+275,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(3988,500)
                        gamb = False
                    if(oitava==8):          
                        si = [pygame.draw.rect(g,(preto),Rect((p2+270,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+275,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(7975,500)
                        gamb = False
                    if(oitava==9):          
                        si = [pygame.draw.rect(g,(preto),Rect((p2+270,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+275,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(15950,500)
                        gamb = False
                if(event.key==pygame.K_h):        
                    if(oitava==2):          
                        do_a = [pygame.draw.rect(g,(preto),Rect((p2+330,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+335,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(132,500)
                        gamb = False
                    if(oitava==3):          
                        do_a = [pygame.draw.rect(g,(preto),Rect((p2+330,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+335,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(264,500)
                        gamb = False
                    if(oitava==4):          
                        do_a = [pygame.draw.rect(g,(preto),Rect((p2+330,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+335,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(528,500)
                        gamb = False
                    if(oitava==5):          
                        do_a = [pygame.draw.rect(g,(preto),Rect((p2+330,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+335,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(1056,500)
                        gamb = False
                    if(oitava==6):          
                        do_a = [pygame.draw.rect(g,(preto),Rect((p2+330,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+335,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(2112,500)
                        gamb = False
                    if(oitava==7):          
                        do_a = [pygame.draw.rect(g,(preto),Rect((p2+330,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+335,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(4224,500)
                        gamb = False
                    if(oitava==8):          
                        do_a = [pygame.draw.rect(g,(preto),Rect((p2+330,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+335,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(8448,500)
                        gamb = False
                    if(oitava==9):          
                        do_a = [pygame.draw.rect(g,(preto),Rect((p2+330,y+155),(50,100))),pygame.draw.rect(g,(preto),Rect((p2+335,y+160),(40,90)))]
                        pygame.display.update()
                        winsound.Beep(16896,500)
                        gamb = False
                             
                if(event.key==pygame.K_o and oitava > 2 ):
                   g.blit(font_txt.render(i,1,preto),[0,0])
                   oitava= oitava - 1
                if(event.key==pygame.K_p and oitava < 9):
                   g.blit(font_txt.render(i,1,preto),[0,0])
                   oitava = oitava + 1

                   
                
                
