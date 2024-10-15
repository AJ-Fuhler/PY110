def swap_name(name):
    split_name = name.split()
    last_name = split_name[-1]
    first_name = ' '.join(split_name[:-1])

    return f'{last_name}, {first_name}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True