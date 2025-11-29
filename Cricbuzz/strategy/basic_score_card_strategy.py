from Entities.match import Match
from Entities.team import Team
from service.score_service import ScoreService
class BasicScoreCardStrategy:
    
    def __init__(self, match: Match, team1: Team, team2: Team):
        self.match = match
        self.team1 = team1
        self.team2 = team2

    def display_scorecard(self):
        match_info = self.match.get_match_info()
        print(f"Match ID: {match_info['match_id']}, Team 1: {match_info['team1']}, Team 2: {match_info['team2']}, Status: {match_info['match_status']}")
        ScoreService.get_basic_score(self.match.id)
        display_score_card(self.match.id, self.team1.id, self.team2.id)

        def display_score_card(self, matchId, team1Id, team2Id): #overrride in child strategies
            pass
