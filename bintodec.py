def binToDec(x, a, b):
    binary = ""
    for i in x:
        if i.isdigit() and i == "1" or i == "0":
            binary += i

    if not binary:
        return 0
    elif binary[0] in ["1", "0"]:
        return int(binary[a:b], 2) if a < b else binToDec(x[1:], a, b)
    else:
        return binToDec(binary[1:], a, b)
print(binToDec("!1@1#1$01$%^&",0,13))
print(binToDec("makan 1 bakso 10.000",0,20))
