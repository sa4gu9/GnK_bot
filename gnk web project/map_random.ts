function map_random(mode,amount){
    alert(mode+"  "+amount)
    var map1v1 = '비치 해변 드라이브,쥐라기 공룡 무덤,브로디 비밀의 연구소,네모 산타의 비밀공간,빌리지 고가의 질주,월드 리오 다운힐,도검 구름의 협곡,신화 신들의 세계,WKC 코리아 서킷,차이나 서안 병마용';

    var mapnormal = '브로디 비밀의 연구소,월드 뉴욕 대질주,쥐라기 공룡 결투장,월드 두바이 다운타운,사막 놀라운 공룡 유적지,신화 신들의 세계,비치 해변 드라이브,빌리지 고가의 질주,WKC 싱가폴 마리나 서킷,WKC 상해 서킷,월드 리오 다운힐,빌리지 익스트림 경기장,빌리지 남산,어비스 운명의 갈림길';

    var maphard='월드 이탈리아 피사의 사탑,WKC 브라질 서킷,네모 산타의 비밀공간,네모 강철바위 용광로,도검 구름의 협곡,대저택 은밀한 지하실,차이나 골목길 대질주,차이나 서안 병마용,황금문명 오리엔트 황금 좌표,황금문명 비밀장치의 위협,해적 로비 절벽의 전투,빌리지 만리장성,어비스 바다 소용돌이,사막 빙글빙글 공사장,공동묘지 해골성 대탐험';

    var mapveryhard='노르테유 익스프레스,광산 3개의 지름길,광산 위험한 제련소,광산 꼬불꼬불 다운힐,동화 이상한 나라의 문,쥐라기 공룡섬 대모험,어비스 스카이라인,어비스 숨겨진 바닷길,문힐시티 숨겨진 지하터널,공동묘지 마왕의 초대,포레스트 지그재그,팩토리 미완성 5구역,빌리지 붐힐터널';

    var mapall=[];
    var mapresult=[];
    var result=0;

    switch(mode){
        case 1 :
            if(amount>map1v1.split(',').length){
                alert('에결 맵 개수는 '+map1v1.split(',').length+"개 입니다.")
                return;
            }
        case 2 :
            if(amount>mapnormal.split(',').length){
                alert('노멀 맵 개수는 '+mapnormal.split(',').length+"개 입니다.")
                return;
            }
        case 3 :
            if(amount>maphard.split(',').length){
                alert('하드 맵 개수는 '+maphard.split(',').length+"개 입니다.")
                return;
            }
        case 4 :
            if(amount>mapveryhard.split(',').length){
                alert('베리하드 맵 개수는 '+mapveryhard.split(',').length+"개 입니다.")
                return;
            }
        case 5:
            var temp=0;
    
            for (var i=0; i<map1v1.split(',').length; i++){
                mapall.push(map1v1.split(',')[i]);
            }
            for (var i=0; i<mapnormal.split(',').length; i++){
                for(var j=0; j<mapall.length; j++){
                    if(mapnormal.split(',')[i]==mapall[j])
                        break;
                    else
                        temp++;
                    if (temp==mapall.length){
                        mapall.push(mapnormal.split(',')[i])
                        temp=0;
                    }
                }
            }

            for (var i=0; i<maphard.split(',').length; i++){
                for(var j=0; j<maphard.length; j++){
                    if(maphard.split(',')[i]==mapall[j])
                        break;
                    else
                        temp++;
                    if (temp==mapall.length){
                        mapall.push(maphard.split(',')[i])
                        temp=0;
                    }
                }
            }

            for (var i=0; i<mapveryhard.split(',').length; i++){
                for(var j=0; j<mapveryhard.length; j++){
                    if(mapveryhard.split(',')[i]==mapall[j])
                        break;
                    else
                        temp++;
                    if (temp==mapall.length){
                        mapall.push(mapveryhard.split(',')[i])
                        temp=0;
                    }
                }
            }
            if(amount>mapall.length){
                alert('전체 맵 개수는 '+mapall.length+"개 입니다.")
                return;
    }

    for(var i=0; i<amount; i++){
        var temp=0;
        switch(mode){
            case 1:
                result = Math.floor(map1v1.split(',').length*Math.random());
                for(var j=0; j<mapresult.length; j++)
                    if(map1v1.split(',')[result]==mapresult[j])
                        break;
                    else
                        temp++;
                    if (temp==mapresult.length){
                        mapresult.push(map1v1.split(',')[result]);
                        temp=0;
                    }
                    else {
                        i--;
                    }
                break;
            case 2:
                result = Math.floor(mapnormal.split(',').length*Math.random());
                mapresult.push(mapnormal.split(',')[result]);
                break;
            case 3:
                result = Math.floor(maphard.split(',').length*Math.random());
                mapresult.push(maphard.split(',')[result]);
                break;
            case 4:
                result = Math.floor(mapveryhard.split(',').length*Math.random());
                mapresult.push(mapveryhard.split(',')[result]);
                break;
            case 5:           
                console.log(mapall)
                result = Math.floor((Math.random()*mapall.length));
                mapresult.push(mapall[result]);
                break;
            default : 
                alert("잘못 입력함");
                break;
        }
    }
    console.log(mapresult);
    alert(mapresult);

    
    }
}
