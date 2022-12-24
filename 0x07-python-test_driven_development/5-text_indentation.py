#!/usr/bin/python3
def text_indentation(text):
    """
    :param text: a string of text
    to be printed with 2 new lines after '.', '?', and ':'
    unit tests located in tests/5-text_indentation.txt
    :return: Nothing
    """
    if not isinstance(text, str):
        raise TypeError(" text must be a string")
    st = ''
    for i in text:
        st += i
        if i in (':', '.', '?'):
            st += '\n\n'
    print(st, end='')
