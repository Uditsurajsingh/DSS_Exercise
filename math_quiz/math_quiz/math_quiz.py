import random
def random_integer(min, max):
    """
    Generating a random integer withing the given range
    """
    return int(random.randint(min, max))
def operator():
    """
    picking a random operator
    """
    return random.choice(['+', '-', '*'])
def calculator(n1, n2, o):
# Solving the expressing and returning problem and
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a
def math_quiz():
    s = 0
    t_q = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = random_Integer(1, 10); n2 = random_Integer(1, 5); o = operator()

        PROBLEM, ANSWER = calculator(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        raw_number = input("Your answer: ")

        try:
            useranswer = int(raw_number)
        except ValueError:
            print("input is not an integer")
            exit()


        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
