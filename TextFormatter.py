import typing
import os


def format_text(text: str, max_width: str) -> list[str]:
    """ Justifies the given text to fit within the specified maximum width.
    It uses dynamic programming to determine the optimal way to break the text into lines. 
    Parameters:
     -> text (str): The input text to be justified.
     -> max_width (str): The maximum width of each line. """
    words = text.split()
    n = len(words)
    costs = [float('inf')] * (n + 1)
    costs[n] = 0
    breaks = [0] * n

    def cost(line_length):
        return (int(max_width) - line_length) ** 2

    for i in range(n - 1, -1, -1):
        line_length = -1
        for j in range(i, n):
            line_length += len(words[j]) + 1
            if line_length > int(max_width):
                break
            if costs[i] > costs[j + 1] + cost(line_length):
                costs[i] = costs[j + 1] + cost(line_length)
                breaks[i] = j + 1

    result = []
    i = 0
    while i < n:
        j = breaks[i]
        line = ' '.join(words[i:j])
        result.append(line)
        i = j

    return result


def read_file(archive_path:str) -> str:
    """ Read the text from a specific file.
     -> archive_path (str): the relative path of the file. """
    with open(archive_path, 'rt', encoding='UTF-8') as archive:
        lines = archive.readlines()

    string = ''
    for line in lines:
        line_wo_spaces = line.strip()
        string += line_wo_spaces + ' '

    return string[:(len(string) - 1)]


def write(archive_path: str, text: str) -> None:
    """ Write a specific text in a file.
     -> archive_path (str): the relative path of the file.
     -> text (str): the text to write.  """
    with open(archive_path, 'wt', encoding='UTF-8') as archive:
        archive.write(text)


def delete(archive_path: str) -> None:
    os.remove(archive_path)


def main() -> None:
    """ Main function. """

    print("Hello!")
    archive_path = input("Please provide the relative path of the text file (.txt): ")
    print("What would you like to do?")
    print("1. Read text from the file.")
    print("2. Write text to the file (overwrite).")
    print("3. Justify text.")
    print("4. Delete the file.")
    choice = input("Enter your choice (number): ")

    if choice == "1":
        text = read_file(archive_path)
        print("The text in the file is as follows:", text)

    elif choice == "2":
        input_text = input("What would you like to write?: ")
        write(archive_path, input_text)
        print("Operation successful!")

    elif choice == "3":
        max_width = input("Insert the maximum line length of the justified text (int): ")
        print("Would you like to:")
        print("1. Save the justified text in the same file.")
        print("2. Save the justified text in a new file.")
        save_option = input("Enter your preference (number): ")
        text = read_file(archive_path)
        justified_text = format_text(text, max_width)
        
        if save_option == "1":    # overwrite option
            with open(archive_path, 'wt', encoding='UTF-8') as arch:   
                for lines in justified_text:
                    arch.write(lines + "\n")
            print("Operation successful!")
        elif save_option == "2":  # new file option
            name = input("Please write the path of the new file (with the name of your preference): ")
            with open(name, 'xt', encoding='UTF-8') as new_text_file:
                for lines in justified_text:
                    new_text_file.write(lines + "\n")
            print("Operation successful!")
        else:                     # invalid option
            print("Invalid choice")   

    elif choice == "4":
        print("Are you sure you want to delete the file?")
        print("1. Yes")
        print("2. No")
        delete_option = input("Enter the number: ")
        if delete_option == "1":
            delete(archive_path)
            print("File has been deleted.")
        else:
            print("File has not been deleted.")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()