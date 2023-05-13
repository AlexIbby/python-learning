# Write your solution here


def find_words(search_term: str):

    matching_words = []
    
    with open(r"words.txt", "r") as all_words:

        for line in all_words:
            line = line.strip()
            
            #starts with *
            if search_term.startswith("*"):
                if line.endswith(search_term[1:]):
                    matching_words.append(line)

            #ends with * 
            if search_term.endswith("*"):
                if line.startswith(search_term[0:-1]):
                    matching_words.append(line)

            #wild card dot
            if "." in search_term:

                match_count = 0
                dot_count = search_term.count(".")
                exact_match_needed = len(search_term) - dot_count

                if len(search_term) != len(line):
                    continue

                if len(search_term) == len(line):

                    for i in range(len(search_term)):

                        if search_term[i] == ".":
                            continue 

                        if search_term[i] == line[i]:
                            match_count += 1

                    if match_count == exact_match_needed:
                        matching_words.append(line)

            #total word
            if search_term == line:
                matching_words.append(line)


    return matching_words




