import java.util.*;

/*
 *Class for Carpets, Etude 6.
 *
 *@author Joseph Sharratt, ID 2628691.
 *@author David Black
 *@author Irsyaad Rijwan
 *@author Sam Gentry
 */

public class makeCarpet {

   private static ArrayList<String> carpetStrips = new ArrayList<String>();
   private static ArrayList<Integer> usedStrips = new ArrayList<Integer>();
   private static int[] usedStripsForBalanced;
   private static String[] finalCarpet;
   private static String[] finalCarpetTest;
   private static int maxScore;
   private static int carpetSize;
   private static String flag = "";
    
   public static void main(String[] args){
      Scanner scan = new Scanner(System.in);
      while(scan.hasNext()){
         carpetStrips.add(scan.next());
      }
      try{
         carpetSize = Integer.parseInt(args[0]);
         finalCarpet = new String[carpetSize];
      } catch(Exception e){
         System.out.println("Invalid carpet size.");
      }
      try{
         flag = args[1];
      } catch(Exception e){
         System.out.println("Invalid Flag.");
      }
      if(carpetSize > 0 && carpetSize <= carpetStrips.size()){
         if(flag.equals("-n")){
            if(noMatchesCase(0)){
               printCompleteCarpet();
            } else{
               System.out.println("not possible");
            }
         } else if(flag.equals("-m")){
            finalCarpetTest = new String[carpetSize];
            greedyApproach();
            maxMatchesCase(0, 0);
            printCompleteCarpet();
            System.out.println(maxScore);
         } else if(flag.equals("-b")){
            usedStripsForBalanced = new int[carpetSize];
            int score = bestBalanceCase(10000);
            printCompleteCarpet();
            System.out.println(score);
         } else{
            System.out.println("Invalid Flag.");
         }
      }else{
         System.out.println("Invalid carpet size.");    
      }
    }
    
    //Max matches method.
    public static void maxMatchesCase(int stripIndex, int score){
      if(score > maxScore && stripIndex == finalCarpet.length){
         maxScore = score;
         finalCarpet = Arrays.copyOf(finalCarpetTest, finalCarpetTest.length);
         return;
      }
      if((finalCarpet.length-stripIndex)*4 + score <= maxScore){
         return;
      }
      for(int i = 0; i < carpetStrips.size(); i++){
         if(!usedStrips.contains(i)){
            finalCarpetTest[stripIndex] = carpetStrips.get(i);
            int scoreUpdate = score + updateMaxScoreForTest(stripIndex, finalCarpetTest[stripIndex]);
            usedStrips.add(i);
            maxMatchesCase(stripIndex+1, scoreUpdate);
            finalCarpetTest[stripIndex] = reverseString(carpetStrips.get(i));
            scoreUpdate = score + updateMaxScoreForTest(stripIndex, reverseString(finalCarpetTest[stripIndex]));
            maxMatchesCase(stripIndex+1, scoreUpdate);
            Integer x = i;
            usedStrips.remove(x);
         }
      }
      return;
    }
    
    
    //returns a score based on matches to above strip.
    public static int updateMaxScoreForTest(int stripIndex, String str){
      if(stripIndex == 0){
         return 0;
      } else{
         int score = 0;
         for(int i = 0; i < str.length(); i++){
            if(finalCarpetTest[stripIndex-1].charAt(i) == str.charAt(i)){
               score++;;
            }
         }
         return score;
      }
    }
    
    //initialise finalCarpet array
    public static void greedyApproach(){
      Collections.sort(carpetStrips);
      for(int i = 0; i < finalCarpet.length; i++){
         finalCarpet[i] = carpetStrips.get(i);
         maxScore += updateMaxScore(i, finalCarpet[i]);
      }
    }
    
    //Best balance method.
    public static int bestBalanceCase(int maxChecks){
      Random rand = new Random();
      int carpetStrip, randPos;
      int count = 0;
      int score = 0;
      for(int i = 0; i < finalCarpet.length; i++){
         carpetStrip = rand.nextInt(carpetStrips.size());
         while(doesContainIndex(carpetStrip)){
            carpetStrip = rand.nextInt(carpetStrips.size());
         }
         finalCarpet[i] = carpetStrips.get(carpetStrip);
         score += updateScore(i, carpetStrips.get(carpetStrip));
         usedStripsForBalanced[i] = carpetStrip;
      }
      while(count != maxChecks && score != 0){
         carpetStrip = rand.nextInt(carpetStrips.size());
         
         while(doesContainIndex(carpetStrip)){
            carpetStrip = rand.nextInt(carpetStrips.size());
         }
         randPos = rand.nextInt(finalCarpet.length);
         int prevUpdate = updateScore(randPos, finalCarpet[randPos]);
         int tempScore = score + updateScore(randPos, carpetStrips.get(carpetStrip)) - prevUpdate;
         if(Math.abs(tempScore) < Math.abs(score)){
            finalCarpet[randPos] = carpetStrips.get(carpetStrip);
            usedStripsForBalanced[randPos] = carpetStrip;
            score = tempScore;
         }
         count++;
      }
      
      return score;
    }
    
    //No matches method.
    public static boolean noMatchesCase(int numOfStrips){
      if(numOfStrips == carpetSize){
         return true;
      }
      ArrayList<String> repeatStrips = new ArrayList<String>();
      for(int i = 0; i < carpetStrips.size(); i++){
         if(!usedStrips.contains(i)){
            if(!repeatStrips.contains(carpetStrips.get(i))){
               if(checkNoMatch(numOfStrips, carpetStrips.get(i))){
                  finalCarpet[numOfStrips] = carpetStrips.get(i);
                  usedStrips.add(i);
                  if(noMatchesCase(numOfStrips+1)){
                     return true;
                  }
                  Integer x = i;
                  usedStrips.remove(x);
                  repeatStrips.add(carpetStrips.get(i));
                  repeatStrips.add(reverseString(carpetStrips.get(i)));
               } else if(checkNoMatch(numOfStrips, reverseString(carpetStrips.get(i)))){
                  finalCarpet[numOfStrips] = reverseString(carpetStrips.get(i));
                  usedStrips.add(i);
                  if(noMatchesCase(numOfStrips+1)){
                     return true;
                  }
                  Integer x = i;
                  usedStrips.remove(x);
                  repeatStrips.add(carpetStrips.get(i));
                  repeatStrips.add(reverseString(carpetStrips.get(i)));
               } else{
                  repeatStrips.add(carpetStrips.get(i));
                  repeatStrips.add(reverseString(carpetStrips.get(i)));
               }
            }
         }
      }
      return false;
    }
    
    //returns a score based on matches to above strip.
    public static int updateMaxScore(int stripIndex, String str){
      if(stripIndex == 0){
         return 0;
      } else{
         int score = 0;
         for(int i = 0; i < str.length(); i++){
            if(finalCarpet[stripIndex-1].charAt(i) == str.charAt(i)){
               score++;;
            }
         }
         return score;
      }
    }
    
    //returns an updated score based on the index whose strip is being replaced.
    public static int updateScore(int stripIndex, String str){
      int score = 0;
      if(stripIndex == 0){
         if(finalCarpet[stripIndex+1] != null){
            for(int i = 0; i < str.length(); i++){
               if(finalCarpet[stripIndex+1].charAt(i) == str.charAt(i)){
                  score++;
               } else{
                  score--;
               }
            }
         }
      } else if(stripIndex == finalCarpet.length-1){
         if(finalCarpet[stripIndex-1] != null){
            for(int i = 0; i < str.length(); i++){
               if(finalCarpet[stripIndex-1].charAt(i) == str.charAt(i)){
                  score++;
               } else{
                  score--;
               }
            }
         }
      } else{
         if(finalCarpet[stripIndex-1] != null){
            for(int i = 0; i < str.length(); i++){
               if(finalCarpet[stripIndex-1].charAt(i) == str.charAt(i)){
                  score++;
               } else{
                  score--;
               }
            }
         }
         if(finalCarpet[stripIndex+1] != null){
            for(int i = 0; i < str.length(); i++){
               if(finalCarpet[stripIndex+1].charAt(i) == str.charAt(i)){
                  score++;
               } else{
                  score--;
               }
            }
         }
      }
      return score;
    }
    
    //returns true if used strips contiansthe strip we are looking for.
    public static boolean doesContainIndex(int strip){
      for(int i = 0; i < usedStripsForBalanced.length; i ++){
         if(usedStripsForBalanced[i] == strip){
            return true;
         }
      }
      return false;
    }
    
    //returns true if there are no char matches between two strings.
    public static boolean checkNoMatch(int stripIndex, String str){
      if(stripIndex == 0){
         return true;
      } else{
         for(int i = 0; i < str.length(); i++){
            if(finalCarpet[stripIndex-1].charAt(i) == str.charAt(i)){
               return false;
            }
         }
         return true;
      }
    }

    
    //reverses a string.
    public static String reverseString(String str){
      String reverseStr = "";
      char ch;
      for (int i = 0; i < str.length(); i++){
        ch = str.charAt(i);
        reverseStr = ch+reverseStr;
      }
      return reverseStr;
    }
    
    //Prints the final complete carpet if found.
    public static void printCompleteCarpet(){
      for(int i = 0; i < finalCarpet.length; i++){
         System.out.println(finalCarpet[i]);
      }
    }
}
