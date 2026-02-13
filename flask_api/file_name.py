import os

def get_pretty_names(folder_path, split_char, chars_to_remove=None, remove_after_char=None):
    # split_name_collections = []
    # folder_path = input("Folder name: ")
    entries = os.scandir(folder_path)
    for entry in entries:
        if os.path.isfile(entry):
            print(entry.name)
            char_removed_name = remove_characters(entry.name, chars_to_remove)
            cleaned_name = clean_name(char_removed_name, remove_after_char, split_char)
            # split_name_collections.append(cleaned_name)            
            print(f"{entry.path} -> {os.path.join(folder_path, cleaned_name + get_file_extension(entry.name))}")
            os.rename(entry.path, os.path.join(folder_path, cleaned_name + get_file_extension(entry.name)))

    # print(split_name_collections)

def get_file_extension(file_name):
    return os.path.splitext(file_name)[1]

def remove_characters(name, chars_to_remove):
    """
    Remove specified characters from a string.

    Args:
        name (str): The input string from which characters will be removed.
        chars_to_remove (str): A comma-separated string of characters to remove from the input string.
                               If empty or None, the original string is returned unchanged.

    Returns:
        str: The input string with all specified characters removed.

    Examples:
        >>> remove_characters("hello-world", "-")
        "helloworld"
        >>> remove_characters("a,b,c,d", "a,c")
        "b,d"
        >>> remove_characters("test", "")
        "test"
    """
    if not chars_to_remove:
        return name
    chars_array = chars_to_remove.split(',')
    for char in chars_array:
        name = name.replace(char.strip(), '')
    return name

def clean_name(name, remove_after_char, split_char):
    name = name.split(remove_after_char)[0].strip()
    name_parts = name.split(split_char)
    return '-'.join(name_parts)


# get_pretty_names('D:\\Music\\New - Copy', '-', '@', '(')