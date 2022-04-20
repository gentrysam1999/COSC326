package io;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Process a file consisting of poems or stanzas of poems separated by blank
 * lines, preceding each by the number of the poem followed by a full stop, 
 * then the number of the line, padding with white space to width 10, then the 
 * line itself. Place one blank line between poems. Number from 1.
 * 
 * @author Michael Albert
 */
public class Poems {

  static int poemNumber = 0;
  static final String TEN_SPACES = "          ";
  
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    ArrayList<String> poem = new ArrayList<>();
    while (in.hasNextLine()) {
      String line = in.nextLine();
      if (line.trim().isEmpty() && poem.size() > 0) { // Allows for multiple blank lines between poems
        process(poem);
        poem.clear();
        System.out.println(); // Here rather than in process so no blank line after last poem
      } else {
        poem.add(line);
      }
    }
    if (poem.size() > 0) process(poem); // Processes final poem if not followed by blank line
  }

  private static void process(ArrayList<String> poem) {
    poemNumber++;
    int lineNumber = 0;
    for(String line: poem) {
      lineNumber++;
      String prefix = (poemNumber + "." + lineNumber + TEN_SPACES).substring(0,10);
      System.out.println(prefix + line);
    }
            
            
  }
  
}
