#include <bits/stdc++.h>
using namespace std;

int main() {
  int p;
  string text;
  int price;
  cin >> p;

  // パターン1
  if (p == 1) {
    cin >> price;
  }

  // パターン2
  if (p == 2) {
    cin >> text >> price;
  }

  int N;
  cin >> N;

  if (text != "") cout << text << "!" << endl;
  cout << price * N << endl;
}

// C++の書き方的にあんまりよくないのと、最適化がされていない。
// if (!text.empty()) {
//   cout << price * N << endl;
// }
// こういう書き方がいいのと、パターンが2通りだから
// 当該パターンに当てはまるもののみif文内でcoutして、それぞれの固定の値はif文の外で取得・coutするのがスマート。