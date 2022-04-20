package sequencium;

import sequencium.*;
import java.util.*;

/**
 * A purely random Sequencium player (randomly chooses a place to move to, puts
 * one more than one of its neighbours there.)
 *
 * @author Michael Albert
 */
public class RandomPlayer implements Player {

  static final Random R = new Random();
  String name = "";

  /**
   * Initialise with a random name (four letter string).
   */
  public RandomPlayer() {
    for (int i = 0; i < 4; i++) {
      name += (char) ('a' + R.nextInt(26));
    }
  }

  /**
   * Choose a random move
   *
   * @param board the board
   * @return a random move
   */
  public int[] makeMove(int[][] board) {
    ArrayList<int[]> moves = new ArrayList<>();
    int rows = board.length;
    int cols = board[0].length;
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if (board[r][c] > 0) {
          for (int[] n : Utilities.neighbours(r, c, rows, cols)) {
            if (board[n[0]][n[1]] == 0) {
              moves.add(new int[]{n[0], n[1], board[r][c] + 1});
            }
          }
        }
      }
    }
    Collections.shuffle(moves);
    if (moves.size() > 0) {
      return moves.get(0);
    } else {
      return new int[0];
    }

  }

  /**
   * What is your name?
   *
   * @return Your name.
   */
  public String getName() {
    return name;
  }
;

}
