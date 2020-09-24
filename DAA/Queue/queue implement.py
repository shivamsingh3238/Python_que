class queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,k):
        self.queue.append(i)
    def dequeue(self):
        self.queue.pop(0)




q=queue()
print("print que before doing any operation")
ele= list(map(int,input().split()))
for i in ele:
    q.enqueue(i)
print(self.queue)
print("after dequeue frist element")

q.dequeue()
print(self.queue)
