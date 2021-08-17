public class ArrayStackMain{
    public static void main(String[] args){
        ArrayStack<Integer> stack = new ArrayStack<Integer>(10);
        System.out.println("The stack will be inputed from 1 to 15. It should also double in size after 10");
        for (int i = 1; i < 16; i++)
            stack.push(i);
        
        System.out.println("Top of the stack is: "+stack.peek());


        //stack prints in the FIFO order.
        stack.printStack();
        for(int i = 0; i < 15; i++)
            System.out.println(stack.pop());

        System.out.println("Is the stack empty?: "+stack.isEmpty());
    }
}