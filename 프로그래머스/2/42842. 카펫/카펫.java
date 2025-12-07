import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        List<Integer> yellowYaksu = new ArrayList<>();
        
        for (int i = 1; i <= yellow; i++) {
            if (yellow % i == 0) {
                yellowYaksu.add(i);
            }
        }
        
        for (int i : yellowYaksu) {       
            for (int j : yellowYaksu) { 
                if (i < j) {
                    continue;
                }
                
                if (i * j == yellow && (i + 2) * (j + 2) == (yellow + brown)) {
                    answer[0] = i + 2; 
                    answer[1] = j + 2; 
                    return answer;
                }
            }
        }
        
        return answer;
    }
}