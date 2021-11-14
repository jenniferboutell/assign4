#Jennifer Boutell
#UW Net ID: boutellj
#Time Complexity: O(n)

the_string = input("Enter a string to see if it is a palindrome.")
palindrome_num = len(the_string)


def is_palindrome(the_string):
    palindrome_check = ""
    palindrome_strip = ""
    neg_index = -1

    for i in range(0, palindrome_num):
        if the_string[neg_index].isalpha():
            palindrome_check = palindrome_check + the_string[neg_index].lower()
            neg_index -= 1
        else:
            neg_index -= 1

    for i in range(0, palindrome_num):
        if the_string[i].isalpha():
            palindrome_strip = palindrome_strip + the_string[i].lower()
            i += 1
        else:
            i += 1
    print("Forward " + palindrome_check)
    print("Backward " + palindrome_strip)

    if palindrome_check == palindrome_strip:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


is_palindrome(the_string)
