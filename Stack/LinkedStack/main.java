public class main{
    public static void main(String[] args){
        LinkedStack<Integer> stack = new LinkedStack<Integer>();
        System.out.println("Entered into the stack is 1,2,3,4.");
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.printStack();
        System.out.println("The top data on the stack is: ");
        System.out.print(stack.peek()+ "\n");
        stack.pop();
        stack.pop();
        System.out.println("After popping from the stack twice.");
        stack.printStack();
        stack.clear();
        stack.push(5);
        stack.push(6);
        System.out.println("Clearing the stack then adding 5 and 6");
        stack.printStack();
    }
}