def fibonacci(index):
    a = 0
    b = 1
    for i in range(index):
        c = a + b
        a = b
        b = c

    return a
index = int(input("Введiть iндекс бажаного числа Фiбоначчi: "))
fibonacci_number = fibonacci(index)
print(f"Число Фiбоначчi з iндексом {index} дорiвнює {fibonacci_number}.")