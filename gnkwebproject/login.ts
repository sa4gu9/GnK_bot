const cry = require('crypto');
function logins(nick,psw){
    console.log(nick);
    console.log(psw);
    var password=cry.createHash('sha512').update(psw+'R9Wf2PN%qk9!Jn*Sd$PeB10iJ').digest('hex');
    console.log(password);
}