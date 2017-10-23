import textwrap
def wrap(string, max_width):
    templst = textwrap.wrap(string,max_width)
    str_edit = " ".join(templst)
    return textwrap.fill(str_edit,max_width)