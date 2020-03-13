import discord
import urllib
import urllib.request
import bs4
from botinfo import TOKEN
client = discord.Client()

#깃허브올림
#봇정보
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game("재상병신")
    await client.change_presence(status=discord.Status.online, activity=game)


# 봇명령어
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!전적검색"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)

        url = "http://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")

        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"})
        rank3 = rank2.text

        print(rank3)

        '''urank1 = bsObj.find("div", {"class": "TierRankInfo"})
        urank2 = urank1.find("div", {"class": "TierRank unranked"})
        urank3 = urank2.text'''
        if rank3 != 'Unranked':
            jumsu1 = rank1.find("div", {"class": "TierInfo"})
            jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
            jumsu3 = jumsu2.text
            jumsu4 = jumsu3.strip()
            print(jumsu4)

            winlose1 = jumsu1.find("span", {"class": "WinLose"})
            winlose2 = winlose1.find("span", {"class": "wins"})
            winlose2_1 = winlose1.find("span", {"class": "losses"})
            winlose2_2 = winlose1.find("span", {"class": "winratio"})

            winlose2txt = winlose2.text
            winlose2_1txt = winlose2_1.text
            winlose2_2txt = winlose2_2.text

            print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)
            embed = discord.Embed(
            title='전적검색결과',
            description='',
            colour=discord.Colour.green()
        )
        if rank3 == 'Unranked':
            embed.add_field(name='당신의 티어', value=rank3, inline=False)
            embed.add_field(name='-당신은 언랭-', value="언랭은 더이상의 정보는 제공하지 않습니다.", inline=False)
            await message.channel.send(embed=embed)
            print('He is unranked')
        else:
            embed.add_field(name='티어', value=rank3, inline=False)
            embed.add_field(name='LP(점수)', value=jumsu4, inline=False)
            embed.add_field(name='승,패 정보', value=winlose2txt + " " + winlose2_1txt, inline=False)
            embed.add_field(name='승률', value=winlose2_2txt, inline=False)
            await message.channel.send(embed=embed)

client.run(TOKEN)