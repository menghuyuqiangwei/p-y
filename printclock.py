from turtle import *
from datetime import *
import time

def Frame(radius):            #建立时钟外框
    reset()
    home()#将位置和方向恢复至初始状态
    penup()
    right(30)
    pensize(2)
    i=0
    while i<60:
        fd(radius)
        color("red")
        pendown()
        if i%5==0:
            fd(10)
            write(i//5+1)
        else:
            dot(3)
        penup()#抬起画笔
        goto(0,0)
        right(6)
        i+=1


def mkHand(name,length):      #注册turtle形状，建立表针turtle
    reset()#清空页面
    penup()
    fd(-length*0.1)
    pendown()
    begin_poly()#表示开始记录多边形第一个顶点
    fd(length*1.1)
    end_poly()#表示结束记录多边形顶点
    handForm = get_poly()#表示获取最后记录的多边形
    register_shape(name,handForm)#添加到shapelist中

def Init():                 #初始化表针和文字内容
    global secHand,minHand,hurHand,printer
    mode("logo")             #重置turtle指向北

    mkHand("secHand",135)    #建立三个表针并初始化
    mkHand("minHand",125)
    mkHand("hurHand",70)

    secHand = Turtle()
    secHand.shape("secHand")#使用新添加的shape
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")

    for hand in secHand,minHand,hurHand:
        hand.shapesize(1,1,2)
        hand.speed(0)#速度最快
    
    printer = Turtle()
    printer.hideturtle()
    printer.penup()
        
def butt():                        #判断用户输入
    global dhour,dsec,dmin,dday,year,month,day
    screen=getscreen()
    timeyear=screen.numinput("修改时间", "请输入年",0,0,10000)#time是输入的数
    if timeyear!=None and timeyear>0:
        year= int(timeyear)
    else:
        year=time.localtime().tm_year
    timemon=screen.numinput("修改时间", "请输入月", 0, 0, 12)
    if timemon!=None and timemon>0:
        month=int(timemon)
    else:
        month=time.localtime().tm_mon
    timeday=screen.numinput("修改时间", "请输入日", 0, 0, 31)
    if timeday!=None and timeday>0:
        day=int(timeday)
        dday=account(time.localtime().tm_mon,time.localtime().tm_mday)-account(month,day)
    else:
        dday=0
    timehour=screen.numinput("修改时间", "请输入时", 0, 0, 24)
    if timehour!=None and timehour>0:
        dhour=time.localtime().tm_hour-int(timehour)
    else:
        dhour=0
    timemin=screen.numinput("修改时间", "请输入分", 0, 0, 60)
    if timemin!=None and timemin>0:
        dmin=time.localtime().tm_min-int(timemin)
    else:
        dmin=0
    timesec=screen.numinput("修改时间", "请输入秒", 0, 0, 60)
    if timesec!=None and timesec>0:
        dsec=time.localtime().tm_sec-int(timesec)
    else:
        dsec=0 
        
def Date(t):                     #控制输出日期格式
    y = year
    m = month
    d = account(time.localtime().tm_mon,time.localtime().tm_mday)-dday-account(month,day)+day
    return '%d年%d月%d日' % (y ,m, d)


def Time(t):                    #控制输出时间格式
    s = t.second-dsec
    m = t.minute-dmin
    h = t.hour-dhour
    return '%02d:%02d:%02d' % (h, m, s)
    

def tiangan():                  #计算天干

    n=year
    ge=int(n%10)
    TG = ["庚","辛","壬","癸","甲","乙","丙","丁","戊","己"]

    return TG[ge]


def dizhi():                    #计算地支

    n=year
    di= (n%12)
    DZ = ["申 猴 年","酉 鸡 年","戌 狗 年","亥 猪 年","子 鼠 年","丑 牛 年","寅 虎 年","卯 兔 年","辰 龙 年","巳 蛇 年","午 马 年","未 羊 年"]
    return DZ[di]
    
def leapyear():                 #判断是否为闰年

    if (year%4==0 and year%100!=0) or(year%400==0):
        return True
    else:
        return False
    
def account(x,y):
    
    if leapyear():
        iMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        iMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    S = 0
    for i in range(0,x-1):
        S = S + iMonth[i]
        
    S = S + y
    return S
    
    
    
def printreset():               #实现秒表跳秒刷新
    reset()
    t=datetime.today()
    write(Time(t),align = 'center', font = ('Courier', 14, 'bold'))
    
        
        
def Tick():
    t = datetime.today()
    s= t.second #+ t.microsecond * 0.000001
    m = t.minute #+ s/60.0
    h = t.hour + (m-dmin)/60.0
    secHand.seth(6*(s-dsec))  #确定方向
    minHand.seth(6*(m-dmin))
    hurHand.seth(30*(h-dhour))

    printer.reset()
    printer.penup()
    tracer(False)
    printer.forward(-45)
    printer.write(Date(t), align = 'center', font = ('Courier', 14, 'bold'))
    printer.back(25)
    printer.write(Time(t), align = 'center',font = ('Courier',14,'bold'))
    printer.back(25)
    if leapyear():
        printer.write("闰年", align = 'center', font = ('Courier', 14,'bold'))
    else:
        printer.write("平年", align = 'center', font = ('Courier', 14,'bold'))
    printer.back(25)
    printer.left(90)
    printer.forward(50)
    printer.write(tiangan(), align = 'center',font = ('Courier',14,'bold'))
    printer.right(180)
    printer.forward(67)
    printer.write(dizhi(), align = 'center',font = ('Courier',14,'bold'))
    printer.home()
    tracer(True)
    
    ontimer(Tick,100)                #100ms后继续调用tick


def main():
    tracer(False)
    Init()
    Frame(150)
    tracer(True)
    butt()
    Tick()  
    hideturtle()
    mainloop()

main()
