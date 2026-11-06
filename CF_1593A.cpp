#include <iostream>
#include <algorithm>

using namespace std;

int to_win (int a, int b, int c){
    if (a > b && a > c){
        return 0;
    } else {
        a = max(b, c) - a + 1;
        return a;
    }
}

int main(){
    int test_cases;
    cin >> test_cases;

    for (int i{}; i < test_cases; ++i){
        int a, b, c;
        cin >> a >> b >> c;

        cout << to_win (a, b, c) << ' ' << to_win (b, a, c) << ' ' << to_win(c, a, b);
        cout << '\n';
    }
    return 0;
}
