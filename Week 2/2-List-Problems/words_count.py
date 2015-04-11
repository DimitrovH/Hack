a = input("Enter a word: ")

n = input("Enter a number: ")
n = int(n)

counter = 0
word_list = []

while counter < n:
	word = input("Enter a word:")
	word_list += [word]
	counter += 1

counter_word = 0

for word in word_list:
	if word == a:
		counter_word += 1

print(a + " was found " + str(counter_word) + " times.")
