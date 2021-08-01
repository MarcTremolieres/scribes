#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

vector<string> lecture_entree();
int main() {
    vector<string> lignes = lecture_entree();
    for (string ligne:lignes) {
        cout << ligne << "\n";
    }
}