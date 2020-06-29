var pick=0;
var finalmap=[];
var mode="밴";
var number=[];
function map_banpick(){

    var second=40;
    var team=1;
    var player=1;

    var x=setInterval(function(){
        second=Math.round((second-0.01)*100)/100;
        document.getElementById("start").style.visibility="hidden";
        if(mode=="밴"||mode=="픽")
            document.getElementById("timer").innerHTML=team+"팀 "+"플레이어 "+player+"의 "+mode+" 남은시간 : "+second+"초";
        else
            document.getElementById("timer").innerHTML=mode;

        console.log(pick+"   "+mode)
        
        if(mode=="종료"){
            document.body.style.background='#FAEC85';
            document.body.style.color='black';
        }
        else if(team==1){
            document.body.style.background='#04E5F6';
            document.body.style.color='black';
        }
        else{
            document.body.style.background='#E65053';
            document.body.style.color='white';
        }


        if (second<=0||(pick==2&&mode=="밴")||(pick==1&&mode=="픽")){
            if(mode=="밴"){
                if (team==1)
                    team=2;
                else{
                    if(player!=4){
                        team=1;
                        player++;
                    }
                    else{
                        mode="픽"
                    }
                }
            }
            else{
                if (team==2)
                    team=1;
                else{
                    if(player!=1){
                        team=2;
                        player--;
                    }
                    else{
                        mode="종료";
                        for(var i=0; i<3; i++){
                            var result=Math.floor(Math.random()*number.length);
                            var idx=number.indexOf(number[result]);
                            document.getElementById("pick").innerHTML+="<br>"+document.getElementById(`${number[result]}`).innerHTML;
                            document.getElementById(`${number[result]}`).style.visibility="hidden";
                            number.splice(idx,1);
                        }
                    }
                }
            }

            pick=0;
            second=40;
        }    
    },10)

    
}

function picked(number1){
    pick++;
    var idx=number.indexOf(number1)
    number.splice(idx,1);
    console.log(number)
    if(mode=="픽"){
        document.getElementById("pick").innerHTML+="<br>"+(document.getElementById(number1).innerHTML);
    }
}