################################################################################
# Champion Data Code
#
# Purpose: Get the data about champion from Riot API.
#          Using Adaptor pattern to change the information from the Riot API to
#          user-friendly format.
#
#
# Author: Yiming Liu
# Contact: liu1330@mcmaster.ca
#
################################################################################
import json
import math
import requests
import ConfigInfo


# Get all the champions and match with their ids.
class AllChampion(object):
    def __init__(self):
        version = ConfigInfo.configInfo().version
        language = ConfigInfo.configInfo().language
        lol_champion_response = requests.get("https://ddragon.leagueoflegends.com/cdn/" +
                                             version + "/data/" + language + "/champion.json")
        championData = json.loads(lol_champion_response.text)
        self.championData = championData['data']
        self.champions = []
        self.championsToNumber = []
        self.championList_text = "Champion List:\n"
        self.all = 0
        for i in self.championData:
            championName = self.championData[i]['id']
            key = int(self.championData[i]['key'])
            self.championsToNumber.append([championName, key])
            self.champions.append(championName)
            self.all += 1
            if math.remainder(self.all, 7) == 0:
                self.championList_text += championName + ' ' * (12 - len(championName)) + ' | ''\n'
            else:
                self.championList_text += championName + ' ' * (12 - len(championName)) + ' | '

    def getAllChampions(self):
        return self.champions

    def showAllChampions(self):
        return self.championList_text

    def totalNumberOfChampion(self):
        return print(self.all)


class ChampionDetail:
    # Initially get the basic details from the champion that selected.
    def __init__(self, championName):
        version = ConfigInfo.configInfo().version
        language = ConfigInfo.configInfo().language
        self.championName = championName
        championList = AllChampion().champions
        if self.championName not in championList:
            raise Exception('The champion name is wrong. Please enter the correct one.')
        championDetail_response = requests.get('https://ddragon.leagueoflegends.com/cdn/' +
                                               version + '/data/' + language + '/champion/'
                                               + self.championName + '.json')
        championDetail_json = json.loads(championDetail_response.text)['data']
        self.championInfo = championDetail_json[self.championName]
        self.championTitle = self.championInfo['title']
        self.championStory = self.championInfo['lore']
        self.championSkin = self.championInfo['skins']
        self.championTips = self.championInfo['allytips']
        self.championAgainstTips = self.championInfo['enemytips']
        self.championTags = self.championInfo['tags']
        self.championBasicInfo = self.championInfo['stats']
        self.championSpell = self.championInfo['spells']
        self.championPassive = self.championInfo['passive']
        self.championSkinList = []
        for i in self.championSkin:
            if i['num'] == 0:
                self.championSkinList.append(self.championName + ' default skin: ' +
                                             'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/' +
                                             self.championName + '_' + str(i['num']) + '.jpg')
            else:
                self.championSkinList.append(i['name'] + ': ' +
                                             'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/' +
                                             self.championName + '_' + str(i['num']) + '.jpg')
        self.numberOfSkins = len(self.championSkinList)

    # Give back all the skins that the champion have in a list.
    def ChampionSkin(self):
        championSkin_text = "There are " + str(self.numberOfSkins) + " skins for " + \
                            self.championName + '.\n'
        for i in self.championSkinList:
            championSkin_text += i + '\n'
        return championSkin_text

    # This method is going to compare the number of skins that each champion has. This method will take a little
    # bit long time because there are more than 160 champions to compare.
    @staticmethod
    def Top3SkinChampion():
        allChampion = AllChampion().champions
        championSkinNumberList = []
        for i in allChampion:
            championSkinNumberList.append([i, ChampionDetail(i).numberOfSkins])
        first = 0
        second = 0
        third = 0
        firstChampion = ''
        secondChampion = ''
        thirdChampion = ''
        for i in championSkinNumberList:
            if i[1] > first:
                thirdChampion = secondChampion
                third = second
                secondChampion = firstChampion
                second = first
                firstChampion = i[0]
                first = i[1]
            elif i[1] == first:
                firstChampion += ', ' + i[0]
            elif first > i[1] > second:
                thirdChampion = secondChampion
                third = second
                secondChampion = i[0]
                second = i[1]
            elif i[1] == second:
                secondChampion += ', ' + i[0]
            elif second > i[1] > third:
                thirdChampion = i[0]
                third = i[1]
            elif i[1] == third:
                thirdChampion += ', ' + i[0]

        Top3SkinChampion_text = 'The champions have the most skins are ' + firstChampion + '.\n' + \
                                'They have ' + str(first) + ' skins.' + '\n' + \
                                'The champions have the second most skins are ' + secondChampion + '.\n' + \
                                'They have ' + str(second) + ' skins.' + '\n' + \
                                'The champions have the Third most skins are ' + thirdChampion + '.\n' + \
                                'They have ' + str(third) + ' skins.'
        return Top3SkinChampion_text

    # Gives back the champion story.
    def Story(self):
        story_text = self.championName + "'s Story.\n" + self.championStory + \
                     "\n********************************************************************************\n"
        return story_text

    # Gives back the basic stats of the champion.
    def BasicStats(self):
        championTag_text = ''
        championTag_text = self.championTags[0]
        if len(self.championTags) > 1:
            championTag_text += " or " + self.championTags[1]
        basicStats_text = self.championName + "is a " + championTag_text + ".\n" + \
                          self.championName + "'s basic stats:\n" + \
                          self.championName + "'s " + 'basic hp is ' + \
                          str(self.championBasicInfo['hp']) + ' and increases ' + \
                          str(self.championBasicInfo['hpperlevel']) + ' per level.\n' + \
                          self.championName + "'s " + 'basic armor is ' + \
                          str(self.championBasicInfo['armor']) + ' and increases ' + \
                          str(self.championBasicInfo['armorperlevel']) + ' per level.\n' + \
                          self.championName + "'s " + 'basic attack damage is ' + \
                          str(self.championBasicInfo['attackdamage']) + ' and increases ' + \
                          str(self.championBasicInfo['attackdamageperlevel']) + ' per level.\n' + \
                          self.championName + "'s " + 'basic move speed is ' + \
                          str(self.championBasicInfo['movespeed']) + '.\n' + \
                          self.championName + "'s " + 'basic attack speed is ' + \
                          str(self.championBasicInfo['attackspeed']) + \
                          '.\n********************************************************************************\n'

        return basicStats_text

    # The tips for playing the champion
    def ChampionTips(self):
        tips_text = self.championName + "'s Tips:\n"
        for i in self.championTips:
            tips_text += i + '\n'
        return tips_text + "********************************************************************************\n"

    # The tips for fighting against the champion.
    def AgainstTips(self):
        AgainstTips_text = 'Against ' + self.championName + "'s Tips:\n"
        for i in self.championAgainstTips:
            AgainstTips_text += i + "\n"
        return AgainstTips_text + '********************************************************************************\n'

    # Champion Spells.
    def Spells(self):
        spell_text = self.championName + "'s Spells\n" + \
                     'Passive: ' + self.championPassive['name'] + '\nDescription: ' + \
                     self.championPassive['description'] + \
                     '\nImage: https://ddragon.leagueoflegends.com/cdn/12.12.1/img/passive/' + \
                     self.championPassive['image']['full'] + '\n'
        spell = ['Q', 'W', 'E', 'R']
        spellNumber = 0
        for i in self.championSpell:
            spell_text += spell[spellNumber] + ': ' + i['name'] + '\nDescription: ' + \
                          i['description'] + '\nImage: https://ddragon.leagueoflegends.com/cdn/12.12.1/img/spell/' + \
                          i['image']['full'] + '\n'
            spellNumber += 1
        return spell_text + "\n********************************************************************************\n"

    # Get all the information together.
    def Combined(self):
        combined_text = "********************************************************************************\n" + \
                        self.BasicStats() + self.Story() + self.Spells() + self.ChampionTips() + \
                        self.AgainstTips() + self.ChampionSkin()
        return combined_text
