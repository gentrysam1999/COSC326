package sequencium;

/**
 * An interface for a Sequencium player to be implemented in order to play the
 * game.
 *
 * @author Michael Albert
 */
public interface Player {

  /**
   * Make a move as requested given a board. Your numbers are positive integers
   * on the board, your opponent's numbers are negative integers and vacant
   * places are 0's.
   * <p>
   * If the move returned is invalid, you will be deemed to have passed (i.e.,
   * done nothing).
   * <p>
   * In practice, the board you receive will only be a copy of the actual board,
   * so changing it directly is safe but has no effect on the game.
   *
   * @param board the current game goard
   * @return your move as a three element array {r, c, v} intended to indicate
   * that you wish to make board[r][c] = v.
   */
  public int[] makeMove(int[][] board);

  /**
   * What is your name?
   *
   * @return Your name.
   */
  public String getName();

}
