import turtle
import re

archivo=open('ebayWiki.txt','a+')

def Graficar():
    turtle.setup(800, 600)      # set the window size to 800 by 600 pixels
    wn = turtle.Screen()        # set wn to the window object
    wn.bgcolor("lightpink")    # set the window background color
    wn.title("Automata web ebay")    # set the window title

    l=turtle.Turtle()
    l.hideturtle()
    l.penup()
    l.goto(50,270)
    l.write("START",font=('Cambria',20,'bold'))
    f0=turtle.Turtle()######################
    f0.color("lightpink")
    f0.pensize(5)
    f0.penup()
    f0.left(90)
    f0.forward(275)
    f0.right(90)
    f0.forward(85)
    f0.right(150)
    f0.pendown()
    f0.color("darkslateblue")
    f0.forward(55)
    tess = turtle.Turtle()#####################
    tess.color("lightpink")         
    tess.pensize(4)             
    tess.left(90)
    tess.speed(20)
    tess.hideturtle()
    tess.penup()
    tess.forward(190)
    tess.color("white") 
    tess.right(90)
    tess.pendown()
    for i in range (36):
        tess.left(10)
        tess.forward(7)
    l0=turtle.Turtle()
    l0.hideturtle()
    l0.penup()
    l0.goto(-14,217)
    l0.write("q0",font=('Cambria',20,'bold'))
    f1=turtle.Turtle()######################
    f1.color("lightpink")
    f1.pensize(4)
    f1.penup()
    f1.left(90)
    f1.forward(225)
    f1.left(90)
    f1.forward(43)
    f1.left(38)
    f1.pendown()
    f1.color("darkslateblue")
    f1.forward(95)
    l1=turtle.Turtle()#######################
    l1.hideturtle()
    l1.penup()
    l1.goto(-80,200)
    l1.write("w",font=('Cambria',12,'bold'))
    tess1 = turtle.Turtle()####################
    tess1.color("lightpink")
    tess1.pensize(4)
    tess1.speed(40)
    tess1.left(150)#right210
    tess1.hideturtle()
    tess1.penup()
    tess1.forward(190)
    tess1.pendown()
    tess1.speed(20)
    tess1.color("white")
    for i in range (36):
        tess1.right(10)
        tess1.forward(7)
    l1.goto(-150,120)####################
    l1.write("q1",font=('Cambria',20,'bold'))
    f2=turtle.Turtle()######################
    f2.color("lightpink")
    f2.pensize(4)
    f2.penup()
    f2.left(149)
    f2.forward(175)
    f2.left(121)
    f2.pendown()
    f2.color("darkslateblue")
    f2.forward(38)
    l1.goto(-165,65)####################
    l1.write("e",font=('Cambria',12,'bold'))
    tess2 = turtle.Turtle()####################
    tess2.hideturtle()
    tess2.color("lightpink")
    tess2.pensize(4)
    tess2.speed(40)
    tess2.right(168)
    tess2.penup()
    tess2.forward(142)
    tess2.pendown()
    tess2.speed(20)
    tess2.color("white")
    for i in range (36):
        tess2.right(10)
        tess2.forward(7)
    l1.goto(-150,0)####################
    l1.write("q2",font=('Cambria',20,'bold'))
    f3=turtle.Turtle()######################
    f3.color("lightpink")
    f3.pensize(4)
    f3.penup()
    f3.right(168)
    f3.forward(155)
    f3.left(78)
    f3.pendown()
    f3.color("darkslateblue")
    f3.forward(25)
    l1.goto(-165,-55)####################
    l1.write("b",font=('Cambria',12,'bold'))
    tess3 = turtle.Turtle()####################
    tess3.color("lightpink")
    tess3.speed(40)
    tess3.pensize(4)
    tess3.right(132)
    tess3.hideturtle()
    tess3.penup()
    tess3.forward(172)
    tess3.pendown()
    tess3.speed(20)
    tess3.color("white")
    for i in range (36):
        tess3.right(10)
        tess3.forward(7)
    tess3.color("lightpink")
    tess3.pensize(3)
    tess3.hideturtle()
    tess3.penup()
    tess3.right(90)
    tess3.forward(12)
    tess3.left(90)
    tess3.pendown()
    tess3.color("white")
    for i in range (36):
        tess3.right(10)
        tess3.forward(5)
    l1.goto(-155,-110)####################
    l1.write("q3",font=('Cambria',20,'bold'))
    f4=turtle.Turtle()######################
    f4.color("lightpink")
    f4.pensize(4)
    f4.penup()
    f4.left(90)
    f4.forward(225)
    f4.right(90)
    f4.forward(43)
    f4.right(38)
    f4.pendown()
    f4.color("darkslateblue")
    f4.forward(95)
    l1.goto(80,200)
    l1.write("e",font=('Cambria',12,'bold'))
    tess4 = turtle.Turtle()####################
    tess4.color("lightpink")
    tess4.pensize(4)
    tess4.left(30)
    tess4.speed(20)
    tess4.hideturtle()
    tess4.penup()
    tess4.forward(190)
    tess4.pendown()
    tess4.color("white")
    for i in range (36):
        tess4.left(10)
        tess4.forward(7)
    l1.goto(130,120)####################
    l1.write("q4",font=('Cambria',20,'bold'))
    f5=turtle.Turtle()######################
    f5.color("lightpink")
    f5.pensize(4)
    f5.penup()
    f5.left(31)
    f5.forward(175)
    f5.right(121)
    f5.pendown()
    f5.color("darkslateblue")
    f5.forward(38)
    l1.goto(155,57)
    l1.write("b",font=('Cambria',12,'bold'))
    tess5 = turtle.Turtle()####################
    tess5.color("lightpink")
    tess5.pensize(4)
    tess5.right(12)
    tess5.speed(20)
    tess5.hideturtle()
    tess5.penup()
    tess5.forward(142)
    tess5.pendown()
    tess5.color("white")
    for i in range (36):
        tess5.left(10)
        tess5.forward(7)
    l1.goto(130,0)####################
    l1.write("q5",font=('Cambria',20,'bold'))
    f6=turtle.Turtle()######################
    f6.color("lightpink")
    f6.pensize(4)
    f6.penup()
    f6.right(12)
    f6.forward(155)
    f6.right(78)
    f6.pendown()
    f6.color("darkslateblue")
    f6.forward(25)
    l1.goto(155,-50)
    l1.write("a",font=('Cambria',12,'bold'))
    tess6 = turtle.Turtle()####################
    tess6.color("lightpink")
    tess6.pensize(4)
    tess6.right(48)
    tess6.speed(20)
    tess6.hideturtle()
    tess6.penup()
    tess6.forward(172)
    tess6.pendown()
    tess6.color("white")
    for i in range (36):
        tess6.left(10)
        tess6.forward(7)
    l1.goto(130,-110)####################
    l1.write("q6",font=('Cambria',20,'bold'))
    f7=turtle.Turtle()######################
    f7.color("lightpink")
    f7.pensize(4)
    f7.penup()
    f7.right(42.5)
    f7.forward(208)
    f7.right(47.5)
    f7.pendown()
    f7.color("darkslateblue")
    f7.forward(30)
    l1.goto(155,-160)
    l1.write("y",font=('Cambria',12,'bold'))
    tess7 = turtle.Turtle()####################
    tess7.color("lightpink")
    tess7.pensize(4)
    tess7.right(65)
    tess7.speed(20)
    tess7.hideturtle()
    tess7.penup()
    tess7.forward(260)
    tess7.pendown()
    tess7.color("white")
    for i in range (36):
        tess7.left(10)
        tess7.forward(7)
    tess7.color("lightpink")
    tess7.pensize(3)
    tess7.hideturtle()
    tess7.penup()
    tess7.left(90)
    tess7.forward(12)
    tess7.right(90)
    tess7.pendown()
    tess7.color("white")
    for i in range (36):
        tess7.left(10)
        tess7.forward(5)
    l1.goto(130,-233)####################
    l1.write("q7",font=('Cambria',20,'bold'))

    f8=turtle.Turtle()######################
    f8.color("lightpink")
    f8.pensize(4)
    f8.penup()
    f8.right(180)
    f8.forward(110)
    f8.right(90)
    f8.forward(150)
    f8.right(53)
    f8.pendown()
    f8.color("darkorchid")
    f8.forward(90)
    l1.goto(-70,160)
    l1.write("no w,e",font=('Cambria',12,'bold'))
    f10=turtle.Turtle()######################
    f10.color("lightpink")
    f10.pensize(4)
    f10.penup()
    f10.left(159)
    f10.forward(139)
    f10.right(69)
    f10.pendown()
    f10.color("darkorchid")
    f10.forward(35)
    l1.goto(-127,57)
    l1.write("w",font=('Cambria',12,'bold'))
    f11=turtle.Turtle()######################
    f11.color("lightpink")
    f11.pensize(4)
    f11.penup()
    f11.forward(108)
    f11.left(90)
    f11.forward(155)
    f11.left(53)
    f11.pendown()
    f11.color("darkorchid")
    f11.forward(93)
    l1.goto(20,165)
    l1.write("no w,e,b",font=('Cambria',12,'bold'))
    f12=turtle.Turtle()######################
    f12.color("lightpink")
    f12.pensize(4)
    f12.penup()
    f12.right(24)
    f12.forward(139)
    f12.left(170)
    f12.pendown()
    f12.color("gray")
    f12.forward(280)
    l1.goto(120,55)
    l1.write("e",font=('Cambria',12,'bold'))
    f13=turtle.Turtle()######################
    f13.color("lightpink")
    f13.pensize(4)
    f13.penup()
    f13.left(20)
    f13.forward(140)
    f13.left(70)
    f13.pendown()
    f13.color("springgreen")
    f13.forward(35)
    f14=turtle.Turtle()######################
    f14.color("lightpink")
    f14.pensize(4)
    f14.penup()
    f14.right(22)
    f14.forward(170)
    f14.left(80)
    f14.pendown()
    f14.color("springgreen")
    f14.forward(100)
    f14.left(60)
    f14.forward(90)
    l1.goto(215,0)####################
    l1.write("e",font=('Cambria',12,'bold'))
    l1.goto(237,0)####################
    l1.write("e",font=('Cambria',12,'bold'))
    f15=turtle.Turtle()######################
    f15.color("lightpink")
    f15.pensize(4)
    f15.penup()
    f15.right(47)
    f15.forward(245)
    f15.left(110)
    f15.pendown()
    f15.color("springgreen")
    f15.forward(200)
    f15.left(60)
    f15.forward(140)
    f16=turtle.Turtle()######################
    f16.color("lightpink")
    f16.pensize(4)
    f16.penup()
    f16.right(50)
    f16.forward(290)
    f16.left(105)
    f16.pendown()
    f16.color("orangered")
    f16.forward(330)
    f16.left(70)
    f16.forward(180)
    f16.left(44)
    f16.forward(240)
    f17=turtle.Turtle()######################
    f17.color("lightpink")
    f17.pensize(4)
    f17.penup()
    f17.right(30)
    f17.forward(210)
    f17.left(80)
    f17.pendown()
    f17.color("orangered")
    f17.forward(200)
    f17.left(80)
    f17.forward(180)
    f17.left(34)
    f17.forward(160)
    l1.goto(255,25)####################
    l1.write("no w,e,y",font=('Cambria',12,'bold'))
    l1.goto(317,55)####################
    l1.write("no w,e",font=('Cambria',12,'bold'))
    f18=turtle.Turtle()######################
    f18.color("lightpink")
    f18.pensize(4)
    f18.penup()
    f18.left(20)
    f18.forward(115)
    f18.left(122)
    f18.pendown()
    f18.color("orangered")
    f18.forward(110)
    f18.right(30)
    f18.forward(91)
    f19=turtle.Turtle()######################
    f19.color("lightpink")
    f19.pensize(4)
    f19.penup()
    f19.left(20)
    f19.forward(115)
    f19.left(137)
    f19.pendown()
    f19.color("gray")
    f19.forward(230)
    f20=turtle.Turtle()######################
    f20.color("lightpink")
    f20.pensize(4)
    f20.penup()
    f20.left(50)
    f20.forward(160)
    f20.left(127)
    f20.pendown()
    f20.color("gray")
    f20.forward(205)
    f21=turtle.Turtle()######################
    f21.color("lightpink")
    f21.pensize(4)
    f21.penup()
    f21.right(60)
    f21.forward(215)
    f21.right(172.5)
    f21.pendown()
    f21.color("gray")
    f21.forward(360)
    l1.goto(-100,105)####################
    l1.write("w",font=('Cambria',12,'bold'))
    f22=turtle.Turtle()######################
    f22.color("lightpink")
    f22.pensize(4)
    f22.penup()
    f22.right(140)
    f22.forward(135)
    f22.right(160)
    f22.pendown()
    f22.color("gray")
    f22.forward(100)
    f22.left(60)
    f22.forward(115)
    f23=turtle.Turtle()######################
    f23.color("lightpink")
    f23.pensize(4)
    f23.penup()
    f23.right(140)
    f23.forward(135)
    f23.right(180)
    f23.pendown()
    f23.color("springgreen")
    f23.forward(280)
    f24=turtle.Turtle()######################
    f24.color("lightpink")
    f24.pensize(4)
    f24.penup()
    f24.right(180)
    f24.forward(100)
    f24.right(155)
    f24.pendown()
    f24.color("springgreen")
    f24.forward(235)
    l1.goto(0,105)####################
    l1.write("no w,e,a",font=('Cambria',12,'bold'))
    l1.goto(90,88)####################
    l1.write("e",font=('Cambria',12,'bold'))
    f25=turtle.Turtle()######################
    f25.color("lightpink")
    f25.pensize(4)
    f25.penup()
    f25.right(140)
    f25.forward(135)
    f25.left(140)
    f25.pendown()
    f25.color("red")
    f25.forward(210)
    l1.goto(0,-100)####################
    l1.write("a",font=('Cambria',12,'bold'))
    f26=turtle.Turtle()######################
    f26.color("lightpink")
    f26.pensize(4)
    f26.penup()
    f26.right(150)
    f26.forward(210)
    f26.right(90)
    f26.pendown()
    f26.color("orangered")
    f26.forward(210)
    f26.right(60)
    f26.forward(210)
    f26.right(60)
    f26.forward(150)
    f27=turtle.Turtle()######################
    f27.color("lightpink")
    f27.pensize(4)
    f27.penup()
    f27.right(180)
    f27.forward(181)
    f27.right(60)
    f27.pendown()
    f27.color("orangered")
    f27.forward(100)
    f27.right(60)
    f27.forward(170)
    f27.right(60)
    f27.forward(105)
    l1.goto(-295,60)####################
    l1.write("no w,e,a",font=('Cambria',12,'bold'))
    l1.goto(-240,40)####################
    l1.write("no w,e,b",font=('Cambria',12,'bold'))
    f28=turtle.Turtle()######################
    f28.color("lightpink")
    f28.pensize(3)
    f28.penup()
    f28.left(90)
    f28.forward(255)
    f28.right(90)
    f28.forward(30)
    f28.pendown()
    f28.color("royalblue")
    f28.left(45)
    for i in range(19):
        f28.left(11)
        f28.forward(4)
    f29=turtle.Turtle()######################
    f29.color("lightpink")
    f29.pensize(3)
    f29.penup()
    f29.left(130)
    f29.forward(225)
    f29.right(40)
    f29.pendown()
    f29.color("royalblue")
    for i in range(21):
        f29.left(11)
        f29.forward(4)

    f30=turtle.Turtle()######################
    f30.color("lightpink")
    f30.pensize(3.5)
    f30.penup()
    f30.left(40)
    f30.forward(233)
    f30.pendown()
    f30.color("royalblue")
    for i in range(19):
        f30.left(11)
        f30.forward(4)
    l1.goto(-50,272)####################
    l1.write("no w,e",font=('Cambria',12,'bold'))
    l1.goto(-200,170)####################
    l1.write("w",font=('Cambria',12,'bold'))
    l1.goto(190,170)####################
    l1.write("e",font=('Cambria',12,'bold'))

    wn.exitonclick()

#########################################################################################################################################################
opcion=6#un valor cualquiera para que se inicialice
while(opcion!=0):
    opcion=int(input("1 para manual, 2 para automatico, 3 para ver el grafico, 0 para salir: "))
    if(opcion==1):
        estado=0
        columna=0
        cad=""
        algo=False
        algo2=False
        cadenita=input("Introduzca la palabra: ")
        f=open('WEBAY.txt','a+')
        f.write("\n\nMODO MANUAL: "+cadenita)
        for i in cadenita:#el estado se inicializa en 0
            columna=columna+1
            #if(re.search(i,"aáäàbcdeéèëfghiíìïjklmnñoóòöpqrstuúùüvwxyzAÁÀÄBCDÉÈËEFGHÍÌÏIJKLMNÑÓÒÖOPKRSTÚÙÜUWXYZ")):
            #intente tambien chr() y un range... crh() es para devolver el char de cierto numero ej: chr(97) es a
            if(i=='a'or i=='á'or i=='ä'or i=='à'or i=='b'or i=='c'or i=='d'or  i=='e' or i=='é'or i=='è'or i=='ë'or i=='f'or i=='g' or i=='h'or i=='i'or i=='í'or i=='ì'or i=='ï'or i=='j'or i=='k'or i=='l'or i=='m'or i=='n'or i=='ñ'or i=='o'or i=='ó'or i=='ò'or i=='ö'or i=='p'or i=='q'or i=='r'or i=='s' or  i=='t'or i=='u'or i=='ú'or i=='ù'or i=='ü'or i=='v'or i=='w'or i=='x'or i=='y'or i=='z'or i=='A'or i=='Á'or i=='À'or i=='Ä'or i=='B'or i=='C'or i=='D'or i=='É'or i=='È'or i=='Ë'or i=='E'or i=='F'or i=='G'or i=='H'or i=='Í'or i=='Ì'or i=='Ï'or i=='I'or i=='J'or i=='K'or i=='L'or i=='M'or i=='N'or i=='Ñ'or i=='Ó'or i=='Ò'or i=='Ö'or i=='O'or i=='P'or i=='K'or i=='R'or i=='S'or i=='T'or i=='Ú'or i=='Ù'or i=='Ü'or i=='U'or i=='W'or i=='X'or i=='Y'or i=='Z'):
                cad=cad+i
                if(estado==0):
                    if(i=='w' or i=='W'):
                        estado=1
                    elif(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                        estado=4
                    else:
                        estado=0
                    print("q"+str(estado)+" - "+i)
                    f.write("\nq"+str(estado)+" - "+i)
                elif(estado==1):
                    if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                        estado=2
                    elif(i=='w' or i=='W'):
                        estado=1
                    else:
                        estado=0
                    print("q"+str(estado)+" - "+i)
                    f.write("\nq"+str(estado)+" - "+i)
                elif(estado==2):
                    if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                        estado=4
                        print("q"+str(estado)+" - "+i)
                        f.write("\nq"+str(estado)+" - "+i)
                    elif(i=='b' or i=='B'):
                        estado=3#################
                        algo=True
                        print("q"+str(estado)+" - "+i+"  en la columna "+str(columna))
                        f.write("\nq"+str(estado)+" - "+i+"  en la columna "+str(columna))
                    elif(i=='w' or i=='W'):
                        estado=1
                        print("q"+str(estado)+" - "+i)
                        f.write("\nq"+str(estado)+" - "+i)
                    else:
                        estado=0
                        print("q"+str(estado)+" - "+i)
                        f.write("\nq"+str(estado)+" - "+i)
                elif(estado==3):
                    if(i=='w' or i=='W'):
                        estado=1
                    elif(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                        estado=4
                    elif(i=='a' or i=='á' or i=='à' or i=='ä' or i=='Á' or i=='A' or i=='À' or i=='Ä'):
                        estado=6           
                    else:
                        estado=0
                    print("q"+str(estado)+" - "+i)
                    f.write("\nq"+str(estado)+" - "+i)
                elif(estado==4):
                    if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                        estado=4
                    elif(i=='w' or i=='W'):
                        estado=1
                    elif(i=='b' or i=='B'):
                        estado=5
                    else:
                        estado=0
                    print("q"+str(estado)+" - "+i)
                    f.write("\nq"+str(estado)+" - "+i)
                elif(estado==5):
                    if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                        estado=4
                    elif(i=='w' or i=='W'):
                        estado=1
                    elif(i=='a' or i=='á' or i=='à' or i=='ä' or i=='Á' or i=='A' or i=='À' or i=='Ä'):
                        estado=6
                    else:
                        estado=0
                    print("q"+str(estado)+" - "+i)
                    f.write("\nq"+str(estado)+" - "+i)
                elif(estado==6):
                    if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                        estado=4
                        print("q"+str(estado)+" - "+i)
                        f.write("\nq"+str(estado)+" - "+i)
                    elif(i=='w' or i=='W'):
                        estado=1
                        print("q"+str(estado)+" - "+i)
                        f.write("\nq"+str(estado)+" - "+i)
                    elif(i=='y' or i=='Y'):
                        estado=7####################
                        algo2=True
                        print("q"+str(estado)+" - "+i+"  columna "+str(columna))
                        f.write("\nq"+str(estado)+" - "+i+"  en la columna "+str(columna))
                    else:
                        estado=0
                        print("q"+str(estado)+" - "+i)
                        f.write("\nq"+str(estado)+" - "+i)
                elif(estado==7):
                    if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                        estado=4
                    elif(i=='w' or i=='W'):
                        estado=1
                    else:
                        estado=0
                    print("q"+str(estado)+" - "+i)
                    f.write("\nq"+str(estado)+" - "+i)
            else:
                estado=0
                print("q"+str(estado)+" - "+i)
                f.write("\nq"+str(estado)+" - "+i)
                if(algo==True and algo2==True):
                    print("palabra "+cad)
                    f.write("\npalabra "+cad)
                elif(algo==True):
                    print("palabra: "+cad)
                    f.write("\npalabra "+cad)
                elif(algo2==True):
                    print("palabra: "+cad)
                    f.write("\npalabra "+cad)
                algo=False
                algo2=False
                cad=""#para el automatico poner if i==\n columna 0...
        f.close()
    elif(opcion==2):##################################################################################################################################
        c=open("WEBAY.txt","a+")
        c.write("\n\nMODO AUTOMATICO:")
        archivo=open("oki.txt","r+")
        linea=0
        for line in archivo:
            cad=""
            algo=False
            algo2=False
            estado=0
            columna=0
            linea=linea+1
            for i in line:
                    columna=columna+1
                    #if(re.search(i,"aáäàbcdeéèëfghiíìïjklmnñoóòöpqrstuúùüvwxyzAÁÀÄBCDÉÈËEFGHÍÌÏIJKLMNÑÓÒÖOPKRSTÚÙÜUWXYZ")):
                    #intente tambien chr() y un range... crh() es para devolver el char de cierto numero ej: chr(97) es a
                    if(i=='a'or i=='á'or i=='ä'or i=='à'or i=='b'or i=='c'or i=='d'or  i=='e' or i=='é'or i=='è'or i=='ë'or i=='f'or i=='g' or i=='h'or i=='i'or i=='í'or i=='ì'or i=='ï'or i=='j'or i=='k'or i=='l'or i=='m'or i=='n'or i=='ñ'or i=='o'or i=='ó'or i=='ò'or i=='ö'or i=='p'or i=='q'or i=='r'or i=='s' or  i=='t'or i=='u'or i=='ú'or i=='ù'or i=='ü'or i=='v'or i=='w'or i=='x'or i=='y'or i=='z'or i=='A'or i=='Á'or i=='À'or i=='Ä'or i=='B'or i=='C'or i=='D'or i=='É'or i=='È'or i=='Ë'or i=='E'or i=='F'or i=='G'or i=='H'or i=='Í'or i=='Ì'or i=='Ï'or i=='I'or i=='J'or i=='K'or i=='L'or i=='M'or i=='N'or i=='Ñ'or i=='Ó'or i=='Ò'or i=='Ö'or i=='O'or i=='P'or i=='K'or i=='R'or i=='S'or i=='T'or i=='Ú'or i=='Ù'or i=='Ü'or i=='U'or i=='W'or i=='X'or i=='Y'or i=='Z'):
                        cad=cad+i
                        if(estado==0):
                            if(i=='w' or i=='W'):
                                estado=1
                            elif(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                                estado=4
                            else:
                                estado=0
                            print("q"+str(estado)+" - "+i)
                            c.write("\nq"+str(estado)+" - "+i)
                        elif(estado==1):
                            if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                                estado=2
                            elif(i=='w' or i=='W'):
                                estado=1
                            else:
                                estado=0
                            print("q"+str(estado)+" - "+i)
                            c.write("\nq"+str(estado)+" - "+i)
                        elif(estado==2):
                            if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                                estado=4
                                print("q"+str(estado)+" - "+i)
                                c.write("\nq"+str(estado)+" - "+i)
                            elif(i=='b' or i=='B'):
                                estado=3#################
                                algo=True
                                print("q"+str(estado)+" - "+str(i)+",  en la linea "+str(linea)+",  en la columna "+str(columna))
                                c.write("\nq"+str(estado)+" - "+str(i)+", en la linea "+str(linea)+",  en la columna "+str(columna))
                            elif(i=='w' or i=='W'):
                                estado=1
                                print("q"+str(estado)+" - "+i)
                                c.write("\nq"+str(estado)+" - "+i)
                            else:
                                estado=0
                                print("q"+str(estado)+" - "+i)
                                c.write("\nq"+str(estado)+" - "+i)
                        elif(estado==3):
                            if(i=='w' or i=='W'):
                                estado=1
                            elif(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                                estado=4
                            elif(i=='a' or i=='á' or i=='à' or i=='ä' or i=='Á' or i=='A' or i=='À' or i=='Ä'):
                                estado=6           
                            else:
                                estado=0
                            print("q"+str(estado)+" - "+i)
                            c.write("\nq"+str(estado)+" - "+i)
                        elif(estado==4):
                            if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                                estado=4
                            elif(i=='w' or i=='W'):
                                estado=1
                            elif(i=='b' or i=='B'):
                                estado=5
                            else:
                                estado=0
                            print("q"+str(estado)+" - "+i)
                            c.write("\nq"+str(estado)+" - "+i)
                        elif(estado==5):
                            if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                                estado=4
                            elif(i=='w' or i=='W'):
                                estado=1
                            elif(i=='a' or i=='á' or i=='à' or i=='ä' or i=='Á' or i=='A' or i=='À' or i=='Ä'):
                                estado=6
                            else:
                                estado=0
                            print("q"+str(estado)+" - "+i)
                            c.write("\nq"+str(estado)+" - "+i)
                        elif(estado==6):
                            if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                                estado=4
                                print("q"+str(estado)+" - "+i)
                                c.write("\nq"+str(estado)+" - "+i)
                            elif(i=='w' or i=='W'):
                                estado=1
                                print("q"+str(estado)+" - "+i)
                                c.write("\nq"+str(estado)+" - "+i)
                            elif(i=='y' or i=='Y'):
                                estado=7####################
                                algo2=True
                                print("q"+str(estado)+" - "+i+",  en la linea "+str(linea)+",  en la columna "+str(columna))
                                c.write("\nq"+str(estado)+" - "+str(i)+", en la linea "+str(linea)+",  en la columna "+str(columna))
                            else:
                                estado=0
                                print("q"+str(estado)+" - "+i)
                                c.write("\nq"+str(estado)+" - "+i)
                        elif(estado==7):
                            if(i=='e' or i=='é' or i=='è' or i=='ë' or i=='É' or i=='E' or i=='È' or i=='Ë'):
                                estado=4
                            elif(i=='w' or i=='W'):
                                estado=1
                            else:
                                estado=0
                            print("q"+str(estado)+" - "+i)
                            c.write("\nq"+str(estado)+" - "+i)
                    else:
                        estado=0
                        print("q"+str(estado)+" - "+i)
                        c.write("\nq"+str(estado)+" - "+i)
                        if(algo==True and algo2==True):
                            print("palabra "+cad)
                            c.write("\npalabra "+cad)
                        elif(algo==True):
                            print("palabra: "+cad)
                            c.write("\npalabra "+cad)
                        elif(algo2==True):
                            print("palabra: "+cad)
                            c.write("\npalabra "+cad)
                        algo=False
                        algo2=False
                        cad=""
        c.close()
    elif(opcion==3):
        Graficar()
    elif(opcion==0):
        opcion=0
    else:#lo tuve que poner asi porque cuando le daba cero el volvia a salir el menu a pesar que ya habia terminado el programa
        print("incorrecto, vuelva a intentar")



        
