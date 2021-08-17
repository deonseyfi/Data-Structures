import java.lang.*;
import java.util.*;


public class ArrayStack<T>
{
    //This array stack implementation does not use the top index of the array as the peak of the stack
    //As the array gets filled, the top index will be incremented by 1 therefore that index is the top of the stack
    //Once popped the topIndex of the array will be given a null value and the topIndex will be reduced by one.


    private T[] stack;
    private int topIndex;
    private static boolean initialized = false;
    private static final int defaultCapacity = 50;
    private static final int maxCapacity = 10000;

    public ArrayStack(){
        this(defaultCapacity);
    }

    public ArrayStack(int arrSize){
        checkCapacity(arrSize);


        @SuppressWarnings("unchecked")
        T[] tempStack = (T[])new Object[arrSize];
        this.stack = tempStack;
        this.topIndex = -1;
        this.initialized = true;
    }
    private void checkInitialization(){
        if (!initialized)
        throw new SecurityException("ArrayBag object is not initialized properly.");
    }
    private void checkCapacity(int capacity){
        if(capacity > maxCapacity)
        throw new IllegalStateException("The attempt to make a larger array exceed the max size of: "+maxCapacity);
    }
    //In the event that the stack becomes filled and new entries are being added, the array of the stack would double in size, 
    //while maintaining maximum size.
    private void ensureArraySize(){
        if (topIndex == stack.length-1){
            int newLength = stack.length*2;
            checkCapacity(newLength);
            stack = Arrays.copyOf(stack,newLength);
            System.out.println("The stack has doubled in size.");
        }
    }
    //O(1) operation time
    public void push(T input)
    {
        checkInitialization();
        ensureArraySize();
        stack[topIndex+1] = input;
        topIndex++;
    }
    //O(1) operation time
    public T peek(){
        checkInitialization();
        if (isEmpty())
            throw new EmptyStackException();
        else
            return stack[topIndex];
    }
    //O(1) operation time
    public T pop(){
        checkInitialization();
        if (isEmpty())
            throw new EmptyStackException();
        else{
            T popValue = stack[topIndex];
            stack[topIndex] = null;
            topIndex--;
            return popValue;
        }
    }
    public boolean isEmpty(){
        return topIndex < 0;
    }
    //Print method runs in O(n)
    public void printStack(){
  
        for (int i = topIndex; i>-1; i--)
        {
            System.out.println(stack[i]);
        }
    }

}