#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, A;
  cin >> N >> A;

  for (int i = 0; i < N; i++) {
    string op;
    int B;
    int ans;
    cin >> op >> B;
    if (op == "+") {
      A += B;
      cout<< i + 1 << ":" << A << endl;
    }
    else if (op == "-") {
      A -= B;
      cout<< i + 1 << ":" << A << endl;
    }
    else if (op == "*") {
      A *= B;
      cout<< i + 1 << ":" << A << endl;
    }
    else if (op == "/" and B != 0) {
      A /= B;
      cout<< i + 1 << ":" << A << endl;
    }
    else if (op == "/" and B == 0) {
      cout << "error" << endl;
      break;
    }
  }
}
