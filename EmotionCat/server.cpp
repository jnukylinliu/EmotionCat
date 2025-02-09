#include "server.h"
#include <iostream>
#include <fstream>


// д��������ļ�
void Server::printToHtmlFile(const std::string& output) {
    std::ofstream file("output.txt", std::ios::app);
    if (file.is_open()) {
        file << output << std::endl;
        file.close();
    }
    else {
        std::cerr << "�޷����ļ����.txt" << std::endl;
    }
}

// ��ȡ����ļ����ݵĺ���
std::string Server::readOutputFromFile() {
    std::ifstream file("output.txt");
    std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    return content;
}

// �����û�����ĺ���
void Server::handleUserInput(const std::string& input) {
    std::cout << "�û�����: " << input << std::endl;

    // ���ļ���������д���ļ�
    std::ofstream out_file("output.txt", std::ios::app);  // ʹ��׷��ģʽ���ļ�
    if (out_file.is_open()) {
        out_file << input << std::endl;  // д���û�����
        out_file.close();  // �ر��ļ�
        std::cout << "������д�� output.txt" << std::endl;
    }
    else {
        std::cerr << "�޷����ļ� output.txt" << std::endl;
    }
}

Server::Server() {
    // �����ļ�д��һЩ���
    printToHtmlFile("Hello from C++!");
    printToHtmlFile("Another message.");

    // ���� OPTIONS ����Ԥ������
    svr.Options("/send_input", [](const httplib::Request& req, httplib::Response& res) {
        // ��������������Ӧͷ
        res.set_header("Access-Control-Allow-Origin", "*");
        res.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS");
        res.set_header("Access-Control-Allow-Headers", "Content-Type");
        res.set_content("", "text/plain");
        });

    // ���� GET �����������ṩ�ļ�����
    svr.Get("/get_output", [this](const httplib::Request&, httplib::Response& res) {
        res.set_header("Access-Control-Allow-Origin", "*");
        res.set_header("Content-Type", "text/plain; charset=utf-8");  // ����UTF-8����
        std::string output = readOutputFromFile();
        res.set_content(output, "text/plain; charset=utf-8");  // ����UTF-8����
        });

    // ���� POST ���������������û�����
    svr.Post("/send_input", [this](const httplib::Request& req, httplib::Response& res) {
        res.set_header("Access-Control-Allow-Origin", "*");
        res.set_header("Content-Type", "text/plain; charset=utf-8");  // ����UTF-8����

        // ���������� JSON ����
        try {
            nlohmann::json json_data = nlohmann::json::parse(req.body);
            std::string user_input = json_data["user_input"];
            handleUserInput(user_input);  // �����û�����
            res.set_content("�������յ�", "text/plain; charset=utf-8");  // ����UTF-8����
        }
        catch (const std::exception& e) {
            res.status = 400;
            res.set_content("��Ч������", "text/plain; charset=utf-8");
        }
        });
}

void Server::start() {
    svr.listen("localhost", 8080);
}
