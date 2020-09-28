class node:
     def __init__(self,data):
         self.data= data
         self.next = None
class linklist:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    link_list= linklist()

    #assign value
    link_list.head=node(1)
    second=node(2)
    third=node(5)
    forth=node(8)

    #connect node
    link_list.head.next=second
    second.next=third
    third.next=forth
    

    #print linklist
    while link_list.head!=None:
        print(link_list.head.data,end="  ")
        link_list.head=link_list.head.next
        
