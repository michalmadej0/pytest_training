square = [x **2 for x in range(10)]
print(square)


def fizzbuzz():
    lista = {}
    for x in range(0,101):
        if x % 2 == 0 and x % 3 == 0:
            print('FizzBuzz')
            lista.append(key=x,value="Fizzbuzz")
            lista.append('Fizzbuzz')

        elif x % 2 == 0:
            print("Fizz")
        elif x % 3 == 0:
            print("Buzz")

    print(lista)


fizzbuzz()

# def test_fizz_2():
#     for
#
#     assert fizzbuzz(x) == "Fizz"