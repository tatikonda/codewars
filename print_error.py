def printer_error(s):
    denominator_ = len(s)
    errors = 0
    good_letters='abcdefghijklm'
    for i in s:
        if i not in good_letters:
            errors += 1
    return str(errors) + "/" + str(denominator_)

print(printer_error('abcedfghsjkslkppwerasfelxmzu'))
