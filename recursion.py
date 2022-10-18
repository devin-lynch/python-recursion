# recursive function is one that calls itself
def navel_gazer():
    # do some logic
    print('hmmmm....')
    #invokes itself
    navel_gazer()

# navel_gazer() # this would crash! there was no 'base case', causing an infinite loop!

# elements of a recursive function
    # 1. must have a 'base case' (a condition which terminates the recursion)
    # 2. recursive case (a condition in which the function invokes itself)
    # 3. must change its state to move closer to the base case each time the function recurses

    # EXAMPLE OF FOR LOOP
    # for (state;     base case;       drive state towards the base case)
    # for (let i=0;   i < arr.length;  i++)

# ITERATIVE
def iterative_loop(end_num):
    # loop up to end_num and print out each number
    # iterative! (non recursive)
    for i in range(0, end_num + 1):
        print('current number:', i)

# iterative_loop(20)


# RECURSIVE
def recursive_loop(end_num, current_num = 0):
    # recursive logic
    print('current number:', current_num)
    # base case -- stops the recursion
    if current_num == end_num:
        return
    # recursive case
    return recursive_loop(end_num, current_num + 1) # drives state towards the base case!

# recursive_loop(20)


# manage state by modifying input value given
def print_loop(end_num):
    # base case -- end_num is less than zero
    if end_num < 0:
        return

    #function logic
    print('current number is:', end_num)

    # recursive case that drives state towards the base case
    print_loop(end_num - 1)

print_loop(20)