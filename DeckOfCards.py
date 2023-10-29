import random

"""Create class to represent individual playing cards"""


class Card:
    def __init__(self, suit, name, rank):
        self.suit = suit
        self.rank = rank
        self.name = name

    def __str__(self):
        return f"Suit: {self.suit}, Name: {self.name}, Rank: {self.rank}"

    """comparisons between cards based on their ranks"""

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        return self.rank < other.rank

    """comparisons between cards based on their ranks"""

    def __gt__(self, other):
        if self.rank == other.rank:
            return self.suit > other.suit
        return self.rank > other.rank


# Create a `Deck` class to represent a standard deck of cards
class DeckCards():
    def __init__(self):
        """An array containing a deck of cards"""
        self.deck = []
        # Creating a joker card
        self.joker = Card("Joker", "Joker", float("inf"))
        # An array that contains all suit
        self.all_suit = ["Spade", "Heart", "Diamond", "Club"]
        # An array that contains all name
        self.all_name = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Prince', 'Queen', 'King']
        # Creating a deck of cards
        for suit in self.all_suit:
            for name in range(len(self.all_name)):
                # Create a card by calling the constructor of the parent class
                one_card = Card(suit, self.all_name[name], name + 1)
                # Adds a card to the deck
                self.deck.append(one_card)
        # Adding jokers to the deck
        for i in range(2):
            self.deck.append(self.joker)

    """shuffle the cards in the deck"""

    def shuffle(self):
        random.shuffle(self.deck)

    """draw a single card from the deck"""

    def draw(self):
        draw_card = self.deck.pop()
        return (f"Suit: {draw_card.suit} Name:{draw_card.name} Rank: {draw_card.rank}\n")

    """return the number of cards in the deck"""

    def __len__(self):
        return len(self.deck)

    """provide a human-readable representation of the deck"""

    def __str__(self):
        result = ""
        for card in self.deck:
            result += f"Suit: {card.suit}, Name: {card.name}, Rank: {card.rank}\n"
        return result

    """access cards in the deck by index"""
    def __getitem__(self, item):
        return self.deck[item]

    """sort the deck by rank"""
    def sort_by_rank(self):
        self.deck.sort(key=lambda card: card.rank)

    """sort the deck by suit"""
    def sort_by_suit(self):
        self.deck.sort(key=lambda card: card.suit)

"""deal a specified number of cards from the deck into a hand"""
def deal_hand(deck, num_cards):
    hand = ""
    for i in range(num_cards):
        hand += deck.draw()
    # Returns all the cards that came out of the deck
    return str(hand)


"""count how many cards of each rank are in the deck"""
def count_cards(deck):
    # Resets a deck
    count = {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'Prince': 0, 'Queen': 0,
             'King': 0, 'Joker': 0}
    # If a card is in the deck, add 1 to the count
    for card in deck.deck:
        name = str(card.name)
        count[name] += 1
    return count


if __name__ == "__main__":
    # one_card = Card("Heart", 5,5)
    Game_Card = DeckCards()
    Game_Card.sort_by_suit()
    Game_Card.sort_by_rank()
    Game_Card.shuffle()
    print(deal_hand(Game_Card, 4))
    print(count_cards(Game_Card))

    # print(len(a))
    # a.shuffle()
    # hand = deal_hand(a, 30)
    # hand = count_cards(a)
    # print(hand)
    # print(count_cards(a))
    #
    # card1 = Card("Heart", "King", 11)
    # card2 = Card("Club", "Queen", 11)
    # print(card1 < card2)
    # print(card1 > card2)

    # a.draw()

    # a.sort_by_suit()
    # a.sort_by_rank()
    # print(a)
    # print(len(a))
    # print(str(one_card))
    # print(str(a))
    # print(f"Current card: {a[5]}")
