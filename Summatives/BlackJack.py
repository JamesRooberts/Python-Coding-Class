
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) < 10:
            self.build()
        return self.cards.pop()

class BlackjackHand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value, aces = 0, 0
        for card in self.cards:
            if card.value.isnumeric():
                value += int(card.value)
            elif card.value in ["J", "Q", "K"]:
                value += 10
            else:
                aces += 1

        value += aces
        while value <= 11 and aces > 0:
            value += 10
            aces -= 1

        return value

    def can_split(self):
        return len(self.cards) == 2 and self.cards[0].value == self.cards[1].value

    def has_blackjack(self):
        return len(self.cards) == 2 and self.calculate_value() == 21

class Player:
    def __init__(self, bankroll=1000):
        self.hands = [BlackjackHand()]
        self.bankroll = bankroll
        self.current_bet = [0]

    def bet(self, amount, hand_idx=0):
        if amount <= self.bankroll:
            self.bankroll -= amount
            self.current_bet[hand_idx] = amount
        else:
            print("You don't have enough money!")
            return False
        return True

    def split(self, hand_idx):
        if self.hands[hand_idx].can_split() and self.bet(self.current_bet[hand_idx], len(self.hands)):
            new_hand = BlackjackHand()
            new_hand.add_card(self.hands[hand_idx].cards.pop())
            self.hands.append(new_hand)
            return True
        return False

class Dealer:
    def __init__(self):
        self.hand = BlackjackHand()

def insurance_bet(player, dealer):
    insurance_amount = int(input("Enter insurance bet amount (max half of original bet): "))
    if 0 < insurance_amount <= player.current_bet[0] / 2:
        player.bankroll -= insurance_amount
        if dealer.hand.has_blackjack():
            player.bankroll += insurance_amount * 3
            return True
    return False

def play_blackjack():
    deck = Deck()
    player = Player()
    dealer = Dealer()

    while player.bankroll > 0:
        print(f"\nBankroll: ${player.bankroll}")
        bet_amount = int(input("Place your bet: "))
        player_bet = player.bet(bet_amount)

        if not player_bet:
            continue

        player.hands[0].add_card(deck.draw_card())
        player.hands[0].add_card(deck.draw_card())
        dealer.hand.add_card(deck.draw_card())
        dealer.hand.add_card(deck.draw_card())

        print(f"\nPlayer's hand: {player.hands[0].cards}")
        print(f"Dealer's visible card: {dealer.hand.cards[1]}")

        insurance_won = False
        if dealer.hand.cards[1].value == "A":
            print("Insurance bet available!")
            if input("Do you want to place an insurance bet? (yes, no): ").lower() == "yes":
                insurance_won = insurance_bet(player, dealer)

        for hand_idx, hand in enumerate(player.hands):
            if insurance_won:
                break

            print(f"\nPlaying hand {hand_idx + 1}...")
            while True:
                action = input("Choose an action (hit, stay, double, split): ").lower()

                if action == "hit":
                    hand.add_card(deck.draw_card())
                    print(f"\nPlayer's hand {hand_idx + 1}: {hand.cards}")

                    if hand.calculate_value() > 21:
                        print("You busted!")
                        player_busted = True
                        break
                elif action == "stay":
                    break
                elif action == "double":
                    if player.bet(player.current_bet[hand_idx], hand_idx):
                        hand.add_card(deck.draw_card())
                        print(f"\nPlayer's hand {hand_idx + 1}: {hand.cards}")

                        if hand.calculate_value() > 21:
                            print("You busted!")
                            player_busted = True
                        break
                elif action == "split":
                    if player.split(hand_idx):
                        print(f"\nPlayer's hands after split:")
                        for i, h in enumerate(player.hands):
                            print(f"Hand {i + 1}: {h.cards}")
                    else:
                        print("You cannot split this hand.")
                else:
                    print("Invalid action. Please choose either 'hit', 'stay', 'double', or 'split'.")

            if player_busted:
                break

        if not insurance_won:
            while dealer.hand.calculate_value() < 17:
                dealer.hand.add_card(deck.draw_card())

            print(f"\nDealer's hand: {dealer.hand.cards}")

            for hand_idx, hand in enumerate(player.hands):
                if hand.calculate_value() <= 21:
                    if dealer.hand.calculate_value() > 21 or hand.calculate_value() > dealer.hand.calculate_value():
                        print(f"Hand {hand_idx + 1} won!")
                        player.bankroll += 2 * player.current_bet[hand_idx]
                    else:
                        print(f"Hand {hand_idx + 1} lost!")

        player.hands = [BlackjackHand()]
        player.current_bet = [0]

        if player.bankroll <= 0:
            print("\nYou've run out of money! Game over.")
            break

        play_again = input("\nDo you want to play another round? (yes, no): ").lower()
        if play_again == 'no':
            break

if __name__ == "__main__":
    play_blackjack()
