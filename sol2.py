def main():
    book_path = 'books/frankenstein.txt' # Specify the book path.
    text = readbook(book_path) # This reads the book (using the book function) specified by the book path in the line above.
    num_words = get_num_words(text) # This splits the book into words (using the split function) and applies the number to earlier.
    print(f"{num_words} words found in the document") # Returns a little summary string of words at the end.

#This one actually reads/imports the book as a string
def readbook(path):
    with open(path) as f:
        return f.read()

#This one splits the book into words, and counts the words  
def get_num_words(text):
    words =text.split()
    return len(words)

#Runs the above function like an auto string from the top.
main()

