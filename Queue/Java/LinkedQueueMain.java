import java.util.*;


public class LinkedQueueMain{
    public static void main (String[] args){
        Random rand = new Random();
        LinkedQueue<Integer> queue = new LinkedQueue<Integer>();
        for (int i = 0; i < 10;i++)
            queue.enqueue(rand.nextInt(50)+1);
        queue.printQueue();
        System.out.println("\nThe first dequeue data value is: "+queue.dequeue()+"\n");
        queue.printQueue();
    }
}