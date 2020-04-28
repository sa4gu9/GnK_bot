# -*- coding: utf-8 -*- 

import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='GnK')
token = "NjYxMTc5OTgzNzAzNTcyNDkx.Xp5u9Q.ciODDc8YvlAfXS8CjW4ni6lyaHQ"

map1v1 = '비치 해변 드라이브,쥐라기 공룡 무덤,브로디 비밀의 연구소,네모 산타의 비밀공간,빌리지 고가의 질주,월드 리오 다운힐,도검 구름의 협곡,신화 신들의 세계,WKC 코리아 서킷,차이나 서안 병마용'
mapnormal = '브로디 비밀의 연구소,월드 뉴욕 대질주,쥐라기 공룡섬 결투장,월드 두바이 다운타운,사막 놀라운 공룡 유적지,신화 신들의 세계,비치 해변 드라이브,빌리지 고가의 질주,WKC 싱가폴 마리나 서킷,WKC 상해 서킷'
maphard='월드 이탈리아 피사의 사탑,WKC 브라질 서킷,네모 산타의 비밀공간,네모 강철바위 용광로,도검 구름의 협곡,대저택 은밀한 지하실,차이나 골목길 대질주,차이나 서안 병마용,황금문명 오리엔트 황금 좌표,황금문명 비밀장치의 위협'
mapveryhard='노르테유 익스프레스,광산 3개의 지름길,광산 위험한 제련소,광산 꼬불꼬불 다운힐,동화 이상한 나라의 문,쥐라기 공룡섬 대모험,어비스 스카이라인,어비스 숨겨진 바닷길,문힐시티 숨겨진 지하터널,공동묘지 마왕의 초대'
mapall='비치 해변 드라이브,쥐라기 공룡 무덤,브로디 비밀의 연구소,네모 산타의 비밀공간,빌리지 고가의 질주,월드 리오 다운힐,도검 구름의 협곡,신화 신들의 세계,차이나 서안 병마용,월드 뉴욕 대질주,쥐라기 공룡섬 결투장,월드 두바이 다운타운,사막 놀라운 공룡 유적지,WKC 싱가폴 마리나 서킷,WKC 상해 서킷,월드 이탈리아 피사의 사탑,WKC 브라질 서킷,네모 강철바위 용광로,대저택 은밀한 지하실,차이나 골목길 대질주,황금문명 오리엔트 황금 좌표,황금문명 비밀장치의 위협,노르테유 익스프레스,광산 3개의 지름길,광산 위험한 제련소,광산 꼬불꼬불 다운힐,동화 이상한 나라의 문,쥐라기 공룡섬 대모험,어비스 스카이라인,어비스 숨겨진 바닷길,문힐시티 숨겨진 지하터널,공동묘지 마왕의 초대'
command="도와줘,안녕,에결,에결리스트,노멀,노멀리스트,하드,하드리스트,베리하드,베리하드리스트,전체,전체리스트,버전,추천,가입테스트,그리고 숨겨진 몇개의 명령어들"
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
async def 전체(ctx,amount):
    await ctx.send("```"+random.sample(mapall.split(','),amount)+"```")

@bot.command()
async def 전체리스트(ctx):
    await ctx.send("```"+mapall.replace(",","\n")+"```")

@bot.command()
async def 버전(ctx):
    await ctx.send("V1.0.1")

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
async def 아잉련아(ctx): await ctx.send("????")

@bot.command()
async def 새벽(ctx): await ctx.send("에도 켜져있음")

bot.run(token)