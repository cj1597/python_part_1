# given_int =  input('Input a list of numbers: ')
# nums =list( given_int[1:-1].split(','))
# int_list = [int(y) for y in nums]
# cube_int = [x**3 for x in int_list]
# print(cube_int)
#

given_int = input('Input a list of numbers: ')
nums = list(given_int[1:-1].split(','))
int_list = [int(y) for y in nums]
cube_int = list(map(lambda x: x**3, int_list))
print(cube_int)
