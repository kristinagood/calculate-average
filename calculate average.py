def main():
    scores = input("Enter five test scores seperated by commas: ")
    listScores = scores.split(",")
    determine_grade(listScores)
    calc_average(listScores)

def determine_grade(grades):
    for num in grades:
        if float(num) >= 90 and float(num) <= 100:
            print("A")
        elif float(num) >=80 and float(num) <= 89:
            print("B")
        elif float(num) >=70 and float(num) <= 79:
            print("C")
        elif float(num) >=60 and float(num) <= 69:
            print("D")
        else:
            print("F")


def calc_average(grades):
    total = 0
    for num in grades:
        total += float(num)
    average = total / 5
    print(format(average, '.2f'))



main()
