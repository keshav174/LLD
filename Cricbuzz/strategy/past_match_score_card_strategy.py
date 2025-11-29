from basic_score_card_strategy import BasicScoreCardStrategy
from enums.status import MatchStatus
from service.score_service import ScoreService

class PastMatchScoreCardStrategy(BasicScoreCardStrategy):
    def display_scorecard(self):
        if(self.match.match_status in [MatchStatus.Upcoming, MatchStatus.Live]):
            raise ValueError("Match is not completed yet. Cannot display past match scorecard.")
        if(self.match.match_status in [MatchStatus.Completed, MatchStatus.Drawn]):
            ScoreService.display_score_card(self.match.id, self.team1.id)
            ScoreService.display_score_card(self.match.id, self.team2.id)
        
