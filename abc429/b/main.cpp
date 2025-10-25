#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    bool isAble = false;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }
    for (int j = 0; j < N; j++) {
        vector<int> B(N);
        for (int k = 0; k < N; k++) {
            if (k != j) {
                B[k] = A[k];
            }
        }
        int sum = reduce(begin(B), end(B));
        if (sum == M) {
            isAble = true;
        }
    }
    if (isAble) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}

// 入力値を各要素ずつループでそのループの回数番目のインデックスを排除して足した値がMと合致する場合に"Yes"を出力してbreakすればいい
// 若干時間かかった。
// あとコンテスト中なので最適化に時間がかけられず（そもそも計算量は多くない）、
// 要素一つ一つでループして、その中のループで値を新しいVecterに入れてその配列の合計を求めてbool型の変数を更新し、それを元に出力する方法を選択した。