scores = input("Enter student's scores: ")
scores = int(scores)

if scores <= 50:
	print("Слаб 2")
elif scores >= 51 and scores <= 60:
	print("Среден 3")
elif scores >= 61 and scores <= 70:
	print("Добър 4")
elif scores >= 71 and scores <= 80:
	print("Много добър 5")
elif scores >= 81 and scores < 100:
	print("Отличен 6")
elif scores == 100:
	print("Много отличен 7")