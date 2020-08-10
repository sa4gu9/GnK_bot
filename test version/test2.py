import random

mapnormal = 'WKC 코리아 서킷,쥐라기 공룡 무덤,브로디 비밀의 연구소,월드 뉴욕 대질주,쥐라기 공룡 결투장,월드 두바이 다운타운,사막 놀라운 공룡 유적지,신화 신들의 세계,비치 해변 드라이브,빌리지 고가의 질주,WKC 싱가폴 마리나 서킷,WKC 상해 서킷,월드 리오 다운힐,빌리지 익스트림 경기장,빌리지 남산,어비스 운명의 갈림길'

maphard='월드 이탈리아 피사의 사탑,WKC 브라질 서킷,네모 산타의 비밀공간,네모 강철바위 용광로,도검 구름의 협곡,대저택 은밀한 지하실,차이나 골목길 대질주,차이나 서안 병마용,황금문명 오리엔트 황금 좌표,황금문명 비밀장치의 위협,해적 로비 절벽의 전투,빌리지 만리장성,어비스 바다 소용돌이,사막 빙글빙글 공사장,공동묘지 해골성 대탐험'

mapveryhard='노르테유 익스프레스,광산 3개의 지름길,광산 위험한 제련소,광산 꼬불꼬불 다운힐,동화 이상한 나라의 문,쥐라기 공룡섬 대모험,어비스 스카이라인,어비스 숨겨진 바닷길,문힐시티 숨겨진 지하터널,공동묘지 마왕의 초대,포레스트 지그재그,팩토리 미완성 5구역,빌리지 붐힐터널'




class Map:
    def __init__(self,mapnormal,maphard,mapveryhard):
        self.normal = mapnormal.split(',')
        self.hard = maphard.split(',')
        self.veryhard = mapveryhard.split(',')
        self.mapall=[]

        for i in self.normal:
            self.mapall.append(i)
        for i in self.hard :
            self.mapall.append(i)
        for i in self.veryhard:
            self.mapall.append(i)


    def getAllMap(self):
        return self.mapall

    def getmap(self,mode,amount) : 
        result=[]
        data=[]
        printing=""
        if amount==None : 
            self.amount=5
        else :
            self.amount=int(amount)
        if mode==1 : 
            data= random.sample(self.normal,amount)
        elif mode==2 : 
            data= random.sample(self.hard,amount)
        elif mode==3 : 
            data= random.sample(self.veryhard,amount)
        elif mode==4 :
            data= random.sample(self.mapall,amount)
        else :
            return "1:노멀 2:하드 3:베리하드 4:전체"
        for i in data : 
            printing+=(i+'\n')
        return f"```{printing}```"


maps=Map(mapnormal,maphard,mapveryhard)
print(maps.getmap(4,5))
print(maps.getmap(5,44))

#GnK맵추첨 4 44
