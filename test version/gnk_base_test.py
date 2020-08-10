import discord
from discord.ext import commands,tasks
from discord.utils import get
import random
import asyncio

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

    def getmap(self,mode,amount=5) : 
        self.mode=list(mode)
        self.mode=self.mode[0]
        print(self.mode)
        result=[]
        data=[]
        printing=""
        self.amount=list(amount)
        self.amount=self.amount[0]
        if self.mode==1 : 
            data= random.sample(self.normal,self.amount)
        elif self.mode==2 : 
            data= random.sample(self.hard,self.amount)
        elif self.mode==3 : 
            data= random.sample(self.veryhard,self.amount)
        elif self.mode==4 :
            data= random.sample(self.mapall,self.amount)
        elif self.mode==5 : 
            data=random.sample(self.mapitem,self.amount)
        else :
            return "1:노멀 2:하드 3:베리하드 4:전체(1~3) 5:아이템"
        for i in data : 
            printing+=(i+'\n')
        return f"```{printing}```"

maps=Map(mapnormal,maphard,mapveryhard,mapitem)

@bot.command()
async def 안녕(ctx): await ctx.send("안녕")

@bot.command()
async def 맵추첨(ctx,mode,amount) :
    await ctx.send(f"{maps.getmap({int(mode)},{int(amount)})}")


@bot.command()
async def 노멀리스트(ctx):
    await ctx.send(("```"+mapnormal.replace(",","\n")+"```"))

@bot.command()
async def 하드리스트(ctx):
    await ctx.send("```"+maphard.replace(",","\n")+"```")

@bot.command()
async def 베리하드리스트(ctx):
    await ctx.send("```"+mapveryhard.replace(",","\n")+"```")

@bot.command()
async def 전체리스트(ctx):
    data=""
    for i in mapall : 
        data=data+i+"\n"
    await ctx.send('```'+data+'```')