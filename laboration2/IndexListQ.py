
class IndexListQ:
    def __init__(self):
        self.data = []

    def __str__(self):
        data_string = ""
        for i in self.data:
            data_string += f" {i} "
        return data_string

    def enqueue(self, new_data):
        self.data.insert(0, new_data)

    def dequeue(self):
        return self.data.pop()

    def isEmpty(self):
        if(len(self.data) == 0):
            return True
        return False

def basictest():
    q = IndexListQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue() 

    # Förväntat resultat
    if (x == 1 and y == 2 and q.isEmpty()):
        print("test OK")
    else:
        print("FAILED expected x=1 and y=2 and an empty list but got x =", x, " y =", y, " and empty list is", q.isEmpty())

if __name__ == "__main__":
    basictest()