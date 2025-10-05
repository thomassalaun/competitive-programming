def fake_bin(x):
    bin_x = ""
    for i in x:
        if int(i) >= 5:
            bin_x += "1"
        else:
            bin_x += "0"
    return bin_x