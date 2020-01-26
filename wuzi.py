#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox


size = 15
isplaying = 1 # 判断游戏是否结束
# 保存棋盘
chess = [[0 for i in range(size+1)] for i in range(size+1)]
# 保存棋盘权值
chess_Value = [[0 for i in range(size+1)] for i in range(size+1)]
dic = {"0": 0, "1": 8, "2": 10, "11": 50, "22": 1000, "111": 25000, "222": 30000, "1111": 50000, "2222": 200000,
       "21": 4, "12": 2, "211": 25, "122": 20, "11112": 80000, "112": 30, "1112": 2800, "221": 500, "2221": 2000,
       "22221": 150000}


#dic = {} #调试模式

def paint(event,k):
    # 使棋落在棋盘点上
    if event.x % 30 > 15:
        event.x = event.x//30 + 1
    else:
        event.x = event.x // 30
    if event.y % 30 > 15:
        event.y = event.y // 30 + 1
    else:
        event.y = event.y//30
    if event.x > size:
        event.x = size
    if event.y > size:
        event.y = size
    if event.x < 1:
        event.x = 1
    if event.y < 1:
        event.y = 1

    if chess[event.x][event.y] == 0 and isplaying:
        if k == 1:
            canvas.create_oval(event.x*30 - 15, event.y*30 - 15, event.x*30 + 15, event.y*30 + 15, fill="black",tags = ('black'))
            # 标记最后下的黑棋
            canvas.delete('lastWhite')
            canvas.create_line(event.x*30 - 4, event.y*30, event.x*30 + 4, event.y*30, width=2, fill="white", tags = ('lastWhite'))
            canvas.create_line(event.x*30, event.y*30 - 4, event.x*30, event.y*30 + 4, width=2, fill="white", tags = ('lastWhite'))
            
            chess[event.x][event.y] = 1
            gameover(event.x, event.y)
        elif k == 2:
            canvas.create_oval(event.x*30 - 15, event.y*30 - 15, event.x*30 + 15, event.y*30 + 15, fill="white",tags = ('white'))
            # 标记最后下的白棋
            canvas.delete('lastBlack')
            canvas.create_line(event.x*30 - 4, event.y*30, event.x*30 + 4, event.y*30, width=2, fill="black", tags = ('lastBlack'))
            canvas.create_line(event.x*30, event.y*30 - 4, event.x*30, event.y*30 + 4, width=2, fill="black", tags = ('lastBlack'))
            
            chess[event.x][event.y] = 2
            gameover(event.x, event.y)
        if isplaying: # 如果没有这句，在黑棋获胜后，白子还会下一步
            return 1  # 如果成功则返回1

def mod1(event):    
    if paint(event,1):
        ai()

def mod2(event):
    paint(event,1)

def mod3(event):
    paint(event,2)

def mod4(event):
    global isplaying
    global chess
    global chess_Value
    canvas.delete('black','white','lastBlack','lastWhite','win')
    chess = [[0 for i in range(size+1)] for i in range(size+1)]
    chess_Value = [[0 for i in range(size+1)] for i in range(size+1)]
    isplaying = 1

    
def ai():
    for i in range(1, size+1):
        for j in range(1, size + 1):
            if chess[i][j] == 0:
                code = ""
                chess_color = 0
                # 向右
                for x in range(i + 1, size + 1):
                    # 如果为空就跳出循环
                    if chess[x][j] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是右边第一颗棋子
                            code += str(chess[x][j])  # 记录它的颜色
                            chess_color = chess[x][j]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][j]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][j])  # 记录它的颜色
                            else:  # 右边找到一颗不同颜色的棋子
                                code += str(chess[x][j])
                                break
                # 取出对应的权值
                value = dic.get(code,0) # Index but with a default
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向左
                for x in range(i - 1, 0, -1):
                    # 如果向左的第一位置为空就跳出循环
                    if chess[x][j] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是左边第一颗棋子
                            code += str(chess[x][j])  # 记录它的颜色
                            chess_color = chess[x][j]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][j]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][j])  # 记录它的颜色
                            else:  # 左边找到一颗不同颜色的棋子
                                code += str(chess[x][j])
                                break
                #  取出对应的权值
                value = dic.get(code,0)
                if value:
                    chess_Value[i][j] += value
                #  把code，chess_color清空
                code = ""
                chess_color = 0
                #  向上
                for y in range(j - 1, 0, -1):
                    #  如果向上的第一位置为空就跳出循环
                    if chess[i][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是上边第一颗棋子
                            code += str(chess[i][y])  # 记录它的颜色
                            chess_color = chess[i][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[i][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[i][y])  # 记录它的颜色
                            else:  # 上边找到一颗不同颜色的棋子
                                code += str(chess[i][y])
                                break
                #  取出对应的权值
                value = dic.get(code,0)
                if value:
                    chess_Value[i][j] += value
                #  把code，chess_color清空
                code = ""
                chess_color = 0
                # 向下
                for y in range(j+1, size+1):
                    # 如果向下的第一位置为空就跳出循环
                    if chess[i][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是下边第一颗棋子
                            code += str(chess[i][y])  # 记录它的颜色
                            chess_color = chess[i][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[i][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[i][y])  # 记录它的颜色
                            else:  # 下边找到一颗不同颜色的棋子
                                code += str(chess[i][y])
                                break
                # 取出对应的权值
                value = dic.get(code,0)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向左下
                for x, y in zip(range(i - 1, 0, -1), range(j + 1, size + 1)):
                    # 如果向左下的第一位置为空就跳出循环
                    if chess[x][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是左下边第一颗棋子
                            code += str(chess[x][y])  # 记录它的颜色
                            chess_color = chess[x][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][y])  # 记录它的颜色
                            else:  # 左下找到一颗不同颜色的棋子
                                code += str(chess[x][y])
                                break
                # 取出对应的权值
                value = dic.get(code,0)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向右上
                for x, y in zip(range(i + 1, size+1), range(j - 1, 0, -1)):
                    # 如果向右上的第一位置为空就跳出循环
                    if chess[x][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是右上边第一颗棋子
                            code += str(chess[x][y])  # 记录它的颜色
                            chess_color = chess[x][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][y])  # 记录它的颜色
                            else:  # 右上找到一颗不同颜色的棋子
                                code += str(chess[x][y])
                                break
                # 取出对应的权值
                value = dic.get(code,0)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向左上
                for x, y in zip(range(i - 1, 0, -1), range(j - 1, 0, -1)):
                    # 如果向左上的第一位置为空就跳出循环
                    if chess[x][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是左
                            # 上边第一颗棋子
                            code += str(chess[x][y])  # 记录它的颜色
                            chess_color = chess[x][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][y])  # 记录它的颜色
                            else:  # 左上找到一颗不同颜色的棋子
                                code += str(chess[x][y])
                                break
                # 取出对应的权值
                value = dic.get(code,0)
                if value:
                    chess_Value[i][j] += value
                # 把code，chess_color清空
                code = ""
                chess_color = 0
                # 向右下
                for x, y in zip(range(i+1, size+1), range(j+1, size+1)):
                    # 如果向右下的第一位置为空就跳出循环
                    if chess[x][y] == 0:
                        break
                    else:
                        if chess_color == 0:  # 这是右下
                            # 上边第一颗棋子
                            code += str(chess[x][y])  # 记录它的颜色
                            chess_color = chess[x][y]  # 保存它的颜色
                        else:
                            if chess_color == chess[x][y]:  # 跟第一颗棋子颜色相同
                                code += str(chess[x][y])  # 记录它的颜色
                            else:  # 右下找到一颗不同颜色的棋子
                                code += str(chess[x][y])
                                break
                # 取出对应的权值
                value = dic.get(code,0)
                if value:
                    chess_Value[i][j] += value


    mymax = 0
    priority = 0
    priorityX = 0
    priorityY = 0
    for a in range(1, size+1):
        for b in range(1, size + 1):
            if chess[a][b] == 0 and countn(a,b) > priority:
                priority = countn(a,b)
                priorityX = a
                priorityY = b

            elif chess[a][b] == 0 and chess_Value[a][b] >= mymax:
                mymax = chess_Value[a][b]
                xxx = a
                yyy = b
    if priority != 0:
        xxx = priorityX
        yyy = priorityY

    chess[xxx][yyy] = 2
    canvas.create_oval(xxx*30-15, yyy*30-15, xxx*30+15, yyy*30+15, fill="white",tags = ('white'))
    # 标记最后下的白棋
    canvas.delete('lastBlack')
    canvas.create_line(xxx*30 - 4, yyy*30, xxx*30 + 4, yyy*30, width=2, fill="black", tags = ('lastBlack'))
    canvas.create_line(xxx*30, yyy*30 - 4, xxx*30, yyy*30 + 4, width=2, fill="black", tags = ('lastBlack'))
    gameover(xxx, yyy)

def countn(xx, yy):
    retu = 0
    count5 = 0
    count6 = 0


    # 水平方向
    count3 = 0 #数的是黑棋第一优先级的个数
    count4 = 0 #数的是白棋第一优先级的个数
    
    count1 = 0 #数的是同色棋子的个数
    count0 = 0 #数的是空位的个数
    chess_color = 0
    for i in range(xx + 1, size+1):   #先向右搜索
        if chess[xx+1][yy] != 0:
            if i == xx+1:             #遇到右侧第一个棋子
                count1 += 2
                chess_color = chess[xx+1][yy]
                continue             #下面的语句不执行

            if chess[i][yy] == chess_color:
                count1 += 1
            elif chess[i][yy] == 0:
                if i+1 < size+1 and chess[i+1][yy]==0: #如果空位的下一个还是空位
                    count0 = 2
                else:                                  #如果空位的下一个是边界或有棋子
                    count0 = 1
                break
            else:              #遇到异色棋子
                break
    for i in range(xx-1, xx-5, -1): # 向左搜索4格
        if chess_color == 0 or (0 < xx-1 and chess[xx-1][yy] == 0) or xx-1 < 1:   #如果两侧有一边的第一个棋子是空位，则直接退出
            count1 = 0
            count0 = 0
            break

        if 0 < i and chess[i][yy] == chess_color:
            count1 += 1
        elif 0 < i and chess[i][yy] == 0:
            if count0 == 0 or count0 == 2:
                count0 += 1
            else:              #如果count0 == 1
                if i-1 > 0 and chess[i-1][yy]==0:
                    count0 = 3
                else:
                    count0 = 2
            break              #判断完后退出
        else:                  #边界或异色
            if count0 == 2:    #这里，之前没考虑到
                count0 = 1
            break
    if count1 >= 5 and chess_color == 2: #2x222 or 22x22 or 222x2    #这里不能写==5,因为可能有连续6,7个
        retu = 8
    elif count1 >= 5 and chess_color == 1: #1x111 or 11x11 or 111x1
        retu = 7
    elif count1 == 4 and count0 >= 2 and chess_color == 2: #02x220 or 022x20  #这里用count2==0来代表两侧有两个空位是不对的，因为可能遇到边界直接退出循环就没有记录count2
        retu = 6
        count4 += 0.1
    elif count1 == 4 and count0 >= 2 and chess_color == 1: #01x110 or 011x10
        retu = 5
        count3 += 0.1
    elif count1 == 4 and count0 == 1 and chess_color == 2: #02x221
        count4 += 1
    elif count1 == 4 and count0 == 1 and chess_color == 1: #01x112
        count3 += 1
    elif count1 == 3 and count0 == 3 and chess_color == 2: #02x200
        count4 += 1
    elif count1 == 3 and count0 == 3 and chess_color == 1: #01x100
        count3 += 1

    for k in range(2,0,-1): #判断两种颜色
        for m in range(-1,3,2): #在(-1,1)中循环
            count = 0    #数一侧连续棋子的个数，不算当前位置
            count00 = 0  #遇到空位则加一,取值范围为(0,1,2,3)
            for i in range(xx+m,xx+5*m,m):  #数一侧4个棋子,先左后右
                if 0 < i < size+1 and chess[i][yy] == k: #同色
                    count += 1
                elif 0 < i < size+1 and chess[i][yy] == 0: #空位
                    count00 += 1
                    if 0 < i+m < size+1 and chess[i+m][yy] == 0: #如果空位的下一个还是空位，count00再加一变成2  #本来写的是if 0 < i+1 < size+1 and chess[i+1][yy] == 0:
                        count00 +=1
                    break
                else:                                    #异色或遇到边界
                    break

            if count00 == 2:
                if 0 < xx-m < size+1 and chess[xx-m][yy] == 0:    #如果另一侧的第一颗棋子为0
                    count00 = 3
                else:
                    count00 = 1
            else:                                                 #count00 == 0 or 1
                if 0 < xx-m < size+1 and chess[xx-m][yy] == 0:    #如果另一侧的第一颗棋子为0
                    count00 += 1

            if count == 4 and k == 2: #x2222
                retu = 8
            elif count == 4 and k == 1 and retu < 7: #x1111
                retu = 7
            elif count == 3 and k == 2:
                if count00 > 1 and retu < 6: #0x2220
                    retu = 6
                    count4 += 0.1
                elif count00 == 1: #0x2221
                    count4 += 1
            elif count == 3 and k == 1:
                if count00 > 1 and retu < 5: #0x1110
                    retu = 5
                    count3 += 0.1
                elif count00 == 1: #0x1112
                    count3 += 1
            elif count == 2 and count00 == 3: #这里有逻辑问题，c=2,c00=3 时，除了0x1100还有可能是0011x01，和下面的讨论重复
            #不太好排除多余情况，只能限定每一个大方向上c3和c4不大于1,然后再加一个特殊情况21110x01112
                if k == 2:            #0x2200
                    count4 += 1
                elif k == 1:          #0x1100
                    count3 += 1


    # 这个循环是为了找出0x2020或者1x2202这两种（实际有12*2种）
    for k in range(2,0,-1): #k为棋子颜色，2或1
        markP = 0 #用来比较中间空位的位置，如何相同说明是同一个，只有不同才能算两次
        for n in range(-1,3,2):  #又加了一重循环，主要作用是先向右再向左搜索一遍，再数个数；第二次，先向左再向右搜索，再数个数，主要是为了排除120x2020这种情况，避免和0x2020混淆
        #但是也因此将相同的算了两次
            count = 0    #数连续（忽略一个空位）棋子的个数
            count00 = 0  #记录中间空位的个数，必须要有一个
            count01 = 0  #记录两侧空位的个数
            for m in range(-1*n,3*n,2*n):  #第一次取值(1,-1)，第二次(-1,1)
                for i in range(xx+m,xx+5*m,m):
                    if 0 < i < size+1 and chess[i][yy] == k:  #不超出范围且遇到同色棋子
                        count += 1
                    elif 0 < i < size+1 and chess[i][yy] == 0:  #不超出范围且遇到空位
                        if count00 == 0:     #还未遇到中间空位
                            if 0 < i+m < size+1 and chess[i+m][yy] == k: #如果下一个还是同色 #一开始写的是if 0 < i+1 < size+1 and chess[i+1][yy] == k:
                                if i != markP:
                                    markP = i
                                    count00 = 1  #记录中间空位
                                else:            #如果相同，说明是第二次，而且重复计算，所以直接退出循环
                                    break
                            else:
                                count01 += 1
                                break
                        elif count00 == 1:   #已经遇到中间空位
                            count01 += 1
                            break
                    else:                  #遇到异色棋子或者超出范围，也就是被挡住
                        break
            if count == 3 and count00 == 1:
                if k == 2:         #1x0222
                    count4 += 1
                if k == 1:         #2x1011
                    count3 += 1
            if count == 2 and count00 == 1 and count01 == 2:
                if k == 2:         #0x2020
                    count4 += 1
                if k == 1:         #01x010
                    count3 += 1

    # 限定每一个大方向上c3和c4不大于1
    if count4:
        if isinstance(count4,int):
            count4 = 1
        else:
            count4 = 1.1
    if count3:
        if isinstance(count3,int):
            count3 = 1
        else:
            count3 = 1.1

    # 补充一个特殊情况21110x01112
    if 0<xx-4 and xx+4<size+1:
        for k in range(2,0,-1):
            if (0<xx-5 and chess[xx-5][yy]!=k and chess[xx-5][yy]!=0 or xx-5<1) and (xx+5<size+1 and chess[xx+5][yy]!=k and chess[xx+5][yy]!=0 or xx+5>size):
                if chess[xx-4][yy]==k and chess[xx-3][yy]==k and chess[xx-2][yy]==k and chess[xx-1][yy]==0:
                    if chess[xx+4][yy]==k and chess[xx+3][yy]==k and chess[xx+2][yy]==k and chess[xx+1][yy]==0:                    
                        if k == 2:
                            count4 += 2
                        elif k == 1:
                            count3 += 2
                    
    count6 += count4
    count5 += count3

    # 竖直方向
    count3 = 0 #数的是黑棋第一优先级的个数
    count4 = 0 #数的是白棋第一优先级的个数
    
    count1 = 0
    count0 = 0
    chess_color = 0
    for i in range(yy + 1, size+1):        
        if chess[xx][yy+1] != 0:
            if i == yy+1:
                count1 += 2
                chess_color = chess[xx][yy+1]
                continue

            if chess[xx][i] == chess_color:
                count1 += 1
            elif chess[xx][i] == 0:
                if i+1 < size+1 and chess[xx][i+1]==0:
                    count0 = 2
                else:
                    count0 = 1
                break
            else:
                break
    for i in range(yy-1, yy-5, -1):
        if chess_color == 0 or (yy-1>0 and chess[xx][yy-1] == 0) or yy-1 < 1:
            count1 = 0
            count0 = 0
            break
        if i > 0 and chess[xx][i] == chess_color:
            count1 += 1
        elif i > 0 and chess[xx][i] == 0:
            if count0 == 0 or count0 == 2:
                count0 += 1
            else:              #如果count0 == 1
                if i-1 > 0 and chess[xx][i-1]==0:
                    count0 = 3
                else:
                    count0 = 2
            break
        else:
            if count0 == 2:
                count0 = 1
            break
    if count1 >= 5 and chess_color == 2:
        retu = 8
    elif count1 >= 5 and chess_color == 1 and retu < 7:
        retu = 7
    elif count1 == 4 and count0 >= 2 and chess_color == 2 and retu < 6:
        retu = 6
        count4 += 0.1
    elif count1 == 4 and count0 >= 2 and chess_color == 1 and retu < 5:
        retu = 5
        count3 += 0.1
    elif count1 == 4 and count0 == 1 and chess_color == 2:
        count4 += 1
    elif count1 == 4 and count0 == 1 and chess_color == 1:
        count3 += 1
    elif count1 == 3 and count0 == 3 and chess_color == 2:
        count4 += 1
    elif count1 == 3 and count0 == 3 and chess_color == 1:
        count3 += 1

    for k in range(2,0,-1):
        for m in range(-1,3,2):
            count = 0    #数一侧连续棋子的个数
            count00 = 0  #遇到空位则加一,取值范围为range(0,4)
            for i in range(yy+m,yy+5*m,m):  #数一侧的棋子
                if 0 < i < size+1 and chess[xx][i] == k:
                    count += 1
                elif 0 < i < size+1 and chess[xx][i] == 0:
                    count00 += 1
                    if 0 < i+m < size+1 and chess[xx][i+m] == 0: #如果空位的下一个还是空位，count00再加一变成2
                        count00 +=1
                    break
                else:
                    break

            if count00 == 2:
                if 0 < yy-m < size+1 and chess[xx][yy-m] == 0:    #如果另一侧的第一颗棋子为0
                    count00 = 3
                else:
                    count00 = 1
            else:
                if 0 < yy-m < size+1 and chess[xx][yy-m] == 0:    #如果另一侧的第一颗棋子为0
                    count00 += 1

            if count == 4 and k == 2: #x2222
                retu = 8
            elif count == 4 and k == 1 and retu < 7: #x1111
                retu = 7
            elif count == 3 and k == 2:
                if count00 > 1 and retu < 6: #0x2220
                    retu = 6
                    count4 += 0.1
                elif count00 == 1: #0x2221
                    count4 += 1
            elif count == 3 and k == 1:
                if count00 > 1 and retu < 5: #0x1110
                    retu = 5
                    count3 += 0.1
                elif count00 == 1: #0x1112
                    count3 += 1
            elif count == 2 and count00 == 3:
                if k == 2:            #0x2200
                    count4 += 1
                elif k == 1:          #0x1100
                    count3 += 1


    # 这个循环是为了找出0x2020或者x2202这两种（实际有12*2种）
    for k in range(2,0,-1): #k为棋子颜色，2或1
        markP = 0
        for n in range(-1,3,2):  #又加了一重循环，主要作用是先向右再向左搜索一遍，再数个数；第二次，先向左再向右搜索，再数个数，主要是为了排除120x2020这种情况，避免和0x2020混淆
            count = 0    #数连续（忽略一个空位）棋子的个数
            count00 = 0  #记录中间空位的个数，必须要有一个
            count01 = 0  #记录两侧空位的个数
            for m in range(-1*n,3*n,2*n):  #第一次取值(1,-1)，第二次(-1,1)
                for i in range(yy+m,yy+5*m,m):
                    if 0 < i < size+1 and chess[xx][i] == k:  #不超出范围且遇到同色棋子
                        count += 1
                    elif 0 < i < size+1 and chess[xx][i] == 0:  #不超出范围且遇到空位
                        if count00 == 0:     #还未遇到中间空位
                            if 0 < i+m < size+1 and chess[xx][i+m] == k: #如果下一个还是同色
                                if i != markP:
                                    markP = i
                                    count00 = 1
                                else:
                                    break
                            else:
                                count01 += 1
                                break
                        elif count00 == 1:   #已经遇到中间空位
                            count01 += 1
                            break
                    else:                  #遇到异色棋子或者超出范围，也就是被挡住
                        break
            if count == 3 and count00 == 1:
                if k == 2:         #x0222
                    count4 += 1
                if k == 1:         #x1011
                    count3 += 1
            if count == 2 and count00 == 1 and count01 == 2:
                if k == 2:         #0x2020
                    count4 += 1
                if k == 1:         #01x020
                    count3 += 1

    # 限定每一个大方向上c3和c4不大于1
    if count4:
        if isinstance(count4,int):
            count4 = 1
        else:
            count4 = 1.1
    if count3:
        if isinstance(count3,int):
            count3 = 1
        else:
            count3 = 1.1


    # 补充一个特殊情况21110x01112
    if 0<yy-4 and yy+4<size+1:
        for k in range(2,0,-1):
            if (0<yy-5 and chess[xx][yy-5]!=k and chess[xx][yy-5]!=0 or yy-5<1) and (yy+5<size+1 and chess[xx][yy+5]!=k and chess[xx][yy+5]!=0 or yy+5>size):
                if chess[xx][yy-4]==k and chess[xx][yy-3]==k and chess[xx][yy-2]==k and chess[xx][yy-1]==0:
                    if chess[xx][yy+4]==k and chess[xx][yy+3]==k and chess[xx][yy+2]==k and chess[xx][yy+1]==0:                    
                        if k == 2:
                            count4 += 2
                        elif k == 1:
                            count3 += 2
    
    count6 += count4
    count5 += count3

    # 主对角线
    count3 = 0 #数的是黑棋第一优先级的个数
    count4 = 0 #数的是白棋第一优先级的个数
    
    count1 = 0
    count0 = 0
    chess_color = 0
    for i,j in zip(range(xx+1, size+1), range(yy+1, size+1)):        
        if chess[xx+1][yy+1] != 0:
            if i == xx+1:
                count1 += 2
                chess_color = chess[xx+1][yy+1]
                continue
            if chess[i][j] == chess_color:
                count1 += 1
            elif chess[i][j] == 0:
                if i+1 < size+1 and j+1 < size+1 and chess[i+1][j+1] == 0:
                    count0 = 2
                else:
                    count0 = 1
                break
            else:
                break
    for i,j in zip(range(xx-1, xx-5, -1), range(yy-1, yy-5, -1)):
        if chess_color == 0 or (xx-1>0 and yy-1>0 and chess[xx-1][yy-1] == 0) or xx-1<1 or yy-1<1:
            count1 = 0
            count0 = 0
            break
        if i>0 and j>0 and chess[i][j] == chess_color:
            count1 += 1
        elif i>0 and j>0 and chess[i][j] == 0:
            if count0 == 0 or count0 == 2:
                count0 += 1
            else:
                if i-1 > 0 and j-1 > 0 and chess[i-1][j-1] == 0:
                    count0 = 3
                else:
                    count0 = 2
            break
        else:
            if count0 == 2:
                count0 = 1
            break
    if count1 >= 5 and chess_color == 2:
        retu = 8
    elif count1 >= 5 and chess_color == 1 and retu < 7:
        retu = 7
    elif count1 == 4 and count0 >= 2 and chess_color == 2 and retu < 6:
        retu = 6
        count4 += 0.1
    elif count1 == 4 and count0 >= 2 and chess_color == 1 and retu < 5:
        retu = 5
        count3 += 0.1
    elif count1 == 4 and count0 == 1 and chess_color == 2:
        count4 += 1
    elif count1 == 4 and count0 == 1 and chess_color == 1:
        count3 += 1
    elif count1 == 3 and count0 == 3 and chess_color == 2:
        count4 += 1
    elif count1 == 3 and count0 == 3 and chess_color == 1:
        count3 += 1

    for k in range(2,0,-1):
        for m in range(-1,3,2):
            count = 0    #数一侧连续棋子的个数
            count00 = 0  #遇到空位则加一,取值范围为range(0,4)
            for i,j in zip(range(xx+m,xx+5*m,m),range(yy+m,yy+5*m,m)):   #数一侧的棋子
                if 0 < i < size+1 and 0 < j < size+1 and chess[i][j] == k:
                    count += 1
                elif 0 < i < size+1 and 0 < j < size+1 and chess[i][j] == 0:
                    count00 += 1
                    if 0 < i+m < size+1 and 0 < j+m < size+1 and chess[i+m][j+m] == 0: #如果空位的下一个还是空位，count00再加一变成2
                        count00 +=1
                    break
                else:
                    break

            if count00 == 2:
                if 0 < xx-m < size+1 and 0 < yy-m < size+1 and chess[xx-m][yy-m] == 0:    #如果另一侧的第一颗棋子为0
                    count00 = 3
                else:
                    count00 = 1
            else:
                if 0 < xx-m < size+1 and 0 < yy-m < size+1 and chess[xx-m][yy-m] == 0:    #如果另一侧的第一颗棋子为0
                    count00 += 1

            if count == 4 and k == 2: #x2222
                retu = 8
            elif count == 4 and k == 1 and retu < 7: #x1111
                retu = 7
            elif count == 3 and k == 2:
                if count00 > 1 and retu < 6: #0x2220
                    retu = 6
                    count4 += 0.1
                elif count00 == 1: #0x2221
                    count4 += 1
            elif count == 3 and k == 1:
                if count00 > 1 and retu < 5: #0x1110
                    retu = 5
                    count3 += 0.1
                elif count00 == 1: #0x1112
                    count3 += 1
            elif count == 2 and count00 == 3:
                if k == 2:            #0x2200
                    count4 += 1
                elif k == 1:          #0x1100
                    count3 += 1

    # 这个循环是为了找出0x2020或者x2202这两种（实际有12*2种）
    for k in range(2,0,-1): # k为棋子颜色，2或1
        markP = 0
        for n in range(-1,3,2):  # 又加了一重循环，主要作用是先向右再向左搜索一遍，再数个数；第二次，先向左再向右搜索，再数个数，主要是为了排除120x2020这种情况，避免和0x2020混淆
            count = 0    # 数连续（忽略一个空位）棋子的个数
            count00 = 0  # 记录中间空位的个数，必须要有一个
            count01 = 0  # 记录两侧空位的个数
            for m in range(-1*n,3*n,2*n):  # 第一次取值(1,-1)，第二次(-1,1)
                for i,j in zip(range(xx+m,xx+5*m,m),range(yy+m,yy+5*m,m)):
                    if 0 < i < size+1 and 0 < j < size+1 and chess[i][j] == k:  # 不超出范围且遇到同色棋子
                        count += 1
                    elif 0 < i < size+1 and 0 < j < size+1 and chess[i][j] == 0:  # 不超出范围且遇到空位
                        if count00 == 0:     # 还未遇到中间空位
                            if 0 < i+m < size+1 and 0 < j+m < size+1 and chess[i+m][j+m] == k: # 如果下一个还是同色
                                if i != markP:
                                    markP = i
                                    count00 = 1
                                else:
                                    break
                            else:
                                count01 += 1
                                break
                        elif count00 == 1:   # 已经遇到中间空位
                            count01 += 1
                            break
                    else:                  # 遇到异色棋子或者超出范围，也就是被挡住
                        break
            if count == 3 and count00 == 1:
                if k == 2:         #x0222
                    count4 += 1
                if k == 1:         #x1011
                    count3 += 1
            if count == 2 and count00 == 1 and count01 == 2:
                if k == 2:         #0x2020
                    count4 += 1
                if k == 1:         #01x020
                    count3 += 1
    # 限定每一个大方向上c3和c4不大于1
    if count4:
        if isinstance(count4,int):
            count4 = 1
        else:
            count4 = 1.1
    if count3:
        if isinstance(count3,int):
            count3 = 1
        else:
            count3 = 1.1
    # 补充一个特殊情况21110x01112
    if 0<xx-4 and xx+4<size+1 and 0<yy-4 and yy+4<size+1:
        for k in range(2,0,-1):
            if 0<xx-5 and 0<yy-5 and chess[xx-5][yy-5]!=k and chess[xx-5][yy-5]!=0 or xx-5<1 or yy-5<1:
                if xx+5<size+1 and yy+5<size+1 and chess[xx+5][yy+5]!=k and chess[xx+5][yy+5]!=0 or xx+5>size or yy+5>size:
                    if chess[xx-4][yy-4]==k and chess[xx-3][yy-3]==k and chess[xx-2][yy-2]==k and chess[xx-1][yy-1]==0:
                        if chess[xx+4][yy+4]==k and chess[xx+3][yy+3]==k and chess[xx+2][yy+2]==k and chess[xx+1][yy+1]==0:                    
                            if k == 2:
                                count4 += 2
                            elif k == 1:
                                count3 += 2
    count6 += count4
    count5 += count3

    # 次对角线
    count3 = 0 # 数的是黑棋第一优先级的个数
    count4 = 0 # 数的是白棋第一优先级的个数
    
    count1 = 0
    count0 = 0
    chess_color = 0
    for i,j in zip(range(xx - 1, 0, -1), range(yy + 1, size+1)):        
        if chess[xx-1][yy+1] != 0:
            if i == xx-1:
                count1 += 2
                chess_color = chess[xx-1][yy+1]
                continue
            if chess[i][j] == chess_color:
                count1 += 1
            elif chess[i][j] == 0:
                if i-1 > 0 and j+1 < size+1 and chess[i-1][j+1] == 0:
                    count0 = 2
                else:
                    count0 = 1
                break
            else:
                break
    for i, j in zip(range(xx+1, xx+5), range(yy-1, yy-5, -1)):
        if chess_color == 0 or (xx+1 < size+1 and yy-1>0 and chess[xx+1][yy-1] == 0) or xx+1>size or yy-1<1:
            count1 = 0
            count0 = 0
            break
        if i<size+1 and j>0 and chess[i][j] == chess_color:
            count1 += 1
        elif i<size+1 and j>0 and chess[i][j] == 0:
            if count0 == 0 or count0 == 2:
                count0 += 1
            else:
                if i+1 < size+1 and j-1 > 0 and chess[i+1][j-1] == 0:
                    count0 = 3
                else:
                    count0 = 2
            break
        else:
            if count0 == 2:
                count0 = 1
            break
    if count1 >= 5 and chess_color == 2:
        retu = 8
    elif count1 >= 5 and chess_color == 1 and retu < 7:
        retu = 7
    elif count1 == 4 and count0 >= 2 and chess_color == 2 and retu < 6:
        retu = 6
        count4 += 0.1
    elif count1 == 4 and count0 >= 2 and chess_color == 1 and retu < 5:
        retu = 5
        count3 += 0.1
    elif count1 == 4 and count0 == 1 and chess_color == 2:
        count4 += 1
    elif count1 == 4 and count0 == 1 and chess_color == 1:
        count3 += 1
    elif count1 == 3 and count0 == 3 and chess_color == 2:
        count4 += 1
    elif count1 == 3 and count0 == 3 and chess_color == 1:
        count3 += 1


    for k in range(2,0,-1):
        for m in range(-1,3,2):
            count = 0    # 数一侧连续棋子的个数
            count00 = 0  # 遇到空位则加一,取值范围为range(0,4)
            for i,j in zip(range(xx-m,xx-5*m,-m),range(yy+m,yy+5*m,m)):   # 数一侧的棋子，这里本来写的是range(xx-m,xx-5*m,m)，后来发现在这个方向上没法识别
                if 0 < i < size+1 and 0 < j < size+1 and chess[i][j] == k:
                    count += 1
                elif 0 < i < size+1 and 0 < j < size+1 and chess[i][j] == 0:
                    count00 += 1
                    if 0 < i-m < size+1 and 0 < j+m < size+1 and chess[i-m][j+m] == 0: # 如果空位的下一个还是空位，count00再加一变成2
                        count00 +=1
                    break
                else:
                    break

            if count00 == 2:
                if 0 < xx+m < size+1 and 0 < yy-m < size+1 and chess[xx+m][yy-m] == 0:    # 如果另一侧的第一颗棋子为0
                    count00 = 3
                else:
                    count00 = 1
            else:
                if 0 < xx+m < size+1 and 0 < yy-m < size+1 and chess[xx+m][yy-m] == 0:    # 如果另一侧的第一颗棋子为0
                    count00 += 1

            if count == 4 and k == 2: #x2222
                retu = 8
            elif count == 4 and k == 1 and retu < 7: #x1111
                retu = 7
            elif count == 3 and k == 2:
                if count00 > 1 and retu < 6: #0x2220
                    retu = 6
                    count4 += 0.1
                elif count00 == 1: #0x2221
                    count4 += 1
            elif count == 3 and k == 1:
                if count00 > 1 and retu < 5: #0x1110
                    retu = 5
                    count3 += 0.1
                elif count00 == 1: #0x1112
                    count3 += 1
            elif count == 2 and count00 == 3:
                if k == 2:            #0x2200
                    count4 += 1
                elif k == 1:          #0x1100
                    count3 += 1

    # 这个循环是为了找出0x2020或者x2202这两种（实际有12*2种）
    for k in range(2,0,-1): # k为棋子颜色，2或1
        markP = 0
        for n in range(-1,3,2):  # 又加了一重循环，主要作用是先向右再向左搜索一遍，再数个数；第二次，先向左再向右搜索，再数个数，主要是为了排除120x2020这种情况，避免和0x2020混淆
            count = 0    # 数连续（忽略一个空位）棋子的个数
            count00 = 0  # 记录中间空位的个数，必须要有一个
            count01 = 0  # 记录两侧空位的个数
            for m in range(-1*n,3*n,2*n):  # 第一次取值(1,-1)，第二次(-1,1)
                for i,j in zip(range(xx-m,xx-5*m,-m),range(yy+m,yy+5*m,m)):
                    if 0 < i < size+1 and 0 < j < size+1 and chess[i][j] == k:  # 不超出范围且遇到同色棋子
                        count += 1
                    elif 0 < i < size+1 and 0 < j < size+1 and chess[i][j] == 0:  # 不超出范围且遇到空位
                        if count00 == 0:     # 还未遇到中间空位
                            if 0 < i-m < size+1 and 0 < j+m < size+1 and chess[i-m][j+m] == k: # 如果下一个还是同色
                                if i != markP:
                                    markP = i
                                    count00 = 1
                                else:
                                    break
                            else:
                                count01 += 1
                                break
                        elif count00 == 1:   # 已经遇到中间空位
                            count01 += 1
                            break
                    else:                  # 遇到异色棋子或者超出范围，也就是被挡住
                        break
            if count == 3 and count00 == 1:
                if k == 2:         #x0222
                    count4 += 1
                if k == 1:         #x1011
                    count3 += 1
            if count == 2 and count00 == 1 and count01 == 2:
                if k == 2:         #0x2020
                    count4 += 1
                if k == 1:         #01x020
                    count3 += 1
    # 限定每一个大方向上c3和c4不大于1
    if count4:
        if isinstance(count4,int):
            count4 = 1
        else:
            count4 = 1.1
    if count3:
        if isinstance(count3,int):
            count3 = 1
        else:
            count3 = 1.1
    # 补充一个特殊情况21110x01112
    if 0<xx-4 and xx+4<size+1 and 0<yy-4 and yy+4<size+1:
        for k in range(2,0,-1):
            if xx+5<size+1 and 0<yy-5 and chess[xx+5][yy-5]!=k and chess[xx+5][yy-5]!=0 or xx+5>size or yy-5<1:
                if 0<xx-5 and yy+5<size+1 and chess[xx-5][yy+5]!=k and chess[xx-5][yy+5]!=0 or xx-5<1 or yy+5>size:
                    if chess[xx+4][yy-4]==k and chess[xx+3][yy-3]==k and chess[xx+2][yy-2]==k and chess[xx+1][yy-1]==0:
                        if chess[xx-4][yy+4]==k and chess[xx-3][yy+3]==k and chess[xx-2][yy+2]==k and chess[xx-1][yy+1]==0:                    
                            if k == 2:
                                count4 += 2
                            elif k == 1:
                                count3 += 2
    count6 += count4
    count5 += count3






    # 如果c5、c6>=2，给予优先级3和4
    if count6 >= 2:
        if isinstance(count6,int) and retu < 4:
            retu = 4
        elif isinstance(count6,int) == False and retu < 6.5:
            retu = 6.5 # 又额外加了6.5和5.5这两个优先级，补充了在优先级为3时的有一个方向上是活4的情况
    if count5 >= 2:
        if isinstance(count5,int) and retu < 3:
            retu = 3
        elif isinstance(count5,int) == False and retu < 5.5:
            retu = 5.5

    return retu

# 判断输赢的方法
def gameover (xx, yy):
    global isplaying
    over = 0 # 判断是否有五子连珠的情况
    x1 = xx   # 记录起始坐标
    y1 = yy
    x2 = xx
    y2 = yy
    if isplaying:
        count = 0 
        for i in range(xx + 1, size+1):
            if chess[i][yy] == chess[xx][yy]:
                count += 1
                x1 = i
                y1 = yy
            else:
                break
        for i in range(xx, 0, -1):
            if chess[i][yy] == chess[xx][yy]:
                count += 1
                x2 = i
                y2 = yy
            else:
                break
        if count >= 5:
            isplaying = 0
            over = 1
        else:
            x1 = xx  # 复原
            y1 = yy
            x2 = xx
            y2 = yy

    if isplaying:            
        count = 0
        for i in range(yy + 1, size+1):
            if chess[xx][i] == chess[xx][yy]:
                count += 1
                x2 = xx
                y2 = i
            else:
                break
        for i in range(yy, 0, -1):
            if chess[xx][i] == chess[xx][yy]:
                count += 1
                x1 = xx
                y1 = i
            else:
                break
        if count >= 5:
            isplaying = 0
            over = 1
        else:
            x1 = xx  # 复原
            y1 = yy
            x2 = xx
            y2 = yy

    if isplaying:            
        count = 0
        for i, j in zip(range(xx+1, size+1), range(yy+1, size+1)):
            if chess[i][j] == chess[xx][yy]:
                count += 1
                x1 = i
                y1 = j
            else:
                break
        for i, j in zip(range(xx, 0, -1), range(yy, 0, -1)):
            if chess[i][j] == chess[xx][yy]:
                count += 1
                x2 = i
                y2 = j
            else:
                break
        if count >= 5:
            isplaying = 0
            over = 1
        else:
            x1 = xx  # 复原
            y1 = yy
            x2 = xx
            y2 = yy

    if isplaying:            
        count = 0
        for i, j in zip(range(xx - 1, 0, -1), range(yy + 1, size+1)):
            if chess[i][j] == chess[xx][yy]:
                count += 1
                x1 = i
                y1 = j                
            else:
                break
        for i, j in zip(range(xx, size+1), range(yy, 0, -1)):
            if chess[i][j] == chess[xx][yy]:
                count += 1
                x2 = i
                y2 = j                
            else:
                break
        if count >= 5:
            isplaying = 0
            over = 1

    if over:
        if chess[xx][yy] == 1:
            canvas.create_line(x1*30, y1*30, x2*30, y2*30, width=2, fill="red", tags = ('win'))
            tkinter.messagebox.showinfo("", "you win")
        else:
            canvas.create_line(x1*30, y1*30, x2*30, y2*30, width=2, fill="cyan", tags = ('win'))
            tkinter.messagebox.showinfo("", "you lose")

# 创建窗体
tk = Tk()
tk.title("五子棋")
tk.geometry("480x480")
# 窗体上加画布
canvas = Canvas(tk, width=500, height=500)
canvas.pack(expand = YES, fill = BOTH)

# 给画布加监听
canvas.bind("<Button-1>", mod1)         # 单击 正常下棋
canvas.bind("<Button-3>", mod2)         # 右击 只下黑棋
canvas.bind("<Button-2>", mod3)         # 中击 只下白棋
canvas.bind("<Double-Button-2>", mod4)  # 双击中键 重新开始
canvas.bind("<Double-Button-3>", mod4)  # 双击右键 重新开始
canvas.bind("<Button-4>", mod4)         # 滚轮上滑 重新开始 不过不起作用？
canvas.bind("<Button-5>", mod4)         # 滚轮下滑 同上 对win10系统不起作用

# 画棋盘
for num in range(1, size+1): # 划竖线
    canvas.create_line(num*30, 30, num*30, 450, width=2) 
for num in range(1, size+1): # 划横线
    canvas.create_line(30, num*30, 450, num*30, width=2)
tk.mainloop()

# 当左右两侧棋子颜色一致，权值要加强（未考虑）
