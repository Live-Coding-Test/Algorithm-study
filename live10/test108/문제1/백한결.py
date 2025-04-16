def main():
    expression = input()
    numList = expression.split('-')
    totalSum = 0
    totalMinus = []


    for i in numList[0].split('+'):
        totalSum += int(i)

    for i in range(1, len(numList)):
        totalMinus.append(numList[i].split('+'))

        for j in totalMinus.pop():
            totalSum -= int(j)

    print(totalSum)

if __name__ == "__main__":
    main()