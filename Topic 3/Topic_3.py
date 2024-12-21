def maximizeExpressionWithParentheses(expression):
    import re

    # Parse expression into numbers and operators
    nums = list(map(int, re.findall(r'\d+', expression)))
    ops = re.findall(r'[+\-]', expression)

    n = len(nums)
    maxGraph = [[{'value': float('-inf'), 'expr': ''} for _ in range(n)] for _ in range(n)]
    minGraph = [[{'value': float('inf'), 'expr': ''} for _ in range(n)] for _ in range(n)]

    # Initialize base cases
    for i in range(n):
        maxGraph[i][i] = {'value': nums[i], 'expr': str(nums[i])}
        minGraph[i][i] = {'value': nums[i], 'expr': str(nums[i])}

    # Compute values and expressions for subexpressions
    for length in range(2, n + 1):  # Subexpression lengths
        for i in range(n - length + 1):  # Start index
            j = i + length - 1  # End index
            for k in range(i, j):  # Possible splits
                op = ops[k]

                # Calculate max value
                if op == '+':
                    maxValue = maxGraph[i][k]['value'] + maxGraph[k + 1][j]['value']
                    minValue = minGraph[i][k]['value'] + minGraph[k + 1][j]['value']
                elif op == '-':
                    maxValue = maxGraph[i][k]['value'] - minGraph[k + 1][j]['value']
                    minValue = minGraph[i][k]['value'] - maxGraph[k + 1][j]['value']

                # Update maxGraph
                if maxValue > maxGraph[i][j]['value']:
                    maxGraph[i][j]['value'] = maxValue
                    maxGraph[i][j]['expr'] = f"({maxGraph[i][k]['expr']} {op} {maxGraph[k + 1][j]['expr']})"

                # Update minGraph
                if minValue < minGraph[i][j]['value']:
                    minGraph[i][j]['value'] = minValue
                    minGraph[i][j]['expr'] = f"({minGraph[i][k]['expr']} {op} {minGraph[k + 1][j]['expr']})"

    # Final result
    result = maxGraph[0][n - 1]
    print("Maximum Value:", result['value'])
    print("Expression achieving maximum value:", result['expr'])
    print("\nAll Parenthesized Expressions and Values:")
    for i in range(n):
        for j in range(n):
            if maxGraph[i][j]['expr']:
                print(f"From {i} to {j}: {maxGraph[i][j]['expr']} = {maxGraph[i][j]['value']}")

    return result['value'], result['expr']

# Example usage
expression = "4 + 3 - 2 - 5 + 1 - 6 + 7"
maximizeExpressionWithParentheses(expression)
