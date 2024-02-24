# alwi arfan solin
# 122140197
# Soal 1

def segitiga(n) :
	k = n - 1

	for i in range (0, n) :
		for j in range (0, k) :
			print(end = ' ')

		k = k - 1
		for j in range (0, i + 1) :

			print("* ", end = "")
		print('\r')

n = int(input('Height : ',))
segitiga(n) 