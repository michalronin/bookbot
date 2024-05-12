def main():
    report("books/frankenstein.txt")


def count_words(str):
    words = str.split()
    return len(words)


def count_letters(str):
    lowered = str.lower()
    result = {}
    for c in lowered:
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1
    return result


def sort_on(dict):
    return dict["count"]


def convert_to_list(dict):
    result = []
    for key in dict:
        if key.isalpha():
            result.append({"name": key, "count": dict[key]})
    result.sort(reverse=True, key=sort_on)
    return result


def report(file):
    with open(file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_count = convert_to_list(count_letters(file_contents))
        print(f"--- Begin report of {file} ---")
        print(f"{word_count} words found in the document")
        print("")

        for letter in letter_count:
            print(f"The {letter["name"]} character was found {letter["count"]} times")


main()
