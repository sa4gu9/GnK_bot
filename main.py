# -*- coding: utf-8 -*- 

import sys
import os.path
import discord
from discord.ext import commands
import random
import math

members=[]
path='''C:\\Users\\user\\Desktop\\discord bot\\user info.txt'''
if os.path.isfile(path):
    with open(path,"r") as tf:
        line=None
        while line != '':
            line=(tf.readline())
            print(line.strip('\n'))
            temp1=line.strip('\n').split(',')
            for i in temp1 :
                if len(i)==18 : 
                    members.append(int(i))
else : 
    tf = open(path,"w")
tf.close()

print(members)

bot = commands.Bot(command_prefix='GnK')
token = "NjYxMTc5OTgzNzAzNTcyNDkx.Xp5u9Q.ciODDc8YvlAfXS8CjW4ni6lyaHQ"

map1v1 = '비치 해변 드라이브,쥐라기 공룡 무덤,브로디 비밀의 연구소,네모 산타의 비밀공간,빌리지 고가의 질주,월드 리오 다운힐,도검 구름의 협곡,신화 신들의 세계,WKC 코리아 서킷,차이나 서안 병마용'#10

mapnormal = '브로디 비밀의 연구소,월드 뉴욕 대질주,쥐라기 공룡섬 결투장,월드 두바이 다운타운,사막 놀라운 공룡 유적지,신화 신들의 세계,비치 해변 드라이브,빌리지 고가의 질주,WKC 싱가폴 마리나 서킷,WKC 상해 서킷,월드 리오 다운힐,빌리지 익스트림 경기장,빌리지 남산'#13

maphard='월드 이탈리아 피사의 사탑,WKC 브라질 서킷,네모 산타의 비밀공간,네모 강철바위 용광로,도검 구름의 협곡,대저택 은밀한 지하실,차이나 골목길 대질주,차이나 서안 병마용,황금문명 오리엔트 황금 좌표,황금문명 비밀장치의 위협,해적 로비 절벽의 전투,빌리지 만리장성,어비스 바다 소용돌이,사막 빙글빙글 공사장'#14

mapveryhard='노르테유 익스프레스,광산 3개의 지름길,광산 위험한 제련소,광산 꼬불꼬불 다운힐,동화 이상한 나라의 문,쥐라기 공룡섬 대모험,어비스 스카이라인,어비스 숨겨진 바닷길,문힐시티 숨겨진 지하터널,공동묘지 마왕의 초대,포레스트 지그재그,팩토리 미완성 5구역,빌리지 붐힐터널'#13


mapall=[]

for i in map1v1.split(',') : 
    mapall.append(i)

temp=0

for i in mapnormal.split(',') : 
    for j in mapall :
        if i==j : 
            break
        else :
            temp=temp+1
        if temp==len(mapall):
            mapall.append(i)
            temp=0

for i in maphard.split(',') : 
    for j in mapall :
        if i==j : 
            break
        else :
            temp=temp+1
        if temp==len(mapall):
            mapall.append(i)
            temp=0

for i in mapveryhard.split(',') : 
    for j in mapall :
        if i==j : 
            break
        else :
            temp=temp+1
        if temp==len(mapall):
            mapall.append(i)
            temp=0

print(mapall)


command="도와줘,안녕,에결,에결리스트,노멀,노멀리스트,하드,하드리스트,베리하드,베리하드리스트,전체,전체리스트,버전,추천,가입테스트,가입,모아,베팅,그리고 숨겨진 몇개의 명령어들"

commandlist="도와줘,안녕,에결,에결리스트,노멀,노멀리스트,하드,하드리스트,베리하드,베리하드리스트,전체,전체리스트,버전,추천,킹오hi,욕해줘,아잉련아,새벽,가입테스트"

@bot.event
async def on_ready():
    print("bot login test")
    print(bot.user.name)

    print(bot.user.id)
    print("-----------")
    await bot.change_presence(status=discord.Status.online,activity=discord.Game('도움말 : GnK도와줘'))

@bot.command()
async def 도와줘(ctx): await ctx.send("```"+command.replace(",","\n")+"```")

@bot.command()
async def 안녕(ctx): await ctx.send("안녕")

@bot.command()
async def 에결(ctx): await ctx.send("```"+random.choice(map1v1.split(','))+"```")

@bot.command()
async def 에결리스트(ctx):
    await ctx.send(("```"+map1v1.replace(",","\n")+"```"))

@bot.command()
async def 노멀(ctx): await ctx.send("```"+random.choice(mapnormal.split(','))+"```")

@bot.command()
async def 노멀리스트(ctx):
    await ctx.send(("```"+mapnormal.replace(",","\n")+"```"))

@bot.command()
async def 하드(ctx): await ctx.send("```"+random.choice(maphard.split(','))+"```")

@bot.command()
async def 하드리스트(ctx):
    await ctx.send("```"+maphard.replace(",","\n")+"```")

@bot.command()
async def 베리하드(ctx): await ctx.send("```"+random.choice(mapveryhard.split(','))+"```")

@bot.command()
async def 베리하드리스트(ctx):
    await ctx.send("```"+mapveryhard.replace(",","\n")+"```")

@bot.command()
async def 전체(ctx,amount=None):
    if amount==None:
        amount=10
    data=random.sample(mapall,int(amount))
    str1=""
    for i in data:
        str1=str1+i+"\n"
    await ctx.send("```"+str1+"```")

@bot.command()
async def 전체리스트(ctx):
    data=""
    for i in mapall : 
        data=data+i+"\n"
    await ctx.send('```'+data+'```')

@bot.command()
async def 버전(ctx):
    await ctx.send("V1.0.3")

@bot.command()
async def 추천(ctx): await ctx.send("```"+random.choice(commandlist.split(','))+"```")    

@bot.command()
async def 가입테스트(ctx): await ctx.send("https://cdn.discordapp.com/attachments/702739996947251234/703170259322011679/unknown.png"+"\n필수 : 연구소, 로비, 협곡, 산타 중 2개 선택\n선택 : 나머지 맵들 중 2개 선택\n\n기회 맵당 3번")

#숨겨진 몇몇 명령어들
@bot.command()
async def 킹오hi(ctx): await ctx.send("킹오야 안녕")

@bot.command()
async def 욕해줘(ctx): await ctx.send("ㅅㅂ")

@bot.command()
async def 아잉련아(ctx): await ctx.send("?????????")

@bot.command()
async def 새벽(ctx): await ctx.send("에도 켜져있음")

@commands.cooldown(1, 20, commands.BucketType.user)
@bot.command()
async def 가입(ctx) : 
    f = open(path,"a")
    if not ctx.author.id in members :
        f.write(str(len(members))+",")
        f.write(str(ctx.author.id)+",")
        f.write(str(5000).zfill(8)+","+"\n")
        members.append(ctx.author.id)
        await ctx.send("가입 성공!")
    else :
        await ctx.send("이미 가입이 되어 있습니다.")
    f.close()

@commands.cooldown(1, 20, commands.BucketType.user)
@bot.command()
async def 모아(ctx) : 
    t1 = members.index(ctx.author.id)
    print(t1)
    f=open(path)
    lines=f.readlines()
    tps = lines[t1].split(',')
    print(tps)
    for i in tps : 
        if len(str(i))==8 : 
            await ctx.send(int(i))
    print("모아 명령어 작동 완료")

@commands.cooldown(1, 20, commands.BucketType.user)
@bot.command()
async def 베팅(ctx,moa=None,mode=None) : 
    end=0
    whole=""
    lose=0
    chance=0
    profit=0
    money=0
    multiple=0
    t1 = members.index(ctx.author.id)
    with open(path) as f:
        whole=f.read()
        f.seek(0)
        lines=f.readlines()
        tps = lines[t1].split(',')
        for i in tps : 
            if len(str(i))==8 : 
                money=int(i)
                f.close()
    if money<int(moa) : 
        await ctx.send("보유량보다 많이 베팅할수 없습니다.")
        return
    if moa==None : 
        await ctx.send("GnK베팅 거실돈 모드\n(모드 종류 : 1 80% 1.4배, 2 64% 1.8배, 3 48% 2.2배, 4 32% 2.6배, 5 16% 3배)")
        return
    else :
        lose=int(moa)
        print("lose : "+str(lose))
        if int(mode)==1 : 
            chance=80
            multiple=1.4
        if int(mode)==2 : 
            chance=64
            multiple=1.8
        if int(mode)==3 : 
            chance=48
            multiple=2.2
        if int(mode)==4 : 
            chance=32
            multiple=2.6
        if int(mode)==5 : 
            chance=16
            multiple=3       
    if int(mode)<6 and int(mode)>0 : 
        result=random.randrange(0,100)
        print(str(result)+" "+str(chance))
        if result<chance : 
            profit=math.floor(multiple*int(moa))
            print(profit)
            print(lose)
            print(money)
            end=money-lose+profit
            whole=whole.replace((str(ctx.author.id)+","+str(money).zfill(8)),(str(ctx.author.id)+","+str(end).zfill(8)))
            await ctx.send("축하합니다!"+str(moa)+"모아에서 "+str(profit)+"모아가 되었습니다!")
        else :
            end=money-lose
            whole=whole.replace((str(ctx.author.id)+","+str(money).zfill(8)),(str(ctx.author.id)+","+str(end).zfill(8)))
            await ctx.send("아쉽습니다. "+str(moa)+"모아를 잃으셨습니다.")
        files=open(path,"w")
        print(whole)
        files.write(whole)
        files.close()                             
    else : 
        await ctx.send("모드를 선택해주세요. 1 80% 1.4배, 2 64% 1.8배, 3 48% 2.2배, 4 32% 2.6배, 5 16% 3배")
    print("베팅 명령어 작동 완료")
    

bot.run(token)