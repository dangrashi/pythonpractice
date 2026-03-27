#WAP to ask the user to enter names of their 3 favourite movies and store them in a list. 
mov=[]

mov1=input("enter the movie:")
mov2=input("enter the movie:")
mov3=input("enter the movie:")

mov.append(mov1)
mov.append(mov2)
mov.append(mov3)

print(mov)

#WAP to check if a list contains a palindrome of elements
list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if copy_list1==list1:
    print("paindrome")
else:
    print("NOT palindrome")
