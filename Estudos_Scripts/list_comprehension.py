def main():
    lista_1 = [2,3,4,5,6]

    multiples = [x * 2 for x in lista_1 if x % 2 == 0 or x > 5]

    print(multiples)


if __name__ == "__main__":
    main()