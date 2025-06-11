# 자바의 간단한 문법들
## 문자열

### 문자열 입력
```Java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


BufferReader br = new BufferReader(new InputStreamReader(System.in)); 
StringTokenizer st = new StringTokenizer(br.readLine());

int cnt = st.countTokens();
while (st.hasMoreTokens()) {
            String token = st.nextToken();
            int i = Integer.parseInt(st.nextToken);
            
        }
```
### 문자열 관리
- int n = Integer.parseInt(String s) : 문자열을 정수로 변환
- String toString(int i) : 정수를 문자열로 변환
- char charAt(int i) : i인덱스 문자 값 리턴
- int compareTo(String s): 문자열 순서 비교 -> 같으면 0, s 보다 먼저나오면 -1, 늦게나오면 1
- String concat(String s): 현재 문자열 + 문자열 s 값 리턴
- boolean contains(String s) : s가 문자열에 포함되어있는지 여부
- int length() : 문자열 길이 리턴
- String replace(String a, String b) : a의 문자들을 b로 치환
- String[] split(String regex) : regex를 중심으로 스트링 분리
- String trim() : 앞뒤 공백제거
- String toLowerCase(), toUpperCase() : 소문자, 대문자 스트링 리턴

### StringBuilder
- immutable인 String을 대신할 문자열 관리 클래스 (속도가 더 빠름)
```Java
StringBuilder sb = new StringBuilder(st.nextToken());
sb.append(" world");
sb.insert(6, "world");
sb.replace(6,10, " world");
sb.delete(6,10);
sb.deleteCharAt(6);
sb.reverse();
int capacity = sb.capacity();
char ch = sb.chatAt(4);
int len = sb.length();
String str = sb.toString();
```

