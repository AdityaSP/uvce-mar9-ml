li = ['Please help Jeff Geerling by spreading the word about this book on Twitter!', 'The suggested tweet for this book is:', 'I just purchased @Ansible4DevOps by @geerlingguy on @leanpub -', 'https://leanpub.com/ansible-for-devops #ansible']

print("Has", sum([ len([ s for s in line.split() if len(s)> 3]) for line in li]), "words")


word_count = 0
for line in li:
    word_count += len(line.split())
    
print("Has ", word_count, "words")

