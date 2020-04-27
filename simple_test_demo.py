# testing
our_family = [['puppy',45], ['kitty', 44], ['hannah', 6], ['hamnah',4], ['haroun',2]]

def print_family(family):
    for member in family:
        print(f'{member} is in my family')

def how_old_in_so_many_years(family, future_years :int):
    for member in family:
        print(f'{member[0]} will be {member[1] + future_years} years old in {future_years} years time')

def age_in_next_years(current_age :int, future_years :int):
    return current_age + future_years

def increment(x):
    return x + 1

def decrement(x):
    return x - 1

if __name__ == "__main__":
    print_family(our_family)
    how_old_in_so_many_years(our_family, 5)

    for name,age in our_family:
        print(name, age)
        future_years:int = 5
        print(f'{name} will be {age_in_next_years(age,future_years)} years old in {future_years} years time')
