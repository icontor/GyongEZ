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

    if message.content.startswith('안녕'):
        await message.channel.send('안녕!')

    if message.content.startswith('재상이는 병신이야?'):
        await message.channel.send('그게 맞지')

    if message.content.startswith("!롤"):

        #Construct the Username
        userInstruction = message.content.split(" ")
        userName = userInstruction[1]

        url = "http://www.op.gg/summoner/userName=" + urllib.parse.quote(userName)
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"}).text

        print("He's rank is " + rank2)

        #Construct the discord chatbot Object
        embed = discord.Embed(
            title=userName,
            colour=discord.Colour.green()
        )

        #case 1: Unrank
        if "Unranked" in rank2:
            embed.add_field(name="죄송합니다", value='언랭은 검색 하실 수 없습니다', inline=False)
            await message.channel.send(embed=embed)
        #case 2: Rank
        else:
            #Crawling the info
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

            MostCP = winlose1.find("")

            print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)



            #Reconstruct the discord chatbot Object
            embed.add_field(name='티어', value=rank2, inline=False)
            embed.add_field(name='LP(점수)', value=jumsu4, inline=False)
            embed.add_field(name='승,패 정보', value=winlose2txt + " " + winlose2_1txt, inline=False)
            embed.add_field(name='승률', value=winlose2_2txt, inline=False)
            await message.channel.send(embed=embed)

client.run(TOKEN)