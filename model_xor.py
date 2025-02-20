import numpy as np

# 모델 작업은 Class로 하는 것 권유
class XorModel:
    def __init__(self):
        # 파라메터
        self.weights = np.random.rand(2)
        self.bias = np.random.rand(1)

    def train(self):
        learning_rate = 0.1
        epochs = 20
        inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        outputs = np.array([0, 1, 1, 0])        
        for epoch in range(epochs):
            for i in range(len(inputs)):
                # 총 입력 계산
                total_input = np.dot(inputs[i], self.weights) + self.bias
                # 예측 출력 계산
                prediction = self.sigmoid(total_input)
                # 오차 계산
                error = outputs[i] - prediction
                print(f'inputs[i] : {inputs[i]}')
                print(f'weights : {self.weights}')
                print(f'bias before update: {self.bias}')
                print(f'prediction: {prediction}')
                print(f'error: {error}')
                # 가중치와 편향 업데이트
                self.weights += learning_rate * error * inputs[i]
                self.bias += learning_rate * error
                print('====')        

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    
    def predict(self, input_data): # input_data -> 배열 형태, 2개
        total_input = np.dot(input_data, self.weights) + self.bias
        return self.sigmoid(total_input)    
    