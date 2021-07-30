import re 

#Arithmetic Formatter Project: The objective of this project is to solve arithmetic problems while clearly stating when a problem occurs.

#We still find problems: Operations not displayed correctly, problems not solved.

def arithmetic_arranger(problems, solve = False):

    if(len(problems) > 5):
      return 'Error: Too Many Problems'

    first_number = ""
    second_number = ""
    lines = ""
    sumres = ""
    string = ""
    for problem in problems :
      if re.search('[^\s0-9.+-]', problem) :
        if re.search('[/]', problem) or re.search('[*]', problem) :
          return 'Error: operator must be "+" or "-"'
        return 'Error: numbers must contain only digits'

      number_one = problem.split(' ')[0] #Arrays
      number_two = problem.split(' ')[1]
      operator = problem.split(' ')[2]

      if (len(number_one) >= 5) or (len(number_two) >= 5) :
        return 'Error: number cannot have more than 4 digits'
      
      sum = ''
      if (operator == '+') :
        sum = str(int(number_one) + int(number_two))
      elif (operator == '-') :
        sum = str(int(number_one) - int(number_two))

      length = max(len(number_one), len(number_two))
      top = str(number_one).rjust(length)
      bottom = operator + str(number_two).rjust(length - 1)
      line = ''
      sol = str(sum).rjust(length)
      for s in range (length) :
        line += '-'

      if problem != problems[-1]:
        first_number += top + ' '
        second_number += bottom + ' '
        lines += line + ' '
        sumres += sol + ' '
      else:
        first_number += top
        second_number += bottom
        lines += line
        sumres += sol
      
    if solve:
      string = first_number + '\n' + second_number + '\n' + lines + '\n' + sumres
    else:
      string = first_number + '\n' + second_number + '\n' + lines
    return string

  
from arithmetic_arranger import arithmetic_arranger
from unittest import main


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
