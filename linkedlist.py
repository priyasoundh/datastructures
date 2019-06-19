class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Singly_linked:
  def __init__(self):
    self.head=None
    self.tail=None

  def insert_beg(self,data):
    if(self.head==None):
      newnode=Node(data)
      self.head=newnode
      self.tail=newnode
    else:
      newnode=Node(data)
      newnode.next=self.head
      self.head=newnode
    newnode=None

  def insert_end(self,data):
    if(self.head==None):
      newnode=Node(data)
      self.head=newnode
      self.tail=newnode
    else:
      newnode=Node(data)
      self.tail.next=newnode
      self.tail=self.tail.next
    newnode=None
  
  def insert_pos(self,data,pos):
    if(self.head==None):
      newnode=Node(data)
      self.head=newnode
      self.tail=newnode
    else:
      newnode=Node(data)
      temp=self.head
      for i in range(1,pos-1):
        temp=temp.next
      newnode.next=temp.next
      temp.next=newnode
    newnode=None
  
  def delete_beg(self):
    temp=self.head
    self.head=temp.next
    temp.next=None

  def delete_end(self):
    temp=self.head
    while(temp.next.next!=None):
      temp=temp.next
    temp.next=None
  
  def delete_pos(self,pos):
    temp=self.head
    for i in range(1,pos-1):
      temp=temp.next
    new=temp.next
    temp.next=new.next
    new.next=None
  
  def search(self,x):
    temp=self.head
    while(temp!=None):
      if(temp.data==x):
        return True
      temp=temp.next
    return False
   
  def le(self):
    if(self.head==None):
      return 0
    temp=self.head
    count=0
    while(temp!=None):
      count=count+1
      temp=temp.next
    return count

  def display(self):
    temp=self.head
    while(temp.next!=None):
      print(temp.data,end='->')
      temp=temp.next
    print(temp.data)

def menu():
  print("Linkedlist")
  s=Singly_linked()
  while(1):
    print("1-->insert")
    print("2-->delete")
    print("3-->search")
    print("4-->display")
    print("5-->count number of elements")
    print("6-->exit")
    x=int(input())
    if(x==1):
      print("1--> insert at beginning")
      print("2--> insert at end")
      print("3--> insert in between beginning and end")
      y=int(input())
      val=input("data to insert:")
      if(y==1):
        s.insert_beg(val)
      if(y==2):
        s.insert_end(val)
      if(y==3):
        b=int(input("position:"))
        s.insert_pos(val,b)
    elif(x==2):
      if(s.le()>0):
        print("1--> delete at beginning")
        print("2--> delete at end")
        print("3--> delete in between beginning and end")
        y=int(input())
        if(y==1):
          s.delete_beg()
        if(y==2):
          s.delete_end()
        if(y==3):
          b=int(input("position:"))
          s.delete_pos(b)
      else:
        print("no elements found")
    elif(x==3):
      if(s.le()>0):
        a=input("data:")
        b=s.search(a)
        if(b):
          print("yes")
        else:
          print("No")
      else:
        print("no elements found")
    elif(x==5):
      print("count",s.le())
    elif(x==4):
      if(s.le()>0):
        s.display()
      else:
        print("no elemenys found")
    elif(x==6):
      break

menu()
