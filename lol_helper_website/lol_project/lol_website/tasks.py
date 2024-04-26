import requests
from django.db.models import Q
from lol_website.models import LPHistory, APIKey


def get_summoner_info(summoner_name):
    try:
        apikey = APIKey.objects.all().first().api_key
    except:
        print("API Key Not Found")
        return

    summoner_response = requests.get(f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={apikey}')
    summoner_data = summoner_response.json()
    try:
        id = summoner_data['id']
        puuid = summoner_data['puuid']
    except:
        print("API Key has expired")
        return

    summoner_account = requests.get(f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}?api_key={apikey}')
    summoner_account_data = summoner_account.json()

    name = summoner_account_data['gameName']
    print(f"Checking Summoner Name: {name}")


    rank_info_response = requests.get(f'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{id}?api_key={apikey}')
    rank_info_data = rank_info_response.json()
    summoner_flex = LPHistory.objects.filter(Q(queueType="RANKED_FLEX_SR") 
                                            & Q(summonerName=name)).order_by("updated_on").last()
    summoner_solo = LPHistory.objects.filter(Q(queueType="RANKED_SOLO_5x5") 
                                            & Q(summonerName=name)).order_by("updated_on").last()
    for rank_info in rank_info_data:
        if rank_info['queueType'] == "RANKED_FLEX_SR":
            print(f"Flex Rank: {rank_info['tier']} {rank_info['rank']} {rank_info['leaguePoints']} LP")
            if summoner_flex:
                if rank_info["wins"] != summoner_flex.wins or rank_info["losses"] != summoner_flex.losses:
                    print("Flex Rank has changed")
                    history = LPHistory(queueType="RANKED_FLEX_SR", 
                                        tier=rank_info['tier'], 
                                        rank=rank_info['rank'], 
                                        summonerName=name, 
                                        leaguePoints=rank_info['leaguePoints'], 
                                        wins=rank_info['wins'], 
                                        losses=rank_info['losses'])
                    history.save()
            else:
                history = LPHistory(queueType="RANKED_FLEX_SR", 
                                    tier=rank_info['tier'], 
                                    rank=rank_info['rank'], 
                                    summonerName=name, 
                                    leaguePoints=rank_info['leaguePoints'], 
                                    wins=rank_info['wins'], 
                                    losses=rank_info['losses'])
                history.save()
        elif rank_info['queueType'] == "RANKED_SOLO_5x5":
            print(f"Solo Rank: {rank_info['tier']} {rank_info['rank']} {rank_info['leaguePoints']} LP")
            if summoner_solo:
                if rank_info["wins"] != summoner_solo.wins or rank_info["losses"] != summoner_solo.losses:
                    print("Solo Rank has changed")
                    history = LPHistory(queueType="RANKED_SOLO_5x5", 
                                        tier=rank_info['tier'], 
                                        rank=rank_info['rank'], 
                                        summonerName=name, 
                                        leaguePoints=rank_info['leaguePoints'], 
                                        wins=rank_info['wins'], 
                                        losses=rank_info['losses'])
                    history.save()
            else:
                history = LPHistory(queueType="RANKED_SOLO_5x5", 
                                    tier=rank_info['tier'], 
                                    rank=rank_info['rank'], 
                                    summonerName=name, 
                                    leaguePoints=rank_info['leaguePoints'], 
                                    wins=rank_info['wins'], 
                                    losses=rank_info['losses'])
                history.save()
    
