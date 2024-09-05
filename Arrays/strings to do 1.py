# remove blanks 
def rmv_blank(string):
    result = ''
    for char in string:
        if char != ' ':
            result += char
    return result

print(rmv_blank('my na me is ah ma ad')) 

# get digits 
def get_digit(string):
    digit = ''
    for char in string :
        if char.isdigit():
            digit += char
    return int(digit)
print(get_digit('my1name3is4ahmad2nezam')) 


def acronym(phrase):
  
    words = phrase.split()
    
  
    acronym_str = ''.join([word[0].upper() for word in words if word[0].isalpha()])
    
    return acronym_str


print(acronym(" there's no free lunch - gotta pay yer way. ")) 
print(acronym("Live from New York, it's Saturday Night!"))     

# remove shorter
def removeShorterStrings(strings, min_length):
   
    filtered_strings = [s for s in strings if len(s) >= min_length]
    
    return filtered_strings


print(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)) 
print(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3)) 

