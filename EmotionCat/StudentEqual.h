#ifndef STUDENT_EQUAL_H
#define STUDENT_EQUAL_H

#include "Student.h"

struct StudentEqual {
    bool operator()(const Student& lhs, const Student& rhs) const {
        return lhs.name == rhs.name && lhs.age == rhs.age;
    }
};

#endif // STUDENT_EQUAL_H
