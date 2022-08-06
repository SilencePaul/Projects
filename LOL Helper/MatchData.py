################################################################################
# Match data Code
#
# Purpose: Get matches data from Riot API about an specific summoner
# #          Using Adaptor pattern to change the information from the Riot API to
# #          user-friendly format.
#
# Author: Yiming Liu
# Contact: liu1330@mcmaster.ca
#
################################################################################
import json
import requests
from datetime import *
import ChampionData
import ItemData
import ConfigInfo


class MatchesInfo:
    # Initialize the connection to the Riot API to get the summoner's match information.
    def __init__(self, name):
        self.api_key = ConfigInfo.configInfo().apikey
        self.name = name
        nameInfo = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' +
                                self.name + '?api_key=' + self.api_key)
        nameInfo_json = json.loads(nameInfo.text)
        self.puuid = nameInfo_json['puuid']
        self.accountI = nameInfo_json['accountId']
        self.id = nameInfo_json['id']
        self.summonerLevel = nameInfo_json['summonerLevel']
        RecentMatchInfo = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' +
                                       self.puuid + '/ids?start=0&count=20' + '&api_key=' + self.api_key)
        self.RecentMatchInfo_json = json.loads(RecentMatchInfo.text)

    # Summoner's Champion Masteries base on their level
    def summonerChampionMasteries(self, level):
        championMasteries = requests.get('https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries'
                                         '/by-summoner/' + self.id + '?api_key=' + self.api_key)
        championMasteries_json = json.loads(championMasteries.text)
        championMasteries_text = 'Champion Mastery Level ' + str(level) + '\n' + 'Champion' + \
                                 ' ' * (14 - len('Champion')) + 'Level  Last Play date\n'
        for i in championMasteries_json:
            if i['championLevel'] == level:
                championID = i['championId']
                for j in ChampionData.AllChampion().championsToNumber:
                    if championID == j[1]:
                        championName = j[0]
                        lastTimePlayed = round(i['lastPlayTime'] / 1000)
                        lastTimePlayed_date = datetime.fromtimestamp(lastTimePlayed).strftime('%Y/%m/%d')
                        championMasteries_text += championName + ' ' * (16 - len(championName)) + \
                                                  str(i['championLevel']) + ' ' * 5 + \
                                                  lastTimePlayed_date + '\n'
        return championMasteries_text

    # Basic information about the summoner.
    def summonerBasicInfo(self):
        summonerInfo = requests.get('https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' +
                                    self.id + '?api_key=' + self.api_key)
        summonerInfo_json = json.loads(summonerInfo.text)
        summonerInfo_text = 'Summoner Name:' + self.name + '\nLevel: ' + str(self.summonerLevel) + '\n'
        for i in summonerInfo_json:
            gameType = i['queueType']
            tier = i['tier']
            rank = i['rank']
            wins = i['wins']
            losses = i['losses']
            winrate = str(round(wins / (wins + losses) * 100))
            summonerInfo_text += gameType + ': ' + tier + ' ' + rank + '\nWins: ' + str(wins) + \
                                 '\tLosses: ' + str(losses) + '\tWinrate: ' + winrate + '%\n'

        return summonerInfo_text

    # Get the recent 20 brief information for users to see and select.
    # Get the brief information base on the matchBriefInfo function.
    def Recent20GamesBriefInfo(self):
        matches = self.getMatches()
        num = 0
        print('********************************************************************************')
        for i in matches:
            num += 1
            if num < 10:
                print('(' + str(num) + ')  ' + self.matchBriefInfo(i))
            else:
                print('(' + str(num) + ') ' + self.matchBriefInfo(i))

    # Get the matches ids for a desired summoner.
    def getMatches(self):
        matches = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + self.puuid +
                               '/ids?start=0&count=20&api_key=' + self.api_key)
        matches_json = json.loads(matches.text)
        return matches_json

    # Get a match information from Riot API.
    def matchBriefInfo(self, matchID):
        matchInfo = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/' +
                                 matchID + '?api_key=' + self.api_key)
        matchInfo_json = json.loads(matchInfo.text)
        participants = matchInfo_json['info']['participants']
        num = 0
        for i in matchInfo_json['metadata']['participants']:
            if i == self.puuid:
                break
            num += 1

        gameTime = round(matchInfo_json['info']['gameEndTimestamp'] / 1000)
        dateTime = datetime.fromtimestamp(gameTime).strftime('%Y/%m/%d')
        gameMode = matchInfo_json['info']['gameMode']
        gameDuration = str(timedelta(seconds=matchInfo_json['info']['gameDuration']))
        time = datetime.strptime(gameDuration, '%H:%M:%S')
        gameDuration_text = str(time.minute) + ':' + str(time.second)
        searcher = participants[num]
        champion = searcher['championName']
        assist = searcher['assists']
        deaths = searcher['deaths']
        kills = searcher['kills']
        win = searcher['win']
        KDA = str(kills) + '/' + str(deaths) + '/' + str(assist)
        if win:
            VictoryOrDefeat = 'Victory'
        else:
            VictoryOrDefeat = 'Defeat'
        briefInfo_text = gameMode + ' ' * (8 - len(gameMode)) + '|' + VictoryOrDefeat + ' ' * \
                         (8 - len(VictoryOrDefeat)) + '|' + gameDuration_text + ' ' * (5 - len(gameDuration_text)) + '|' \
                         + champion + ' ' * (12 - len(champion)) + '|' + KDA + \
                         ' ' * (8 - len(KDA)) + '|' + dateTime + ' |'
        return briefInfo_text

    # Get the detailed information for a single match
    def SingleMatchDetail(self, matchID):
        matchInfo = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/' +
                                 matchID + '?api_key=' + self.api_key)
        matchInfo_json = json.loads(matchInfo.text)
        participants = matchInfo_json['info']['participants']
        gameTime = round(matchInfo_json['info']['gameEndTimestamp'] / 1000)
        dateTime = datetime.fromtimestamp(gameTime).strftime('%Y/%m/%d %H:%m')
        gameDuration = str(timedelta(seconds=matchInfo_json['info']['gameDuration']))
        time = datetime.strptime(gameDuration, '%H:%M:%S')
        gameDuration_text = str(time.minute) + ':' + str(time.second)
        winTeam = []
        loseTeam = []

        itemData = ItemData.AllItems().itemToNumber
        singleMatch_text = '********************************************************************************\n' + \
                           'Game Date: ' + dateTime + '\nGame Duration: ' + gameDuration_text + '\n'
        singleMatch_text += 'Victory Team\n'
        for i in participants:
            summonerName = i['summonerName']
            champion = i['championName']
            assists = i['assists']
            deaths = i['deaths']
            kills = i['kills']
            win = i['win']
            itemlist = []
            itemName = []
            itemText = ''
            KDA = format((int(assists) + int(kills)) / int(deaths), '.2f')
            itemlist.append([str(i['item0']), str(i['item1']), str(i['item2'])
                                , str(i['item3']), str(i['item4']), str(i['item5'])])
            for i in itemData:
                for j in range(0, 6):
                    if i[1] == itemlist[0][j]:
                        itemName.append(i[0])
            for i in itemName:
                itemText += i + ', '
            itemText = itemText[:-2]
            if win:
                winTeam.append([summonerName, champion, 'KDA: ' + str(KDA) + ':1',
                                str(kills) + '/' + str(deaths) + '/' + str(assists), itemText])
            else:
                loseTeam.append([summonerName, champion, 'KDA: ' + str(KDA) + ':1',
                                 str(kills) + '/' + str(deaths) + '/' + str(assists), itemText])

        for i in range(0, 5):
            singleMatch_text += '|' + winTeam[i][0] + ' ' * (16 - len(winTeam[i][0])) + \
                                '|' + winTeam[i][1] + ' ' * (12 - len(winTeam[i][1])) + \
                                '|' + winTeam[i][2] + ' ' * (12 - len(winTeam[i][2])) + \
                                '|' + winTeam[i][3] + ' ' * (8 - len(winTeam[i][3])) + \
                                '|' + winTeam[i][4] + '|\n'

        singleMatch_text += 'Defeat Team\n'
        for i in range(0, 5):
            singleMatch_text += '|' + loseTeam[i][0] + ' ' * (16 - len(loseTeam[i][0])) + \
                                '|' + loseTeam[i][1] + ' ' * (12 - len(loseTeam[i][1])) + \
                                '|' + loseTeam[i][2] + ' ' * (12 - len(loseTeam[i][2])) + \
                                '|' + loseTeam[i][3] + ' ' * (8 - len(loseTeam[i][3])) + \
                                '|' + loseTeam[i][4] + '|\n'

        return singleMatch_text
