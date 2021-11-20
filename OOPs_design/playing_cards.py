"""

1.  For the first part, you must design a Game class representing the game, and these following functions
    associated with the class.

    add_card(suit, value): Creates a new card object with a suit from one of the following strings: Hearts, Spades,
    Clubs, Diamonds, and a value from one of the following strings: A, 2~10, J, Q, K. This card is represented by i,
    where i is an integer indicating how many cards have been created before. card_string(card): Returns the string
    representation of the card represented by i. It follows the format <value> of <suit>. For example, a card created by
    add_card("Spades", "3") should have a string representation of 3 of Spades. card_beats(card_a, card_b): Check if the
    card represented by card_a beats the one represented by card_b. A card beats another card if and only if it has a
    greater value. The value of the cards are ordered from A to K. You may implement these however you like. However,
    preferably this should be easily expandable to accommodate new requirements.

2.  For this part, we ask you to implement the Jokers into the system.

    In addition to the functionalities above, also implement the following functions:

    add_joker(color): Creates a Joker card of with color of either Red or Black. Joker beats everything else except
    other jokers. This card is represented by i, where i is an integer indicating how many cards have been created
    before, including both normal cards and jokers. A joker's string representation is Red Joker or Black Joker,
    depending on the color.

3.  This game also involve a concept of a Hand and comparing the size of the two hands. For this part,
    add these following functions to the Game class:

    add_hand(card_indices): Create a new Hand with cards represented by the list of integer representation of cards
    card_indices. The hand can be represented by i, where i is the number of hands added before. hand_string(hand):
    Return the string representation of the hand represented by hand. It is a list of string representation of cards
    by their insertion order, separated by ", ". For example, if hand has a 9 of Clubs, K of Hearts, and a Black
    Joker, the string representation is "9 of Clubs, K of Hearts, Black Joker". beats_hand(hand_a, hand_b): Check if
    the hand represented by hand_a beats the hand represented by hand_b according to the following rules: Starting
    from the largest card in each hand, compare them. If a card beats another, that hand beats the other hand.
    Otherwise, compare the next largest card. Repeat this process until one hand beats the other, or one hand runs
    out of cards. If a hand runs out of cards, neither hand beat each other.
    """

from enum import Enum, auto


class Card:
    def __init__(self):
        pass

    @property
    def card_value(self):
        raise NotImplemented()

    def __gt__(self, other):
        return self.card_value > other.card_value


class Suits(Enum):
    SPADES = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    CLUBS = auto()


# Creating another class that extends BaseClass. Liskov Substitution
class PlayingCard(Card):
    SUITS = {
        "Diamonds": Suits.DIAMONDS,
        "Spades": Suits.SPADES,
        "Hearts": Suits.HEARTS,
        "Clubs": Suits.CLUBS,
        }
    suits_names = {value: key for key, value in SUITS.items()}
    VALUES = {
        "A": 1,
        **{str(num): num for num in range(2, 11)},
        "J": 11,
        "Q": 12,
        "K": 13,
        }
    value_names = {value: key for key, value in VALUES.items()}

    def __init__(self, suit: str, value: str):
        super().__init__()
        self.__suit = self.SUITS[suit]
        self.__value = self.VALUES[value]

    @property
    def card_value(self):
        return self.__value

    def __str__(self):
        return f"{self.value_names[self.__value]} of {self.suits_names[self.__suit]}"


class Colors(Enum):
    RED = auto()
    BLACK = auto()


class Joker(Card):
    COLORS = {"Red": Colors.RED, "Black": Colors.BLACK}
    colors_names = {value: key for key, value in COLORS.items()}

    def __init__(self, color):
        super().__init__()
        self.__color = self.COLORS[color]

    def __str__(self):
        return f"{self.colors_names[self.__color]} Joker"

    @property
    def card_value(self):
        return 14


class Hand(PlayingCard, Joker):
    def __init__(self, card_indexes, cards):
        self.hand = [cards[card_index] for card_index in card_indexes]

    def __str__(self):
        return ", ".join([str(card) for card in self.hand])

    def __gt__(self, other):
        side_a = sorted([card.card_value for card in self.hand])
        side_b = sorted([card.card_value for card in other.hand])
        shorter = side_a
        if len(side_b) < len(side_a):
            shorter = side_b
        for index in range(len(shorter)):
            if side_a[len(side_a) - 1 - index] > side_b[len(side_b) - 1 - index]:
                return True
        return False


class Game:
    def __init__(self):
        # Implement initializer here
        self.cards = []
        self.hands = []

    def add_card(self, suit: str, value: str) -> None:
        # Implement function here
        self.cards.append(PlayingCard(suit, value))

    def card_string(self, card: int) -> str:
        # Implement function here
        return str(self.cards[card])

    def card_beats(self, card_a: int, card_b: int) -> bool:
        # Implement function here
        return self.cards[card_a] > self.cards[card_b]

    def add_joker(self, color):
        self.cards.append(Joker(color))

    def add_hand(self, card_indices: list[int]) -> None:
        # Implement function here
        self.hands.append(Hand(card_indices, self.cards))

    def hand_string(self, hand: int) -> str:
        # Implement function here
        return str(self.hands[hand])

    def hand_beats(self, hand_a: int, hand_b: int) -> bool:
        # Implement function here
        return self.hands[hand_a] > self.hands[hand_b]


if __name__ == "__main__":
    game = Game()
    hand_a_list = []
    n_1 = 5
    input1 = ["Clubs 9", "Joker Red", "Diamonds 7", "Spades 3", "Diamonds A"]

    for i in range(n_1):
        suit, value = input1[i].split()
        game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
        hand_a_list.append(i)
    game.add_hand(hand_a_list)
    print(game.hand_string(0))
    hand_b_list = []
    n_2 = 3
    input2 = ["Hearts K", "Diamonds K", "Spades J"]
    for i in range(n_1, n_1 + n_2):
        suit, value = input2[i - n_1].split()
        game.add_joker(value) if suit == "Joker" else game.add_card(suit, value)
        hand_b_list.append(i)
    game.add_hand(hand_b_list)
    print(game.hand_string(1))
    print("true" if game.hand_beats(0, 1) else "false")
