package io;

import java.util.Scanner;

/**
 * Refines the HelloWorld example to skip lines consisting only of whitespace
 * and to trim any leading and trailing whitespace. The significant point is not
 * to do anything in the main method except getting the input.
 *
 * @author Michael Albert
 */
public class HelloRefined {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while (in.hasNextLine()) {
      sayHello(in.nextLine());
    }
  }

  private static void sayHello(String nextLine) {
    String name = nextLine.trim();
    if (name.isEmpty()) return;
    System.out.println("Hello " + name);
  }

}
