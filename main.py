from stats import count_words, count_characters, sort_dictionary;
import sys;

def get_book_test(filePath):
    with open(filePath) as file:
     content = file.read();
     return content;


def main():
    book_paths = sys.argv[1:];
    
    if(len(book_paths) <=0):
        print("Usage: python3 main.py <path_to_book>");
        sys.exit(1);


    content = get_book_test(book_paths[0]); 
    num_words =  count_words(content);
    char_dictionary = count_characters(content);

    print("============ BOOKBOT ============");
    print(f"Analyzing book found at {book_paths[0]}...");
    print("----------- Word Count ----------");
    print(f"Found {num_words} total words");
    print("--------- Character Count -------")

    sorted_dictionary_list =  sort_dictionary(char_dictionary);

    for char_dict in sorted_dictionary_list:
        if(char_dict['char'].isalpha()):
            print(f"{char_dict['char']}: {char_dict['num']}")
        

    print("============= END ===============");    

main();       