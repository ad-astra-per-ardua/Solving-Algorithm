#include <string>
#include <cctype>
#include <vector>
using namespace std;
const string invalid = "invalid";

string rule1(string str){
    string result;
    if(str.size() < 3) return "-1";
    char secondChar = str[1];
    bool isLowerExist = false;
    for(int i = 0; i < str.size(); i++){
        if(islower(str[i])) isLowerExist = true;
        if(i % 2 == 0){
            if(islower(str[i])) return "-1";
            result += str[i];
        }else{
            if(secondChar != str[i]) return "-1";
        }
    }
    if(!isLowerExist) return "-1";
    return result;
}

string allUpper(string str){
    string result;
    for(char c : str){
        if(!isupper(c)) return "-1";
        result += c;
    }
    return result;
}

string solution(string sentence) {
    vector<bool> used(26, 0);
    string answer = "";
    while(!sentence.empty()){
        string result;
        vector<int> positions;
        if(islower(sentence[0])){
            if(used[sentence[0] - 'a']) return invalid;
            used[sentence[0] - 'a'] = 1;
            for(int i = 0; i < sentence.size(); i++){
                if(sentence[i] == sentence[0]) {
                    positions.push_back(i);
                }
            }
            if(positions.size() != 2) return invalid;

            string center = sentence.substr(1, positions.back() - 1);
            if(center == "") return invalid;
            result = rule1(center);
            if(result == "-1") {
                result = allUpper(center);
                if(result == "-1"){
                    return invalid;
                }
            }else{
                if(used[sentence[2] - 'a']) return invalid;
                used[sentence[2] - 'a'] = 1;
            }
            sentence = sentence.substr(positions.back() + 1);
        }else{
            if(sentence.size() == 1 || isupper(sentence[1])){
                result = sentence[0];
                sentence = sentence.substr(1);
            }else{
                for(int i = 0; i < sentence.size(); i++){
                    if(sentence[1] == sentence[i]) positions.push_back(i); 
                }
                if(positions.size() != 2){
                    if(positions.back() == sentence.size() - 1) return invalid;
                    if(islower(sentence[positions.back() + 1])) return invalid;
                    string center = sentence.substr(0, positions.back() + 2);
                    result = rule1(center);
                    if(result == "-1") return invalid;
                    if(used[sentence[1] - 'a']) return invalid;
                    used[sentence[1] - 'a'] = 1;
                    sentence = sentence.substr(positions.back() + 2);
                }else{
                    result = sentence[0];
                    sentence = sentence.substr(1);
                }   
            }
        }
        answer += result + " ";
    }
    answer.pop_back();
    return answer;
}
