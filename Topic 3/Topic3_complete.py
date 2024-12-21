import random
import time
import matplotlib.pyplot as plt

def generate_random_expression(size):
    numbers = [str(random.randint(1, 10)) for _ in range(size)]
    operators = [random.choice(["+", "-"]) for _ in range(size - 1)]
    expression = ""
    for i in range(size - 1):
        expression += numbers[i] + " " + operators[i] + " "
    expression += numbers[-1]
    return expression

def maximize_expression(expression):
    numbers, operators = parse_expression(expression)
    n = len(numbers)
    
    # Initialize DP tables
    maxGraph = [[None for _ in range(n)] for _ in range(n)]
    minGraph = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        maxGraph[i][i] = {"value": numbers[i], "expr": str(numbers[i])}
        minGraph[i][i] = {"value": numbers[i], "expr": str(numbers[i])}

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            maxGraph[i][j] = {"value": float("-inf"), "expr": ""}
            minGraph[i][j] = {"value": float("inf"), "expr": ""}

            for k in range(i, j):
                op = operators[k]
                leftMax = maxGraph[i][k]["value"]
                rightMax = maxGraph[k + 1][j]["value"]
                leftMin = minGraph[i][k]["value"]
                rightMin = minGraph[k + 1][j]["value"]

                if op == "+":
                    results = [
                        (leftMax + rightMax, f"({maxGraph[i][k]['expr']} + {maxGraph[k+1][j]['expr']})"),
                        (leftMin + rightMin, f"({minGraph[i][k]['expr']} + {minGraph[k+1][j]['expr']})"),
                    ]
                elif op == "-":
                    results = [
                        (leftMax - rightMin, f"({maxGraph[i][k]['expr']} - {minGraph[k+1][j]['expr']})"),
                        (leftMin - rightMax, f"({minGraph[i][k]['expr']} - {maxGraph[k+1][j]['expr']})"),
                    ]

                for value, expr in results:
                    if value > maxGraph[i][j]["value"]:
                        maxGraph[i][j] = {"value": value, "expr": expr}
                    if value < minGraph[i][j]["value"]:
                        minGraph[i][j] = {"value": value, "expr": expr}

    return maxGraph[0][n - 1]

def parse_expression(expression):
    tokens = expression.split()
    numbers = list(map(int, tokens[0::2]))
    operators = tokens[1::2]
    return numbers, operators


def measure_runtime():
    input_sizes = [10, 20, 50, 100, 200]
    runtimes = []

    for size in input_sizes:
        expression = generate_random_expression(size)
        start_time = time.time()
        maximize_expression(expression)
        end_time = time.time()
        runtimes.append(end_time - start_time)

    return input_sizes, runtimes

def plot_runtime(input_sizes, runtimes):
    plt.plot(input_sizes, runtimes, marker='o', color='b')
    plt.title("Input Size vs Runtime")
    plt.xlabel("Input Size (Number of Terms)")
    plt.ylabel("Runtime (seconds)")
    plt.grid()
    plt.show()

# # Example usage
# expression = "4 + 3 - 2 - 5 + 1 - 6 + 7"
# result = maximize_expression(expression)
# print(f"Maximum Value: {result['value']}")
# print(f"Expression: {result['expr']}")


# Example usage
input_sizes, runtimes = measure_runtime()
print(f"Input Sizes: {input_sizes}")
print(f"Runtimes: {runtimes}")

plot_runtime(input_sizes, runtimes)

