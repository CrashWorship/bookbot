import sys

def main(path_to_file: str):
    with open (path_to_file) as f:
        file_contents = f.read()

        # print(file_contents)
        print(len(file_contents.split()))

        character_count = {}

        for char in file_contents:
            char = char.lower()

            if char in character_count:
                character_count[char] += 1
            else:
                character_count.update({char: 1})
            
        character_count_sorted = sorted(character_count.items())

        print(character_count_sorted)


main(sys.argv[1])