from Entities.team import Team
from Entities.match import Match
from Entities.player import Player
from strategy.basic_score_card_strategy import BasicScoreCardFactory
from strategy.past_match_score_card_strategy import PastMatchScoreCardStrategy
from strategy.live_score_card_strategy import LiveScoreCardStrategy
from service.score_service import ScoreService


class Cricbuzz:
    _instance = None
    match_list = []

    #singleton class
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Cricbuzz, cls).__new__(cls)
        return cls._instance    
    
    player1 = Player(1, "Player One", 28, 1)
    player2 = Player(2, "Player Two", 30, 2)

    player3 = Player(3, "Player Three", 25, 1)
    player4 = Player(4, "Player Four", 27, 2)

    team1 = Team(1, "Team A", [player1, player2])
    team2 = Team(2, "Team B", [player3, player4])

    match1 = Match(101, team1, team2)

    match_list.append(match1)

    match1.initiate_match(team1)
    def display(self):
        LiveScoreCardStrategy.display_scorecard(self.match_list[0])


if __name__ == "__main__":
    cricbuzz = Cricbuzz()
    cricbuzz.display()