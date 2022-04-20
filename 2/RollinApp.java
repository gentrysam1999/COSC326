import rollin.*;
import java.util.*;


public class RollinApp extends Rollin{

    public RollinApp(){
        super();
    }
    public static void main(String args[]) {
        Random rand = new Random();
        int upperbound = 5;
        RollinApp accessor = new RollinApp();

        int roll_count = 0;
        boolean done = false;
        
        // accessor.handleRoll(4);
        System.out.println(accessor.getDice());
    

        while(!done){
            
            if(roll_count == 0){
                // set up dice with initial rolls
                
                roll_count+=1;
            }
            int roll = rand.nextInt(upperbound);
            System.out.println(roll);
            accessor.handleRoll(roll);
            // if we want to stop rolling set done to true
            // done = true;
        }
     }

     /**
     * @param roll The value of the die roll
     * @return The index of the die whose value will be replaced by the roll, or
     * any int outside of 0 to 5 if no replacement is made.
     */
    public int handleRoll(int roll) {
        // just filler code atm, needs to recieve the roll of a dice and return which dice to change
        RollinApp accessor = new RollinApp();
        return -1;
        

    }

    
    

    
    

}



