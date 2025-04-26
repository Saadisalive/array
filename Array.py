import array as arr
 #Create an arrry
arry_num = arr.array('i',[1,3,5,3,7,9,3])
print("Orignal array:"+str(arry_num))

#count number of occurences
print("Number of Occurances of the number 3 in the said array:"+str(arry_num.count(3)))

#reverse the array
arry_num.reverse()
print("reverse the order of the items")
print(str(arry_num))