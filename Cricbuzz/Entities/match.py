from Entities.team import Team
from enums.status import MatchStatus


class Match:
    def __init__(self, id, team1: Team=None, team2: Team=None, match_status: MatchStatus=None, innings=0):
        self.id = id
        self.team1 = team1
        self.team2 = team2  
        self.current_team_playing = None
        self.match_status = match_status
        self.innings = innings

    
    def initiate_match(self, team):
        if(team != self.team1 and team != self.team2):
            raise ValueError("Team not part of this match")
        self.current_team_playing = team
        self.match_status = MatchStatus.Live

    def complete_innings(self):
            if(self.current_team_playing is None):
                raise ValueError("No innings to complete")
            self.innings += 1
            self.current_team_playing = None

    def initiate_second_innings(self, team):
        if(team != self.team1 and team != self.team2):
            raise ValueError("Team not part of this match")
        if(team == self.current_team_playing):
            raise ValueError("Same team cannot play consecutive innings")
        self.current_team_playing = team

    def get_match_info(self):
        return {
            "match_id": self.id,
            "team1": self.team1.name,
            "team2": self.team2.name,
            "current_team_playing": self.current_team_playing.name if self.current_team_playing else None,
            "match_status": self.match_status.value
        }       
    
    def match_overview(self):
        return f"Match {self.id} between {self.team1.name} and {self.team2.name} is currently {self.match_status.value}."