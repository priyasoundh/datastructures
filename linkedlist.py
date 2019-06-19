def insert_beg(l,a):
  l.insert(0,a)
  display(l)

def insert_end(l,a):
  l.append(a)
  display(l)

def insert_mid(l,a,b):
  l.insert(b-1,a)
  display(l)

def delete_beg(l):
  del l[0]
  display(l)

def delete_end(l):
  l.pop()
  display(l)

def delete_mid(l,b):
  del l[int(b)-1]
  display(l)

def search(l,a):
  if a in l:
    return True
  else:
    return False
  
def display(l):
  if(len(l)>0):
    for x in range(0,len(l)-1):
      print(l[x],end='->')
    print(l[-1])
  else:
    print("no elements found")

def menu():
  l=[]
  print("Linked list")
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
        insert_beg(l,val)
      if(y==2):
        insert_end(l,val)
      if(y==3):
        b=int(input("position:"))
        insert_mid(l,val,b)
    elif(x==2):
      if(len(l)>0):
        print("1--> delete at beginning")
        print("2--> delete at end")
        print("3--> delete in between beginning and end")
        y=int(input())
        if(y==1):
          delete_beg(l)
        if(y==2):
          delete_end(l)
        if(y==3):
          b=int(input("position:"))
          if(b<=len(l)):
            delete_mid(l,b)
          else:
            print("invalid position")
      else:
        print("no elements found")
    elif(x==3):
      if(len(l)>0):
        a=input("data:")
        b=search(l,a)
        if(b):
          print("yes")
        else:
          print("No")
      else:
        print("empty")
    elif(x==4):
      display(l)
    elif(x==5):
      print("count:",len(l))
    elif(x==6):
      break
    else:
      print("enter valid input")

menu()
