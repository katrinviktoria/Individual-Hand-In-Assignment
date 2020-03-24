def Add(Numbers):
    if Numbers == "":
        return 0
    elif "," in Numbers:
        num1, num2 = Numbers.split(",")
        the_sum = int(num1) + int(num2)
        return the_sum
    elif Numbers.isdigit:
        return int(Numbers)
    