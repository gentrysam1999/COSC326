import java.util.*;

/*
 *Class for 1d solitaire, Etude 12.
 *
 *@author Joseph Sharratt, ID 2628691.
 *@author Sam Gentry, ID 4919289.
 */

public class joinedUpWriting{

   static ArrayList<String> dict = new ArrayList<String>();
   static HashMap<String, String> wordLinks = new HashMap<String, String>();
   static String startWord;
   static String endWord;

   public static void main(String[] args){
      try{
         startWord = args[0];
         endWord = args[1];
      } catch(ArrayIndexOutOfBoundsException e){
         System.out.println("Invalid arguments");
      }
      Scanner scan = new Scanner(System.in);
      String line;
      while(scan.hasNextLine()){
         line = scan.nextLine();
         Scanner scanLine = new Scanner(line);
         while(scanLine.hasNext()){
            dict.add(scanLine.next());
         }
      }
      System.out.println(startWord + " " + endWord);
      if((line = singleLink(startWord)) != null){
         printList(line);
      } else{
         System.out.println("0");
      }
      wordLinks.clear();
      if((line = doubleLink(startWord)) != null){
         printList(line);
      } else{
         System.out.println("0");
      }
   }
   
   /**
    *Prints the completed link using hashmap.
    *
    *@param word final word in link besides endWord.
    */
   public static void printList(String word){
      ArrayList<String> wordList = new ArrayList<String>();
      int x = 0;
      while(word != startWord){
         wordList.add(word);
         word = wordLinks.get(word);
         x++;
      }
      System.out.print(x+2 + " " + startWord);
      for(x = wordList.size()-1; x >= 0; x--){
         System.out.print(" " + wordList.get(x));
      }
      System.out.print(" " + endWord);
      System.out.println();
   }
   
   /**
    *Computes single link hashmap.
    *
    *@param word starting word in link.
    *@return final word in link besides endWord.
    */
   public static String singleLink(String word){
      Queue<String> wordsToCheck = new LinkedList<String>();
      wordsToCheck.add(word);
      boolean linkFound = false;
      while((word = wordsToCheck.poll()) != null && !linkFound){
         for(int i = 0; i < dict.size(); i++){
            String subString = word;
            while(true){
               if(dict.get(i).startsWith(subString)){
                  if(subString.length() >= Double.valueOf(word.length())/2.0 || subString.length() >= Double.valueOf(dict.get(i).length())/2.0){
                     if(dict.get(i).equals(endWord)){
                        linkFound = true;
                        return word;
                     } else if(wordLinks.get(dict.get(i)) == null){
                        wordsToCheck.add(dict.get(i));
                        wordLinks.put(dict.get(i), word);
                        break;
                     } else{
                        break;
                     }
                  }
                  break;
               } else{
                  try{
                     subString = subString.substring(1, subString.length());
                  }catch(StringIndexOutOfBoundsException e){
                     break;
                  }
               }
            }
         }
      }
      return null;
   }
   
   /**
    *Computes double link hashmap.
    *
    *@param word starting word in link.
    *@return final word in link besides endWord.
    */
   public static String doubleLink(String word){
      Queue<String> wordsToCheck = new LinkedList<String>();
      wordsToCheck.add(word);
      boolean linkFound = false;
      while((word = wordsToCheck.poll()) != null && !linkFound){
         for(int i = 0; i < dict.size(); i++){
            String subString = word;
            while(true){
               if(dict.get(i).startsWith(subString)){
                  if(subString.length() >= Double.valueOf(word.length())/2.0 && subString.length() >= Double.valueOf(dict.get(i).length())/2.0){
                     if(dict.get(i).equals(endWord)){
                        linkFound = true;
                        return word;
                     } else if(wordLinks.get(dict.get(i)) == null){
                        wordsToCheck.add(dict.get(i));
                        wordLinks.put(dict.get(i), word);
                        break;
                     } else{
                        break;
                     }
                  }
                  break;
               } else{
                  try{
                     subString = subString.substring(1, subString.length());
                  }catch(StringIndexOutOfBoundsException e){
                     break;
                  }
               }
            }
         }
      }
      return null;
   }
}