import java.lang.*;
import java.util.*;

public class LinkedQueue<T>{
    private Node firstNode;
    private Node lastNode;
    public LinkedQueue(){
        firstNode = null;
        lastNode = null;
    }
    public boolean isEmpty(){
        return (firstNode == null) && (lastNode == null);
    }
    //O(1) time complexity
    public void enqueue(T entry){
        Node tempNode = new Node(entry,null);
        if (isEmpty())
            firstNode = tempNode;
        else
            lastNode.setNext(tempNode);
        lastNode = tempNode;

    }
    //O(1) time complexity
    public T dequeue(){
        T front = getFront();
        
        assert firstNode != null;
        firstNode.setData(null);
        firstNode = firstNode.getNext();
        if(firstNode == null)
            lastNode = null;
        return front;
    }
    public T getFront(){
        if(isEmpty())
            throw new EmptyStackException();
        else
            return firstNode.getData();
    }
    public void clear(){
        firstNode = null;
        lastNode = null;
    }


    public void printQueue(){
        if(isEmpty())
            System.out.println("The Queue is Emtpy");
        else if (firstNode == null && lastNode != null)
            System.out.println(lastNode.getData());
        else{
            Node tempNode = firstNode;
            while (tempNode != null)
            {
                System.out.println(tempNode.getData());
                tempNode = tempNode.getNext();
            }
        }
    }

     //Node class

    private class Node{
        private T data;
        private Node next;


        private Node(T data){
            this.data = data;
            this.next = null;
        }
        private Node(T data, Node next)
        {
            this.data = data;
            this.next = next;
        }
        private T getData(){
            return data;
        }
        private Node getNext(){
            return next;
        }
        private void setData(T newData){
            data = newData;
        }
        private void setNext(Node nextNode){
            next = nextNode;
        }

    }
}