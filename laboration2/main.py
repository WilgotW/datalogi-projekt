from IndexListQ import IndexListQ
import copy

def card_trick(cards):

    cards_copy = IndexListQ()
    table_cards = IndexListQ()
    
    for i in range(len(cards)):
        print(i)
        #cards_copy.enqueue(cards[len(cards) - i])
    
    for i in cards_copy.data:
        cards_copy.dequeue()
        if((i+1) % 2):
            table_cards.enqueue(cards[i])
        else:
            cards_copy.enqueue(cards[i])
            

def main():
    answer = input("Vilken ordning ligger korten i?")
    cards = answer.strip().split()
    print(len(cards))
    trick = card_trick(cards)
    # print("Det kommer i följande steg: ", end="")
    # for card in trick:
    #     print(card, end=" ")
    # print()

main()