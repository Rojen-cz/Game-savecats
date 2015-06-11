from graphics import *
from button import *
import random
import time
import pygame
multilist = [[0 for col in range(6)] for row in range(6)]
list=["money.gif","heart.gif","swort.gif","magic.gif"]
lists=["moneys.gif","hearts.gif","sworts.gif","magics.gif"]
listcat=["cat1.gif","cat2.gif","cat3.gif","cat4.gif","cat5.gif","cat6.gif","cat7.gif","cat8.gif","cat9.gif","cat10.gif","cat11.gif","cat12.gif",]
listillcat=["badcat1.gif","badcat2.gif","badcat3.gif","badcat4.gif","badcat5.gif","badcat6.gif"]


def preinitialize(win):
    background1=Image(Point(225,300),"background1.gif")
    background1.draw(win)
    pygame.init()
    pygame.mixer.music.load("start.wav")
    pygame.mixer.music.play()
    while(1):
        q=win.getMouse()
        dx=q.getX()
        dy=q.getY()
        if (dx > 40 and dx < 130 and dy>230 and dy<260):
            background1.undraw()
            catnum=choosecat(win)
            return catnum
            break
        if (dx > 35 and dx < 130 and dy>275 and dy<315):
            background1.undraw()
            catnum=introduction(win)
            print "preinitialize",catnum
            background1=Image(Point(225,300),"background1.gif")
            background1.draw(win)
            return catnum
        if (dx > 35 and dx < 120 and dy>330 and dy<360):
            win.close()

def introduction(win):
    background2=Image(Point(225,300),"background2.gif")
    background2.draw(win)
    while(1):
        q=win.getMouse()
        dx=q.getX()
        dy=q.getY()
        if (dx > 170 and dx < 260 and dy>540 and dy<560):
            background2.undraw()
            break
        if (dx > 100 and dx < 360 and dy>500 and dy<520):
            background2.undraw()
            catnum=choosecat(win)
            return catnum
            print "introduction",catnum
            break

def choosecat(win):
    background3=Image(Point(225,300),"background3.gif")
    background3.draw(win)
    witch=Image(Point(80,465),"catwitch.gif")
    witch.draw(win)
    a=catshow(0,win)
    catnum=1
    fight=Text(Point(225,240),"Fighting?Point the start opinion above.")
    fight.setSize(16)
    flag=0
    while(1):
        p=win.getMouse()
        dx=p.getX()
        dy=p.getY()
        if(dx>378 and dx<440 and dy>115 and dy<215 and a<10):
            a=catshow(a,win)
            fight.undraw()
            flag=0
        if(dx>20 and dx<75 and dy>115 and dy<215 and a>2):
            if (a>5):
                a=catshow(a-6,win)
                fight.undraw()
                flag=0
            else:
                a=catshow(0,win)
                fight.undraw()
                flag=0
        if(dx>78 and dx<178 and dy>115 and dy<215):
            if (flag==1):
                fight.setText("Choose another cat?ok,Point the start opinion above.")
            if (flag==0):
                catnum = a-2
                fight.draw(win)
                print "ok"
                flag=1
        if(dx>178 and dx<278 and dy>115 and dy<215) :
            if (flag==1):
                fight.setText("Choose another cat?ok,Point the start opinion above.")
            if (flag==0):
                catnum = a-1
                fight.draw(win)
                flag=1
                print "ok"
        if(dx>278 and dx<378 and dy>115 and dy<215):
            if (flag==1):
                fight.setText("Choose another cat?ok,Point the start opinion above.")
            if (flag==0):
                catnum= a
                fight.draw(win)
                flag=1
                print "ok"
        if(dx>170 and dx<275 and dy>30 and dy<70):
            illustation(win)
            return catnum
            break


def catshow(a,win):
    location=0
    for a in range(a,a+3):
        cat=Image(Point(128+location*100,165),listcat[a])
        cat.draw(win)
        location=location+1
        a=a+1
    return a

def illustation(win):
    background5=Image(Point(225,300),"background5.gif")
    background5.draw(win)
    #b1=Rectangle(Point(326,505),Point(420,536))
    #b1.draw(win)
    while(1):
        p=win.getMouse()
        dx=p.getX()
        dy=p.getY()
        if(dx>326 and dx<420 and dy>505 and dy<536):
            break

def initialize(win):
    Image(Point(225,300),"background.gif").draw(win)
    for a in range(0,6):
        for b in range (0,6):
            num=random.randint(0, 3)
            multilist[a][b] = cube(win, 37.5+75*a, 100+37.5+75*b, list[num], num)
    linetop=Line(Point(0,100),Point(450,100))
    linebottom=Line(Point(0,550),Point(450,550))
    linetop.draw(win)
    linebottom.draw(win)
    line1=Line(Point(155,0),Point(155,100))
    line2=Line(Point(280,0),Point(280,100))
    line1.draw(win)
    line2.draw(win)
    PlHp=Text(Point(115,20), "Hp:")
    PlHp.setSize(16)
    Plle=Text(Point(123,50),"Level:")
    Plle.setSize(16)
    PlHp.draw(win)
    Plle.draw(win)
    MoHp=Text(Point(300,20), "Hp:")
    MoHp.setSize(16)
    MoHp.draw(win)
    Round=Text(Point(210,30),"Round:")
    Round.setSize(24)
    Round.draw(win)
    cButton = Button(win,Point(50,580),100,40,"Cancel")
    cButton.label.setSize(20)
    aButton = Button(win,Point(400,580),100,40,"Assure")
    aButton.label.setSize(20)
    rButton = Button(win,Point(225,580),100,40,"Regret")
    rButton.label.setSize(20)
    hButton = Button(win,Point(217,87),100,22,"Strong Hit!")
    hButton.label.setSize(16)
    cButton.activate()
    return cButton, aButton, rButton,hButton

def changingboard(win,player1,monster1):
    hp=Text(Point(138,20),str(player1.hp))
    hp.setSize(16)
    hp.draw(win)
    lev=Text(Point(147,50),str(player1.level))
    lev.setSize(16)
    lev.draw(win)
    monsterhp=Text(Point(325,20),str(monster1.hp))
    monsterhp.setSize(16)
    monsterhp.draw(win)
    r=1
    Rou=Text(Point(255,30),str(r))
    Rou.setSize(24)
    Rou.draw(win)
    Moneyshow=Text(Point(220,60),"Miao~:"+str(player1.money))
    Moneyshow.setSize(20)
    Moneyshow.draw(win)
    return hp,lev,monsterhp,Rou,r,Moneyshow

def endboard(win):
    endstory1=Text(Point(220,100),"You Win!Little cats return to a happy life~")
    endstory2=Text(Point(220,150),"However......dinginginging-----(Ring bell)")
    endstory3=Text(Point(220,200),"You waked up and found it was only a dream..")
    endstory4=Text(Point(220,250),"You run to the housetop to find those cat-friends..")
    endstory5=Text(Point(220,300),"But..no one..")
    endstory6=Text(Point(220,350),"After a long time, you smiled and feel relieved")
    endstory7=Text(Point(220,400),"Because they all lived in your memory.")
    endstory8=Text(Point(220,470),"FOREVER.")
    endstory1.setSize(16)
    endstory2.setSize(16)
    endstory3.setSize(16)
    endstory4.setSize(16)
    endstory5.setSize(16)
    endstory6.setSize(16)
    endstory7.setSize(16)
    endstory8.setSize(24)
    endstory1.setTextColor(color_rgb(255,255,255))
    endstory2.setTextColor(color_rgb(255,255,255))
    endstory3.setTextColor(color_rgb(255,255,255))
    endstory4.setTextColor(color_rgb(255,255,255))
    endstory5.setTextColor(color_rgb(255,255,255))
    endstory6.setTextColor(color_rgb(255,255,255))
    endstory7.setTextColor(color_rgb(255,255,255))
    endstory8.setTextColor(color_rgb(255,255,255))
    background4=Image(Point(450,300),"background4.gif")
    background4.draw(win)
    pygame.mixer.music.fadeout(1000)
    pygame.init()
    pygame.mixer.music.load("end.wav")
    pygame.mixer.music.play()
    for a in range(0,95):
        background4.move(-a/10,0)
        time.sleep(0.05)
        if(a==1):
            endstory1.draw(win)
            endstory2.draw(win)
            endstory3.draw(win)
            endstory4.draw(win)
            endstory5.draw(win)
            endstory6.draw(win)
            endstory7.draw(win)
            endstory8.draw(win)
    time.sleep(5)
    endstory1.undraw()
    endstory2.undraw()
    endstory3.undraw()
    endstory4.undraw()
    endstory5.undraw()
    endstory6.undraw()
    endstory7.undraw()
    endstory8.undraw()
    endstory9=Text(Point(220,380),"CLICK TO CLOSE.")
    endstory9.setSize(18)
    endstory9.setTextColor(color_rgb(255,255,255))
    endstory9.draw(win)
    endstory10=Text(Point(220,280),"<THE END>")
    endstory10.setSize(28)
    endstory10.setTextColor(color_rgb(255,255,255))
    endstory10.draw(win)
    win.getMouse()
    pygame.mixer.music.fadeout(2000)

def falldown(win):
    for a in range(0,6):
        for b in range(0,6):
            tempa=a
            tempb=b
            if (multilist[tempa][tempb]!= None and multilist[tempa][tempb].c<0):
                multilist[tempa][tempb].f.undraw()
                multilist[tempa][tempb] = None
                recordtempb=tempb
                while(tempb>0 and multilist[tempa][tempb-1]!=None):
                    multilist[tempa][tempb]=multilist[tempa][tempb-1]
                    multilist[tempa][tempb].fall(1)
                    print "falldown:"
                    print tempa,tempb
                    multilist[tempa][tempb-1] = None
                    print "none1:", tempa, tempb-1
                    tempb=tempb-1
    for a in range(0,6):
        for b in range(0,6):
            if(multilist[a][b]==None):
                num=random.randint(0, 3)
                print "empty:"
                print a,b
                multilist[a][b] = cube(win, 37.5+75*a, 100+37.5+75*b, list[num], num)


class cube:
    def __init__(self,wVal,xVal,yVal,filename,num):
        self.w = wVal
        self.x = xVal
        self.y = yVal
        self.f = Image(Point(self.x,self.y),filename)
        self.c = num
        self.f.draw(self.w)
    def fall(self,n):
        self.f.move(0,75*n)

class player:
    def __init__(self,hp,level,money,image,win):
        self.hp=hp
        self.level=level
        self.money=money
        self.recordhp=hp
        self.image=Image(Point(50,50),listcat[image])
        self.image.draw(win)
    def attack(self,num,count,monster):
        if (num==0):
            self.money=self.money+count
        if (num==1):
            if(self.recordhp>self.hp+count*10):
                self.hp=self.hp+count*10
            else:
                self.hp=self.recordhp
        if (num==2):
            monster.hp=monster.hp-count*10
        if (num==3):
            monster.hp=monster.hp-count*4
            if(self.recordhp>self.hp+count*10):
                self.hp=self.hp+count*3
            else:
                self.hp=self.recordhp

class monster:
    def __init__(self,hp,level,image,win):
        self.hp=hp
        self.level=level
        self.image=Image(Point(400,50),listillcat[image])
        self.image.draw(win)
    def attack(self,playerhp,level,hp):
        if(hp>10):
            playerhp=playerhp-level*5
        else:
            playerhp=playerhp-level*10
        return playerhp

def checkmonster(win,monster1,player1,monsterhp,temphp,templevel,illcatnum,lev,hp,r,Rou):
    if(monster1.hp>0):
        player1.hp=monster1.attack(player1.hp,monster1.level,monster1.hp)
        monsterhp.setText(str(monster1.hp))
    else:
        monster1.hp=temphp+5*templevel
        monster1.level=templevel+1
        monsterhp.setText(str(monster1.hp))
        illcatnum=illcatnum+1

        if(illcatnum<6):
            monster1.image.undraw()
            monster1.image=Image(Point(400,50),listillcat[illcatnum])
            monster1.image.draw(win)
            temphp=monster1.hp
            templevel=monster1.level
            player1.level=player1.level+1
            lev.setText(str(player1.level))
            player1.hp = player1.level*10 + player1.recordhp
            player1.recordhp=player1.hp
            hp.setText(str(player1.hp))
            r=r+1
            Rou.setText(str(r))
    return monster1,player1,monsterhp,temphp,templevel,illcatnum,lev,hp,r,Rou

def main():
    win=GraphWin("Save Cat-Country",450,600)
    catnum=preinitialize(win)
    catnum=catnum-1
    cButton, aButton,rButton,hButton = initialize(win)
    illcatnum=0
    player1=player(50,1,1,catnum,win)
    monster1=monster(80,1,illcatnum,win)
    temphp=monster1.hp
    templevel=monster1.level
    flag=5
    count=0
    hp,lev,monsterhp,Rou,r,Moneyshow = changingboard(win,player1,monster1)
    pygame.mixer.music.fadeout(1000)
    pygame.init()
    pygame.mixer.music.load("middle.wav")
    pygame.mixer.music.play()
    while(1):
        p=win.getMouse()
        dx=p.getX()
        dy=p.getY()
        xa=int(round((dx-37.5)/75))
        yb=int(round((dy-137.5)/75))
        if(xa<6 and xa>=0 and yb<6 and yb>=0):
            num=multilist[xa][yb].c
            if((flag==num)and(xa>exxa-2 and xa<exxa+2)and(yb>exyb-2 and yb<exyb+2)):
                multilist[xa][yb].f.undraw()
                multilist[xa][yb] = cube(win, 37.5+75*xa, 100+37.5+75*yb, lists[num], num-4)
                exxa,exyb=xa,yb
                count=count+1
            if (flag==5):
                multilist[xa][yb].f.undraw()
                multilist[xa][yb] = cube(win, 37.5+75*xa, 100+37.5+75*yb, lists[num], num-4)
                flag=num
                exxa,exyb=xa,yb
                count=count+1
            if (count>=3):
                aButton.activate()
            if (count>=1):
                rButton.activate()
        if hButton.clicked(p):
            monster1.hp=monster1.hp-100
            monsterhp.setText(str(monster1.hp))
            monster1,player1,monsterhp,temphp,templevel,illcatnum,lev,hp,r,Rou=checkmonster(win,monster1,player1,monsterhp,temphp,templevel,illcatnum,lev,hp,r,Rou)
            hButton.deactivate()
            player1.money=player1.money-10
            Moneyshow.setText("Miao~:"+str(player1.money))
        if aButton.clicked(p):
            player1.attack(num,count,monster1)
            monster1,player1,monsterhp,temphp,templevel,illcatnum,lev,hp,r,Rou=checkmonster(win,monster1,player1,monsterhp,temphp,templevel,illcatnum,lev,hp,r,Rou)
            if(player1.hp>0):
                hp.setText(str(player1.hp))
                Moneyshow.setText("Miao~::"+str(player1.money))
                if(player1.money>=10):
                    hButton.activate()
            else:
                for a in range(0,6):
                    for b in range (0,6):
                        multilist[a][b].f.undraw()
                hint=Text(Point(225,300),"YOU LOSE!")
                hint.setSize(24)
                hint.draw(win)
                hp.setText(str(player1.hp))
                aButton.deactivate()
                rButton.deactivate()
                win.getMouse()
                break
            exxa,exyb,count,flag=0,0,0,5
            rButton.deactivate()
            falldown(win)
        if (illcatnum==6):
            endboard(win)
            break
        if(count==0):
            aButton.deactivate()
        if rButton.clicked(p):
            for a in range(0,6):
                for b in range (0,6):
                    if(multilist[a][b].c<0):
                        multilist[a][b].f.undraw()
                        num=multilist[a][b].c+4
                        multilist[a][b] = cube(win, 37.5+75*a, 100+37.5+75*b, list[num], num)
            exxa,exyb,count,flag=0,0,0,5
        if cButton.clicked(p):
            win.close()
main()
