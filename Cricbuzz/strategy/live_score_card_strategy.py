from basic_score_card_strategy import BasicScoreCardStrategy
from enums.status import MatchStatus
from service.score_service import ScoreService

class LiveScoreCardStrategy(BasicScoreCardStrategy):
    def display_scorecard(self):
        if self.match.match_status != MatchStatus.Live:
            raise ValueError("Match is not live. Cannot display live scorecard.")
        if self.match.innings == 1:
            ScoreService.display_batting_score_card(self.match.id, self.match.team2.id)
            ScoreService.display_bowling_score_card(self.match.id, self.match.team1.id)
        elif self.match.innings == 0:
            ScoreService.display_batting_score_card(self.match.id, self.match.team1.id)
            ScoreService.display_bowling_score_card(self.match.id, self.match.team2.id)
        if self.match.innings >=2:
            print("both ininis are completed)")