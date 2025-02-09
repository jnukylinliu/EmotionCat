#include "StudentManager.h"
#include <iostream>
#include <numeric>
#include <random>

// 1. 使用vector存储基础数据
StudentManager::StudentManager() : mathScores({ 85, 92, 78, 90, 68, 88, 95, 62, 75, 81 }) {}

// 2. 使用算法计算统计值
void StudentManager::calculateStatistics() {
    double avg = std::accumulate(mathScores.begin(), mathScores.end(), 0.0) / mathScores.size();
    auto [min_it, max_it] = std::minmax_element(mathScores.begin(), mathScores.end());

    std::cout << "数学成绩统计:\n";
    std::cout << "平均分: " << avg << "\n";
    std::cout << "最高分: " << *max_it << "\n";
    std::cout << "最低分: " << *min_it << "\n\n";
}

// 3. 使用list进行插入排序
void StudentManager::sortScores() {
    for (auto score : mathScores) {
        auto pos = std::upper_bound(sortedScores.begin(), sortedScores.end(), score);
        sortedScores.insert(pos, score);
    }
}

// 4. 使用map建立学生信息映射
void StudentManager::buildStudentMap() {
    students.insert({ "Alice", Student("Alice", 18, 92.5) });
    students.emplace("Bob", Student("Bob", 19, 85.0));
    students.emplace("Charlie", Student("Charlie", 20, 78.5));
}

// 5. 使用unordered_map进行快速查找
void StudentManager::buildStudentSet() {
    for (const auto& [name, student] : students) {
        scoreMap[name] = student.score;
    }
}

// 6. 使用set自动排序学生对象
void StudentManager::performAlgorithms() {
    for (const auto& [name, student] : students) {
        sortedStudents.insert(student);
    }

    for (const auto& [name, student] : students) {
        studentQueue.push_front(student);
        studentQueue.push_back(student);
    }

    for (const auto& [name, student] : students) {
        topStudents.push(student);
    }

    for (const auto& s : sortedStudents) {
        reverseOrder.push(s);
    }

    std::transform(students.begin(), students.end(), std::back_inserter(allStudents),
        [](const std::pair<std::string, Student>& p) { return p.second; });

    allStudents.erase(
        std::remove_if(allStudents.begin(), allStudents.end(),
            [](const Student& s) { return s.score < 80; }),
        allStudents.end());

    std::random_device rd;
    std::mt19937 g(rd());
    std::shuffle(allStudents.begin(), allStudents.end(), g);

    for (const auto& s : allStudents) {
        studentSet.insert(s);
    }
}

// 7. 复杂数据转换：map转vector
void StudentManager::displayResults() {
    std::vector<std::pair<std::string, double>> scoreVec;
    std::transform(students.begin(), students.end(), std::back_inserter(scoreVec),
        [](const std::pair<std::string, Student>& p) {
            return std::make_pair(p.first, p.second.score);
        });

    // 输出结果
    std::cout << "学生信息:\n";
    std::cout << "按成绩排序:\n";
    for (const auto& s : sortedStudents) {
        std::cout << s.name << ": " << s.score << "\n";
    }

    std::cout << "\n前3名学生:\n";
    for (int i = 0; i < 3 && !topStudents.empty(); ++i) {
        auto s = topStudents.top();
        std::cout << s.name << ": " << s.score << "\n";
        topStudents.pop();
    }

    std::cout << "\n随机排序后的合格学生:\n";
    for (const auto& s : allStudents) {
        std::cout << s.name << ": " << s.score << "\n";
    }
}

void StudentManager::processData() {
    calculateStatistics();
    sortScores();
    buildStudentMap();
    buildStudentSet();
    performAlgorithms();
    displayResults();
}
