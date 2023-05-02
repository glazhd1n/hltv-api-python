from typing import List
import __players__, Player

async def getTopPlayers(number_of_players) -> List[Player.Player]:
    list_of_players = __players__.getTopPlayers(number_of_players)
    players = []
    for player_id in list_of_players:
        player = await Player.getPlayerById(player_id[1])
        players.append(player)
    return players