package sequencium;

import java.util.Arrays;

/**
 * Representation of a sequencium game
 *
 * @author Michael Albert
 */
public class Game {

  private final Player RED; // Positive from the standpoint of game
  private final Player BLUE; // Negative from the standpoint of game
  private int ROWS = 8;
  private int COLS = 8;
  private int[][] board;
  private boolean VERBOSE = false;
  private final StringBuilder LOG = new StringBuilder();
  
  /**
   * Initialise a standard 6 by 6 game
   * @param RED the red player
   * @param BLUE the blue player
   */
  public Game(Player RED, Player BLUE) {
    this(RED, BLUE, 6, 6);   
  }
  
  /**
   * Initialise a square game.
   * @param RED the red player
   * @param BLUE the blue player
   * @param dim the side-length of the square
   */
  public Game(Player RED, Player BLUE, int dim) {
    this(RED, BLUE, dim, dim);
  }
  
  /**
   * Initialise a rectangular game.
   * 
   * @param RED the red player
   * @param BLUE the blue player
   * @param ROWS the number of rows
   * @param COLS the number of columns
   */
  public Game(Player RED, Player BLUE, int ROWS, int COLS) {
    this.RED = RED;
    this.BLUE = BLUE;    
    this.ROWS = ROWS;
    this.COLS = COLS;
    this.board = new int[ROWS][COLS];
    board[0][0] = 1;
    board[ROWS-1][COLS-1] = -1;
  }
  
  /**
   * Turn full game reporting on.
   */
  public void makeVerbose() {
    VERBOSE = true;
  }
  
  /**
   * Turn full game reporting off.
   */
  public void makeQuiet() {
    VERBOSE = false;
  }
  
  /**
   * Run the game.
   */
  public void run() {
    int[][] bc = boardCopy();
    int[] rm = new int[0];
    int[] bm = new int[0];
    rm = null; bm = null;
    if (Utilities.hasMove(bc)) {
      rm = RED.makeMove(bc);
      if (Utilities.checkMove(rm, board)) {
        board[rm[0]][rm[1]] = rm[2];
      } else {
        rm = null;
      }    
    }
    bc = negativeBoardCopy();
    if (Utilities.hasMove(bc)) {
      bm = BLUE.makeMove(bc);
      if (Utilities.checkMove(bm, negativeBoardCopy())) {
        board[bm[0]][bm[1]] = -bm[2];
      } else {
        bm = null;
      }
    }    
    if (VERBOSE) {
      logMoves(rm, bm);
    }    
    if (rm == null && bm == null) {
      reportOutcome(); return;
    }    
    run();
  }
  
  /**
   * Create a copy of the board
   * @return a copy of the current board
   */
  public int[][] boardCopy() {
    int[][] result = new int[ROWS][];
    for(int r = 0; r < ROWS; r++) {
      result[r] = Arrays.copyOf(board[r], COLS);
    }
    return result;
  }
  
  /**
   * Create a copy of the board with the signs changed.
   * @return A sign-changed copy of the board.
   * 
   */
  public int[][] negativeBoardCopy() {
    int[][] result = boardCopy();
    for(int r = 0; r < ROWS; r++) {
      for(int c = 0; c < COLS; c++) {
        result[r][c] *= -1;
      }
    }
    return result;
  }
  
  /**
   * Add the game outcome to the log.
   */
  public void reportOutcome() {
    int redScore = 0;
    int blueScore = 0;
    for(int r = 0; r < ROWS; r++) {
      for(int c = 0; c < COLS; c++) {
        redScore = (redScore >= board[r][c]) ? redScore : board[r][c];
        blueScore = (blueScore <= board[r][c]) ? blueScore : board[r][c];
      }
    }
    System.out.println(RED.getName() + " " + redScore + " " + BLUE.getName() + " " + (-blueScore));
    LOG.append(RED.getName() + " " + redScore + " " + BLUE.getName() + " " + (-blueScore));
  }
  
  /**
   * Log a pair of moves.
   * @param rm Red's move
   * @param bm Blue's move
   */
  public void logMoves(int[] rm, int[] bm) {
    if (rm != null) {
      LOG.append("R " + rm[0] + " " + rm[1] + " -> " + rm[2] + "\n");
    } else {
      LOG.append("R pass\n");
    }
    if (bm != null) {
      LOG.append("B " + bm[0] + " " + bm[1] + " -> " + (-bm[2]) + "\n");
    } else {
      LOG.append("B pass\n");
    }
    LOG.append(displayBoard());
    LOG.append("\n");
  }
  
  /**
   * A character sequence representing the board.
   * @return A character sequence representing the board.
   */
  public CharSequence displayBoard() {
    StringBuilder result = new StringBuilder();
    for(int r = 0; r < ROWS; r++) {
      for(int c = 0; c < COLS; c++) {
        result.append(String.format("%4d", board[r][c]));
      }
      result.append("\n");
    }    
    return result;
  }
  
  /**
   * The log of a game
   * @return a game log as a string.
   */
  public String getLog() {
    return LOG.toString();
  }

  
}