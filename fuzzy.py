from fuzzywuzzy import fuzz
Str1 = "united states v. nixon"
Str2 = "Nixon v. United States"
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower())
Token_Sort_Ratio = fuzz.token_sort_ratio(Str1,Str2)


target_sentence = "In the eighteenth century it was often convenient to regard man as a clockwork automaton."

sentences = ["In the eighteenth century it was often convenient to regard man as a clockwork automaton.",
             "in the eighteenth century    it was often convenient to regard man as a clockwork automaton",
             "In the eighteenth century, it was often convenient to regard man as a clockwork automaton.",
             "In the eighteenth century, it was not accepted to regard man as a clockwork automaton.",
             "In the eighteenth century, it was often convenient to regard man as clockwork automata.",
             "In the eighteenth century, it was often convenient to regard man as clockwork automatons.",
             "It was convenient to regard man as a clockwork automaton in the eighteenth century.",
             "In the 1700s, it was common to regard man as a clockwork automaton.",
             "In the 1700s, it was convenient to regard man as a clockwork automaton.",
             "In the eighteenth century.",
             "Man as a clockwork automaton.",
             "In past centuries, man was often regarded as a clockwork automaton.",
             "The eighteenth century was characterized by man as a clockwork automaton.",
             "Very long ago in the eighteenth century, many scholars regarded man as merely a clockwork automaton.",]

print(target_sentence)
for s in sentences:
    print(fuzz.token_sort_ratio(target_sentence, s), ' : ', s)

