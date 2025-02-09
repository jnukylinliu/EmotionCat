#include "server.h"
#include <iostream>
#include <fstream>


// 写入输出到文件
void Server::printToHtmlFile(const std::string& output) {
    std::ofstream file("output.txt", std::ios::app);
    if (file.is_open()) {
        file << output << std::endl;
        file.close();
    }
    else {
        std::cerr << "无法打开文件输出.txt" << std::endl;
    }
}

// 读取输出文件内容的函数
std::string Server::readOutputFromFile() {
    std::ifstream file("output.txt");
    std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    return content;
}

// 处理用户输入的函数
void Server::handleUserInput(const std::string& input) {
    std::cout << "用户输入: " << input << std::endl;

    // 打开文件并将输入写入文件
    std::ofstream out_file("output.txt", std::ios::app);  // 使用追加模式打开文件
    if (out_file.is_open()) {
        out_file << input << std::endl;  // 写入用户输入
        out_file.close();  // 关闭文件
        std::cout << "输入已写入 output.txt" << std::endl;
    }
    else {
        std::cerr << "无法打开文件 output.txt" << std::endl;
    }
}

Server::Server() {
    // 先向文件写入一些输出
    printToHtmlFile("Hello from C++!");
    printToHtmlFile("Another message.");

    // 处理 OPTIONS 请求（预检请求）
    svr.Options("/send_input", [](const httplib::Request& req, httplib::Response& res) {
        // 设置允许跨域的响应头
        res.set_header("Access-Control-Allow-Origin", "*");
        res.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS");
        res.set_header("Access-Control-Allow-Headers", "Content-Type");
        res.set_content("", "text/plain");
        });

    // 定义 GET 请求处理器，提供文件内容
    svr.Get("/get_output", [this](const httplib::Request&, httplib::Response& res) {
        res.set_header("Access-Control-Allow-Origin", "*");
        res.set_header("Content-Type", "text/plain; charset=utf-8");  // 设置UTF-8编码
        std::string output = readOutputFromFile();
        res.set_content(output, "text/plain; charset=utf-8");  // 设置UTF-8编码
        });

    // 定义 POST 请求处理器，接收用户输入
    svr.Post("/send_input", [this](const httplib::Request& req, httplib::Response& res) {
        res.set_header("Access-Control-Allow-Origin", "*");
        res.set_header("Content-Type", "text/plain; charset=utf-8");  // 设置UTF-8编码

        // 解析传来的 JSON 数据
        try {
            nlohmann::json json_data = nlohmann::json::parse(req.body);
            std::string user_input = json_data["user_input"];
            handleUserInput(user_input);  // 处理用户输入
            res.set_content("输入已收到", "text/plain; charset=utf-8");  // 设置UTF-8编码
        }
        catch (const std::exception& e) {
            res.status = 400;
            res.set_content("无效的输入", "text/plain; charset=utf-8");
        }
        });
}

void Server::start() {
    svr.listen("localhost", 8080);
}
