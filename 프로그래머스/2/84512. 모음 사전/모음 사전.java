class Solution {
    public int solution(String word) {

        int[] weight = {781, 156, 31, 6, 1};
        int answer = 0;

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);

            int order = 0;
            switch (c) {
                case 'A': order = 0; break;
                case 'E': order = 1; break;
                case 'I': order = 2; break;
                case 'O': order = 3; break;
                case 'U': order = 4; break;
            }

            answer += order * weight[i] + 1;
        }

        return answer;
    }
}