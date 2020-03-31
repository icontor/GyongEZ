import urllib
import urllib.request
import bs4
import discord

bot = discord.Client()
#if you want add bot command add here
def Guide():
    text = ""
    text += "!전적검색 소환사닉네임 : 자신의 솔로랭크 전적을 보여줍니다"
    text += ""
    return text

def SearchingRank(userName):
    url = "http://www.op.gg/summoner/userName=" + urllib.parse.quote(userName)
    html = urllib.request.urlopen(url)

    bsObj = bs4.BeautifulSoup(html, "html.parser")
    rank1 = bsObj.find("div", {"class": "TierRankInfo"})
    rank2 = rank1.find("div", {"class": "TierRank"}).text
    print(userName)
    # Construct the discord chatbot Object
    embed = discord.Embed(
        title=userName,
        colour=discord.Colour.green()
    )
    # case 1: Unrank
    if "Unranked" in rank2:
        result = embed.add_field(name="죄송합니다", value='언랭은 검색 하실 수 없습니다', inline=False)
        return result
    # case 2: Rank
    else:
        # Crawling the info
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

        # Reconstruct the discord chatbot Object
        result = embed.add_field(name='티어', value=rank2, inline=False)
        embed.add_field(name='LP(점수)', value=jumsu4, inline=False)
        embed.add_field(name='승,패 정보', value=winlose2txt + " " + winlose2_1txt, inline=False)
        embed.add_field(name='승률', value=winlose2_2txt, inline=False)
        return result




