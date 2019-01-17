
import os
def read_file(filename):
	product = []
	with open (filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name, price])
		print(product)
	return product


#使用者輸入
def user_input(product):
	while True:
		name = input('請輸入商品名稱： ')
		if name == 'q':
			break
		price = input('請輸入商品價格： ')
		price = int(price)
		product.append([name, price])
	print(product)
	return product
def print_product(product):
	for p in product:
		print(p[0], '的價格是： ', p[1])

def write_file(filename, product):
	with open (filename, 'w' , encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in product:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'product.csv'
	if os.path.isfile(filename):
		print('找到檔案了')
		product = read_file(filename)
	else:
		print('找不到檔案')
	product = read_file('product.csv')
	product = user_input(product)
	print_product(product)
	write_file('product.csv', product)

main()