import time


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

#------ OLD ------#

# for name_1 in names_1:
#   for name_2 in names_2:
#       if name_1 == name_2:
#          duplicates.append(name_1)

#------ NEW ------#
for n in names_1:
    if n in names_2:
        duplicates.append(n)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")


print (f"runtime: {end_time - start_time} seconds")


# Original Runtimes = 5.077877521514893 seconds
# Original Runtimes = 4.85344386100769 seconds

# New Runtimes = 0.7262749671936035 seconds
# New Runtimes = 0.7247662544250488 seconds