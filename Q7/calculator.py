import sys


def calc(entry):
    try:
        component = entry.strip().split()
        if not component:
            return None
        if len(component) != 3:
            return f"{entry.strip()}\nERROR: Line format is erroneous!"

        operand1_str, operator, operand2_str = component

        try:
            operand1 = float(operand1_str)
        except ValueError:
            return f"{entry.strip()}\nERROR: First operand is not a number!"

        try:
            operand2 = float(operand2_str)
        except ValueError:
            return f"{entry.strip()}\nERROR: Second operand is not a number!"

        if operator not in ['+', '-', '*', '/']:
            return f"{entry.strip()}\nERROR: There is no such an operator!"

        result = 0
        if operator == '+':
            result = operand1 + operand2
        elif operator == '-':
            result = operand1 - operand2
        elif operator == '*':
            result = operand1 * operand2
        elif operator == '/':
            if operand2 != 0:
                result = operand1 / operand2
            else:
                return f"{entry.strip()}\nERROR: Division by zero!"

        return f"{entry.strip()}\n={result:.2f}"

    except ValueError as e:
        return f"{entry.strip()}\nERROR: {e}"


def algorithm(input_file, output_file):
    answers = []
    try:
        with open(input_file, "r") as input_file:
            for line in input_file:
                result = calc(line)
                if result is not None:
                    answers.append(result)

        with open(output_file, 'w') as output1:
            output1.write('\n'.join(answers))
    except FileNotFoundError:
        print(f"ERROR: File '{input_file}' not found or permission issue!")
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print("ERROR: This program needs two command line arguments.")
        print("Sample run command: python3 calculator.py input.txt output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    algorithm(input_file, output_file)


if __name__ == "__main__":
    main()
