class circularequeue():
    def __init__(self,k):
        self.k=k
        self.queue=[None]*k
        self.front = self.rear = -1

    #add element into circulare queue
    def enqueue(self,d):
        if ((self.rear + 1) % self.k == self.front):
            print("queue is full")
            print(d)
        elif  (self.front==-1):
              self.front=0
              self.real=0
              self.queue[self.rear]=d
        else:
            self.rear=(self.rear+1)%self.k
            self.queue[self.rear]=d
    def show(self):
        if (self.front==-1):
            print("no item present in queue")

        elif (self.rear > self.front):
            for i in range(self.front, self.rear+1):
                print(self.queue[i])
        else:
            for i in range(self.front,self.rear):
                print(self.queue[i])
            for i in range(0,self.rear):
                print(self.queue[i])
    
            
            


#n=int(input("how many item in your queue"))
q=circularequeue(5)
##ele=list(map(int,input().split()))
##for i in ele:
q.enqueue(1)
q.enqueue(2)
q.enqueue(6)
q.enqueue(5)
q.enqueue(7)
print("after all dequeue",q.show())
