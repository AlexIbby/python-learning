# Problem


# Given a non-empty string like "Code" return a string like "CCoCodCode".


# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
    second = 1
    new_str = ""
    for letter in str:
        added = str[0:second]
        new_str = new_str + added
        second += 1
    return new_str
