def int_to_roman(input):

    if not isinstance(input, type(1)):
        raise TypeError, "prepei na einai akeraios, got %s" % type(input)
    if not 0 < input < 1000000:
        raise ValueError, "O arithmos prepei na einai metaksi 1 kai 1000000"
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)
print int_to_roman(input("Dwse enan akeraio apo 1 mexri 1000000 "))