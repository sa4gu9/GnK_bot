# -*- coding: utf-8 -*- 

import sys
import os.path
import discord
from discord.ext import commands
from discord.utils import get
import random
import math
import time
import asyncio
import string

members=[]
path='''user info.txt'''
path2='betting stat.txt'
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

if not os.path.isfile(path2):
    tf = open(path2,"w")
    tf.write("0,0")
    tf.close()


version="V1.1.2"

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


command="도와줘,안녕,에결,에결리스트,노멀,노멀리스트,하드,하드리스트,베리하드,베리하드리스트,전체,전체리스트,버전,추천,가입테스트,가입,모아,베팅,기부,상점,구걸,그리고 숨겨진 몇개의 명령어들"

commandlist="도와줘,안녕,에결,에결리스트,노멀,노멀리스트,하드,하드리스트,베리하드,베리하드리스트,전체,전체리스트,버전,추천,킹오hi,욕해줘,아잉련아,새벽,가입테스트,베팅,가입,모아,기부,상점,구걸"

@bot.event
async def on_message(ctx) :
    role = discord.utils.find(lambda r: r.name == 'Muted',ctx.guild.roles)
    money=0
    nick=""
    end=0
    if role in ctx.author.roles :
        whole=""
        if len(members)!=0 : 
            t1 = members.index(ctx.author.id)
            with open(path) as f:
                whole=f.read()
                f.seek(0)
                lines=f.readlines()
                print(t1)
                print(lines)
                tps = lines[t1].split(',')
                f.close()
                for i in tps : 
                    if len(str(i))==8 : 
                        money=int(i)
                    elif len(i)>3 and len(i)<8 : 
                        nick=i
            end=money-4000
            whole=whole.replace((str(ctx.author.id)+","+str(money).zfill(8)),(str(ctx.author.id)+","+str(end).zfill(8)))
            f=open(path,"w")
            f.write(whole)
            f.close()
            await ctx.delete()
        await ctx.author.send(f'{nick}님, mute 상태에서 채팅을 쳐서 {money}모아에서 {end}모아가 되었습니다.')
    await bot.process_commands(ctx)

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
    await ctx.send(version)

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

@commands.cooldown(1, 5, commands.BucketType.default)
@bot.command()
async def 가입(ctx,nickname=None) : 
    if len(nickname)>3 and len(nickname)<8 : 
        f = open(path,"a")
        if not ctx.author.id in members :
            f.write(str(len(members))+",")
            f.write(str(nickname)+",")
            f.write(str(ctx.author.id)+",")
            f.write(str(5000).zfill(8)+",")
            f.write(str(0).zfill(3)+",\n")
            f.close()
            members.append(ctx.author.id)
            await ctx.author.send("가입 성공!")
        else :
            await ctx.author.send("이미 가입이 되어 있습니다.")
    else : 
        await ctx.author.send("닉네임 제한 4~7, 한글3 영어1")

@commands.cooldown(1, 1, commands.BucketType.default)
@bot.command()
async def 모아(ctx,nickname=None) : 
    nick=""
    money=0
    if nickname==None : 
        t1 = members.index(ctx.author.id)
        print(t1)
        f=open(path)
        lines=f.readlines()
        tps = lines[t1].split(',')
        print(tps)
        for i in tps : 
            if len(i)>3 and len(i)<8 : 
                print(i)
                nick=i
            elif len(str(i))==8 : 
                money=int(i)
        await ctx.author.send(f'{nick} 님의 모아는 {money}모아 입니다.')
    else : 
        with open(path) as f:
            f.seek(0)
            lines=f.readlines()
        for i in lines : 
            if i.find(nickname)>0 : 
                words = i.split(',')
                for j in words : 
                    if len(j)==8 : 
                        money=int(j)
        await ctx.send(f'{nickname} 님의 모아는 {money}모아 입니다.')
    print("모아 명령어 작동 완료")

@commands.cooldown(1, 2, commands.BucketType.default)
@bot.command()
async def 베팅(ctx,moa=None,mode=None,repeat=None) :
    if repeat==None : 
        repeat=1
    if int(repeat)<=10 and int(repeat)>0 : 
        for num in range(int(repeat)) : 
            stat=open(path2,"r")
            stats=stat.read()
            stat.close()
            stats=stats.split(',')
            role = discord.utils.find(lambda r: r.name == 'Muted',ctx.guild.roles)
            if not role in ctx.author.roles :
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
                        elif len(i)>3 and len(i)<8 : 
                            nick=i
                if money<int(moa) or int(moa)<0 : 
                    await ctx.author.send(nick+"님 보유량보다 많거나 0원 미만으로 베팅하실 수 없습니다.")
                    return
                elif moa==None : 
                    await ctx.author.send("GnK베팅 거실돈 모드\n(모드 종류 : 1 80% 1.4배, 2 64% 1.8배, 3 48% 2.2배, 4 32% 2.6배, 5 16% 3배)")
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
                        await ctx.author.send("축하합니다!"+nick+"님! "+str(moa)+"모아에서 "+str(profit)+"모아가 되었습니다!")
                    else :
                        end=money-lose
                        whole=whole.replace((str(ctx.author.id)+","+str(money).zfill(8)),(str(ctx.author.id)+","+str(end).zfill(8)))
                        await ctx.author.send("아쉽습니다. "+nick+"님... "+str(moa)+"모아를 잃으셨습니다.")
                        stats[0]=int(stats[0])+1
                        await ctx.send(str(stats[0])+"번째 실패")
                        if money>=5000000 :
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.7)
                        elif money>=4000000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.6)
                        elif money>=3000000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.5)
                        elif money>=2000000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.4)
                        elif money>=1000000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.3)
                        elif money>=500000 : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.2)
                        else : 
                            stats[1]=int(stats[1])+math.floor(int(moa)*0.1)
                    files=open(path,"w")
                    print(whole)
                    files.write(whole)
                    files.close()
                    if int(stats[0])>=100 : 
                        userids=0
                        stat=open(path2,"w")
                        stat.write("0,0")
                        stat.close()
                        luckym=(math.floor(int(stats[1])*0.1))
                        print(luckym)
                        getuser=random.randrange(0,len(members))
                        print(getuser)
                        print(lines)
                        linesplit = lines[getuser].split(',')
                        money2=0
                        print(linesplit)
                        end2=0
                        nickname2=""
                        discorduser=""
                        for i in linesplit : 
                            if len(i)==8 : 
                                money2=int(i)
                            elif len(i)==18 : 
                                userids=i
                                discorduser=bot.get_user(int(i))
                            elif len(i)>3 and len(i)<8 : 
                                nickname2=i      
                        end2=money2+luckym
                        whole=whole.replace((str(userids)+","+str(money2).zfill(8)),(str(userids)+","+str(end2).zfill(8)))
                        editfile=open(path,"w")
                        editfile.write(whole)
                        editfile.close()
                        await ctx.send(str(nickname2)+"님이 럭키팡에 당첨되어 "+str(luckym)+"모아를 받았습니다!")
                        await discorduser.send(str(nickname2)+"님 축하합니다! 럭키팡에 당첨되어 "+str(luckym)+"모아를 받았습니다!")
                    else : 
                        stat=open(path2,"w")
                        stat.write(str(stats[0])+','+str(stats[1]))
                        stat.close()
                else : 
                    await ctx.author.send("모드를 선택해주세요. 1 80% 1.4배, 2 64% 1.8배, 3 48% 2.2배, 4 32% 2.6배, 5 16% 3배")
                    break
            else : 
                ctx.author.send("구걸 상태라 베팅을 할 수 없습니다.")
                break
    else : 
        await ctx.author.send("1~10회만 반복 가능합니다.")        
    print("베팅 명령어 작동 완료")

@bot.command()
async def 구걸(ctx) : 
    role = discord.utils.find(lambda r: r.name == 'Muted',ctx.guild.roles)
    if not role in ctx.author.roles :
        hour=7
        minute=0
        second=0
        money=0
        nick=""
        end=0
        t1 = members.index(ctx.author.id)
        with open(path) as f:
            whole=f.read()
            f.seek(0)
            lines=f.readlines()
            tps = lines[t1].split(',')
            f.close()
            for i in tps : 
                if len(str(i))==8 : 
                    money=int(i)
                elif len(i)>3 and len(i)<8 : 
                    nick=i
        member = ctx.message.author
        await member.add_roles(get(ctx.guild.roles,name="Muted"))
        await ctx.send(f'{nick}님이 구걸 하기 위해 {hour}시간 {minute}분 {second}초 뮤트 되어 30000모아를 지급하였습니다. 뮤트상태에서 채팅을 치면 4000모아를 뺏깁니다.')
        end=money+30000
        whole=whole.replace((str(ctx.author.id)+","+str(money).zfill(8)),(str(ctx.author.id)+","+str(end).zfill(8)))
        f = open(path,"w")
        f.write(whole)
        f.close()
        await asyncio.sleep(hour*60*60+minute*60+second)
        await member.remove_roles(get(ctx.guild.roles,name="Muted"))
    else : 
        await ctx.author.send("이미 구걸 중입니다.")
    
@commands.cooldown(1, 5, commands.BucketType.default)
@bot.command()
async def 기부(ctx,nickname2=None,moa=None) : 
    role = discord.utils.find(lambda r: r.name == 'Muted',ctx.guild.roles) 
    if not role in ctx.author.roles :
        end1=0
        end2=0
        whole=""
        money1=0
        money2=0
        nickname1=""
        user=0
        t1 = members.index(ctx.author.id)
        with open(path) as f:
            whole=f.read()
            f.seek(0)
            lines=f.readlines()
            tps = lines[t1].split(',')
            for i in tps : 
                if len(str(i))==8 : 
                    money1=int(i)
                    f.close()
                elif len(i)>3 and len(i)<8 : 
                    nickname1=i
            for i in lines : 
                if i.find(nickname2)>0 : 
                    words = i.split(',')
                    for j in words : 
                        if len(j)==8 : 
                            money2=int(j)
                        elif len(j)==18 : 
                            ids=j
                            user=bot.get_user(int(j))
        if money1<int(moa) or int(moa)<0 : 
            await ctx.author.send(nickname1+"님 보유량보다 많거나 0원 미만으로 기부할수 없습니다.")
            return
        elif nickname1==str(nickname2) : 
            await ctx.author.send("자기 자신한테 기부할수 없습니다.")
        elif moa==None : 
            await ctx.author.send("기부할 돈을 입력해주세요.")
            return
        else : 
            with open(path) as f:
                whole=f.read()
                f.close()
            end1=money1-int(moa)
            ttemp=math.floor(int(moa)*0.9)
            end2=money2+ttemp
            whole=whole.replace((str(ctx.author.id)+","+str(money1).zfill(8)),(str(ctx.author.id)+","+str(end1).zfill(8)))
            whole=whole.replace(nickname2+","+str(ids)+","+str(money2).zfill(8),nickname2+","+str(ids)+","+str(end2).zfill(8))
            print(user)
            print(ctx.author)
            await user.send(f'{nickname1}님이 {moa}모아를 기부하셔서 수수료 10%를 뺀 {money2}모아에서 {end2}모아가 되었습니다!')
            await ctx.author.send(f"{nickname1}님, {nickname2}님에게 {moa}모아를 기부해서 {money1}모아에서 {end1}모아가 되었습니다!")
            files=open(path,"w")
            files.write(whole)
            files.close()                             
    else : 
        ctx.author.send("구걸 상태라 기부 할 수 없습니다.")
    print("기부 명령어 작동 완료")

@bot.command()
async def 상점(ctx,item=None) : 
    num=0
    num2=0
    end=0
    money=0
    if item==None : 
        await ctx.send("번호\t\t\t상품 이름\t\t\t가격\n1.\t\t\t내전 참가권\t\t\t30000모아")
    elif int(item)==1 : 
        file = open(path,"r")
        whole = file.read()
        file.seek(0)
        list1 = file.readlines()
        string1 = ""
        nickname=""
        print(list1)
        for i in list1 : 
            print(i)
            print(ctx.author.id)
            if str(ctx.author.id) in i : 
                string1 = i
                break
        print(string1.split(','))
        for i in string1.split(',') : 
            if len(i)==3 : 
                num=int(i)
            elif len(i)==8 : 
                money=int(i)
            elif len(i)>3 and len(i)<8 : 
                nickname=i
        num2=num+1
        if money>=30000 : 
            end=money-30000
            print(str(ctx.author.id)+","+str(money).zfill(8)+","+str(num).zfill(3))
            print(str(ctx.author.id)+","+str(end).zfill(8)+","+str(num2).zfill(3))
            whole=whole.replace(str(ctx.author.id)+","+str(money).zfill(8)+","+str(num).zfill(3),str(ctx.author.id)+","+str(end).zfill(8)+","+str(num2).zfill(3))
            await ctx.author.send("내전 참가권을 구입하는데 성공했습니다!")
            await ctx.send(f"{nickname}님이 내전 참가권을 구입하였습니다! 현재 보유 개수는 {num2}개 입니다.")
            file=open(path,"w")
            file.write(whole)
            file.close()
        else : 
            await ctx.author.send(f"모아가 부족합니다!")
        
@commands.cooldown(1, 2, commands.BucketType.default)
@bot.command()
async def 럭키팡(ctx) : 
    stat=open(path2,"r")
    whole=stat.read()
    stats=whole.split(',')
    await ctx.send("누적 횟수 : "+stats[0]+", 누적 모아 : "+stats[1])

@bot.command()
async def 에결추천(ctx) : 
    await ctx.send("준비중입니다")

@bot.command()
async def 문의(ctx):
    count=1
    guild = ctx.guild
    for member in guild.members : 
        for role in member.roles : 
            if "문의" in role.name : 
                count=count+1
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.author: discord.PermissionOverwrite(read_messages=True,send_messages=True),
    }
    await guild.create_role(name="문의 "+str(count))
    role = discord.utils.get(ctx.guild.roles, name="문의 "+str(count))
    cate = discord.utils.get(guild.categories,name="문의")
    server = ctx.guild
    user = ctx.message.author
    await user.add_roles(role)
    channel = await guild.create_text_channel("문의 "+str(count), overwrites=overwrites,category=cate)

bot.run(token)