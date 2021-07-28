import java.lang.*;
import java.util.*;


public class LinkedStack<T>
{
    private Node topNode;

    public LinkedStack(){
        topNode = null;
    }
    public LinkedStack(Node stackInput){
        topNode = stackInput;
    }
    //Method runs in O(1)
    public void push(T newData){
        Node newNode = new Node(newData, topNode);
        topNode = newNode;

    }
    //Method runs in O(1)
    public T pop(){
        if (topNode != null){
            T tempData = topNode.getData();
            topNode = topNode.getNext();
            return tempData;
        }
        else
            throw new EmptyStackException();
    }
    //Method runs in O(1)
    public T peek(){
        if (isEmpty())
            throw new EmptyStackException();
        else
            return topNode.getData();
    }
    //Method runs in O(1)
    public boolean isEmpty(){
        return topNode == null;
    }
    //Method runs in O(1)
    public void clear(){
        topNode = null; 
    }
    //Print method runs in O(n)
    public void printStack(){
        Node tempNode = topNode;
        while (tempNode != null)
        {
            System.out.println(tempNode.getData());
            tempNode = tempNode.getNext();
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
