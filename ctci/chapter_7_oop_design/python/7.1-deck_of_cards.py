from enum import Enum
from abc import ABC, abstractmethod


class Suit(Enum):
    CLUB = 1
    DIAMOND = 2
    HEART = 2
    SPADE = 3


class Deck:
    def __init__(self):
        """
        Deck constructor.
        """
        self.cards = []
        self.dealt_index = 0

    def set_deck_of_cards(self):
        """
        Initialize deck of cards.
        """
        pass

    def shuffle(self):
        """
        Shuffle deck of cards.
        """
        pass

    def remaining_cards(self) -> int:
        """
        Returns remaining number of cards in deck.
        """
        return len(self.cards) - self.dealt_index

    def deal_hand(self, number):
        """
        Deal a hand according to given input number of cards.
        """
        pass

    def deal_card(self):
        """
        Deals a card.
        """
        pass


class Card(ABC):
    def __init__(self, c: int, s: Suit):
        """
        Card constructor
        """
        self.available = True
        """
        Number or face that's on card - a number 2 through 10, or 11 for Jack, 12 for Queen, 13 for King, or 1 for Ace.
        """
        self.face_value = c
        self.suit = s

    def is_available(self):
        """
        Checks if the card is available to be given out to someone.
        """
        return self.available

    def mark_unavailable(self):
        """
        Marks card as unavailable.
        """
        self.available = False

    def mark_available(self):
        """
        Marks card as available.
        """
        self.available = True

    @abstractmethod
    def value(self):
        """
        Returns value as evaluated from derived class.
        """
        pass


class Hand:
    def __init__(self):
        """
        Hand constructor
        """
        self.cards = []

    def score(self):
        """
        Returns score as a sum of all of cards' values.
        """
        score = 0
        for card in self.cards:
            score += card.value

    def add_card(self, card):
        """
        Add a card to hand.
        """
        self.cards.append(card)


class BlackJackHand(Hand):

    """
    There are multiple possible scores for a blackjack hand, since aces have multiple values. Return the highest possible score that's under 21, or the lowest score that is over.
    """

    def score(self) -> int:
        """
        Returns best possible score in hand.
        """
        scores = self.possible_scores()
        max_under = float("-inf")
        min_over = float("inf")
        for s in scores:
            if s > 21 and s < min_over:
                min_over = s
            elif s < 21 and s > max_under:
                max_under = s
        if max_under == float("-inf"):
            return min_over
        else:
            return max_under

    def possible_scores(self):
        """
        Returns all possible scores that can be derived from hand.
        """
        pass

    def is_busted(self) -> bool:
        """
        Determines if hand is "busted" or over score limit.
        """
        return self.score > 21

    def is_21(self) -> bool:
        """
        Determines if hand's score equals 21.
        """
        return self.score == 21

    def is_blackjack(self):
        """
        Determines if hand has an Ace and a face value.
        """
        pass


class BlackJackCard(Card):
    def __init__(self, c: int, s: Suit):
        """
        Blackjack Card constructor.
        """
        super().__init__(c, s)

    def value(self) -> int:
        """
        Returns the card's value.
        """
        if self.is_ace():
            return 1
        elif self.is_face_card():
            return 10
        return self.face_value

    def is_ace(self):
        """
        Determines if the card is an ace.
        """
        return self.face_value == 1

    def min_value(self) -> int:
        """
        Returns the minimum value of a card.
        """
        if self.is_ace():
            return 1
        return self.value()

    def max_value(self) -> int:
        """
        Returns the maximum value of a card.
        """
        if self.is_ace():
            return 11
        return self.value()

    def is_face_card(self) -> bool:
        """
        Determines if a card is a face card.
        """
        return self.face_value >= 11 and self.face_value <= 13


ace_spaces = BlackJackCard(1, Suit.CLUB.name)
print(ace_spaces.__dict__)
# {'available': True, 'face_value': 1, 'suit': 'CLUB'}
print(ace_spaces.max_value())  # 11
print(ace_spaces.min_value())  # 1
