#ifndef TEMPERATUREPREDICTOR_H
#define TEMPERATUREPREDICTOR_H

#include <vector>

class TemperaturePredictor {
public:
    // ���캯��
    TemperaturePredictor();

    // ѵ��ģ��
    void train(const std::vector<std::vector<float>>& X, const std::vector<float>& y, int epochs, float learning_rate);

    // Ԥ��δ��һ����¶�
    float predictNextTemperature(const std::vector<float>& temperatures);

    // ��ӡ��ʷ����
    void printHistoricalData(const std::vector<float>& temperatures);

private:
    // �������������ĵ��
    float dotProduct(const std::vector<float>& vec1, const std::vector<float>& vec2);

    // Softmax����
    std::vector<float> softmax(const std::vector<float>& scores);

    // ��Ȩ��ͣ������µı�ʾ��
    std::vector<float> weightedSum(const std::vector<float>& attention_weights, const std::vector<std::vector<float>>& values);

    // ���������ʧ����
    float meanSquaredError(const std::vector<float>& predicted, const std::vector<float>& actual);

    // Ȩ��
    std::vector<std::vector<float>> W_Q;
    std::vector<std::vector<float>> W_K;
    std::vector<std::vector<float>> W_V;
};

#endif // TEMPERATUREPREDICTOR_H
