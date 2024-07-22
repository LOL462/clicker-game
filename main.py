import time as timer
from pygame import*
import subprocess
window = display.set_mode((500,500))
bg = (0, 30, 163)
clock = time.Clock()
score = 0
game = True

with open("timer.txt","r") as file:
    timeadd = file.read()

class Coockie():
    def __init__(self,img,x,y,width,hight): 
        self.img = transform.scale(image.load(img),(width,hight))
        self.orriginalimg = self.img.copy()
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.hight = hight
        self.clickedtime  = None
    def drawer(self,window):
        window.blit(self.img,(self.rect.x,self.rect.y))
    def click(self,x,y):
        return self.rect.collidepoint(x,y)
    def checklickandresice(self,x,y):
        if self.click(x,y):
            self.img = transform.scale(self.orriginalimg,(self.width/2,self.hight/2))
            self.rect = self.img.get_rect(center = self.rect.center)
            self.clickedtime = time.get_ticks()
            global score
            score += 1
    def updatecoockie(self):
        if self.clickedtime is not None:
            if time.get_ticks() - self.clickedtime > 75:
                self.img = self.orriginalimg
                self.rect = self.img.get_rect(center = self.rect.center)
                self.clickedtime = None
coockie = Coockie("coockieremovebg.png",150,150,200,200)
font.init()
myfont = font.Font(None,40)
finish = False
gametime = 10
starttime = timer.time()
currenttime = starttime
ttext = myfont.render("time:" + str(gametime),True,(255,255,255))

level = 1
points = 10
lose = myfont.render("You lose",True,(234, 21, 21))




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
        if e.type == MOUSEBUTTONDOWN:
            x,y = e.pos
            coockie.checklickandresice(x,y)
    if not finish:
        window.fill(bg)
        coockie.updatecoockie()
        coockie.drawer(window)
        scoretext = myfont.render(str(score),True,(255,255,255))
        new_time = timer.time()
        if int(new_time) - int(currenttime) == 1: 
            ttext = myfont.render("Time: " + str(int(gametime -(new_time - starttime))), True, (255,255,255))
            currenttime = new_time
        if score >= points and new_time - starttime <= gametime :
            level += 1
            points += 5 
            gametime *= float(timeadd) 
            score = 0 
        if new_time - starttime >= gametime:
            finish = True
            window.blit(lose,(200,180))
            with open("lvl.txt","w") as file:
                file.write(str(level))
            display.update()
            time.wait(2500)
            subprocess.Popen(["python","menu.py"])
            quit()
        goal = myfont.render("Goal:"+str(points),True,(255, 255, 255))
        window.blit(goal,(200,20))

        window.blit(ttext,(20,10))
        window.blit(scoretext,(450,5))
        lvltext = myfont.render("Level:"+str(level),True,(255,255,255))
        window.blit(lvltext,(20,50))
    display.update()
    clock.tick(45)



