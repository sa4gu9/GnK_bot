#region 코인 명령어
'''
@bot.command()
async def 코인시세(ctx) : 
    con=pymysql.connect(host="localhost",user="root",password="dkahfmrptdk00&",database="gnkscore")
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
async def 코인구매(ctx,amount=None) : 
    if amount==None : 
        await ctx.send("개수를 입력해주세요.")
        return
    con=pymysql.connect(host="localhost",user="root",password="dkahfmrptdk00&",database="gnkscore")
    cur=con.cursor()
    moa=0
    price=0
    coin=0
    nickname=""
    sql=f"select nickname, moa, coin from user_info where discorduserid={ctx.author.id}"
    cur.execute(sql)
    datas = cur.fetchall()
    for i in datas : 
        nickname=i[0]
        moa=int(i[1])
        coin=int(i[2])
    sql=f"select price from gnkcoin"
    cur.execute(sql)
    datas=cur.fetchall()
    for i in datas : 
        price=int(i[0])
    if price==0 : 
        await ctx.send("0원인 상태에서는 구매할수 없습니다.")
        return
    else :
        print(f"{moa}     {price*int(amount)}")
        if moa>=price*int(amount) : 
            sql=f"update user_info set moa={moa-price*int(amount)}, coin=coin+{int(amount)} where discorduserid='{ctx.author.id}'"
            cur.execute(sql)
            con.commit()
            await ctx.send(f"구매에 성공하였습니다! 현재 {nickname}의 보유 개수는 {coin+int(amount)}개 입니다.")
        else : 
            await ctx.send("모아가 부족합니다.")

@bot.command()
async def 코인판매(ctx,amount=None) : 
    if amount==None : 
        await ctx.send("개수를 입력해주세요.")
        return
    con=pymysql.connect(host="localhost",user="root",password="dkahfmrptdk00&",database="gnkscore")
    cur=con.cursor()
    moa=0
    price=0
    coin=0
    nickname=""
    sql=f"select nickname, moa, coin from user_info where discorduserid={ctx.author.id}"
    cur.execute(sql)
    datas = cur.fetchall()
    for i in datas : 
        nickname=i[0]
        moa=int(i[1])
        coin=int(i[2])
    if coin==0 : 
        await ctx.send("GnK코인을 가지고 있지 않습니다.")
        return
    sql=f"select price from gnkcoin"
    cur.execute(sql)
    datas=cur.fetchall()
    for i in datas : 
        price=int(i[0])
    if price==0 : 
        await ctx.send("0원인 상태에서는 판매 할 수 없습니다.")
        return
    else :
        if not int(amount)>coin : 
            sql=f"update user_info set coin={coin-int(amount)}, moa=moa+{int(amount)*price} where nickname='{nickname}'"
            cur.execute(sql)
            con.commit()
            await ctx.send(f"GnKcoin {amount}개를 판매하여 {int(amount)*price}모아를 얻었습니다.")
        else : 
            await ctx.send(f"보유량을 넘었습니다. 현재 {nickname}의 보유 개수는 {coin}개 입니다.")
'''
#endregion