################################################################################
# LOL Checker Code
#
# Purpose: TO check the information that is available for the program to work.
#
# Author: Yiming Liu
# Contact: liu1330@mcmaster.ca
#
################################################################################
import json
import requests
import ChampionData
import pymysql
import ItemData
import ConfigInfo
from abc import ABC, abstractmethod


# Check project in chain-of-responsibility
class check(ABC):
    @abstractmethod
    def checkInfo(self):
        pass

    def __init__(self, info):
        self.info = info


# Check for the api key for the Riot API.
class apiCheck(check):
    def __init__(self, info):
        super().__init__(info)

    def checkInfo(self):
        r = requests.get('https://na1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=' + self.info)
        r_json = json.loads(r.text)
        if 'status' not in r_json:
            checkResult = 'True'
        else:
            checkResult = 'False'
            print("The Api key is invalid. Please check the Api key in the config file.")

        return checkResult


# Check for the version is in the range of Riot API.
class versionCheck(check):
    def __init__(self, info):
        super().__init__(info)

    def checkInfo(self):
        r = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
        r_json = json.loads(r.text)
        checkResult = ''
        if self.info not in r_json:
            latestVersion = r_json[0]
            checkResult = 'False'
            print('The version is invalid. Please check the version in the config file.\n'
                  'The latest version is ' + latestVersion +
                  '\nYou can find any available version in https://ddragon.leagueoflegends.com/api/versions.json')

        return checkResult


# Check the language is fit for the Riot API.
class languageCheck(check):
    def __init__(self, info):
        super().__init__(info)

    def checkInfo(self):
        r = requests.get('https://ddragon.leagueoflegends.com/cdn/languages.json')
        r_json = json.loads(r.text)
        checkResult = ''
        if self.info not in r_json:
            english = r_json[0]
            checkResult = 'False'
            print('The language is invalid. Please check the language in the config file.\n'
                  'The English language is ' + english +
                  '\nYou can find any available languages in https://ddragon.leagueoflegends.com/cdn/languages.json')
        return checkResult


# Check for the name that user entered is findable.
class nameCheck(check):
    def __init__(self, info):
        super().__init__(info)

    def checkInfo(self):
        api_key = ConfigInfo.configInfo().apikey
        name = self.info
        checkResult = ''
        r = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + name +
                         '?api_key=' + api_key)
        r_json = json.loads(r.text)
        for i in r_json:
            if i == 'id':
                checkResult = 'True'
            elif i == 'status':
                if r_json['status']['status_code'] == 404:
                    checkResult = 'False'
                    print('The summoner name cant be found.')

        return checkResult


# Check for the item name that user entered is right.
class itemCheck(check):
    def __init__(self, info):
        super().__init__(info)

    def checkInfo(self):
        allItem = ItemData.AllItems().itemName
        checkResult = ''
        if self.info not in allItem:
            checkResult = 'False'
            print('The item name is invalid.')
        return checkResult


# Check for the champion name is correct.
class championCheck(check):
    def __init__(self, info):
        super().__init__(info)

    def checkInfo(self):
        allChampion = ChampionData.AllChampion().champions
        checkResult = ''
        if self.info not in allChampion:
            checkResult = 'False'
            print('The champion name is invalid.')
        return checkResult


# Check for the database connection.
class dataBaseCheck(check):
    def __init__(self, info):
        super().__init__(info)
        host = ConfigInfo.configInfo().host
        user = ConfigInfo.configInfo().user
        password = ConfigInfo.configInfo().password
        database = ConfigInfo.configInfo().database
        self.db = pymysql.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.db.cursor()

    def checkInfo(self):
        self.cursor.execute('DROP TABLE if EXISTS checkConnection')
        self.cursor.execute('Create table checkConnection ('
                            'id int not null auto_increment,'
                            'Data text,'
                            'primary key (id)'
                            ')')
        insert = 'INSERT INTO checkConnection (Data) VALUES (%s)'
        value = "True"
        self.cursor.execute(insert, value)
        self.db.commit()
        self.cursor.execute("SELECT * FROM checkConnection")
        checkInfo = self.cursor.fetchall()[-1][1]
        if checkInfo == 'True':
            checkResult = 'True'
        else:
            checkResult = 'False'
            print("Connection to the database check false. Please check the database information in the Config file.")

        return checkResult
