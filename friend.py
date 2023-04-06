from datetime import date

# Python list that contains a dictionary object
friend_list = [{"name": "test1 test2", "age": 20, "future": 30, "past": 10  }, ]

def calculate_current_age(birth_year):
    today = date.today()
    return today.year - float(birth_year)

def calculate_future_age(current_age):
    return current_age + 10

def calculate_past_age(current_age):
    return current_age - 10


def add_friend(first_name, last_name, current_age, future_age, past_age):
    #create a dictionary from the input
    friend_dict = {"name": first_name + " " + last_name, "age": current_age, "future": future_age, "past": past_age}
    #append this dictionary to the main list
    friend_list.append(friend_dict)
    return

  
def collectUserDetails():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    birth_year = float(input("What year were you born?"))
    
    return (first_name, last_name, birth_year)
    
 
def main():
    
    print(friend_list)
    
    first_name, last_name, birth_year = collectUserDetails()
    
    current_age = calculate_current_age(birth_year)
    
    future_age = calculate_future_age(current_age)
    
    past_age = calculate_past_age(current_age)
    
    add_friend(first_name, last_name, current_age, future_age, past_age)
    
    print(friend_list)



if __name__ == "__main__":
    main()
