def take(n, string):

    new_string = ""

    for index in range(0, min(n, len(string))):
        new_string += string[index]

    return new_string

def string_matrix(matrix_width, strings):

    result = ""

    for i in range(0, matrix_width):
        for k in range(0, matrix_width):
            if len(strings[i]) > matrix_width:
                strings[i] = take(matrix_width, strings[i])

            if len(strings[i]) < matrix_width:
                while len(strings[i]) != matrix_width:
                    strings[i] += "X"
                    
            if len(strings[i]) == matrix_width:
                for ch in strings[i][k]:
                    if k < (matrix_width - 1):
                        result += "| " + strings[i][k] + " "
                    else:
                        result += "| " + strings[i][k] + " |" + "\n"

    return result

print(string_matrix(6,["python","gogo","perl","kava","haskell","ruby0nRails"]))