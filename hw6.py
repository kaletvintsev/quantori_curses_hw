if __name__ == "__main__":
    count = 0
    for i in range(1000000):
        str_number = str(i)
        bin_number = bin(i)[2:]
        if str_number == str_number[:: -1] and bin_number == bin_number[:: -1]:
            count += i
    print(count)
