def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
    
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print("The two strings are anagrams of each other.")
else:
    print("The two strings are not anagrams of each other.")
