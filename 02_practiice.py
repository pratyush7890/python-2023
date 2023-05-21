sub1=int(input("Enter the mathssubject              marks\n"))
sub2=int(input("Enter the python subject            marks\n"))
sub3=int(input("Enter the electronic subject        marks\n"))
sub4=int(input("Enter the chemistry subject         marks\n"))
sub5=int(input("Enter the english subject           marks\n"))
sub6=int(input("Enter the field project subject     marks\n"))
sub7=int(input("Enter the engeering drawing subject marks\n"))
if(sub1<33 or sub2<33 or sub3<33 or sub4<33 or sub5<33 or sub6<33 or sub7<33):
    print("congrulation you are fail ")
elif(sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7)/7 <40 :
    print("you are fail less than 40%")
else:
    print("you are passed")    