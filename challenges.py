def add_chocolate(shopping_list: list):
    """My housemate is a real health-nut, but I like chocolate. This function 
    adds the string "chocolate" to any list it receives, and returns the 
    modified list. That way our shopping list is always correct.

    Arguments:
        - shopping_list: a list of strings

    Returns:
        - the same list, with the string "chocolate" added to the end
    """
    shopping_list.append("chocolate")
    return shopping_list

###############################################################################################

def lou_bega(lyrics_list: list):
    """This function accepts a list of strings and adds the words 
    "A little bit of " to the front of each.
    
    Arguments:
        - lyrics_list: a list of strings
    
    Returns:
        - the same list, but each string now has "A little bit of " 
        prepended to it.

    Example input: 
        [
            "Monica in my life", 
            "Erica by my side", 
            "Rita's all I need"
        ]
        
    Example output: 
        [
            "A little bit of Monica in my life", 
            "A little bit of Erica by my side", 
            "A little bit of Rita's all I need"
        ]
    """
    lyric = "A little bit of "
    new_lyrics_list = []
    for lyrics in lyrics_list:
        # print(lyrics)
        # print(lyrics_list)
        # print(lyric)
        new_lyrics = (lyric + lyrics)
        # print(new_lyrics)
        new_lyrics_list.append(new_lyrics)
        # print(new_lyrics_list)
    
    return new_lyrics_list
    
result = lou_bega( ["Monica in my life", "Erica by my side", "Rita's all I need"])
print(result)

###############################################################################################

def assemble_guest_list():
    """This function repeatedly prompts the user for the name of a dinner guest.
    Each string the user supplies is added to a list. If/when the user hits 
    "Enter" without typing anything, the function stops asking and 
    returns the list.
    
    Arguments: None!
    
    Returns:
        - a list of strings supplied by the user
    """
    guest_list = []
    while True:
        guest_name = input("Enter name of a dinner guest: ")
        if guest_name == "":
            break
        guest_list.append(guest_name)
    return guest_list

###############################################################################################
    
def is_prime(some_number: int): # A bit trickier!
    """This function tests to see if the input is a prime number.
    Whenever a prime number is divided by an integer larger than 1 and smaller
    than itself, the result includes a remainder.

    NOTE: The lowest prime number is 2. 1 and 0 are not prime.
    
    Arguments:
        - some_number: an integer to be tested for prime-ness

    Returns:
        - a boolean representing whether or not some_number is prime
    """
    if some_number <= 1:
        return False
    if some_number == 2:
        return True
    for x in range(2, some_number): # list[2, 3, 4]
        if some_number%x == 0:
            print(x)
            return False
    return True

prime=is_prime(21)
print(prime)
    
    
    # Hint: 
    #   int(1.5) == 1.0

