# TEXT_FILE_PATH = "./books/frankenstein.txt"


def get_words(string):
    return string.split()


def get_chars(string):
    chars = {}
    for char in string:
        less_angry = char.lower()
        if less_angry in chars:
            chars[less_angry] += 1
        else:
            chars[less_angry] = 1
    return chars


def sort_on(dict):
    return dict["num"]


def get_char_list(input_dict):
    output = []
    for char in input_dict:
        if char.isalpha():
            output.append({"character": char, "num": input_dict[char]})
    output.sort(reverse=True, key=sort_on)
    return output


def main():
    try:
        print("Enter the path to your text file")
        print("Example: ~/Documents/MyFancyTextFile.txt")
        TEXT_FILE_PATH = input()
        with open(TEXT_FILE_PATH) as f:
            file_contents = f.read()
            words = get_words(file_contents)
            chars = get_char_list(get_chars(file_contents))
            print("STARTING")
            print(f"{len(words)} words in file")
            for char in chars:
                print(f"'{char['character']}' appears {char['num']} times")
            print("DONE")
    except:
        print("Error!")
        print("Make sure that the path to your text file is correct!")


main()
