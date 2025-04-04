def main():
    N = int(input())
    a = list(map(int, input().strip().split()))[:N]

    min_price = float('inf')
    max_profit = 0

    for i in a:
        if i < min_price:
            min_price = i
        profit = i - min_price
        if profit > max_profit:
            max_profit = profit

    print(max_profit)



if __name__ == "__main__":
    main()