#prework homework Question 1
def hello_name(user_name):
    print("hello_" + str(user_name))
hello_name("Muhammed")

#prework homework Question 2
def first_odds():
    for i in range(1, 100, 2):
        print(i)
first_odds()

#prework homework Question 3
def max_num_in_list(a_list):
    print(max(a_list))
max_num_in_list([54, 125, 35, 184, 2022, 1995, 1911])

#prework homework Question 4
def is_leap_year(a_year):
    if(a_year % 4 == 0):
        if(a_year % 100 != 0):
            if(a_year % 400 == 0):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(is_leap_year(2022)) #this question makes no sense...

#prework homework Question 5
def is_consecutive(a_list): 
    for i,n in enumerate(a_list):
        if i == (len(a_list)-1):
            return True
        if(n + 1 != a_list[i + 1]):
            return False
    return True
print(is_consecutive([17,18,19,20,21,22,23,24]))    
