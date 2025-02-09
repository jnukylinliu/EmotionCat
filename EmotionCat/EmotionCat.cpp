
#include "server.h"
#include <iostream>
#include "StudentManager.h"

int main() {

    //cmd to html
    Server svr;
    svr.start();
    
    //test
    StudentManager manager;
    manager.processData();
    std::cout << "按任意键退出程序...\n";
    std::cin.get();  // 等待用户按下回车键

    return 0;
}






/*

#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <string>
#include <unordered_map>
#include <random>
#include <unordered_set>

using namespace std;

struct Student {
    string name;
    int age;
    double score;

    Student(string n, int a, double s) : name(n), age(a), score(s) {}

    bool operator<(const Student& other) const {
        return score < other.score;
    }
};

// 自定义哈希函数用于unordered_map
struct StudentHash {
    size_t operator()(const Student& s) const {
        return hash<string>()(s.name) ^ hash<int>()(s.age);
    }
};

// 自定义相等比较函数
struct StudentEqual {
    bool operator()(const Student& lhs, const Student& rhs) const {
        return lhs.name == rhs.name && lhs.age == rhs.age;
    }
};

int main() {
    // 1. 使用vector存储基础数据
    vector<int> mathScores = { 85, 92, 78, 90, 68, 88, 95, 62, 75, 81 };

    // 2. 使用算法计算统计值
    double avg = accumulate(mathScores.begin(), mathScores.end(), 0.0) / mathScores.size();
    auto [min_it, max_it] = minmax_element(mathScores.begin(), mathScores.end());

    cout << "数学成绩统计:\n";
    cout << "平均分: " << avg << "\n";
    cout << "最高分: " << *max_it << "\n";
    cout << "最低分: " << *min_it << "\n\n";

    // 3. 使用list进行插入排序
    list<double> sortedScores;
    for (auto score : mathScores) {
        auto pos = upper_bound(sortedScores.begin(), sortedScores.end(), score);
        sortedScores.insert(pos, score);
    }

    // 4. 使用map建立学生信息映射
    map<string, Student> students;
    students.insert({ "Alice", Student("Alice", 18, 92.5) });
    students.emplace("Bob", Student("Bob", 19, 85.0));
    students.emplace("Charlie", Student("Charlie", 20, 78.5));

    // 5. 使用unordered_map进行快速查找
    unordered_map<string, double> scoreMap;
    for (const auto& [name, student] : students) {
        scoreMap[name] = student.score;
    }

    // 6. 使用set自动排序学生对象
    set<Student> sortedStudents;
    for (const auto& [name, student] : students) {
        sortedStudents.insert(student);
    }

    // 7. 使用deque进行双端操作
    deque<Student> studentQueue;
    studentQueue.push_front(Student("David", 21, 95.0));
    studentQueue.push_back(Student("Eve", 22, 88.5));

    // 8. 使用priority_queue进行成绩排序
    priority_queue<Student> topStudents;
    for (const auto& [name, student] : students) {
        topStudents.push(student);
    }

    // 9. 使用stack进行逆序操作
    stack<Student> reverseOrder;
    for (const auto& s : sortedStudents) {
        reverseOrder.push(s);
    }

    // 10. 使用算法处理数据
    vector<Student> allStudents;
    transform(students.begin(), students.end(), back_inserter(allStudents),
        [](const pair<string, Student>& p) { return p.second; });

    // 移除分数低于80的学生
    allStudents.erase(
        remove_if(allStudents.begin(), allStudents.end(),
            [](const Student& s) { return s.score < 80; }),
        allStudents.end());

    // 随机打乱顺序
    random_device rd;
    mt19937 g(rd());
    shuffle(allStudents.begin(), allStudents.end(), g);

    // 11. 使用unordered_set进行快速存在性检查
    unordered_set<Student, StudentHash, StudentEqual> studentSet;
    for (const auto& s : allStudents) {
        studentSet.insert(s);
    }

    // 12. 复杂数据转换：map转vector
    vector<pair<string, double>> scoreVec;
    transform(students.begin(), students.end(), back_inserter(scoreVec),
        [](const pair<string, Student>& p) {
            return make_pair(p.first, p.second.score);
        });

    // 13. 使用算法查找信息
    auto it = find_if(scoreVec.begin(), scoreVec.end(),
        [](const pair<string, double>& p) {
            return p.second > 90;
        });

    // 输出结果
    cout << "学生信息:\n";
    cout << "按成绩排序:\n";
    for (const auto& s : sortedStudents) {
        cout << s.name << ": " << s.score << "\n";
    }

    cout << "\n前3名学生:\n";
    for (int i = 0; i < 3 && !topStudents.empty(); ++i) {
        auto s = topStudents.top();
        cout << s.name << ": " << s.score << "\n";
        topStudents.pop();
    }

    cout << "\n查找结果:\n";
    if (it != scoreVec.end()) {
        cout << "找到高分学生: " << it->first << " (" << it->second << ")\n";
    }

    cout << "\n随机排序后的合格学生:\n";
    for (const auto& s : allStudents) {
        cout << s.name << ": " << s.score << "\n";
    }
    cout << "按任意键退出程序...\n";
    cin.get();  // 等待用户按下回车键
    return 0;
}
*/


