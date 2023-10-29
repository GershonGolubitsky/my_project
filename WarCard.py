from DeckOfCards import DeckCards

"""Definition of the "Player" class representing a player in the game"""
class Player:
    def __init__(self, idx, name: str, hand: list = None):
        """Initialize a player with a name, an identifier (idx), and an empty hand"""
        self.name = name
        self.idx = idx
        if hand:
            self.hand = hand
        else:
            self.hand = []
        self.victories = 0

    def get_card(self, war=False):
        """Get a card from the player's hand"""
        if not self.hand:
            return None
        cards = self.hand.pop(0)
        if war:
            n = min(4, len(self.hand))
            cards = self.hand[:n]
            self.hand = self.hand[n:]
        return cards

    def win_round(self, cards):
        """Add the cards from a won round to the player's hand and update their victory count"""
        self.hand += cards
        self.victories += 1

"""Definition of the "Game" class representing the actual game"""
class Game:
    def __init__(self, num_players, rounds=None):
        """Initialize the game with a specified number of players and optional rounds"""
        self.deck = DeckCards()
        self.deck.shuffle()
        self.players = [Player(p, f"Player {p + 1}") for p in range(num_players)]
        self.rounds = rounds

    def is_a_war(self, top):
        """Check if there is a war based on the status of players"""
        num_participating_players = len([player for player in top.values() if player is not None])
        return num_participating_players > 1

    def play_round(self):
        """Prepare for a new round and handle any wars"""
        top = {p.idx: p.get_card() for p in self.players}
        pile = []
        while self.is_a_war(top):
            """Handle the case when there's a war"""
            war_players = list(self.players)
            pile += [top[p] for p in war_players]
            for p in war_players:
                top[p] = p.get_card()

        else:
            max_idx = self.get_winner_idx()
        winner = self.players[max_idx]
        winner.win_round(pile)

    def get_winner_idx(self):
        """Find the winning player at the end of the round"""
        max_rank = -1
        winning_idx = -1

        for idx, player in enumerate(self.players):
            if player.hand and player.hand[-1].rank > max_rank:
                max_rank = player.hand[-1].rank
                winning_idx = idx
        return winning_idx

"""The main function that runs the game"""
if __name__ == "__main__":
    """Create a game with 2 players and 5 rounds"""
    Game_Card = Game(2, rounds=5)
    for round in range(Game_Card.rounds):
        # Play the specified number of rounds
        Game_Card.play_round()

    # Print the results to the screen
    for player in Game_Card.players:
        print(f"Player: {player.name}, Number of victories: {player.victories}")
