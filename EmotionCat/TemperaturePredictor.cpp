#include "TemperaturePredictor.h"
#include <iostream>
#include <cmath>
#include <numeric>

TemperaturePredictor::TemperaturePredictor() {
    // 初始化权重
    W_Q = { {0.5, 0.2, 0.1} };
    W_K = { {0.3, 0.7, 0.5} };
    W_V = { {0.6, 0.4, 0.3} };
}

float TemperaturePredictor::dotProduct(const std::vector<float>& vec1, const std::vector<float>& vec2) {
    float sum = 0.0;
    for (size_t i = 0; i < vec1.size(); i++) {
        sum += vec1[i] * vec2[i];
    }
    return sum;
}

std::vector<float> TemperaturePredictor::softmax(const std::vector<float>& scores) {
    std::vector<float> result(scores.size());
    float max_val = *std::max_element(scores.begin(), scores.end());
    float sum_exp = 0.0;

    for (float score : scores) {
        sum_exp += std::exp(score - max_val);  // 数值稳定性：减去最大值
    }

    for (size_t i = 0; i < scores.size(); i++) {
        result[i] = std::exp(scores[i] - max_val) / sum_exp;
    }

    return result;
}

std::vector<float> TemperaturePredictor::weightedSum(const std::vector<float>& attention_weights, const std::vector<std::vector<float>>& values) {
    std::vector<float> result(values[0].size(), 0.0);

    for (size_t i = 0; i < attention_weights.size(); i++) {
        for (size_t j = 0; j < values[i].size(); j++) {
            result[j] += attention_weights[i] * values[i][j];
        }
    }

    return result;
}

float TemperaturePredictor::meanSquaredError(const std::vector<float>& predicted, const std::vector<float>& actual) {
    float error = 0.0;
    for (size_t i = 0; i < predicted.size(); i++) {
        error += std::pow(predicted[i] - actual[i], 2);
    }
    return error / predicted.size();
}

void TemperaturePredictor::printHistoricalData(const std::vector<float>& temperatures) {
    std::cout << "Historical temperatures: ";
    for (float temp : temperatures) {
        std::cout << temp << " ";
    }
    std::cout << std::endl;
}

void TemperaturePredictor::train(const std::vector<std::vector<float>>& X, const std::vector<float>& y, int epochs, float learning_rate) {
    for (int epoch = 0; epoch < epochs; epoch++) {
        std::vector<float> predicted_temperatures;
        for (size_t i = 0; i < X.size(); i++) {
            float predicted_temp = predictNextTemperature(X[i]);
            predicted_temperatures.push_back(predicted_temp);
        }

        // 计算损失
        float loss = meanSquaredError(predicted_temperatures, y);
        std::cout << "Epoch " << epoch + 1 << "/" << epochs << " - Loss: " << loss << std::endl;

        // 更新权重（简单的梯度下降）
        for (size_t i = 0; i < W_Q.size(); i++) {
            for (size_t j = 0; j < W_Q[i].size(); j++) {
                W_Q[i][j] -= learning_rate * (predicted_temperatures[i] - y[i]); // 更新 W_Q
            }
        }
        for (size_t i = 0; i < W_K.size(); i++) {
            for (size_t j = 0; j < W_K[i].size(); j++) {
                W_K[i][j] -= learning_rate * (predicted_temperatures[i] - y[i]); // 更新 W_K
            }
        }
        for (size_t i = 0; i < W_V.size(); i++) {
            for (size_t j = 0; j < W_V[i].size(); j++) {
                W_V[i][j] -= learning_rate * (predicted_temperatures[i] - y[i]); // 更新 W_V
            }
        }
    }
}

float TemperaturePredictor::predictNextTemperature(const std::vector<float>& temperatures) {
    // 计算 Q, K, V
    std::vector<std::vector<float>> Q, K, V;

    for (float temp : temperatures) {
        std::vector<float> q = { temp * W_Q[0][0], temp * W_Q[0][1], temp * W_Q[0][2] };
        std::vector<float> k = { temp * W_K[0][0], temp * W_K[0][1], temp * W_K[0][2] };
        std::vector<float> v = { temp * W_V[0][0], temp * W_V[0][1], temp * W_V[0][2] };

        Q.push_back(q);
        K.push_back(k);
        V.push_back(v);
    }

    // 计算点积注意力分数
    std::vector<float> attention_scores;
    for (size_t i = 0; i < Q.size(); i++) {
        float score = dotProduct(Q[0], K[i]);
        attention_scores.push_back(score);
    }

    // Softmax计算
    std::vector<float> attention_weights = softmax(attention_scores);

    // 计算加权求和（生成新的表示）
    std::vector<float> new_representation = weightedSum(attention_weights, V);

    // 预测未来一天的温度（新表示的加权和）
    float predicted_temperature = std::accumulate(new_representation.begin(), new_representation.end(), 0.0f);

    return predicted_temperature;
}
