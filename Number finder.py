# Prime numbers finder by Leszek Michalak

import csv

start_opt = input(
    "Hello! Type: \n'1' to start searching the prime numbers from beggining \n'2' to load the .csv file that stores the progress and continue searching\n'3' to exit")

while True:
    if start_opt == str("1"):
        x = 2
        complexity = 0
        complexity_benchmark = [1, 1]
        prime_numbers = [1, 2]
        break
    if start_opt == str("2"):
        complexity = 0
        prime_numbers = list()
        with open('prime numbers.txt', 'r') as fcont:
            lines = fcont.readline().split(',')
            prime_numbers = list(lines)
            x = int(prime_numbers[-2])
            print("\nsave file loaded!")
            print("the highest prime number you have found is: " + str(x))
        fcont.close()
        with open('complexity benchmark.txt', 'r') as fcontb:
            lines = fcontb.readline().split(',')
            complexity_benchmark = list(lines)
        fcontb.close()
        break
    else:
        start_opt = input("please write again")
        continue
    break

# input of scope
scope = input("Please input the max of the scope of prime numbers finding")

while int(scope) < int(x):
    scope = input("Please input higher number!")

import timeit

start = timeit.default_timer()


def engine(x, complexity, prime_numbers, complexity_benchmark):
    while x < int(scope):
        x += 1
        y = x
        print("Testing" + str(x))
        for y in range(2, y + 1):
            complexity += 1
            # print(str(x)+"/"+str(y)+" -> mod:"+str(x/y))
            if x == y:
                prime_numbers.append(x)
                complexity_benchmark.append(complexity)
                print("Is a prime number")
            break
        if x % y == 0:
            y += 1
            print("Not a prime number")
            break


print("\n\nComplexity of calculation: " + str(complexity))

engine(x, complexity, prime_numbers, complexity_benchmark)


def file_append(x, prime_numbers, complexity, complexity_benchmark):
    with open('prime numbers.csv', 'w+') as f:
        f.write("Prime numbers list:\n" + str(prime_numbers) + "\nComplexity benchmarks:\n" + str(complexity_benchmark))
    f.close()
    with open('prime numbers.txt', 'w+') as ftxt:
        for item in prime_numbers:
            ftxt.write("%s," % item)
    ftxt.close()
    with open('complexity_benchmark.txt', 'w+') as ftxtb:
        for item in complexity_benchmark:
            ftxtb.write("%s," % item)
    ftxtb.close()


file_append(x, prime_numbers, complexity, complexity_benchmark)

# printing the list of all prime numbers:
if len(prime_numbers) > 30:
    print("Please find the prime numbers in prime numbers.csv or prime numbers.txt")
    print("\nTotal found:" + str(len(prime_numbers)))
else:
    print("\nList of prime numbers:")
    print(prime_numbers)
    print("\nTotal found:" + str(len(prime_numbers)))

# for performance check:
stop = timeit.default_timer()
print("\nTime of calculation: ", stop - start)
print("Thank you for using this code!")

graph_opt = input(
    "Do you want a complexity graph (it shows exponential growth of complexity to calculate the next prime number)?yes/no")
if graph_opt == str("yes"):
    import matplotlib.pyplot as plt

    f = plt.figure()
    plt.plot(complexity_benchmark, ".")
    f.savefig("complexity benchmark.pdf", bbox_inches='tight')
else:
    print("Thank you for using this code!")

graph_opt = input("Do you want a prime numbers graph (it shows linear distribution of prime numbers)?yes/no")
if graph_opt == str("yes"):
    import matplotlib.pyplot as plt

    f = plt.figure()
    plt.plot(prime_numbers, ".")
    f.savefig("prime numbers!.pdf", bbox_inches='tight')
else:
    print("Thank you for using this code!")

graph_opt = input("Do you want a combined graph?yes/no")
if graph_opt == str("yes"):
    import matplotlib.pyplot as plt

    f = plt.figure()
    plt.plot(prime_numbers, "*", complexity_benchmark, ".")
    f.savefig("combined.pdf", bbox_inches='tight')
else:
    print("Thank you for using this code!")