# Exercise 1
def odd_sum(num_list):
    total = 0
    for n in num_list:
        if n % 2 != 0:
            total += n
    return total

my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = [2,4,6,8,10,1]
other_list = [11,13,15,17,19,20,22,24]

print(odd_sum(my_list)) # Should print 25
print(odd_sum(new_list)) # Should print 1
print(odd_sum(other_list)) # Should print 75
print('')

# Exercise 2
name_list = ['stanley', 'victoria', 'ian']

print('Please enter your name')
user_name = input().lower()
if user_name in name_list:
    print(f"Hello {user_name}")
else:
    print("Who goes there?")