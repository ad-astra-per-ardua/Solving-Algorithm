#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

class Trie {
public:
    Trie* child[26];
    unordered_map<int, int> num;
    char val;
    int depth;
    Trie(char val, int depth = 0) : val(val), depth(depth) {
        for(int i = 0; i < 26; i++) {
            child[i] = nullptr;
        }
    }

    void push(string word) {
        Trie* node = this;
        while (word.length() > 0) {
            node->num[word.length()] += 1;
            if (node->child[word[0] - 'a'] == nullptr) {
                node->child[word[0] - 'a'] = new Trie(word[0], node->depth + 1);
            }
            node = node->child[word[0] - 'a'];
            word = word.substr(1);
        }
    }

    int search(string word) {
        Trie* node = this;
        while (word.length() > 0) {
            if (word[0] == '?') {
                return node->num[word.length()];
            }
            if (node->child[word[0] - 'a'] == nullptr) {
                return 0;
            }
            node = node->child[word[0] - 'a'];
            word = word.substr(1);
        }
        return 0;
    }
};

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    Trie* t1 = new Trie('a');
    Trie* t2 = new Trie('a');
    for(string word: words) {
        t1->push(word);
        t2->push(string(word.rbegin(), word.rend()));
    }

    for(string query: queries) {
        if (query[0] != '?') {
            answer.push_back(t1->search(query));
        } else {
            answer.push_back(t2->search(string(query.rbegin(), query.rend())));
        }
    }
    return answer;
}
