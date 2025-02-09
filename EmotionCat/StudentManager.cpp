#include "StudentManager.h"
#include <iostream>
#include <numeric>
#include <random>

// 1. ʹ��vector�洢��������
StudentManager::StudentManager() : mathScores({ 85, 92, 78, 90, 68, 88, 95, 62, 75, 81 }) {}

// 2. ʹ���㷨����ͳ��ֵ
void StudentManager::calculateStatistics() {
    double avg = std::accumulate(mathScores.begin(), mathScores.end(), 0.0) / mathScores.size();
    auto [min_it, max_it] = std::minmax_element(mathScores.begin(), mathScores.end());

    std::cout << "��ѧ�ɼ�ͳ��:\n";
    std::cout << "ƽ����: " << avg << "\n";
    std::cout << "��߷�: " << *max_it << "\n";
    std::cout << "��ͷ�: " << *min_it << "\n\n";
}

// 3. ʹ��list���в�������
void StudentManager::sortScores() {
    for (auto score : mathScores) {
        auto pos = std::upper_bound(sortedScores.begin(), sortedScores.end(), score);
        sortedScores.insert(pos, score);
    }
}

// 4. ʹ��map����ѧ����Ϣӳ��
void StudentManager::buildStudentMap() {
    students.insert({ "Alice", Student("Alice", 18, 92.5) });
    students.emplace("Bob", Student("Bob", 19, 85.0));
    students.emplace("Charlie", Student("Charlie", 20, 78.5));
}

// 5. ʹ��unordered_map���п��ٲ���
void StudentManager::buildStudentSet() {
    for (const auto& [name, student] : students) {
        scoreMap[name] = student.score;
    }
}

// 6. ʹ��set�Զ�����ѧ������
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

// 7. ��������ת����mapתvector
void StudentManager::displayResults() {
    std::vector<std::pair<std::string, double>> scoreVec;
    std::transform(students.begin(), students.end(), std::back_inserter(scoreVec),
        [](const std::pair<std::string, Student>& p) {
            return std::make_pair(p.first, p.second.score);
        });

    // ������
    std::cout << "ѧ����Ϣ:\n";
    std::cout << "���ɼ�����:\n";
    for (const auto& s : sortedStudents) {
        std::cout << s.name << ": " << s.score << "\n";
    }

    std::cout << "\nǰ3��ѧ��:\n";
    for (int i = 0; i < 3 && !topStudents.empty(); ++i) {
        auto s = topStudents.top();
        std::cout << s.name << ": " << s.score << "\n";
        topStudents.pop();
    }

    std::cout << "\n��������ĺϸ�ѧ��:\n";
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
