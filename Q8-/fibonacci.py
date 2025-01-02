def fibo_naive(n, output_naive):
    if n <= 0:
        error_message = "ERROR: Fibonacci cannot be calculated for the non-positive numbers!"
        output_naive.write(error_message + "\n")
        return "nan"
    elif n <= 2:
        result = 1
        output_naive.write(f"fib({n}) = {result}\n")
        return result
    else:
        i = n
        if i >= 3:
            output_naive.write(f"fib({i}) = fib({i - 1}) + fib({i - 2})\n")
            i -= 1
        return fibo_naive(n - 1, output_naive) + fibo_naive(n - 2, output_naive)


def fibo_eager(n, memory, output_eager):
    if n <= 0:
        error_message = "ERROR: Fibonacci cannot be calculated for non-positive numbers!"
        output_eager.write(error_message + "\n")
        return "nan"
    elif n <= 2:
        result = 1
        memory[n] = result
        return result
    elif n in memory:
        return memory[n]
    else:
        result = fibo_eager(n - 1, memory, output_eager) + fibo_eager(n - 2, memory, output_eager)
        memory[n] = result
        return result


def main():
    input_file = open("input.txt", "r")
    output_naive = open("output_naive.txt", "w")
    output_eager = open("output_eager.txt", "w")
    numbers = [int(x) for x in input_file.readlines()]

    for number in numbers:
        output_naive.write("-" * 32 + "\n")
        output_naive.write(f"Calculating {number}. Fibonacci number:\n")
        output_naive.write(f"{number}. Fibonacci number is: {fibo_naive(number, output_naive)}\n")

    for number in numbers:
        memory = {}  # Create a new local memory for each iteration
        output_eager.write("-" * 32 + "\n")
        output_eager.write(f"Calculating {number}. Fibonacci number:\n")
        if number > 2:
            output_eager.write(f"fib({number}) = fib({number - 1}) + fib({number - 2})\n")
            output_eager.write(f"fib({number-1}) = {fibo_eager(number-1,memory, output_eager)}\n")
            output_eager.write(f"fib({number-2}) = {fibo_eager(number-2,memory, output_eager)}\n")
        else:
            output_eager.write(f"fib({number}) = {fibo_eager(number, memory, output_eager)}\n")

        output_eager.write(f"{number}. Fibonacci number is: {fibo_eager(number, memory, output_eager)}\n")

    output_eager.write("-" * 32 + "\n")
    output_eager.write(f"Structure for the eager solution:\n{list(memory.values())}\n")
    output_eager.write("-" * 32)
    output_naive.write("-" * 32)


if __name__ == "__main__":
    main()
