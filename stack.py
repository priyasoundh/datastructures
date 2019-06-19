class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Singly_linked:
  def __init__(self):
    self.head=None
    self.tail=None

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

  def delete_end(self):
    temp=self.head
    while(temp.next.next!=None):
      temp=temp.next
    temp.next=None

  def peak(self):
    temp=self.head
    count=1
    while(temp.next!=None):
      temp=temp.next
      count=count+1
    return count

  def search(self,x):
    temp=self.head
    while(temp!=None):
      if(temp.data==x):
        return True
      temp=temp.next
    return False
   
  def le(self):
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
  print("Stack")
  s=Singly_linked()
  while(1):
    print("1-->insert")
    print("2-->delete")
    print("3-->search")
    print("4-->display")
    print("5-->count number of elements")
    print("6-->peek")
    print("7-->exit")
    x=int(input())
    if(x==1):
      val=input("data to insert:")
      s.insert_end(val)
    elif(x==2):
      if(s.le()>0):
        s.delete_end()
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
    elif(x==4):
      if(s.le()>0):
        s.display()
      else:
        print("no elements found")
    elif(x==5):
      print("count:",s.le())
    elif(x==6):
      print("peak:",s.peak())
    elif(x==7):
      break

menu()
