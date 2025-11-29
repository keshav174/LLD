class Team:
    def __init__(self, name, players, id, coach=None):
        self.name = name
        self.players = players
        self.id = id
        self.coach = coach

    
    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def find_palyer_by_name(self, name):
        for player in self.players:
            if player.name == name:
                return player
        return None
    
    def find_palyer_by_id(self, id):
        for player in self.players:
            if(player.id == id):
                return player 
        return None