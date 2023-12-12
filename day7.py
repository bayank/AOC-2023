
"""Test input:
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

"""



def evaluate_hand(hand):
    unique_cards = set(hand)
    card_counts = [hand.count(card) for card in unique_cards]
    if len(unique_cards) == 1:
        # Five of a kind
        return 6
    elif len(unique_cards) == 2:
        if card_counts.count(4) == 1:
            # Four of a kind
            return 5
        elif card_counts.count(3) == 1 and card_counts.count(2) == 1:
            # Full house
            return 4
    elif len(unique_cards) == 3:
        if card_counts.count(3) == 1 and card_counts.count(1) == 2:
            # Three of a kind
            return 3
        elif card_counts.count(2) == 2 and card_counts.count(1) == 1:
            # Two pair
            return 2
    elif len(unique_cards) == 4:
        if card_counts.count(2) == 1 and card_counts.count(1) == 3:
            # One pair
            return 1
    elif len(unique_cards) == 5:
        # High card
        return 0
    return 'Invalid'

def card_weight(card):
    if card.isdigit() and card != '10':
        return int(card)
    return {'A': 14, 'J': 11, 'Q': 12, 'K': 13, 'T': 10}[card]

def sort_key(hand_dict):
    evaluation = hand_dict['evaluation']
    hand = hand_dict['hand']
    weights = [card_weight(card) for card in hand]  # Weights in the order of cards in hand
    return (evaluation, weights)

if __name__ == '__main__':
    sumprod = 0
    card_list = []
    with open('day7_input.txt') as f:
        for line in f:
            cards, bid = line.strip().split(' ')
            hand = list(cards)
            evaluation = evaluate_hand(hand)
            card_dict = {
                'hand': hand,
                'bid': int(bid),
                'evaluation': evaluation,
                'rank': None
            }
            card_list.append(card_dict)

    # Sort the card_list and assign ranks
    card_list.sort(key=sort_key, reverse=True)
    for i, hand in enumerate(card_list, start=1):
        hand['rank'] = len(card_list) - i + 1

    for card in card_list:
        sumprod += card['bid'] * card['rank']
        print(f"{card}")
    print(f'Part 1: {sumprod}')

"""
1. Sort all hands from lowest to highest
    a. for hands with the same weight, evaluate the 1st card, then the 2nd, then the 3rd until one is higher
2. New rank is the order sorted, lowest to highest
3. multiply the bid with the rank for each hand, return the sum
"""