


#------------------------------------------------------
#------- Loop => for---
#-------------------------------------------------------
# for Items in iterable-object :
#    DO somthing with Item
# ---------------------------------------------------------
# Items is A Variable You Create and Call whenever you want
# item refer to the current position and WIll run and Visit all items to the end 
# iterable_object => sequence[list , tuple , dictionary , set , string of characters , etc.... ]
#-----------------------------------------------------------


myNumbers = [1,2,3,4,5,6,7,8,9]
for number in myNumbers :
    # print(number) # 1,2,3,4,5,6,7,8,9
    # print(number * 20) # 20 , 40 , 60 , 80 , 100 , 120 , 140 , 160 , 180
    if number %2 == 0 : # Even
        print(f"The Number {number} is Even") # The Number 2 is Even # The Number 4 is Even # The Number 6 is Even # The Number 8 is Even

    else :
        print(f"The Number {number} is Oddo") # The Number 1 is Oddo # The Number 2 is Even # The Number 3 is Oddo # The Number 4 is Even # The Number 5 is Oddo # The Number 6 is Even # The Number 7 is Oddo # The Number 8 is Even # The Number 9 is Oddo

else :
    print("The Loop is Finished") # The Loop is Finished




myName = "Salar"

for letter in myName :
    # print(letter) # S a l a r
    print(f"[ {letter.upper()} ]") # [S] , [A] , [L] , [A] , [R]




