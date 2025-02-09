#ifndef STUDENT_H
#define STUDENT_H

#include <string>

struct Student {
    std::string name;
    int age;
    double score;

    Student(std::string n, int a, double s) : name(n), age(a), score(s) {}

    bool operator<(const Student& other) const {
        return score < other.score;
    }
};

#endif // STUDENT_H
