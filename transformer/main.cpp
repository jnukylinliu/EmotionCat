#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include "TemperaturePredictor.h"

int main() {
    // 打开 CSV 文件，上一级目录的data文件夹
    std::ifstream file("../data/temperatures.csv");

    if (!file.is_open()) {
        std::cerr << "Failed to open the file!" << std::endl;
        return -1;
    }

    std::vector<float> temperatures;
    std::string line;

    // 跳过文件头部（如果有）
    std::getline(file, line);  // 假设第一行是表头

    // 读取数据
    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string value;
        // 读取每一行数据，假设每一行的温度在第一列
        if (std::getline(ss, value, ',')) {
            try {
                float temp = std::stof(value);  // 转换为 float 类型
                temperatures.push_back(temp);
            }
            catch (const std::invalid_argument& e) {
                std::cerr << "Invalid data: " << value << std::endl;
            }
        }
    }

    // 关闭文件
    file.close();

    // 打印历史数据
    std::cout << "Historical temperatures: ";
    for (const auto& temp : temperatures) {
        std::cout << temp << " ";
    }
    std::cout << std::endl;

    // 构造输入数据和目标数据
    std::vector<std::vector<float>> X;
    std::vector<float> y;

    // 使用前6天的数据训练，且目标数据是未来的温度
    for (size_t i = 0; i < temperatures.size() - 1; ++i) {
        X.push_back({ temperatures[i] });
        y.push_back(temperatures[i + 1]);  // 假设目标是下一天的温度
    }

    // 创建温度预测器对象
    TemperaturePredictor predictor;

    // 训练模型
    int epochs = 100;
    float learning_rate = 0.001;
    predictor.train(X, y, epochs, learning_rate);

    // 使用自注意力机制预测未来一天的温度
    float predicted_temp = predictor.predictNextTemperature(temperatures);

    // 输出预测的温度
    std::cout << "Predicted temperature for the next day: " << predicted_temp << "°C" << std::endl;

    return 0;
}
