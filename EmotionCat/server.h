
#ifndef SERVER_H
#define SERVER_H

#include "D:/EmotionCat/include/cpp-httplib-master/httplib.h"
#include "D:/EmotionCat/include/json-develop/single_include/nlohmann/json.hpp"
#include <string>

class Server {
public:
    Server();
    void start();
private:
    void printToHtmlFile(const std::string& output);
    std::string readOutputFromFile();
    void handleUserInput(const std::string& input);
    httplib::Server svr;
};

#endif // SERVER_H
