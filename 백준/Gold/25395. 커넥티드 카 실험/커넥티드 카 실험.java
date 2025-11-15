import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
    // 
    

    static class info {
        public int id; // 커넥티드카 방문 여부 
        public int position; // 차량 위치
        public int fuel; // 차량 연료
    }

    public static void main(String[] args) throws IOException {

        Deque<Integer> q = new ArrayDeque<>(); 
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        info[] arr = new info[N+1];
        st = new StringTokenizer(bf.readLine());
        for(int i = 1; i<N+1; i++) { // 커넥티드 카의 위치를 초기화
            arr[i] = new info();
            arr[i].id = 0;
            arr[i].position = Integer.parseInt(st.nextToken());

        }

        st = new StringTokenizer(bf.readLine());
        for (int i = 1; i < N+1; i++) { // 커넥티드 카의 연로를 초기화
            arr[i].fuel = Integer.parseInt(st.nextToken());
        }

        q.addLast(S);
        arr[S].id = 1;
        while(!q.isEmpty()) {
            int now = q.pollFirst();
            for(int i=now; i<=N; i++){ // 현재 연결한 커넥티드카 위치 보다 뒤에 있는 애들
                if(arr[i].position >arr[now].position + arr[now].fuel) {
                    break;
                }

                if (arr[i].id ==0) {
                    q.addLast(i);
                    arr[i].id = 1;
                }
            }
            
            for(int j=now; j>0; j--){ // 현재 연결한 커넥티드카 위치 보다 앞에 있는 애들
                if(arr[j].position < arr[now].position - arr[now].fuel) {
                    break;
                }

                if (arr[j].id ==0) {
                    q.addLast(j);
                    arr[j].id = 1;
                }
            }
        }

        StringBuilder answer = new StringBuilder();
        for(int i=1; i<N+1; i++) {
            if (arr[i].id !=0){
                answer.append(i).append(" ");
            }
        }
        System.out.println(answer);
    }

}
