#include <iostream>
#include <string>
// #include<cstdio>
using namespace std;
int main()
{
    string n; // n을 선언 하고
    string result;

    cin >> n; // 입력값을 n에 넣기

    if (n.size() == 1 && n[0] == 'X') // 입력의 길이가 1이면서 그게 'X'이면
    {
        cout << "-1\n";
        return 0;
    }

    int i = 0;
    int cnt = 0;

    /*
    문자열을 표현할때는 문자열의 끝을 의미하는 문자인 '\0' 이 삽입된다. 
    이 문자를 가리켜 널(null) 문자라하며 아스키코드값 0에 해당함. 
    symbol(name)은 NUL 이다. 
    */

    while (n[i] != '\0') // 문자열이 끝날 때까지 반복문
    {
        while (n[i] == 'X' || n[i] != '.') // X값 추출
        {
            i++;
            cnt++;

            if (n[i] == '\0') // 문자열의 끝이면 X를 추출하는 while문 종료
                break;
        }

        if (cnt % 2 == 0) // 짝수 일 때
        {
            while (cnt >= 4) // 4개 연속일 때를 먼저 찾음
            {
                result += "AAAA";
                cnt -= 4;
            }
            while (cnt >= 2) // 그 후에 2개 연속일 때를 찾음
            {
                result += "BB";
                cnt -= 2;
            }
        }

        if (cnt != 0) // 0으로 딱 떨어지지 않으면
        {
            cout << "-1\n"; // -1 리턴
            return 0;
        }
        if (n[i] == '.') // . 이 있으면 . 추가
        {
            result += '.';
            i++;
        }
    }

    cout << result << '\n';
    return 0;
}