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

#region setting

version="V1.2.1.3"

members=[]

con = pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",db="gnkscore",autocommit=True)
cur=con.cursor()
sql="select * from user_info;"
cur.execute(sql)
datas=cur.fetchall()
con.close()
for data in datas : 
    print(data[7])
    members.append(data[7])
    print(members)



path='''user info.txt'''
path2='betting stat.txt'

bot = commands.Bot(command_prefix='GnK')
token = "NjYxMTc5OTgzNzAzNTcyNDkx.Xp5u9Q.ciODDc8YvlAfXS8CjW4ni6lyaHQ"

map1v1 = '비치 해변 드라이브,쥐라기 공룡 무덤,브로디 비밀의 연구소,네모 산타의 비밀공간,빌리지 고가의 질주,월드 리오 다운힐,도검 구름의 협곡,신화 신들의 세계,WKC 코리아 서킷,차이나 서안 병마용'#10

mapnormal = '브로디 비밀의 연구소,월드 뉴욕 대질주,쥐라기 공룡 결투장,월드 두바이 다운타운,사막 놀라운 공룡 유적지,신화 신들의 세계,비치 해변 드라이브,빌리지 고가의 질주,WKC 싱가폴 마리나 서킷,WKC 상해 서킷,월드 리오 다운힐,빌리지 익스트림 경기장,빌리지 남산,어비스 운명의 갈림길'

maphard='월드 이탈리아 피사의 사탑,WKC 브라질 서킷,네모 산타의 비밀공간,네모 강철바위 용광로,도검 구름의 협곡,대저택 은밀한 지하실,차이나 골목길 대질주,차이나 서안 병마용,황금문명 오리엔트 황금 좌표,황금문명 비밀장치의 위협,해적 로비 절벽의 전투,빌리지 만리장성,어비스 바다 소용돌이,사막 빙글빙글 공사장,공동묘지 해골성 대탐험'

mapveryhard='노르테유 익스프레스,광산 3개의 지름길,광산 위험한 제련소,광산 꼬불꼬불 다운힐,동화 이상한 나라의 문,쥐라기 공룡섬 대모험,어비스 스카이라인,어비스 숨겨진 바닷길,문힐시티 숨겨진 지하터널,공동묘지 마왕의 초대,포레스트 지그재그,팩토리 미완성 5구역,빌리지 붐힐터널'


mapall=[]


for i in map1v1.split(',') : 
    mapall.append(i)

for i in mapnormal.split(',') : 
    if not i in mapall : 
        mapall.append(i)

for i in maphard.split(',') : 
    if not i in mapall : 
        mapall.append(i)

for i in mapveryhard.split(',') : 
    if not i in mapall : 
        mapall.append(i)

print(mapall)

#endregion

@bot.event
async def on_message(ctx) :
    role = discord.utils.find(lambda r: r.name == 'Muted',ctx.guild.roles)
    tester = discord.utils.find(lambda r: r.name == '테스터',ctx.guild.roles)
    if role in ctx.author.roles :
        t1=ctx.author.id
        con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore",autocommit=True)
        cur=con.cursor()
        sql=f"update user_info set moa=moa-4000 where discorduserid={t1}"
        print(sql)
        cur.execute(sql)
        con.commit()
        await ctx.delete()
        await ctx.author.send(f'mute 상태에서 채팅을 쳐서 4000모아를 잃었습니다.')
        print(ctx.author.roles)
    if not tester in ctx.author.roles : 
        await bot.process_commands(ctx)
    else : 
        print("123456") 

@bot.event
async def on_ready():
    print("bot login test")
    print(bot.user.name)
    print(bot.user.id)
    print("-----------")
    await bot.change_presence(status=discord.Status.online,activity=discord.Game(f'GnK봇 {version}'))
    job_thread=threading.Thread(target=luckypang)
    coin_thread=threading.Thread(target=GnKcoin)
    job_thread.start()
    coin_thread.start()
    bot.loop.create_task(luckypang())
    bot.loop.create_task(GnKcoin())

async def luckypang():
    nickname2=""
    discorduser=""
    money2=0
    end2=0
    channel=bot.get_channel(713050090486366380)
    while True : 
        timenow=datetime.datetime.now(timezone('Asia/Seoul'))
        timenow_str=str(timenow)
        if timenow_str[11:23]=="12:30:00.000" or timenow_str[11:23]=="18:30:00.000" or timenow_str[11:23]=="08:20:00.000" : 
            con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",db="gnkscore")
            cur=con.cursor()
            sql=f"select pangprice from betstat"
            cur.execute(sql)
            datas=cur.fetchall()
            getusers=[]
            for i in datas : 
                luckym=i[0]
            for i in range(30) :
                getusers.append(random.randrange(0,len(members)))
            getuser=random.choice(getusers)
            sql=f"select nickname,moa,discorduserid from user_info where indexid='{getuser+1}'"
            cur.execute(sql)
            datas=cur.fetchall()
            for i in datas :
                nickname2=i[0]
                money2=i[1]
                discorduser=i[2]    
            end2=money2+luckym
            sql=f"update user_info set moa={end2} where indexid={getuser+1}"
            sql2=f"update betstat set pangprice=0"
            cur.execute(sql)
            cur.execute(sql2)
            con.commit()
            user=bot.get_user(int(discorduser))
            await channel.send(str(nickname2)+"님이 럭키팡에 당첨되어 "+str(luckym)+"모아를 받았습니다!")
            await user.send(str(nickname2)+"님 축하합니다! 럭키팡에 당첨되어 "+str(luckym)+"모아를 받았습니다!")
            con.close()
        await asyncio.sleep(0.001)

async def GnKcoin():
    change=1
    channel=bot.get_channel(713050090486366380)
    price=0
    maxprice=0
    price0=0
    lucky=0
    updown=""
    ratio=0
    while True : 
        timenow=datetime.datetime.now(timezone('Asia/Seoul'))
        timenow_str=str(timenow)
        if timenow_str[14:23]=="00:00.000" or timenow_str[14:23]=="20:00.000" or timenow_str[14:23]=="40:00.000" : 
            sql="select * from gnkcoin"
            con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
            cur=con.cursor()
            cur.execute(sql)
            datas=cur.fetchall()
            for i in datas : 
                price=i[0]
                maxprice=i[1]
                price0=i[2]
            if timenow_str[11:15]=="09:00" : 
                change=1
                await channel.send("지금부터 오후 8시 40분까지 30분마다 GnKcoin의 가격이 바뀝니다! 현재 가격은 {price}입니다.")
            elif timenow_str[11:15]=="20:40" : 
                change=0
                await channel.send(f"지금부터 오전 9시까지 GnKcoin의 가격이 바뀌지 않습니다! 현재 가격은 {price}입니다.")
            else : 
                #region 가격이 바뀌는 코드
                if price==0 : 
                    price=800000
                    sql=f"update user_info set coin=0"
                    sql2=f"update gnkcoin set price=800000"
                    cur.execute(sql)
                    cur.execute(sql2)
                    con.commit()
                    await channel.send(f"전 가격이 0원이어서 80만에서 다시 시작합니다! 가지고있던 코인은 리셋됩니다.")
                elif change==1 : 
                    lucky = random.randrange(100)
                    if lucky<15 : 
                        updown="up"
                    else : 
                        updown="down"
                    lucky = random.randrange(100)
                    if lucky< 12 :
                        ratio=0.01
                    elif lucky<20:
                        ratio=0.05
                    elif lucky<30:
                        ratio=0.1
                    elif lucky<45 :
                        ratio=0.2
                    elif lucky<62:
                        ratio=0.3
                    elif lucky<79 : 
                        ratio=0.4
                    elif lucky<83 : 
                        ratio=0.5
                    elif lucky<88 :
                        ratio=0.8
                    else :
                        ratio=1
                    if updown=="up" : 
                        price=math.floor(price*(1+ratio))
                        sql=f"update gnkcoin set price={price}"
                        print(sql)
                        cur.execute(sql)
                        con.commit()
                    else : 
                        price=math.floor(price*(1-ratio))
                        sql=f"update gnkcoin set price={price}"
                        print(sql)
                        cur.execute(sql)
                        con.commit()
                    if not price==0 :
                        await channel.send(f"GnKcoin의 가격이 바꼈습니다! 현재 가격은 {price}입니다.")
                    else :
                        await channel.send(f"GnKcoin의 가격이 바꼈습니다! 현재 가격은 {price}입니다. 0원이므로 거래가 불가능합니다.")
                        sql=f"update gnkcoin set price0=price0+1"
                        cur.execute(sql)
                        con.commit()
                #endregion
        await asyncio.sleep(0.001)




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
    await ctx.send(version)

# @bot.command()
# async def 추천(ctx): await ctx.send("```"+random.choice(commandlist.split(','))+"```")    

@bot.command()
async def 가입테스트(ctx): await ctx.send("https://cdn.discordapp.com/attachments/702739996947251234/703170259322011679/unknown.png"+"\n필수 : 연구소, 로비, 협곡, 산타 중 2개 선택\n선택 : 나머지 맵들 중 2개 선택\n\n기회 맵당 3번")


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
    con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore",autocommit=True)
    cur=con.cursor()
    if len(nickname)>3 and len(nickname)<11 : 
        if not ctx.author.id in members : 
            string_pool=string.ascii_letters+string.digits
            result1=""
            for i in range(20) : 
                result1=result1+random.choice(string_pool)
            print(string)
            print(members)
            num_user=0
            sql="select * from count_user;"
            sql2="insert into user_info (indexid,nickname,discorduserid,login_string) values (%s,%s,%s,%s)"
            sql3="select nickname from user_info;"
            sql4=f"update count_user set num_user = num_user+1"
            cur.execute(sql)
            datas=cur.fetchall()
            for data in datas :
                print(data)
                num_user=data[0]
            print(num_user)
            cur.execute(sql3)
            datas=cur.fetchall()
            nicks=str(nickname).lower()
            for data in datas : 
                print(data)
                temp=str(data[0]).lower()
                nicknames.append(temp)
                print(nicknames)
                print(nickname)
            if not nickname in nicknames : 
                salt="R9Wf2PN%qk9!Jn*Sd$PeB10iJ"
                hasing=hashlib.sha512()
                hasing.digest()
                result=hashlib.sha512((result1+salt).encode('utf-8')).hexdigest()
                print(result1)
                val = (str(num_user+1),str(nickname),str(ctx.author.id),str(result))
                print(val)
                cur.execute(sql2,val)
                cur.execute(sql4)
                con.close()
                members.append(ctx.author.id)
                await ctx.author.send(f"가입 성공! 당신의 로그인 문자열은 {result1}입니다.")
            else : 
                await ctx.author.send("사용할수 없는 닉네임입니다.")
        else :
            await ctx.author.send("이미 가입이 되어 있습니다.")
    else : 
        await ctx.author.send("닉네임 제한 4~10, 한글3 영어1")


@commands.cooldown(1, 1, commands.BucketType.default)
@bot.command()
async def 모아(ctx,nickname=None) : 
    con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
    cur=con.cursor()
    nick=""
    money=0
    if nickname==None : 
        t1 = ctx.author.id
        print(t1)
        sql=f"select nickname,moa from user_info where discorduserid='{t1}'"
        print(sql)
        cur.execute(sql)
        datas=cur.fetchall()
        for i in datas : 
            nick=i[0]
            money=i[1]
        await ctx.author.send(f'{nick}님의 모아는 {money}모아 입니다.')
    else : 
        sql=f"select moa from user_info where nickname='{nickname}'"
        print(sql)
        cur.execute(sql)
        data = cur.fetchall()
        for i in data :
            print(data)
            money=i[0]
        await ctx.send(f'{nickname} 님의 모아는 {money}모아 입니다.')
    con.close()
    print("모아 명령어 작동 완료")



@commands.cooldown(1, 10, commands.BucketType.default)
@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command()
async def 베팅(ctx,moa=None,mode=None,repeat=None) :
    if repeat==None : 
        repeat=1
    if int(repeat)<=10 and int(repeat)>0 : 
        total_profit=0
        start=0
        stats=[]
        for num in range(int(repeat)) : 
            con = pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore",autocommit=True)
            cur=con.cursor()
            sql=f"select * from betstat"
            cur.execute(sql)
            datas=cur.fetchall()
            for i in datas : 
                print(i)
                stats.append(i[0])
                stats.append(i[1])
            role = discord.utils.find(lambda r: r.name == 'Muted',ctx.guild.roles)
            if not role in ctx.author.roles :
                end=0
                lose=0
                chance=0
                profit=0
                money=0
                multiple=0
                t1 = ctx.author.id
                sql=f"select nickname,moa from user_info where discorduserid='{t1}'"
                cur.execute(sql)
                datas = cur.fetchall()
                for i in datas : 
                    nick=i[0]
                    money=i[1]
                    if num==0 : 
                        start=i[1]
                if money<int(moa) or int(moa)<0 : 
                    await ctx.author.send(nick+"님 보유량보다 많거나 0원 미만으로 베팅하실 수 없습니다.")
                    return
                elif moa==None : 
                    await ctx.author.send("GnK베팅 거실돈 모드\n(모드 종류 : 1 80% 1.4배, 2 64% 1.8배, 3 48% 2.2배, 4 32% 2.6배, 5 16% 3배)")
                    return
                else :
                    lose=int(moa)
                    if int(mode)==1 : 
                        chance=80
                        multiple=1.2
                    if int(mode)==2 : 
                        chance=64
                        multiple=1.6
                    if int(mode)==3 : 
                        chance=48
                        multiple=2.2
                    if int(mode)==4 : 
                        chance=32
                        multiple=3
                    if int(mode)==5 : 
                        chance=16
                        multiple=4       
                if int(mode)<6 and int(mode)>0 : 
                    result=random.randrange(0,100)
                    if result<chance : 
                        profit=math.floor(multiple*int(moa))
                        end=money-lose+profit
                        total_profit=total_profit-lose+profit
                        sql=f"update user_info set moa={end} where discorduserid='{t1}'"
                        sql3=f"insert into userbetstat (nickname,moa,mode,result) values ('{nick}',{int(moa)},{int(mode)},'success')"
                        cur.execute(sql)                       
                        cur.execute(sql3)
                    else :
                        total_profit=total_profit-lose
                        end=money-lose
                        stats[0]=int(stats[0])+1
                        if money>=10000000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.6)
                        elif money>=5000000 :
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.35)
                        elif money>=4000000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.3)
                        elif money>=3000000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.25)
                        elif money>=2000000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.2)
                        elif money>=1000000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.15)
                        elif money>=500000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.1)
                        else : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.05)
                        sql2=f"update user_info set moa={end} where discorduserid='{t1}'"
                        sql=f"update betstat set betcount=betcount+1, pangprice='{stats[1]}'"
                        sql3=f"insert into userbetstat (nickname,moa,mode,result) values ('{nick}',{int(moa)},{int(mode)},'fail')"
                        cur.execute(sql)
                        cur.execute(sql2)
                        cur.execute(sql3)
                        if stats[0]<=700 : 
                            await ctx.send(str(stats[0])+"번째 실패")
                        else : 
                            await ctx.send("700회를 넘겨서 실패 횟수를 알려주지 않습니다.")
                    if stats[0]>=1000 : 
                        print(stats[0])
                        stats[0]=0
                        sql=f"update user_info set moa=moa+100000 where discorduserid='{t1}'"
                        cur.execute(sql)
                        print(nick)
                        await ctx.send(f"총 1000번째로 실패하여 {nick}님이 100000모아를 받았습니다! 다시 0회부터 시작합니다.")
                    sql=f"update betstat set betcount={stats[0]}, pangprice={stats[1]}"
                    cur.execute(sql)
                else : 
                    await ctx.author.send("모드를 선택해주세요. 1 80% 1.2배, 2 64% 1.6배, 3 48% 2.2배, 4 32% 3배, 5 16% 4배")
                    break
            else : 
                ctx.author.send("구걸 상태라 베팅을 할 수 없습니다.")
                break
    else : 
        await ctx.author.send("1~10회만 반복 가능합니다.")
    con.close()
    if total_profit>=0 :
        await ctx.author.send(f"{nick}님 {str(start)}모아에서 {str(start+total_profit)}모아가 되었습니다. {total_profit}모아를 벌었습니다!")
    else : 
        await ctx.author.send(f"{nick}님 {str(start)}모아에서 {str(start+total_profit)}모아가 되었습니다. {total_profit}모아를 잃으셨습니다...")
    print("베팅 명령어 작동 완료")


@bot.command()
async def 구걸(ctx) : 
    role = discord.utils.find(lambda r: r.name == 'Muted',ctx.guild.roles)
    con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
    cur=con.cursor()
    if not role in ctx.author.roles :
        hour=7
        minute=0
        second=0
        money=0
        nick=""
        end=0
        t1 = ctx.author.id
        sql=f"update user_info set moa=moa+30000 where discorduserid='{t1}'"
        sql2=f"select nickname from user_info where discorduserid={t1}"
        print(sql)
        print(sql2)
        cur.execute(sql2)
        datas=cur.fetchall()
        for i in datas : 
            nick=i[0]
        cur.execute(sql)
        con.commit()
        member = ctx.message.author
        await member.add_roles(get(ctx.guild.roles,name="Muted"))
        await ctx.send(f'{nick}님이 구걸 하기 위해 {hour}시간 {minute}분 {second}초 뮤트 되어 30000모아를 지급하였습니다. 뮤트상태에서 채팅을 치면 4000모아를 뺏깁니다.')
        end=money+30000
        await asyncio.sleep(hour*60*60+minute*60+second)
        await member.remove_roles(get(ctx.guild.roles,name="Muted"))
    else : 
        await ctx.author.send("이미 구걸 중입니다.")
    con.close()



@commands.cooldown(1, 5, commands.BucketType.default)
@bot.command()
async def 기부(ctx,nickname2=None,moa=None) : 
    con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
    cur=con.cursor()
    role = discord.utils.find(lambda r: r.name == 'Muted',ctx.guild.roles) 
    if not role in ctx.author.roles :
        end=0
        money1=0
        money2=0
        nickname1=""
        user=0
        t1 = ctx.author.id
        sql=f"select moa,nickname from user_info where discorduserid={t1}"
        sql4=f"select discorduserid,nickname from user_info where nickname='{str(nickname2)}'"
        cur.execute(sql)
        datas=cur.fetchone()
        print(datas)
        money1=datas[0]
        nickname1=datas[1]
        cur.execute(sql4)
        datas=cur.fetchone()
        print(datas)  
        user=bot.get_user(int(datas[0]))
        print(user)
        nickname2=datas[1]
        sql2=f"update user_info set moa=moa-{moa} where discorduserid={t1}"
        sql3=f"update user_info set moa=moa+truncate({moa}*0.9,0) where nickname='{str(nickname2)}'"
        print(sql3)
        if money1<int(moa) or int(moa)<0 : 
            await ctx.author.send(nickname1+"님 보유량보다 많거나 0원 미만으로 기부할수 없습니다.")
            return
        elif nickname1==str(nickname2) : 
            await ctx.author.send("자기 자신한테 기부할수 없습니다.")
        elif moa==None : 
            await ctx.author.send("기부할 돈을 입력해주세요.")
            return
        else :          
            cur.execute(sql2)
            cur.execute(sql3)
            con.commit()
            end=money2+math.floor(int(moa)*0.9)
            await user.send(f'{nickname1}님이 {moa}모아를 기부하셔서 수수료 10%를 뺀 {money2}모아에서 {end}모아가 되었습니다!')
            await ctx.author.send(f"{nickname1}님, {nickname2}님에게 {moa}모아를 기부해서 {money1}모아에서 {money1-int(moa)}모아가 되었습니다!")                         
    else : 
        ctx.author.send("구걸 상태라 기부 할 수 없습니다.")
    print("기부 명령어 작동 완료")



@bot.command()
async def 상점(ctx,item=None) : 
    con = pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
    cur=con.cursor()
    count=0
    have=0
    end=0
    money=0
    need=0
    amount=0
    nickname=""
    name=""
    if item==None : 
        sql=f"select * from gnkstore"
        cur.execute(sql)
        datas=cur.fetchall()
        for i in datas : 
            count=count+1
            await ctx.send(f"{i[0]}    {i[1]}    {i[2]}모아  남은 개수 : {i[3]}")
        con.close()
    elif int(item)>=1 or int(item)<=count : 
        nickname=""
        sql=f"select name,price,amount from gnkstore where itemid={int(item)}"
        cur.execute(sql)
        datas=cur.fetchall()
        for i in datas : 
            name=i[0]
            need=i[1]
            amount=i[2]
        if amount==0 : 
            await ctx.send("이 아이템은 매진되었습니다.")
        sql=f"select nickname,moa,item{int(item)},discorduserid from user_info where discorduserid={ctx.author.id}"
        cur.execute(sql)
        datas = cur.fetchall()
        for i in datas : 
            nickname=i[0]
            money=i[1]
            have=i[2]
        if money>=int(need) : 
            sql=f"update user_info set item{int(item)} = item{int(item)}+1, moa=moa-{int(need)} where discorduserid={ctx.author.id}"
            sql2=f"update gnkstore set amount=amount-1 where itemid='{int(item)}'"
            cur.execute(sql)
            cur.execute(sql2)
            await ctx.author.send(f"{name}을 구입하는데 성공했습니다!")
            await ctx.send(f"{nickname}님이 {name}을 구입하였습니다! 현재 {nickname}님의 보유 개수는 {have+1}개 입니다.")
        else : 
            await ctx.author.send(f"모아가 부족합니다!")
    con.commit()
    con.close()



@commands.cooldown(1, 2, commands.BucketType.default)
@bot.command()
async def 럭키팡(ctx) : 
    con = pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
    cur=con.cursor()
    sql=f"select pangprice from betstat"
    cur.execute(sql)
    datas = cur.fetchall()
    for i in datas : 
        moa=i[0]
    await ctx.send(f"누적 모아 : {moa}")


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
async def 경제규모(ctx) : 
    economy=0
    con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore",autocommit=True)
    cur=con.cursor()
    sql=f"select sum(moa) from user_info;"
    cur.execute(sql)
    datas= cur.fetchall()
    for i in datas : 
        economy=i[0]
    await ctx.send(f"현재 GnK경제규모는 {economy}모아입니다!")
        



@bot.command()
async def 문의(ctx):
    count=0
    nickname=""
    con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
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
async def 재발급(ctx) : 
    salt="R9Wf2PN%qk9!Jn*Sd$PeB10iJ"
    con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
    cur=con.cursor()
    t1 = ctx.author.id
    string_pool=string.ascii_letters+string.digits
    result1=""
    for i in range(20) : 
        result1=result1+random.choice(string_pool)
    hasing=hashlib.sha512()
    hasing.digest()
    result=hashlib.sha512((result1+salt).encode('utf-8')).hexdigest()
    sql=f"update user_info set login_string='{result}' where discorduserid='{t1}'"
    cur.execute(sql)
    con.commit()
    con.close()
    print(result1)
    await ctx.author.send(f"재발급 된 로그인 문자열은 {result1}입니다.")




@bot.command()
async def 점수(ctx,nick=None) : 
    score=0
    con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
    cur=con.cursor()
    if nick==None : 
        sql=f"select score from user_info where discorduserid={ctx.author.id}"
        cur.execute(sql)
        datas=cur.fetchall()
        for i in datas : 
            score=i[0]
        await ctx.author.send(f"당신의 GnK내전 점수는 {score}점 입니다.")
    else : 
        sql=f"select score from user_info where nickname='{nick}'"
        cur.execute(sql)
        datas=cur.fetchall()
        for i in datas : 
            score=i[0]
            await ctx.send(f"{nick}의 GnK내전 점수는 {score}점 입니다.")
    con.close()

@bot.command()
async def 코인시세(ctx) : 
    con=pymysql.connect(host="35.202.81.62",user="root",password="fbmkkrvKHwkz4L5c",database="gnkscore")
    cur=con.cursor()
    price=0
    maxprice=0
    price0=0
    sql=f"select * from gnkcoin"
    cur.execute(sql)
    datas=cur.fetchall()
    for i in datas : 
        price=i[0]
        maxprice=i[1]
        price0=i[2]
    await ctx.send(f"현재 GnKcoin의 시세는 {price}, 최고가는 {maxprice},0원으로 망한 횟수는 {price0}회 입니다.")
    


@bot.command()
async def 내전(ctx) : 
    webpage=urlopen("http://gin7174.dothome.co.kr/inclubgame.html")
    soup=BeautifulSoup(webpage,"html.parser")
    div=str(soup.find('div'))
    div=re.sub('<.+?>','',div,0).strip()
    await ctx.send(div)


bot.run(token)
