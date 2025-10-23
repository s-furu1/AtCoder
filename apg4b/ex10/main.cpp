#include <bits/stdc++.h>
using namespace std;

int main() {
  int A, B;
  cin >> A >> B;

  int i = 0;
  int j = 0;
  string k;
  string l;
  while (i < A) {
    k += "]";
    i++;
  }
  while (j < B) {
    l += "]";
    j++;
  }
  cout << "A:" + k << endl << "B:" + l << endl;
}

// コンパクトにまとまったが、最初にまとめて宣言しなくても変数を初期化しなおして使いまわせる点や
// まとめて出力せずとも、規定値まで行ったら改行を加えることなども選択肢に入ることを意識する。