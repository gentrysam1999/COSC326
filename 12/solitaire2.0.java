import java.util.*;

/*
 *Class for 1d solitaire, Etude 12.
 *
 *@author Joseph Sharratt, ID 2628691.
 *@author Sam Gentry.
 */

public class solitaire{

   static ArrayList<int[]> repeats = new ArrayList<int[]>();
   static int totalNumOfComplete;
   
   public static void main(String[] args){
      int finalNumPegs = Integer.parseInt(args[0]);
      int numPegs = 1;
      int[] pegArray = new int[4*finalNumPegs + 1];
      pegArray[(pegArray.length)/2] = 1;
      pegJumpAndCheck(finalNumPegs, numPegs, pegArray);
      System.out.println("The number of solvable positions for " + finalNumPegs + " is " + totalNumOfComplete);
   }
   
   /**
    *Recursively checks if a peg can jump on either side of itself and if 
    *current peg array is complete.
    *
    *@param numPegs the number of pegs in the current array.
    *@param pegArray the current array.
    */
   public static void pegJumpAndCheck(int finalNumPegs, int numPegs, int[] pegArray){
      if(isRepeat(trimArray(pegArray))){
         return;
      }else {
         repeats.add(trimArray(pegArray));
         repeats.add(trimArray(reverse(pegArray)));
      }
      
      if(numPegs == finalNumPegs){
         totalNumOfComplete++;
         System.out.println(Arrays.toString(trimArray(pegArray)));
         return;
      }
      
      for(int i = 2; i < pegArray.length-2; i++){
         if(pegArray[i] == 1){
            
            if(pegArray[i-1] == 0 && pegArray[i-2] == 0){
               int[] PegArrayOne = Arrays.copyOf(pegArray, pegArray.length);
               pegJumpAndCheck(finalNumPegs, (numPegs + 1), pegJumpLeft(i, PegArrayOne));
            }
            
            if(pegArray[i+1] == 0 && pegArray[i+2] == 0){
               int[] PegArrayTwo = Arrays.copyOf(pegArray, pegArray.length);
               pegJumpAndCheck(finalNumPegs, (numPegs + 1), pegJumpRight(i, PegArrayTwo));
            }
         }
      }
      return;
   }
   
   /**
    *Checks if array is a repeat.
    *
    *@param x array to be checked.
    *@return true if array is repeated.
    */
   public static boolean isRepeat(int[] x){
      for(int i = 0; i < repeats.size(); i++){
         if(Arrays.equals(x, repeats.get(i))){
            return true;
         }
      }
      return false;
   }
   
   /**
    *Reverses array to be added to repeat arraylist.
    *
    *@param pegArray array to be reversed.
    *@return reversed array.
    */
   public static int[] reverse(int[] pegArray){
      int[] x = new int[pegArray.length];
      int n = pegArray.length-1;
      for(int i = 0; i < pegArray.length; i++){
         x[i] = pegArray[n];
         n--;
      }
      return x;
   }

   /**
    *removes all excess zeros from edges of array.
    *
    *@param pegArray array to be trimmed.
    *@return trimmed array.
    */
   public static int[] trimArray(int[] pegArray){
      int start, end;
      int i = 0;
      int[] x;
      while(true){
         if(pegArray[i] != 0){
            start = i;
            break;
         }else {
            i++;
         }
      }
      i = pegArray.length-1;
      while(true){
         if(pegArray[i] != 0){
            end = i;
            break;
         }else {
            i--;
         }
      }
      x = new int[end - start + 1];
      for(i = start; i <= end; i++){
         x[i-start] = pegArray[i];
      }
      return x;
      
   }
   
   /**
    *Jumps a peg to the left.
    *
    *@param i index of peg to be jumped.
    *@param x array that peg lives in.
    *@return updated array.
    */
   public static int[] pegJumpLeft(int i, int[] x){
      x[i] = 0;
      x[i-1] = 1;
      x[i-2] = 1;
      return x;
   }
   
   /**
    *Jumps a peg to the right.
    *
    *@param i index of peg to be jumped.
    *@param x array that peg lives in.
    *@return updated array.
    */
   public static int[] pegJumpRight(int i, int[] x){
      x[i] = 0;
      x[i+1] = 1;
      x[i+2] = 1;
      return x;
   }
}