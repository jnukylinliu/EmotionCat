#ifndef STUDENT_HASH_H
#define STUDENT_HASH_H

#include "Student.h"

struct StudentHash {
    size_t operator()(const Student& s) const {
        return std::hash<std::string>()(s.name) ^ std::hash<int>()(s.age);
    }
};

#endif // STUDENT_HASH_H
