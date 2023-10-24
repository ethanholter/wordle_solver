file1 = open('sgb-words.txt')
file2 = open('wordle-allowed-guesses.txt')

lines = file1.read().split('\n')
lines.extend(file2.read().split('\n'))
lines = sorted(list(set(lines)))

file3 = open('word-list.txt', 'w')

for line in lines:
    file3.write(f'{line}\n')
