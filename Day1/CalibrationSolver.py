import re

def words_to_num(calibration_string):
    # issue where "twone" would be 1 not 21.
    #saw this solve on reddit to cover reused numbers honestly silly
    calibration_string = re.sub(r'(one)', "o1e", calibration_string)
    calibration_string = re.sub(r'(two)', "t2o", calibration_string)
    calibration_string = re.sub(r'(three)', "t3e", calibration_string)
    calibration_string = re.sub(r'(four)', "f4r", calibration_string)
    calibration_string = re.sub(r'(five)', "f5e", calibration_string)
    calibration_string = re.sub(r'(six)', "s6x", calibration_string)
    calibration_string = re.sub(r'(seven)', "s7n", calibration_string)
    calibration_string = re.sub(r'(eight)', "e8t", calibration_string)
    calibration_string = re.sub(r'(nine)', "n9e", calibration_string)

    return calibration_string


# print(re.sub(r'(one)', "1", "oneonetest test one"))

# print(words_to_num("onetwothreefourfivesixseveneightninetest test one"))


sumOfCalibrations = 0

with open('Day1/data/calibrations.txt') as f:
    data = f.readlines()

print(len(data))

def handleClean(string):
    pass

for i in data:
    #regex clean non numerical values
    print("raw: " + i)
    i = words_to_num(i)
    print("Processed: " + i)
    try:
        while not(i[0].isnumeric()):
            i = i[1:]
        while not(i[-1].isnumeric()):
            i = i[:-1]
            
        first = str(i[0])
        last = str(i[-1])

        string_calibration = first + last
        print("Out: " + string_calibration)
        calibration = int(string_calibration)

    except Exception as e:
        print(e)
        print(i)
        pass

    sumOfCalibrations += calibration

print(sumOfCalibrations)