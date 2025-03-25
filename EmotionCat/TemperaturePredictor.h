#ifndef TEMPERATUREPREDICTOR_H
#define TEMPERATUREPREDICTOR_H

#include <vector>

class TemperaturePredictor {
public:
    // 构造函数
    TemperaturePredictor();

    // 训练模型
    void train(const std::vector<std::vector<float>>& X, const std::vector<float>& y, int epochs, float learning_rate);

    // 预测未来一天的温度
    float predictNextTemperature(const std::vector<float>& temperatures);

    // 打印历史数据
    void printHistoricalData(const std::vector<float>& temperatures);

private:
    // 计算两个向量的点积
    float dotProduct(const std::vector<float>& vec1, const std::vector<float>& vec2);

    // Softmax函数
    std::vector<float> softmax(const std::vector<float>& scores);

    // 加权求和（生成新的表示）
    std::vector<float> weightedSum(const std::vector<float>& attention_weights, const std::vector<std::vector<float>>& values);

    // 均方误差损失函数
    float meanSquaredError(const std::vector<float>& predicted, const std::vector<float>& actual);

    // 权重
    std::vector<std::vector<float>> W_Q;
    std::vector<std::vector<float>> W_K;
    std::vector<std::vector<float>> W_V;
};

#endif // TEMPERATUREPREDICTOR_H
