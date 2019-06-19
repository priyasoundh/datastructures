def push(l,a):
  l.append(a)
  display(l)

def pop(l):
  l.pop()
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

def peak(l):
  if(len(l)>0):
    return l[-1]
  else:
    print("no elements found")

def menu():
  l=[]
  print("Stack")
  while(1):
    print("1-->push")
    print("2-->pop")
    print("3-->search")
    print("4-->display")
    print("5-->count number of elements")
    print("6-->peak")
    print("7-->exit")
    x=int(input())
    if(x==1):
      val=input("data to insert:")
      push(l,val)
    elif(x==2):
      if(len(l)>0):
        pop(l)
      else:
        print("underflow")
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
      print("peak:",peak(l))
    elif(x==7):
      break
    else:
      print("enter valid input")

menu()
