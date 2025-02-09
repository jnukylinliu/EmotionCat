#ifndef STUDENT_MANAGER_H
#define STUDENT_MANAGER_H

#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <random>
#include <algorithm>
#include <iterator>
#include "Student.h"
#include "StudentHash.h"
#include "StudentEqual.h"

class StudentManager {
public:
    StudentManager();
    void processData();

private:
    std::vector<int> mathScores;
    std::list<double> sortedScores;
    std::map<std::string, Student> students;
    std::unordered_map<std::string, double> scoreMap;
    std::set<Student> sortedStudents;
    std::deque<Student> studentQueue;
    std::priority_queue<Student> topStudents;
    std::stack<Student> reverseOrder;
    std::vector<Student> allStudents;
    std::unordered_set<Student, StudentHash, StudentEqual> studentSet;

    void calculateStatistics();
    void sortScores();
    void buildStudentMap();
    void buildStudentSet();
    void performAlgorithms();
    void displayResults();
};

#endif // STUDENT_MANAGER_H
