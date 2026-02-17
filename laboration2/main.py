from LinkedListQ import LinkedListQ

def card_trick(cards):
    table = []

    table_cards = LinkedListQ()
    for card in cards: 
        table_cards.enqueue(card)


    while table_cards.isEmpty() is False: 
        removed_val = table_cards.dequeue()
        table_cards.enqueue(removed_val)

        added_val = table_cards.dequeue()
        table.append(added_val)

    return table

def main():
    answer = input("Vilken ordning ligger korten i?")
    cards = answer.strip().split()
    table = card_trick(cards)

    print("Det kommer i följande steg: ", end="")
    print(table)

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