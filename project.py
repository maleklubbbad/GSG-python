name = input("Enter your full name please")
id = int(input("Enter your ID number please"))
num = int(input("Enter your Mobile number please"))

print("Welcome", name , "to the bus station")

buses = { 1 : "From Acre to Haifa" , 2 : "From Haifa to Jaffa" , 3 : "From Gaza to Rafah" ,
          4 : "From Hebron to Jerusalem",5 : "From Tulkarm to Ramallah"}
print("Bus traffic for today will be according to" , buses )
numofbus = int(input("please, Choose the appropriate bus according to its number "))
if (numofbus == 1) :
    seats1 = { 1 : " the Second row  One seat on the right" , 2 : "the fourth row one seats on the left",
               3 : " the Fifth row One seat on the left" ,  4 :"the seventh row  one seats on the left for free ",
               5 : "the ninth One seat on the right for free  "}
    print("the Empty seats in bus 1 : " , seats1)
    seatsbus1 = int(input("Choose the right seat for you (from 1- 5)"))
    print("to " , name , "seat reserved " , seats1[seatsbus1] , " in bus 1 ", buses[1])
elif (numofbus == 2) :
    seats2 = {1: " the Third row  One seat on the right", 2: "the fourth row One seat on the left",
             3: "the Fifth row  one seats on the left for free ", 4: "the eighth One seat on the right for free "}
    print("the Empty seats in bus 2 : ", seats2)
    seatsbus2 = int(input("Choose the right seat for you (from 1-4)"))
    print("to ", name, "seat reserved ", seats2[seatsbus2], " in bus 2 ", buses[2])
elif (numofbus == 3) :
    seats3 = {1: " the first row  One seat on the left", 2: "the Second row One seat on the right",
             3: "the fourth rowOne seat on the left ", 4: "the sixth One seat on the right for free",
             5 : " the seventh row  one seats on the left for free" , 6 : "the eighth One seat on the right for free" }
    print("the Empty seats in bus 3 : ", seats3)
    seatsbus3 = int(input("Choose the right seat for you (from 1-6)"))
    print("to ", name, "seat reserved ", seats3[seatsbus3], " in bus 3 ", buses[3])
elif (numofbus == 4):
    seats4 = {1:"Sorry, the seats is full"}
    print("the Empty seats in bus 4 : ", seats4)
    print("to ", name,  seats4[1], " in bus 4 ", buses[4])
elif (numofbus == 5) :
    seats5 = {1: " the Second row  One seat on the left", 2: "the Third row One seat on the left ",
             3: "the Fifth row One seat on the right  ", 4: "the sixth One seat on the right for free",
             5 : " the seventh row  One seat on the left for free" }
    print("the Empty seats in bus 5 : ", seats5)
    seatsbus5 = int(input("Choose the right seat for you (from 1-5)"))
    print("to ", name, "seat reserved ", seats5[seatsbus5], " in bus 5 ", buses[5])
else: print("The number you entered is not connected to any bus , Please try again . ")