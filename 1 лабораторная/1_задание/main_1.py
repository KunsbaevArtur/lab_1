numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
_1 = sum(numbers[:4])
_2 = sum(numbers[5:])
average = _1 + _2
count = len(numbers)
numbers[4] = average/count
print("Измененный список:", numbers)
