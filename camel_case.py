def to_camel_case(text):
    if len(text) == 0:
        return text
    split_ = text.replace('-', " ").replace('_', " ")
    split_ = split_.split()
    return split_[0] + ''.join(i.capitalize() for i in split_[1:])

print(to_camel_case('hello-what-are'))