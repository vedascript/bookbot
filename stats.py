def count_words(content):
    num_words = content.split();
    return len(num_words) ;


def count_characters(book_content):
    dictionary = {};

    for character in book_content:
         char = character.lower();

         if(char in dictionary):
            dictionary[char] += 1;   
         else:
            dictionary[char] = 1;

    return dictionary;           

def sort_dictionary(dictionary):
    char_dict_list = [];

    for key in dictionary:
        obj={"char":key , "num": dictionary[key]};
        char_dict_list.append(obj);


    char_dict_list.sort(key=lambda x:x['num'],reverse=True);
    return char_dict_list;
