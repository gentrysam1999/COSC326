package io;


import java.util.Scanner;

/**
 * Illustrates basic I/O using stdin and stdout. Just echo "Hello " (name) for
 * each name in a file.
 * 
 * @author MichaelAlbert
 */
public class HelloBasic {

   public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while (in.hasNextLine()) {
      System.out.println("Hello " + in.nextLine());
    }
  }
  
}
