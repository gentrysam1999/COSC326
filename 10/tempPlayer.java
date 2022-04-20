package sequencium;

import sequencium.*;
import java.util.*;


public class tempPlayer implements Player {
   String name = "tempPlayer";
  
   
   public int[] makeMove(int[][] board) {
      ArrayList<int[]> moves = new ArrayList<>();
      ArrayList<int[]> enemyMoves = new ArrayList<>();
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
          } else if(board[r][c] < 0){
            for (int[] en : Utilities.neighbours(r, c, rows, cols)) {
              if (board[en[0]][en[1]] == 0) {
                enemyMoves.add(new int[]{en[0], en[1], -(board[r][c] - 1)});
              }
            }
          }
        }
      }
      
      Collections.sort(moves ,new Comparator<int[]>() {
            public int compare(int[] ints, int[] otherInts) {
                return (-ints[2] + otherInts[2]);
            }
      });
      
      Collections.sort(enemyMoves ,new Comparator<int[]>() {
            public int compare(int[] ints, int[] otherInts) {
                return (-ints[2] + otherInts[2]);
            }
      });
      if(enemyMoves.size() > 0 && moves.size() > 0){
         int highestValue = enemyMoves.get(0)[2];
         for(int i = moves.size()-1; i >= 0; i--){
            int x = enemyMoves.get(0)[2];
            int counter = 0;
            while(x == highestValue && counter < enemyMoves.size()){
               if(enemyMoves.get(counter)[2] < highestValue){
                  break;
               }
               if(moves.get(i)[0] == enemyMoves.get(counter)[0] && moves.get(i)[1] == enemyMoves.get(counter)[1]){
                  return moves.get(i);
               } else{
                  counter++;
               }
            }
         }
      }
      
      if(moves.size() > 0){
         return moves.get(0);
      } else{
         return new int[0];
      }
      
   }

  
   public String getName() {
     return name;
   }
}