# -*- coding: utf-8 -*- 

import sys
import os.path
import discord
from discord.ext import commands,tasks
from discord.utils import get
import random
import math
import time
import asyncio
import string
import pymysql
import hashlib
from urllib.request import urlopen
from bs4 import BeautifulSoup   
import re
import datetime
from pytz import timezone
import threading
import schedule

#region setting

version="V1.3.7"

def makestring() :
    result1=""
    string_pool=string.ascii_letters+string.digits
    for i in range(20) :
        result1=result1+random.choice(string_pool)
    return result1

bot = commands.Bot(command_prefix='GnK')
token = "main12345"
test_token="test12345"

mapnormal = 'WKC 코리아 서킷,쥐라기 공룡 무덤,브로디 비밀의 연구소,월드 뉴욕 대질주,쥐라기 공룡 결투장,월드 두바이 다운타운,사막 놀라운 공룡 유적지,신화 신들의 세계,비치 해변 드라이브,빌리지 고가의 질주,WKC 싱가폴 마리나 서킷,WKC 상해 서킷,월드 리오 다운힐,빌리지 익스트림 경기장,빌리지 남산,어비스 운명의 갈림길'

maphard='월드 이탈리아 피사의 사탑,WKC 브라질 서킷,네모 산타의 비밀공간,네모 강철바위 용광로,도검 구름의 협곡,대저택 은밀한 지하실,차이나 골목길 대질주,차이나 서안 병마용,황금문명 오리엔트 황금 좌표,황금문명 비밀장치의 위협,해적 로비 절벽의 전투,빌리지 만리장성,어비스 바다 소용돌이,사막 빙글빙글 공사장,공동묘지 해골성 대탐험,카멜롯 펜드래건 캐슬,카멜롯 외곽 순찰로'

mapveryhard='노르테유 익스프레스,광산 3개의 지름길,광산 위험한 제련소,광산 꼬불꼬불 다운힐,동화 이상한 나라의 문,쥐라기 공룡섬 대모험,어비스 스카이라인,어비스 숨겨진 바닷길,문힐시티 숨겨진 지하터널,공동묘지 마왕의 초대,포레스트 지그재그,팩토리 미완성 5구역,빌리지 붐힐터널'

mapitem='동화 카드왕국의 미로,차이나 빙등 축제,빌리지 두개의 관문,네모 구구 둥지,빌리지 운하,신화 빛의 길,월드 리오 다운힐,쥐라기 아슬아슬 화산 점프,비치 여객선,대저택 루이의 서재,차이나 서안 병마용,차이나 상해 동방명주,노르테유 허공의 갈림길,광산 3개의 지름길,아이스 신나는 하프파이프,사막 피라미드 탐험,포레스트 통나무,포레스트 골짜기,카멜롯 기사단 훈련장'

mapall=[]

for i in mapnormal.split(',') : 
    mapall.append(i)

for i in maphard.split(',') : 
    mapall.append(i)

for i in mapveryhard.split(',') : 
    mapall.append(i)

#endregion




@bot.event
async def on_message(ctx) :
    await bot.process_commands(ctx)


@bot.event
async def on_ready():
    print("bot login test")
    print(bot.user.name)
    print(bot.user.id)
    print("-----------")
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(f'GnK봇 {version}'))




class Map:
    def __init__(self,mapnormal,maphard,mapveryhard,mapitem):
        self.normal = mapnormal.split(',')
        self.hard = maphard.split(',')
        self.veryhard = mapveryhard.split(',')
        self.mapall=[]
        self.mapitem=mapitem.split(',')

        for i in self.normal:
            self.mapall.append(i)
        for i in self.hard :
            self.mapall.append(i)
        for i in self.veryhard:
            self.mapall.append(i)


    def getAllMap(self):
        return self.mapall

    def get_data(self,mode,amount) :
        if mode==1 : 
            data= random.sample(self.normal,amount)
        elif mode==2 : 
            data= random.sample(self.hard,amount)
        elif mode==3 : 
            data= random.sample(self.veryhard,amount)
        elif mode==4 :
            data= random.sample(self.mapall,amount)
        elif mode==5 : 
            data=random.sample(self.mapitem,amount)
        else :
            data="1:노멀 2:하드 3:베리하드 4:전체(1~3) 5:아이템"
        return data

    def getmap(self,mode,amount=5) : 
        data=[]
        data=self.get_data(mode,amount)
        return data

maps=Map(mapnormal,maphard,mapveryhard,mapitem)

@bot.command()
async def 안녕(ctx): await ctx.send("안녕")

@bot.command()
async def 맵추첨(ctx,mode,amount) :
    await ctx.send(f"{maps.getmap({int(mode)},{int(amount)})}")

async def all_list(ctx,mode) : 
    print(mode)
    if mode==1 : 
        await ctx.send(("```"+mapnormal.replace(",","\n")+"```"))
    elif mode==2 : 
        await ctx.send("```"+maphard.replace(",","\n")+"```")
    elif mode==3 : 
        await ctx.send("```"+mapveryhard.replace(",","\n")+"```")
    elif mode==4 :
        data=""
        for i in mapall : 
            data=data+i+"\n"
        await ctx.send('```'+data+'```')
    else :
        await ctx.send("```"+mapitem.replace(",","\n")+"```")

@bot.command()
async def 리스트(ctx,mode=100):
    if int(mode)>0 and int(mode)<=5 :
        await all_list(ctx,int(mode))
    else :
        await ctx.send("1:노멀 2:하드 3:베리하드 4:전체(1~3) 5:아이템") 

@bot.command()
async def 버전(ctx):
    await ctx.send(version)

@bot.command()
async def 킹오hi(ctx): await ctx.send("킹오야 안녕")

@bot.command()
async def 욕해줘(ctx): await ctx.send("ㅅㅂ")

@bot.command()
async def 아잉련아(ctx): await ctx.send("?????????")

@bot.command()
async def 새벽(ctx): await ctx.send("에도 켜져있음")

@commands.cooldown(1, 5, commands.BucketType.default)
@bot.command()
async def 가입(ctx,nickname=None) : 
    nicknames=[]
    con=connectsql(True)
    cur=con.cursor()
    if len(nickname)>3 and len(nickname)<11 : 
        sql=f"select EXISTS (select * from user_info where discorduserid={ctx.author.id})"
        cur.execute(sql)
        data=cur.fetchone()
        if int(data)==0 :
            sql=f"select EXISTS (select * from user_info where nickname={nickname})"
            cur.execute()
            data=cur.fetchone()
            if int(data)==0:
                result1=makestring()
                sql="insert into user_info (nickname,discorduserid,login_string) values (%s,%s,%s)"
                val=(str(nickname),ctx.author.id,result1)
                cur.execute(sql,val)
                sql="insert into item_money_have (nickname,discorduserid) values (%s,%s)"
                val=(str(nickname),ctx.author.id)
                cur.execute(sql,val)
                await ctx.author.send(f"가입에 성공했습니다. 고유 확인 문자열은 {result1}입니다.")
                return
            else :
                await ctx.author.send("중복 된 닉네임입니다.")
                return
        else :
            await ctx.author.send("이미 가입이 되어 있습니다.")
            return
    else : 
        await ctx.author.send("닉네임 제한 4~10, 한글3 영어1")





@bot.command()
async def 리그에결(ctx) : 
    ace=[]
    webpage=urlopen("http://gin7174.dothome.co.kr/recommand1v1.html")
    soup=BeautifulSoup(webpage,"html.parser")
    div=soup.find_all('a')
    print(div)
    for i in div : 
        ace.append(f"{i['href']}   {re.sub('<.+?>','',str(i),0).strip()}")
    await ctx.send(random.choice(ace))

        
@bot.command()
async def 문의(ctx):
    count=0
    nickname=""
    con=connectsql(False)
    cur=con.cursor()
    sql = f"select count(*) from gnkquestion"
    cur.execute(sql)
    datas=cur.fetchone()
    print(datas)
    for i in datas :
        count=i+1
    guild = ctx.guild
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True,send_messages=True),
    }
    sql=f"select nickname from user_info where discorduserid='{ctx.author.id}'"
    sql2=f"insert into gnkquestion values('{count}','{nickname}')"
    await guild.create_role(name="문의 "+str(count))
    cate = discord.utils.get(guild.categories,name="문의")
    server = ctx.guild
    user = ctx.message.author
    channel = await guild.create_text_channel("문의 "+str(count), overwrites=overwrites,category=cate)
    owner = bot.get_user(382938103435886592) 
    cur.execute(sql)
    datas=cur.fetchone()
    for i in datas : 
        nickname=i
    cur.execute(sql2)
    con.commit()
    con.close()
    await owner.send("문의가 들어왔습니다!")
    await ctx.author.send("문의-"+str(count)+" 게시판이 만들어졌습니다! 이 게시판에서 문의를 해주세요!")



@bot.command()
async def 내전(ctx) : 
    webpage=urlopen("http://gin7174.dothome.co.kr/inclubgame.html")
    soup=BeautifulSoup(webpage,"html.parser")
    div=str(soup.find('div'))
    div=re.sub('<.+?>','',div,0).strip()
    await ctx.send(div)


bot.run(token)