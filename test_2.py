"""
The program is trying to display multiple outputs including
the number of grades, the averag grade, and the percentages of grades
that are above the average grade.
First initialize the function to display the number of grades.
Secondly, write a caluculate_percentage_above_average() function to
calculate the percentage of grades that are aboce the average grade.

Function 1 will kickstart the application, will extract from
the Final.txt file and calculate the average grade and close after the information has been collected.
Function 2 named percentage of grades above average will calculate
the percentage of grades that are above the average grade.
"""

"""
main():
    set Final.txt = input()
    num_grades = list
    average = sum(grades) len(grades)
    calculate above average percent

above_average():
    read in Final.txt
    read from list 
    close file
"""

infile = open("Final.txt", "r")
num_grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(num_grades)):
    num_grades[i] = int(num_grades[i])
average = sum(num_grades) / len(num_grades)
num = 0
for num_grade in num_grades:
        if num_grades > average:
            num += 1
print("Number of grades: ", len(num_grades))
print("Average grade: ", average)
print("Percentage of grades above average: {0:2f}%".format(100*num /len(num_grades)))

