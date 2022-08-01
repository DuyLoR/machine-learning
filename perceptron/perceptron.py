#áp dụng thuật toán perceptron
#input: bảng chân lý, giá trị w0,w1,w2
#output: giá trị y, giá trị W
from numpy import array

def step_function(x): return 0 if x < 0 else 1

def perceptron(training_dataset, weights, learning_rate, expected):
        result = weights[1] * training_dataset[1] + weights[2] * training_dataset[2] - weights[0]
        err = expected - step_function(result)
        for i in range(len(weights)):
                weights[i] = weights[i] + learning_rate * err * training_dataset[i]
        return step_function(result)
        
training_dataset = [

    array([-1, 0, 0]),
    array([-1, 0, 1]),
    array([-1, 1, 0]),
    array([-1, 1, 1]),
]

weights = [0.1, 0.2, 0.3]

and_gate = (0, 0, 0, 1)
or_gate = (0, 1, 1, 1)

learning_rate = 0.2
print("and_gate")
print("x1\tx2\ty\tW0\tW1\tW2")
for i in range(4):
        print("{}\t{}\t{}\t{}\t{}\t{}x".format(
                training_dataset[i][1],
                training_dataset[i][2],
                perceptron(training_dataset[i], weights, learning_rate, and_gate[i]),
                round(weights[0],2),
                round(weights[1],2),
                round(weights[2],2),
                ))
print("OR_gate")        
for i in range(4):
        print("{}\t{}\t{}\t{}\t{}\t{}x".format(
                training_dataset[i][1],
                training_dataset[i][2],
                perceptron(training_dataset[i], weights, learning_rate, or_gate[i]),
                round(weights[0],2),
                round(weights[1],2),
                round(weights[2],2),
                ))
