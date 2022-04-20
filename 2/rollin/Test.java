package rollin;

import java.util.*;

public class Test{

  public static final Random R = new Random();

  public static void main(String[] args) {
    int[] dice = new int[6];
    for(int i = 0; i < dice.length; i++) {
      dice[i] = R.nextInt(6) + 1;
    }
    Rollin roller = new RandomRoller(dice);
    System.out.println(Arrays.toString(dice));
    while (!roller.isComplete()) {
      int roll = R.nextInt(6) + 1;
      int i = roller.handleRoll(roll);
      System.out.println("Rolled " + roll + " used at " + i);
      if (0 <= i && i < 6) {
        dice[i] = roll;
      }
      Arrays.sort(dice);
      System.out.println(Arrays.toString(dice));
      roller.setDice(dice);
    }
  }
}