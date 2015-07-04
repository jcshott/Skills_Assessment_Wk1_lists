"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """
    
    odd_list = []               #create a empty list to add odd numbers to
    
    for item in number_list:        #loop through given numbers 
        if item % 2 != 0:           #check if the item has a remainder when divided by 2, therefore it is odd
            odd_list.append(item)   #if an item is odd add it to our new odd list
    return odd_list                 #return that new list of only the odd integers


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    even_list = []              #same as with odd list, only we add integer to list if it is even
    
    for item in number_list:
        if item % 2 == 0:
            even_list.append(item)
    
    return even_list


def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """

    for item in my_list:                    #loop through list printing indices and item associated
        print my_list.index(item), item

print_indeces(["Toyota", "Jeep", "Volvo"])


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    long_words_list = []                #create new list to feed into
    for word in word_list:              #loop through list, evaluate whether length is greater than 4, if so, append to empty list
        if len(word) > 4:               
            long_words_list.append(word)

    return long_words_list


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5

    If the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """

    if number_list == []:   #immediatly return None if list is empty
        return None
    else:
        number_list.sort()     #if not empty, sort the list smallest to largest. return first (smallest) item
        return number_list[0]


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    if number_list == []:   #immediatly return None if empty list
        return None
    else:
        number_list.sort()  #if contains items, sort list smallest to largest and return last item (largest)
        return number_list[-1]


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """

    number_as_floats = []               #create new lists to feed into
    numbers_divided = []               
    for number in number_list:          #loop through list, convert to float
        number = float(number)
        number_as_floats.append(number)

    for number in number_as_floats:     #loop through new list of floats and divide by two, put into new divided list
        number = number/2.0
        numbers_divided.append(number)

    return numbers_divided                           #return new list of divided numbers


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    length_of_input_words = []

    for word in word_list:                          #loop through words and append value of world length to new list
        length_of_input_words.append(len(word))
    
    return length_of_input_words



def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    sum_of_numbers = 0

    for item in number_list:
        sum_of_numbers = sum_of_numbers + item

    return sum_of_numbers


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    total = 1       #set to one so you aren't multiplying by 0 to start and anything multiplied by 1 is itself

    for number in number_list:  #loop through list, multiplying each item
        total = total * number
    
    return total


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python ha a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    joined_string = ""                          #created empty string to feed into
    for string in word_list:
        joined_string = joined_string + string  #loop through the list and put the words together in new string
    
    return joined_string


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """
    total = 0.0                    #counter for total of inputs

    for item in number_list:        #loop through list, adding to counter, ensuring float since there will likely be decimal places in a division situation
        total = total + float(item)

    return total / float(len(number_list))


# END OF SKILLS TEST; YOU CAN STOP HERE OR YOU CAN WORK ON ADVANCED PROBLEMS


def advanced_join_strings(list_of_words):
    """Return a single string with each word from the input list
    separated by a comma.

        >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> advanced_join_strings(["Pretzel"])
        'Pretzel'

    """
    if len(list_of_words) == 1:     #if only one item in list, return that item
        return list_of_words[0]
    
    else:                               #if more than one item, create new variable that will hold the strings from list
        word_list = ""
        for word in list_of_words[0:-1]:    #loop through the list of words and join together all but the last one with a comma
            word_list = word_list + word + ", "
        return word_list + list_of_words[-1]    #add in last item after you've put together all other times so you don't have a comma at end


##############################################################################
# You can ignore everything after here

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
