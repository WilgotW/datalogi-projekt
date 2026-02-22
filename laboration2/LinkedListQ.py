class LinkedListQ:
    def __init__(self):
        self.__head = None #the first item in the queue
        self.__tail = None #the last item in the queue

    def __str__(self):
        if self.__head == None:
            return "No data"

        que_string = str(self.__head)

        temp = self.__head
        while temp != self.__tail:
            temp = temp.next
            que_string += str(temp)

        return que_string

    #This algorithm is O(1). Besides remove(x)
    def enqueue(self, data):
        new_node = Node(data)

        if self.__tail != None:
            #point current tail to new tail. 
            self.__tail.next = new_node
            self.__tail = new_node
        else:
            #queue is empty
            self.__head = new_node
            self.__tail = new_node

    def dequeue(self):
        if self.__head == None:
            return None

        return_data = self.__head.data
        self.__head = self.__head.next

        if self.__head == None:
            self.__tail = None

        return return_data

    def isEmpty(self):
        if self.__head == None:
            return True
        return False

    def remove(self, data):

        if self.__head is None:
            return

        if self.__head.data == data:
            self.__head = self.__head.next

            if self.__head is None:
                self.__tail = None

            return

        previous = self.__head
        current = self.__head.next

        while current != None:
            if current.data == data:
                #unlink the wanted node
                previous.next = current.next

                #if we unlinked the tail
                if current == self.__tail:
                    self.__tail = previous

                return
            #move pointers forward
            previous = current
            current = current.next

def basictest():
    q = LinkedListQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue() 

    # Förväntat resultat
    if (x == 1 and y == 2 and q.isEmpty()):
        print("test OK")
    else:
        print("FAILED expected x=1 and y=2 and an empty list but got x =", x, " y =", y, " and empty list is", q.isEmpty())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    basictest()