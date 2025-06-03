

words_list=["apple","banana","strawberry","orange","tea","coffe","dog"]


def filtered_word(words_l:list[str] , min_length :int)-> list[str]:
     return  [word for word in words_l if len(words_l) >= min_length]

filter_w=filtered_word(words_list, 7)
print(filter_w)



