package sequencium;

import java.util.ArrayList;

/**
 * Utility methods available to all Sequencium players
 *
 * @author Michael Albert
 */
public class Utilities {

  /**
   * Checks if a move is valid for the board.
   * @param move Proposed move (supposed in {r,c,v} format)
   * @param board The board
   * @return true if the move is valid, false otherwise.
   */
  public static boolean checkMove(int[] move, int[][] board) {
    if (move.length != 3) {
      return false;
    }
    int r = move[0];
    int c = move[1];
    int v = move[2];

    // Is the row valid?
    if (r < 0 || r >= board.length) {
      return false;
    }

    // Is the column valid?
    // Note board[0] to allow for non-square boards.
    if (c < 0 || c >= board[0].length) {
      return false;
    }

    // Is the cell empty?
    if (board[r][c] != 0) {
      return false;
    }

    // Is the move positive?
    if (v <= 0) {
      return false;
    }

    // Now check that there is a neighbouring cell of positive value at
    // least v-1.      
    for (int[] n : neighbours(r, c, board.length, board[0].length)) {
      int rn = n[0];
      int cn = n[1];
      if (board[rn][cn] > 0 && board[rn][cn] >= v - 1) {
        return true;
      }
    }

    return false;
  }

  /**
   * Returns the neighbours of a given cell in a given board size.
   * 
   * @param r the row coordinate of the cell
   * @param c the column coordinate of the cell
   * @param rows the number of rows in the board
   * @param cols the number of columns in the board
   * @return An arraylist of row-column coordinates of this cell's neighbours.
   */
  public static ArrayList<int[]> neighbours(int r, int c,
          int rows, int cols) {

    ArrayList<int[]> result = new ArrayList<>();

    for (int dr = -1; dr <= 1; dr++) {
      if (r + dr < 0 || r + dr >= rows) {
        continue;
      }
      for (int dc = -1; dc <= 1; dc++) {
        if (c + dc < 0 || c + dc >= cols) {
          continue;
        }
        if (dr == 0 && dc == 0) {
          continue;
        }
        result.add(new int[]{r + dr, c + dc});
      }
    }
    return result;
  }

  /**
   * Determine if a move exists on the board
   * 
   * @param board the board
   * @return true if there is a move, false if there isn't.
   */
  public static boolean hasMove(int[][] board) {
    int rows = board.length;
    int cols = board[0].length;
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if (board[r][c] > 0) {
          for (int[] n : neighbours(r, c, rows, cols)) {
            if (board[n[0]][n[1]] == 0) {
              return true;
            }
          }
        }
      }
    }
    return false;
  }
}
