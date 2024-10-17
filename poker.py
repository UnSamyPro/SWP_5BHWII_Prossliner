import random
from typing import Set


# Poker
#x 0 High Card: highest card
#x 1 One Pair: pair, same symbol, different color
#x 2 Two Pairs: 2x pair, same symbol, different color
#x 3 Three of a Kind: three cards, same symbol, different color
#x 4 Straight: 5 cards, consecutive symbols, different color
#x 5 Flush: 5 cards, different symbols, same color
#x 6 Full House: Three of a Kind AND One Pair
#x 7 Four of a Kind: four cards, same symbol, different color
#x 8 Straight Flush: 5 cards, consecutive symbols, same color
# 9 Royal Flush: 10, J, Q, K, A, same color


def main(max_symbols=13, max_colors=4, hand_size=5, max_hands=100000):
    combinations = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House",
                    "Four of a Kind", "Straight Flush", "Royal Flush"]
    symbols = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    colors = ["♠ spades", "♣ clubs", "♦ diamonds", "♥ hearts"]  # spades, clubs, diamonds, hearts

    # {(0,0): "2 ♠", (0,1): "2 ♣", (0,2): "2 ♦", (0,3): "2 ♥", ...}
    cards = {(i, j): f"{symbols[i]} {colors[j]}" for i in range(max_symbols) for j in range(max_colors)}
    print(cards)

    combination_statistic = {k: 0 for k in range(len(combinations))}

    numbers = [i for i in range(0, max_symbols * max_colors)]
    for _ in range(0, max_hands):
        hand = random_hand(numbers, max_symbols, max_colors, hand_size)
        comb_type = combination_type(hand, max_symbols, max_colors, hand_size)
        combination_statistic[comb_type] += 1

        # if comb_type >= 9:
        #     comb_name = combinations[comb_type]
        #     print(f"{hand} -> {comb_name}")
        #     break

    for i in range(len(combination_statistic)):
        print(f"{combinations[i]}: {combination_statistic[i]} ({combination_statistic[i] / max_hands * 100}%)")


def hand_amount_same_symbol(hand: list[tuple[int, int]]) -> list[int]:
    symbols = list(hand[i][0] for i in range(len(hand)))
    counts = list(symbols.count(s) for s in set(symbols))
    return counts


def hand_is_same_symbol(hand: list[tuple[int, int]], matches: list[int]) -> bool:
    counts = hand_amount_same_symbol(hand)
    for match in matches:
        if match not in counts:
            return False
        else:
            counts.remove(match)
    return True


def hand_amount_same_color(hand: list[tuple[int, int]]) -> list[int]:
    colors = list(hand[i][1] for i in range(len(hand)))
    counts = list(colors.count(c) for c in set(colors))
    return counts


def hand_is_same_color(hand: list[tuple[int, int]], matches: list[int]) -> bool:
    colors = hand_amount_same_color(hand)
    for match in matches:
        if match not in colors:
            return False
        else:
            colors.remove(match)
    return True
    # return len(set(hand[i][1] for i in range(len(hand)))) <= len(hand) + 1 - amount_to_match


def combination_type(hand: list[tuple[int, int]], max_symbols=13, max_colors=4, amount=5) -> int:
    # sort hand by symbol ascending
    hand.sort(key=lambda x: x[0])

    # 9 Royal Flush: 10, J, Q, K, A, same color
    if hand_is_same_color(hand, matches=[5]) and any(all(hand[j + k][0] == j + i and hand[j + k][1] == color for j in range(5)) for i in range(8, max_symbols) for k in range(amount - 5 + 1) for color in range(max_colors)):
        return 9
    # 8 Straight Flush: 5 cards, consecutive symbols, same color
    elif hand_is_same_color(hand, matches=[5]) and any(all(hand[j + k][0] == j + i and hand[j + k][1] == color for j in range(5)) for i in range(max_symbols) for k in range(amount - 5 + 1) for color in range(max_colors)):
        return 8
    # 7 Four of a Kind: four cards, same symbol, different color
    elif hand_is_same_symbol(hand, matches=[4]):
        return 7
    # 6 Full House: Three of a Kind AND One Pair
    elif hand_is_same_symbol(hand, matches=[3, 2]):
        return 6
    # 5 Flush: 5 cards, different symbols, same color
    elif hand_is_same_color(hand, matches=[5]):
        return 5
    # 4 Straight: 5 cards, consecutive symbols, different color
    elif any(all(hand[j + k][0] == j + i for j in range(5)) for i in range(max_symbols) for k in range(amount - 5 + 1)):
        return 4
    # 3 Three of a Kind: three cards, same symbol, different color
    elif hand_is_same_symbol(hand, matches=[3]):
        return 3
    # 2 Two Pairs: 2x pair, same symbol, different color
    elif hand_is_same_symbol(hand, matches=[2, 2]):
        return 2
    # 1 One Pair: pair, same symbol, different color
    elif hand_is_same_symbol(hand, matches=[2]):
        return 1
    # 0 High Card: highest card
    return 0


def random_hand(numbers_, max_symbols=13, max_colors=4, hand_size=5) -> list[tuple[int, int]]:
    numbers = [i for i in range(0, max_symbols * max_colors)]
    positions = []
    for i in range(hand_size):
        rand_number_index = random.randint(0, max_symbols * max_colors - i - 1)
        rand_number = numbers[rand_number_index]
        numbers[rand_number_index], numbers[max_symbols * max_colors - i - 1] = \
            numbers[max_symbols * max_colors - i - 1], numbers[rand_number_index]

        positions.append((rand_number // max_colors, rand_number % max_colors))
        pass
    # for i in range(hand_size):
    #     rand_number = numbers[max_symbols * max_colors - i - 1]
    #     symbol_i = rand_number // max_colors
    #     color_j = rand_number % max_colors
    #     positions.append((symbol_i, color_j))
    return positions


if __name__ == "__main__":
    main()
