import java.util.*;

class Solution {
    static List<Integer>[] graph;
    static boolean[] visited;

    public int solution(int n, int[][] wires) {
        graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] wire : wires) {
            int a = wire[0];
            int b = wire[1];
            graph[a].add(b);
            graph[b].add(a);
        }

        int answer = Integer.MAX_VALUE;

        for (int[] wire : wires) {
            int a = wire[0];
            int b = wire[1];

            visited = new boolean[n + 1];

            int count = dfs(a, a, b); 

            int diff = Math.abs((n - count) - count);
            answer = Math.min(answer, diff);
        }

        return answer;
    }

    private int dfs(int node, int cutA, int cutB) {
        visited[node] = true;
        int count = 1;

        for (int nxt : graph[node]) {
            if ((node == cutA && nxt == cutB) || (node == cutB && nxt == cutA)) {
                continue;
            }

            if (!visited[nxt]) {
                count += dfs(nxt, cutA, cutB);
            }
        }

        return count;
    }
}