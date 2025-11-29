from Entities.match import Match
from Entities.team import Team
from service.score_service import ScoreService
class BasicScoreCardStrategy:
    
    def __init__(self, match: Match):
        self.match = match

    def display_scorecard(self):
        match_info = self.match.get_match_info()
        print(f"Match ID: {match_info['match_id']}, Team 1: {match_info['team1']}, Team 2: {match_info['team2']}, Status: {match_info['match_status']}")
        ScoreService.get_basic_score(self.match.id)
        display_score_card(self.match.id, self.match.team1.id, self.match.team2.id)

        def display_score_card(self, team1_id, team2_id): #overrride in child strategies
            pass
