import random as rand

list=(1,2)
noun=["my","your","his","her","its","our"]

def capitalize(string):
    return string.capitalize()

def get_determiner(quantity):
    if quantity==1:
        determiners1 = ["a","an","the","this","my","that","any","some","each","every","either","neither","much","many","little","both","one","two","three","certain","another","such","no","own","several"]
        return rand.choice(determiners1)
    else:
        determiners2 = ["the","these","those","your","his","her","its","our","their","some","any","both","few","several","many","all","most","no","both","other","various","numerous","countless","several","each","either","neither","a couple of","a variety of","lots of","plenty of","dozens of","scores of","multitudes of","a few","several kinds of","different kinds of","multiple","countless"]
        return rand.choice(determiners2)

def get_noun(quantity):
    if quantity==1:
        nouns1 = ["apple","car","dog","city","book","computer","tree","ocean","mountain","friend"]
        return rand.choice(nouns1)
    else:
        nouns2 = ["apples","cars","dogs","cities","books","computers","trees","oceans","mountains","friends"]
        return rand.choice(nouns2)

def get_verb(quantity):
    if quantity==1:
        verbs1 = ["runed","jumps","will swim","read","writes","will speak","listened","creates","wil think","danced"]
        return rand.choice(verbs1)
    else:
        verbs2 = ["had runed","are jumping","will swim","have read","are writing","will speak","had listened","are creating","will think","had danced"]
        return rand.choice(verbs2)

def get_preposition(quantity):
    if quantity == 1:
        prepositions1 = ["in","on","at","by","for","with","about","against","between","during","without","through","over","under","above","below"]
        return rand.choice(prepositions1)
    else:
        prepositions2 = ["in front of","next to","along with","in addition to","out of","due to","instead of","with regard to","in spite of","by means of","in place of","as a result of"]
        return rand.choice(prepositions2)

def get_prepositional_phrase(quantity):
    phrase= (get_preposition(quantity)+" "+get_determiner(quantity)+" "+get_noun(quantity))
    return phrase

def make_sentence(quantity):
    print(f"{capitalize(get_determiner(quantity))} {get_noun(quantity)} {get_verb(quantity)} {get_prepositional_phrase(quantity)}.")

def main():
    make_sentence(1)
    make_sentence(1)
    make_sentence(1)
    make_sentence(2)
    make_sentence(2)
    make_sentence(2)

main()