rows = 5
asterisk_count = 1
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * asterisk_count)
    asterisk_count += 2