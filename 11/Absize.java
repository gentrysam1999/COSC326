import java.util.Scanner;
import java.util.*; 

/**
 * Finds valid words from a file of text to sort and print
 * 
 * @ Sam Gentry
*/
public class Absize{
    public static void main(String[] args){
        HashSet<String> word_set = new HashSet<String>();
        Scanner in = new Scanner(System.in);
        while (in.hasNextLine()) {
            String str = in.nextLine();
            String[] x = str.split("[\\s+]");
            for(String word: x){
                if(word.matches("\"?[A-Z]?[a-z]*\'?[a-z]*[,.;:?!\"]?") && word != ""){
                    char last_char = word.charAt(word.length() - 1);
                    if(!(Character.isLetter(last_char) | last_char=='\'')){
                        word = word.substring(0, word.length() - 1);
                    }
                    if(word != ""){
                        char first_char = word.charAt(0);
                        if(!Character.isLetter(first_char)){
                            word = word.substring(1, word.length());
                        }
                    }
                    if(word != ""){
                        word_set.add(word.toLowerCase());
                    }
                }

            }  
        }
        String[] word_arr = word_set.toArray(String[]::new);
        Arrays.sort(word_arr);
        for(String word: word_arr){
            System.out.println(word);
        }
    }
}