def edge_ngram(contact):
    return [contact[0:idx] for idx in range(1, len(contact) + 1)]

contact_indices = {}
def add(contact):
    for token in edge_ngram(contact):
        contact_indices[token] =contact_indices.get(token, 0) + 1

def find(name):
    return contact_indices.get(name, 0)

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add(contact)
    elif op == 'find':
        print(find(contact))  
