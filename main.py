import discord
import urllib
import urllib.request
import bs4
client = discord.Client()
TOKEN = 'Njg0MjU2NjM0NTE1NzUwOTYw.Xl3eGg.-_YFZRAsvYV-s0epRZ9_oOoM3do'

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
            title='롤 정보',
            description='롤 정보입니다.',
            colour=discord.Colour.green()
        )
        if rank3 == 'Unranked':
            embed.add_field(name='당신의 티어', value=rank3, inline=False)
            embed.add_field(name='-당신은 언랭-', value="언랭은 더이상의 정보는 제공하지 않습니다.", inline=False)
            await message.channel.send(embed=embed)
        else:
            embed.add_field(name='당신의 티어', value=rank3, inline=False)
            embed.add_field(name='당신의 LP(점수)', value=jumsu4, inline=False)
            embed.add_field(name='당신의 승,패 정보', value=winlose2txt + " " + winlose2_1txt, inline=False)
            embed.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)
            await message.channel.send(embed=embed)
client.run(TOKEN)