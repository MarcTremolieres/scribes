#include <vector>
#include <iostream>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
vector<string> lecture_entree() {
    vector<string> lignes;
    string ligne;
    while (getline(cin, ligne)) {
        if (ligne == "") {
            break;
        }
        lignes.push_back(ligne);
    }
    return lignes;
};