################################################################################
# Item Data Code
#
# Purpose: Get the information about item detail data.
# #          Using Adaptor pattern to change the information from the Riot API to
# #          user-friendly format.
#
# Author: Yiming Liu
# Contact: liu1330@mcmaster.ca
#
################################################################################
import json
import math
import requests
import ConfigInfo


class AllItems:
    # Initialize the basic item information from Riot API.
    def __init__(self):
        version = ConfigInfo.configInfo().version
        language = ConfigInfo.configInfo().language
        lol_item_response = requests.get('https://ddragon.leagueoflegends.com/cdn/' +
                                         version + '/data/' + language + '/item.json')
        self.itemData = json.loads(lol_item_response.text)['data']
        self.itemType = []
        self.itemName = []
        self.itemToNumber = []
        self.itemType_text = ''
        self.all = 0
        self.itemTypeCount = 0
        self.BasicItemList = []
        self.EpicItemList = []
        self.LegendaryItemList = []
        self.MythicItemList = []
        self.OrnnUpgradeList = []
        for i in self.itemData:
            itemName = self.itemData[i]['name']
            self.itemToNumber.append([itemName, i])
            self.itemName.append(itemName)
            self.all += 1
            types = self.itemData[i]['tags']
            for j in types:
                if j not in self.itemType:
                    self.itemType.append(j)
                    self.itemTypeCount += 1
                    if math.remainder(self.itemTypeCount, 5) == 0:
                        self.itemType_text += j + ' ' * (17 - len(j)) + ' |\n'
                    else:
                        self.itemType_text += j + ' ' * (17 - len(j)) + ' | '

    @staticmethod
    def AllItemType():
        return AllItems().itemType_text

    def TotalItemAmount(self):
        return self.itemTypeCount

    # Return all item types.
    def ItemTypeSelect(self, itemType):
        itemType = itemType
        typeItems_text = itemType + ' items: \n'
        typeAmount = 0
        for i in self.itemData:
            itemName = self.itemData[i]['name']
            types = self.itemData[i]['tags']
            if itemType in types:
                typeAmount += 1
                if math.remainder(typeAmount, 3) == 0:
                    typeItems_text += itemName + ' ' * (30 - len(itemName)) + ' |\n'
                else:
                    typeItems_text += itemName + ' ' * (30 - len(itemName)) + ' | '
        return typeItems_text

    # Return consumable items.
    def ConsumableItems(self):
        consumableItems = self.ItemTypeSelect('Consumable').replace("Your Cut                       "
                                                                    "| Kalista's Black Spear        "
                                                                    "  |\nKalista's Black Spear        "
                                                                    "  | Abyssal Mask                   |", '')
        return consumableItems

    def Boots(self):
        return self.ItemTypeSelect('Boots')

    def Trinkets(self):
        return self.ItemTypeSelect('Trinket')

    # Starter Item
    def StarterItems(self):
        StarterItemsAmount_text = 'Starter Items:\n'
        StarterItemsList = []
        StarterItemsAmount = 0
        for i in self.itemData:
            itemName = self.itemData[i]['name']
            types = self.itemData[i]['tags']
            tags = self.itemData[i]
            StarterItemsList.append(itemName)
            for j in types:
                if j == 'Consumable' or j == 'Trinket':
                    StarterItemsList.remove(itemName)
            for k in tags:
                if k == 'depth' or k == 'into' or k == 'from' or k == 'inStore':
                    if itemName in StarterItemsList:
                        StarterItemsList.remove(itemName)
        StarterItemsList.sort()
        for starterItem in StarterItemsList:
            StarterItemsAmount += 1
            if math.remainder(StarterItemsAmount, 3) == 0:
                StarterItemsAmount_text += starterItem + ' ' * (30 - len(starterItem)) + ' |\n'
            else:
                StarterItemsAmount_text += starterItem + ' ' * (30 - len(starterItem)) + ' | '
        return StarterItemsAmount_text

    # Basic item
    def BasicItems(self):
        BasicItems_text = 'Basic Items:\n'
        BasicItemsAmount = 0
        for i in self.itemData:
            itemName = self.itemData[i]['name']
            tags = self.itemData[i]
            self.BasicItemList.append(itemName)
            for k in tags:
                if k == 'from' or k == 'inStore':
                    if itemName in self.BasicItemList:
                        self.BasicItemList.remove(itemName)
            if 'into' not in tags:
                if itemName in self.BasicItemList:
                    self.BasicItemList.remove(itemName)
        self.BasicItemList.sort()
        for BasicItem in self.BasicItemList:
            BasicItemsAmount += 1
            if math.remainder(BasicItemsAmount, 3) == 0:
                BasicItems_text += BasicItem + ' ' * (30 - len(BasicItem)) + ' |\n'
            else:
                BasicItems_text += BasicItem + ' ' * (30 - len(BasicItem)) + ' | '
        return BasicItems_text

    def EpicItems(self):
        EpicItems_text = 'Epic Items:\n'
        EpicItemsAmount = 0
        for i in self.itemData:
            itemName = self.itemData[i]['name']
            types = self.itemData[i]['tags']
            tags = self.itemData[i]
            if 'depth' in tags:
                if tags['depth'] == 2:
                    self.EpicItemList.append(itemName)
            for k in tags:
                if k == 'inStore':
                    if itemName in self.EpicItemList:
                        self.EpicItemList.remove(itemName)
            for j in types:
                if j == 'Boots' or j == 'Consumable':
                    if itemName in self.EpicItemList:
                        self.EpicItemList.remove(itemName)
        self.EpicItemList.sort()
        for EpicItem in self.EpicItemList:
            EpicItemsAmount += 1
            if math.remainder(EpicItemsAmount, 3) == 0:
                EpicItems_text += EpicItem + ' ' * (30 - len(EpicItem)) + ' |\n'
            else:
                EpicItems_text += EpicItem + ' ' * (30 - len(EpicItem)) + ' | '
        return EpicItems_text

    def LegendaryItems(self):
        LegendaryItems_text = 'Legendary Items:\n'
        LegendaryItemsAmount = 0
        for i in self.itemData:
            itemName = self.itemData[i]['name']
            tags = self.itemData[i]
            if 'depth' in tags:
                if tags['depth'] == 3:
                    self.LegendaryItemList.append(itemName)
            for k in tags:
                if k == 'into':
                    if itemName in self.LegendaryItemList:
                        self.LegendaryItemList.remove(itemName)
                elif k == 'specialRecipe':
                    if itemName not in self.LegendaryItemList:
                        self.LegendaryItemList.append(itemName)
        self.LegendaryItemList.sort()
        for LegendaryItem in self.LegendaryItemList:
            LegendaryItemsAmount += 1
            if math.remainder(LegendaryItemsAmount, 3) == 0:
                LegendaryItems_text += LegendaryItem + ' ' * (30 - len(LegendaryItem)) + ' |\n'
            else:
                LegendaryItems_text += LegendaryItem + ' ' * (30 - len(LegendaryItem)) + ' | '
        return LegendaryItems_text

    def MythicItems(self):
        MythicItems_text = 'Mythic Items:\n'
        MythicItemsAmount = 0
        for i in self.itemData:
            itemName = self.itemData[i]['name']
            tags = self.itemData[i]
            if 'depth' in tags:
                if tags['depth'] == 3:
                    self.MythicItemList.append(itemName)
            if 'into' not in tags:
                if itemName in self.MythicItemList:
                    self.MythicItemList.remove(itemName)
        print(len(self.MythicItemList))
        self.MythicItemList.sort()
        for MythicItem in self.MythicItemList:
            MythicItemsAmount += 1
            if math.remainder(MythicItemsAmount, 3) == 0:
                MythicItems_text += MythicItem + ' ' * (30 - len(MythicItem)) + ' |\n'
            else:
                MythicItems_text += MythicItem + ' ' * (30 - len(MythicItem)) + ' | '
        return MythicItems_text

    def OrnnUpgrades(self):
        OrnnUpgradeItems_text = 'Ornn Upgrade Mythic Items:\n'
        OrnnUpgradeItemsAmount = 0
        for i in self.itemData:
            itemName = self.itemData[i]['name']
            tags = self.itemData[i]
            if 'depth' in tags:
                if tags['depth'] == 4:
                    self.OrnnUpgradeList.append(itemName)
        print(len(self.OrnnUpgradeList))
        self.OrnnUpgradeList.sort()
        for OrnnUpgradeItem in self.OrnnUpgradeList:
            OrnnUpgradeItemsAmount += 1
            if math.remainder(OrnnUpgradeItemsAmount, 3) == 0:
                OrnnUpgradeItems_text += OrnnUpgradeItem + ' ' * (30 - len(OrnnUpgradeItem)) + ' |\n'
            else:
                OrnnUpgradeItems_text += OrnnUpgradeItem + ' ' * (30 - len(OrnnUpgradeItem)) + ' | '
        return OrnnUpgradeItems_text

    # Get item detail
    def ItemDetail(self, item):
        itemName = item
        itemNumber = 0
        itemDetail_text = ''
        for i in self.itemToNumber:
            if i[0] == itemName:
                itemNumber = i[1]
        itemData = self.itemData[itemNumber]
        image = "https://ddragon.leagueoflegends.com/cdn/12.13.1/img/item/" + itemNumber + ".png"
        gold = itemData['gold']['total']
        sell = itemData['gold']['sell']
        description = itemData['plaintext']
        buildFrom = []
        buildInto = []
        if 'from' in itemData:
            for item in itemData['from']:
                for a in self.itemToNumber:
                    if a[1] == item:
                        buildFrom.append(a[0])
        if 'into' in itemData:
            for item in itemData['into']:
                for a in self.itemToNumber:
                    if a[1] == item:
                        buildInto.append(a[0])
        itemDetail_text += 'Item: ' + itemName + '\nDescription: ' + description + '.\n' + \
                           'Image: ' + image + '\nGold: ' + str(gold) + ' for purchased, ' + str(sell) + \
                           ' for sold.\n'
        if len(buildFrom) != 0:
            itemDetail_text += 'Built From: '
            for i in buildFrom:
                itemDetail_text += i + ','
            itemDetail_text = itemDetail_text[:-1] + '.\n'
        if len(buildInto) != 0:
            itemDetail_text += 'Can be built into: '
            for i in buildInto:
                itemDetail_text += i + ' | '
            itemDetail_text = itemDetail_text[:-1] + '\n'

        return itemDetail_text
