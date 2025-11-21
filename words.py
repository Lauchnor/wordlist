def num_letters(filename):
    f = open(filename, "r")
    count = 0
    for line in f:
        for char in line:
            if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
                count += 1
    f.close()
    return count

assert 
print("Checking assertions.")
