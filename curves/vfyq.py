import sys
import random

def isprime(n):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	r, s = 0, n - 1
	while s % 2 == 0:
		r += 1
		s //= 2
	for _ in range(20):
		a = random.randrange(2, n - 2)
		a = pow(a, s, n)
		if a == 1 or a == n - 1:
			continue
		for _ in range(r - 1):
			a = pow(a, 2, n)
			if a == n - 1:
				break
		else:
			return False
	return True

def tohex(n):
	str = ''
	for i in range(8):
		str += '%02X' % (n % 256)
		n = n // 256
	return str

t = []

def verify_table(filename):
	with open(filename) as f:
		# read table
		while True:
			line = f.readline()
			assert(line)
			if not line.startswith('|-'):
				continue
			for i in range(50):
				line = f.readline()
				assert(line)
				row = line.strip().replace(' ', '').split('|')[1:-1]
				assert(int(row[0]) == i + 1)
				assert(tohex(int(row[1])) == row[2])
				t.append(row[2:])
			break

def verify_sections(filename):
	i = 0
	with open(filename) as f:
		while i < 50:
			# find section #i
			line = f.readline()
			assert(line)
			if line.strip() != '### ' + str(i + 1):
				continue
			# find an entry
			line = f.readline()
			while not line.startswith('```'):
				line = f.readline()
				assert(line)
			# verify seed
			line = f.readline()
			assert(line and line.startswith('seed = 0x'))
			line = line.strip()[len('seed = 0x'):]
			assert(line == t[i][0])
			# verify q
			line = f.readline()
			assert(line and line.startswith('q = '))
			q = int(line[len('q = '):])
			assert(isprime(q))
			# verify a divisor of q - 1
			line = f.readline()
			assert(line and line.startswith(t[i][1]))
			d = int(line.split(' ')[-1])
			nd = int(line.split(' ')[0][1:])
			assert(10**(nd - 1) < d and d < 10**nd)
			assert(isprime(d) == line.startswith('p'))
			assert((q - 1) % d == 0)
			# verify a divisor of q + 1
			line = f.readline()
			assert(line and line.startswith(t[i][2]))
			d = int(line.split(' ')[-1])
			nd = int(line.split(' ')[0][1:])
			assert(10**(nd - 1) < d and d < 10**nd)
			assert(isprime(d) == line.startswith('p'))
			assert((q + 1) % d == 0)
			# next section
			i = i + 1

if __name__ == '__main__':
	verify_table(sys.argv[1])
	verify_sections(sys.argv[1])
