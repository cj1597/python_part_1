list1 =input('Input first list: ').replace("'","")
list2 = input('Input second list: ').replace("'","")

list1_conv = list1[1:-1].split(',')
list2_conv = list2[1:-1].split(',')

comb_list=[a+b for a in list1_conv for b in list2_conv]

print(comb_list)
