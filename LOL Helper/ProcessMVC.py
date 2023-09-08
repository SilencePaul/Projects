################################################################################
# ProcessMVC Code
#
# Purpose: This code is going to provide the menus for the Lol Helper.
#           This code is using the MVC pattern. User just need to choose the
#           selection appear on the screen and enter the champion or item name
#           Or just need to enter a summoner name to search for summoner's data
#           and match information. User don't need to worry about the background work.
#
# Author: Yiming Liu
# Contact: liu1330@mcmaster.ca
#
################################################################################
import LOLChecker
import ItemData
import ChampionData
import MatchData
import PrintReport
import datetime
import pymysql
import ConfigInfo


# User interface
class view:

    @staticmethod
    def mainMenu():
        print("********************************************************************************")
        print("(1) Instant Search")
        print("(2) Print Report")
        print("(3) Exit")
        choice = int(input('Please enter an option: '))
        return choice

    @staticmethod
    def save():
        print("********************************************************************************")
        saveYorN = input("Do you want to save this data for report(Y/N)?")
        return saveYorN

    @staticmethod
    def backMethod():
        print("********************************************************************************")
        print("(1) Back to Previous Menu")
        print("(2) Back to Main Menu")
        choice = input('Please enter an option: ')
        return int(choice)

    @staticmethod
    def printReportMenu():
        print("********************************************************************************")
        reportName = input('Please enter the file name: ')
        reportName += '.txt'
        print("(1) Back to Main Menu")
        print("(2) Exit")
        choice = int(input('Please enter an option: '))
        return reportName, choice

    @staticmethod
    def instantSearchMenu():
        print("********************************************************************************")
        print("(1) Search Champion")
        print("(2) Search Item")
        print("(3) Search Matches")
        print("(4) Back to Main Menu")
        print("(5) Exit")
        choice = int(input('Please enter an option: '))
        return choice

    @staticmethod
    def itemMenu():
        print("********************************************************************************")
        print("(1) Search by Item Tag")
        print("(2) Search by Item Level")
        print("(3) Back to Previous Menu")
        print("(4) Back to Main Menu")
        print("(5) Exit")
        choice = int(input('Please enter an option: '))
        return choice

    @staticmethod
    def itemLevelMenu():
        print("********************************************************************************")
        print("(1) Starter Items")
        print("(2) Basic Items")
        print("(3) Epic Items")
        print("(4) Legendary Items")
        print("(5) Mythic Items")
        print("(6) Ornn Upgraded Items")
        print("(7) Back to Previous Menu")
        print("(8) Back to Main Menu")
        choice = int(input('Please enter an option: '))
        return choice

    @staticmethod
    def summonerNameInput():
        print("********************************************************************************")
        summonerName = input('Please enter Summoner name: ')
        return summonerName

    @staticmethod
    def matchMenu():
        print("********************************************************************************")
        print("(1) Summoner Basic Info")
        print("(2) Summoner Champion Masteries")
        print("(3) Summoner Recent 20 Games")
        print("(4) Back to Previous Menu")
        print("(5) Back to Main Menu")
        print("(6) Exit")
        choice = int(input('Please enter an option: '))
        return choice

    @staticmethod
    def championMenu():
        print("********************************************************************************")
        print("(1) Show All Champion")
        print("(2) Search Single Champion")
        print("(3) Top 3 Champions with Most Skins")
        print("(4) Back to Previous Menu")
        print("(5) Back to Main Menu")
        print("(6) Exit")
        choice = int(input('Please enter an option: '))
        return choice

    @staticmethod
    def championNameInput():
        print("********************************************************************************")
        championName = input('Please enter champion name: ')
        return championName

    @staticmethod
    def searchSingleChampionMenu():
        print("(1) Champion Basic Stats")
        print("(2) Champion Story")
        print("(3) Champion Tips")
        print("(4) Champion Skins")
        print("(5) Combined Information")
        choice = int(input('Please enter an option: '))
        return choice


# Control the action between view and model.
class controller:

    def __init__(self, view, model):
        self.__view = view
        self.__model = model

    def start(self):
        self.__model.createTables()
        apikey = ConfigInfo.configInfo().apikey
        version = ConfigInfo.configInfo().version
        language = ConfigInfo.configInfo().language
        # Check all the requirements by chain of responsibility
        apiCheckResult = LOLChecker.apiCheck(apikey).checkInfo()
        versionCheckResult = LOLChecker.versionCheck(version).checkInfo()
        languageCheckResult = LOLChecker.languageCheck(language).checkInfo()
        databaseCheckResult = LOLChecker.dataBaseCheck(1).checkInfo()
        if apiCheckResult == 'False':
            self.__model.history('API check failed.')
            exit()
        if versionCheckResult == 'False':
            self.__model.history('Version check failed.')
            exit()
        if languageCheckResult == 'False':
            self.__model.history('Language check failed.')
            exit()
        if databaseCheckResult == 'False':
            self.__model.history('Database connection check failed')
            exit()
        self.__model.history('All Config information correct.')
        self.mainMenuProcess()

    def mainMenuProcess(self):
        choice = self.__view.mainMenu()
        if choice == 1:
            self.__model.history('Instant Search')
            self.instantSearchProcess()
        elif choice == 2:
            self.__model.history('Print Report Menu')
            self.printReportProcess()
        else:
            self.__model.history('Exit')
            exit()

    def exitProcess(self):
        self.__model.history('Exit')
        print('GoodBye!')
        history = self.__model.getHistory()
        PrintReport.report().generateReport('UserHistory.txt', history)
        exit()

    def printReportProcess(self):
        name, choice = self.__view.printReportMenu()
        self.__model.history('File name: ' + name)
        print('Report Generated!')
        information = self.__model.getSavedData()
        PrintReport.report().generateReport(name, information)
        self.__model.history('Report generated')
        if choice == 1:
            self.__model.history('Back to Main Menu')
            self.mainMenuProcess()
        elif choice == 2:
            self.exitProcess()

    def instantSearchProcess(self):
        choice = self.__view.instantSearchMenu()
        if choice == 1:
            self.__model.history('Search Champion')
            self.championMenuProcess()
        elif choice == 2:
            self.__model.history('Search Item')
            self.itemMenuProcess()
        elif choice == 3:
            self.__model.history('Search Matches')
            self.matchMenuProcess()
        elif choice == 4:
            self.__model.history('Back to Main Menu')
            self.mainMenuProcess()
        else:
            self.exitProcess()

    def itemMenuProcess(self):
        choice = self.__view.itemMenu()
        if choice == 1:
            self.__model.history('Search by Item Tag')
            print(ItemData.AllItems().AllItemType())
            selectType = input('Please enter one of the type above: ')
            self.__model.history('User entered: ' + selectType)
            print(ItemData.AllItems().ItemTypeSelect(selectType))
            selectItem = ''
            check = "False"
            while check == "False":
                selectItem = input('Please select one item: ')
                self.__model.history('User entered: ' + selectItem)
                check = LOLChecker.itemCheck(selectItem).checkInfo()
            data = ItemData.AllItems().ItemDetail(selectItem)
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Return to item menu')
                self.itemMenuProcess()
            else:
                self.__model.history('Return to main menu')
                self.mainMenuProcess()
        elif choice == 2:
            self.__model.history('Search by item level')
            self.itemLevelMenuProcess()
        elif choice == 3:
            self.__model.history('Return to instant search menu')
            self.instantSearchProcess()
        elif choice == 4:
            self.__model.history('Return to main menu')
            self.mainMenuProcess()
        elif choice == 5:
            self.__model.history('Exit')
            self.exitProcess()

    def itemLevelMenuProcess(self):
        choice = self.__view.itemLevelMenu()
        if choice == 1:
            self.__model.history('Starter Items')
            print(ItemData.AllItems().StarterItems())
            selectItem = ''
            check = "False"
            while check == "False":
                selectItem = input('Please select one item: ')
                self.__model.history('User entered: ' + selectItem)
                check = LOLChecker.itemCheck(selectItem).checkInfo()
            data = ItemData.AllItems().ItemDetail(selectItem)
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.save(data)
                self.__model.history('Data Saved')
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to item level menu')
                self.itemLevelMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 2:
            self.__model.history('Basic Items')
            print(ItemData.AllItems().BasicItems())
            selectItem = ''
            check = "False"
            while check == "False":
                selectItem = input('Please select one item: ')
                self.__model.history('User entered: ' + selectItem)
                check = LOLChecker.itemCheck(selectItem).checkInfo()
            data = ItemData.AllItems().ItemDetail(selectItem)
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.save(data)
                self.__model.history('Data Saved')
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to item level menu')
                self.itemLevelMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 3:
            self.__model.history('Epic Items')
            print(ItemData.AllItems().EpicItems())
            selectItem = ''
            check = "False"
            while check == "False":
                selectItem = input('Please select one item: ')
                self.__model.history('User entered: ' + selectItem)
                check = LOLChecker.itemCheck(selectItem).checkInfo()
            data = ItemData.AllItems().ItemDetail(selectItem)
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history("Data Saved")
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to item level menu')
                self.itemLevelMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 4:
            self.__model.history("Legendary Item")
            print(ItemData.AllItems().LegendaryItems())
            selectItem = ''
            check = "False"
            while check == "False":
                selectItem = input('Please select one item: ')
                self.__model.history('User entered: ' + selectItem)
                check = LOLChecker.itemCheck(selectItem).checkInfo()
            data = ItemData.AllItems().ItemDetail(selectItem)
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.save(data)
                self.__model.history('Data Saved')
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Return to item level menu')
                self.itemLevelMenuProcess()
            else:
                self.__model.history('Return to main menu')
                self.mainMenuProcess()
        elif choice == 5:
            self.__model.history('Mythic Items')
            print(ItemData.AllItems().MythicItems())
            selectItem = ''
            check = "False"
            while check == "False":
                selectItem = input('Please select one item: ')
                self.__model.history('User entered: ' + selectItem)
                check = LOLChecker.itemCheck(selectItem).checkInfo()
            data = ItemData.AllItems().ItemDetail(selectItem)
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to item level menu')
                self.itemLevelMenuProcess()
            else:
                self.__model.history("Back to main menu")
                self.mainMenuProcess()
        elif choice == 6:
            self.__model.history('Ornn Upgrades')
            print(ItemData.AllItems().OrnnUpgrades())
            selectItem = ''
            check = "False"
            while check == "False":
                selectItem = input('Please select one item: ')
                self.__model.history('User entered: ' + selectItem)
                check = LOLChecker.itemCheck(selectItem).checkInfo()
            data = ItemData.AllItems().ItemDetail(selectItem)
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to item level menu')
                self.itemLevelMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 7:
            self.__model.history('Back to item menu')
            self.itemMenuProcess()
        else:
            self.__model.history('Back to main menu')
            self.mainMenuProcess()

    def matchMenuProcess(self):
        summonerName = ''
        check = "False"
        while check == "False":
            summonerName = self.__view.summonerNameInput()
            self.__model.history('User Enter: ' + summonerName)
            check = LOLChecker.nameCheck(summonerName).checkInfo()
        choice = self.__view.matchMenu()
        if choice == 1:
            self.__model.history('Summoner Basic Info')
            data = MatchData.MatchesInfo(summonerName).summonerBasicInfo()
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Return to match menu')
                self.matchMenuProcess()
            else:
                self.__model.history('Return to main menu')
                self.mainMenuProcess()
        elif choice == 2:
            self.__model.history('Summoner Champion Masteries')
            level = int(input('Please enter Mastery Level (1 to 7)： '))
            self.__model.history('Level' + str(level))
            data = MatchData.MatchesInfo(summonerName).summonerChampionMasteries(level)
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to match menu')
                self.matchMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 3:
            self.__model.history('Summoner Recent 20 Games')
            data = MatchData.MatchesInfo(summonerName).Recent20GamesBriefInfo()
            print(data)
            matchSelect = int(input('Please enter the id of the match for detail: '))
            self.__model.history(str(matchSelect) + ' is selected')
            matchID = MatchData.MatchesInfo(summonerName).getMatches()[matchSelect-1]
            matchData = MatchData.MatchesInfo(summonerName).SingleMatchDetail(matchID)
            print(matchData)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(matchData)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to match menu')
                self.matchMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 4:
            self.__model.history('Back to instant search menu')
            self.instantSearchProcess()
        elif choice == 5:
            self.__model.history('Back to main menu')
            self.mainMenuProcess()
        else:
            self.exitProcess()
    
    def championMenuProcess(self):
        choice = self.__view.championMenu()
        if choice == 1:
            self.__model.history('Show all champions')
            data = ChampionData.AllChampion().showAllChampions()
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to champion menu')
                self.championMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 2:
            self.__model.history('Search single champion menu')
            self.searchSingleChampionMenuProcess()
        elif choice == 3:
            print('Processing.......')
            print('It will take a little bit long time.')
            self.__model.history('Top 3 Champions with most skins')
            data = ChampionData.ChampionDetail('Ahri').Top3SkinChampion()
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to champion menu')
                self.championMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 4:
            self.__model.history('Back to instant search menu')
            self.instantSearchProcess()
        elif choice == 5:
            self.__model.history('Back to main menu')
            self.mainMenuProcess()
        else:
            self.exitProcess()

    def searchSingleChampionMenuProcess(self):
        championName = ''
        check = "False"
        while check == "False":
            championName = self.__view.championNameInput()
            self.__model.history('User enter: ' + championName)
            check = LOLChecker.championCheck(championName).checkInfo()
        choice = self.__view.searchSingleChampionMenu()
        if choice == 1:
            self.__model.history('Champion basic stats')
            data1 = ChampionData.ChampionDetail(championName).BasicStats()
            data2 = ChampionData.ChampionDetail(championName).Spells()
            print(data1)
            print(data2)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data1)
                self.__model.save(data2)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to search single champion menu')
                self.searchSingleChampionMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 2:
            self.__model.history('Champion Story')
            data = ChampionData.ChampionDetail(championName).Story()
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to search single champion menu')
                self.searchSingleChampionMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 3:
            self.__model.history('Champion Tips')
            data = ChampionData.ChampionDetail(championName).ChampionTips()
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to search single champion menu')
                self.searchSingleChampionMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 4:
            self.__model.history('Champion skins')
            data = ChampionData.ChampionDetail(championName).ChampionSkin()
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to search Single Champion menu')
                self.searchSingleChampionMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()
        elif choice == 5:
            self.__model.history('Champion Combined information')
            data = ChampionData.ChampionDetail(championName).Combined()
            print(data)
            YorN = self.__view.save()
            if YorN == 'Y':
                self.__model.history('Data Saved')
                self.__model.save(data)
                print('Data Saved')
            nextStep = self.__view.backMethod()
            if nextStep == 1:
                self.__model.history('Back to search single champion menu')
                self.searchSingleChampionMenuProcess()
            else:
                self.__model.history('Back to main menu')
                self.mainMenuProcess()


# model handles the interaction with the database
class model:

    # Initialize the connection to the database.
    def __init__(self):
        host = ConfigInfo.configInfo().host
        user = ConfigInfo.configInfo().user
        password = ConfigInfo.configInfo().password
        database = ConfigInfo.configInfo().database
        self.db = pymysql.connect(host=host,
                                  user=user,
                                  password=password,
                                  database=database,
                                  use_unicode=True,
                                  charset='utf8')
        self.cursor = self.db.cursor()

    # Create two tables one is for user history and another one is for the data that saved.
    def createTables(self):
        self.cursor.execute('DROP TABLE if EXISTS history')
        self.cursor.execute('CREATE TABLE history ('
                            'id int auto_increment, '
                            'timeline timestamp, '
                            'userAction VARCHAR(255), '
                            'primary key (id))')
        self.cursor.execute('DROP TABLE if EXISTS savedData')
        self.cursor.execute('CREATE TABLE savedData ('
                            'id int auto_increment, '
                            'dataInformation text, '
                            'primary key (id))')
        self.db.commit()

    # Store the history data to the history table.
    def history(self, history):
        timeline = datetime.datetime.today()
        insert = 'INSERT INTO history (timeline, userAction) VALUES (%s, %s)'
        value = (timeline, history)
        self.cursor.execute(insert, value)
        self.db.commit()

    # Store the user selected data to the savedDate table.
    def save(self, data):
        insert = 'INSERT INTO savedData (dataInformation) VALUES (%s)'
        self.cursor.execute(insert, data)
        self.db.commit()

    # Get the saved data back from the database.
    def getSavedData(self):
        self.cursor.execute('SELECT * FROM savedData')
        result = self.cursor.fetchall()
        result_text = ''
        for i in result:
            result_text += i[1] + '\n'
        return result_text

    # Get the history data from the database.
    def getHistory(self):
        self.cursor.execute('SELECT * FROM history')
        result = self.cursor.fetchall()
        result_text = ''
        for i in result:
            result_text += '[' + str(i[1]) + '] ' + i[2] + '\n'
        return result_text

