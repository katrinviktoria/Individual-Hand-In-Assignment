def Add(Numbers):
    if Numbers == "":
        return 0
    elif "," in Numbers:
        the_sum = 0
        nums = Numbers.split(",")
        for num in nums:
            the_sum += int(num)
        return the_sum
    elif Numbers.isdigit:
        return int(Numbers)
    