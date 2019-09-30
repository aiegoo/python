name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.splits()
    for navbar in words:
        counts[navbar] = counts.get(navbar, 0) + 1

bigcount = None
bigword = None
for navbar, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = navbar
        bigcount = count

print(bigword, bigcount)
