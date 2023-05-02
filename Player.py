from typing import Optional
import __player__

class Team:
    def __init__(self, id: Optional[int], name: Optional[str]):
        self.id = id
        self.name = name

class Player:
    def __init__( self, 
                  id: int, 
                  teamId: int,
                  teamName: Optional[str], 
                  image: Optional[str], 
                  nickname: str, 
                  name: str, 
                  age: Optional[int], 
                  rating: float, 
                  impact: Optional[float], 
                  dpr: Optional[float], 
                  adr: Optional[float], 
                  kast: Optional[float], 
                  kpr: float, 
                  headshots: int, 
                  maps_played: Optional[int] ):
        self.id = id
        self.team = Team(
            teamId,
            teamName
        )
        self.image = image
        self.nickname = nickname
        self.name = name
        self.age = age
        self.rating = rating
        self.impact = impact
        self.dpr = dpr
        self.adr = adr
        self.kast = kast
        self.kpr = kpr
        self.headshots = headshots
        self.maps_played = maps_played

async def getPlayerById(id: int) -> Player:
    data = __player__.getPlayerById(id)
    return Player(*data)

