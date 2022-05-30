class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLL(head):
    while head is not None:
        print(str(head.data)+"->",end='')
        head=head.next
    print("None")
    return
def length(head):
    count=0
    while head is not None:
        count=count+1
        head=head.next
    return count
def insertAtIR(head,i,data):
    if i<0:
        return head
    if i==0:
        newNode=Node(data)
        newNode.next=head
        return newNode
    if head is None:
        return None
    smallHead=insertAtIR(head.next,i-1,data)
    head.next=smallHead
    return head
def insertAtI(head,i,data):
    if i<0 or i>length(head):
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        
        
        prev=curr
        curr=curr.next
        count=count+1
    newNode=Node(data)
    if prev is not None:
        prev.next=newNode
    else:
        head=newNode
    
    newNode.next=curr
    return head
def takeInput():
    inputList=[int (ele) for ele in input().split()]
    head=None
    tail=None
    for currData in inputList:
        if currData==-1:
            break
        newNode=Node(currData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head
def reverse1(head):
    if head is None or head.next is None:
        return head
    smallHead=reverse1(head.next)
    curr=smallHead
    while curr.next is not None:
        curr=curr.next
    curr.next=head
    head.next=None
    return smallHead


    

head=takeInput()
printLL(head)
head=reverse1(head)
printLL(head)

********************************************************************************************************************************************
#2nd method

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def reverse1(head):
    if head is None or head.next is None:
        return head,head
    smallhead,smalltail = reverse1(head.next)
    smalltail.next = head
    head.next = None
    return smallhead,head
    

def reverseLinkedListRec(head) :
	#Your code goes here
    ans,ans2 = reverse1(head)
    return ans































#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head




def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()

    newHead = reverseLinkedListRec(head)
    printLinkedList(newHead)

    t -= 1
