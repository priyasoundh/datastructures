import java.util.*;
class Node
{
  int data;
  Node next;
  Node(int d)
  {
    data=d;
    next=null;
  }
}

class Linkedlist
{
  Node head;
  Node tail;

  void insert_beg(Node n)
  {
    if(head==null)
    {
      head=n;
      tail=n;
      head.next=null;
    }
    else
    {
      n.next=head;
      head=n;
    }
    n=null;
  }

  void insert_pos(Node n,int p)
  {
    if(head==null)
    {
      head=n;
      tail=n;
      head.next=null;
    }
    else
    {
      Node temp=head;
      for(int i=1;i<p-1;i++)
      {
        temp=temp.next;
      }
      n.next=temp.next;
      temp.next=n;
    }
    n=null;
  }

  void insert_end(Node n)
  {
    if(head==null)
    {
      head=n;
      tail=n;
      head.next=null;
    }
    else
    {
      n.next=null;
      tail.next=n;
      tail=tail.next;
    }
    n=null;
  }

  void del_beg()
  {
    Node temp=head;
    head=head.next;
    temp.next=null;
  }

  void del_end()
  {
    Node temp=head;
    while(temp.next.next!=null)
    {
      temp=temp.next;
    }
    temp.next=null;
    tail=temp;
  }

  void del_pos(int p)
  {
    Node temp=head;
    for(int i=1;i<p-1;i++)
    {
      temp=temp.next;
    }
    Node new1=temp.next;
    temp.next=new1.next;
    new1.next=null;
  }

  void display()
  {
    Node temp=head;
    while(temp.next!=null)
    {
      System.out.print(temp.data+"-->");
      temp=temp.next;
    }
    System.out.println(temp.data);
  }

  int search(int x)
  {
    Node temp=head;
    while(temp!=null)
    {
      if(temp.data==x)
      {
        return 1;
      }
      temp=temp.next;
    }
    return 0;
  }

  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
    Linkedlist l=new Linkedlist();
    while(true)
    {
      System.out.println("1-->insert");
      System.out.println("2-->delete");
      System.out.println("3-->display");
      System.out.println("4-->search");
      int x=sc.nextInt();
      if(x==1)
      {
        System.out.println("1-->beginning");
        System.out.println("2-->end");
        System.out.println("3-->position");
        int y=sc.nextInt();
        System.out.println("enter data:");
        int data=sc.nextInt();
        Node newnode=new Node(data);
        if(y==1)
        {
          l.insert_beg(newnode);
        }
        if(y==2)
        {
          l.insert_end(newnode);
        }
        if(y==3)
        {
          System.out.println("enter position to insert:");
          int p=sc.nextInt();
          l.insert_pos(newnode,p);
        }
      }
      else if(x==2)
      {
        System.out.println("1-->beginning");
        System.out.println("2-->end");
        System.out.println("3-->position");
        int z=sc.nextInt();
        if(z==1)
        {
          l.del_beg();
        }
        if(z==2)
        {
          l.del_end();
        }
        if(z==3)
        {
          int p=sc.nextInt();
          l.del_pos(p);
        }
      }
      else if(x==3)
      {
        l.display();
      }
      else if(x==4)
      {
        int a=sc.nextInt();
        int s=l.search(a);
        if(s==1)
        {
          System.out.println("yes");
        }
        else
        {
          System.out.println("no");
        }
      }
    }
  }
}
