# -*- coding: cp936 -*-

fr=open('public.txt')
arrayLines=fr.readlines()
del arrayLines[0:3]
classLabelVector=[]
dataMat=zeros((1000,2))
index=0
for line in arrayLines:
    listFromLine=line.strip.split('\t')
    dataMat[index,:]=listFromLine[0:2]
    classLabelVector.append(int listFromLines[-1])
    index+=1

bad=0
good=0
badshifuMat=[]
goodshifuMat=[]
for i in range(1000):
    if classLabelVector[i]==1:
        bad+=1
    else:
        good+=1
        goodshifuMat.append(datMat[i])

print good/float(1000)
one=0
two=0
thr=0
fou=0
five=0
six=0
seven=0
eight=0
nine=0
ten=0
for j in len(goodshifuMat):
    if goodshifuMat[j][0]==1:
        one+=1
    if  goodshifu[j][0]==2:
        two+=1
    if goodshifu[j][0]==3:
        three+=1
    if goodshifu[j][0]==4:
        fou+=1
    if goodshifu[j][0]==5:
        five+=1
    if goodshifu[j][0]==6:
        six+=1
    if goodshifu[j][0]==7:
        seven+=1
    if goodshifu[j][0]==8:
        eight+=1
    if goodshifu[j][0]==9:
        nine+=1
    else:
        ten+=1

print one/float(len(goodshifuMat)),',',two/float(len(goodshifuMat)),',',three/float(len(goodshifuMat)),',',fou/float(len(goodshifuMat)),',', five/float(len(goodshifuMat)),',',six/float(len(goodshifuMat)),',',seven/float(len(goodshifuMat)),',',eight/float(len(goodshifuMat)),',',nine/float(len(goodshifuMat)),',',ten/float(len(goodshifuMat))


p2=good/float(1000)                    # 好师傅的先验概率
pf2=nine/float(len(goodshifuMat))        #是好师傅好友个数为9的条件概率
cgoodcount9=0
for k in len(goodshifuMat):
    if goodshifuMat[k,1]==9:
        cgoodcout+=1
pc2=cgoodcount/float(len(goodshifuMat))      #是好师傅聊天次数为9的条件概率


fcount9=0
ccout9=0
for i in 1000:
    if dataMat[i][0]==9:
        fcount9+=1
    if daMat[i][1]==9:
        ccount9+=1

pf=fcount9/float(len(dataMat))             #好友个数为9的概率
pc=ccout9/float(len(dataMat))              #聊天次数为9的概率

print  pf2*pc2*p2/float(pf*pc)          #给定fchatnum=9，cchatnum=9的玩家是好师父的概率




























