from IndexListQ import IndexListQ
from LinkedListQ import LinkedListQ

def card_trick(cards):
    table_cards = LinkedListQ()

    while len(cards) > 0:
        cards_left = []
        for i in range(len(cards)):
            if len(cards) == 1: #sista kortet läggs på bordet
                table_cards.enqueue(cards[i])
            elif i % 2: #var annat kort läggs på bordet
                table_cards.enqueue(cards[i])
            else: #kortet blir kvar i handen
                cards_left.append(cards[i])
        cards = cards_left
    return table_cards


def main():
    answer = input("Vilken ordning ligger korten i?")
    cards = answer.strip().split()
    trick = card_trick(cards)

    print("Det kommer i följande steg: ", end="")
    print(trick)


def test_linkedlistq():
    queue = LinkedListQ()

    queue.enqueue("Hello")
    queue.enqueue("hej")
    queue.enqueue(2)

    queue.remove("hej")
    queue.remove("Hello")
    queue.remove(2)
    print(queue)

    queue.enqueue(1)
    queue.enqueue(5)
    print(queue)

test_linkedlistq()

main()