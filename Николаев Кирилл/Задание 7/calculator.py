# Строковый калькулятор

import re, sys, math

def calculate(expression):

	parsed = []

	def parser(x):
		if len(x) > 0:
			if x[0] in "(+-*/^v).":
				parsed.append(x[0])
				parser(x[1:])
			elif x[0].isdigit:
				parsed.append(re.findall('\d+', x)[0])
				x = x.replace(re.findall('\d+', x)[0], '', 1)
				parser(x)



	def calc(x):

		if x[0] == '(' and x[-1] == ')':
			x = x[1:-1]

		if '.' in x:
			for ind in range(len(x)):
				if x[ind] == '.':
					x[ind-1], x[ind], x[ind+1] = 'x', 'x', ''.join([x[ind - 1], x[ind], x[ind + 1]])
			x = [i for i in x if i != 'x']

		if '-' in x:
			for ind in range(len(x)):
				if x[ind] == '-':
					if ind == 0:
						x[ind], x[ind + 1] = 'x', str(0 - float(x[ind + 1]))
					elif not x[ind - 1].isdigit():
						x[ind], x[ind + 1] = 'x', str(0 - float(x[ind + 1]))
			x = [i for i in x if i != 'x']

		if '(' in x:
			flag = False
			opening = []
			ind = 0
			length = len(x)
			while ind < length:
				if x[ind] == '(':
					flag = True
					opening.append(ind)
					ind += 1
				elif x[ind] == ')' and flag == True:
					newexpr = x[opening[-1]:ind+1]
					x = x[:opening[-1]] + [str(calc(newexpr))] + x[ind + 1:]
					ind = opening[-1] + 1
					opening = opening[:-1]
					length = len(x)
				else:
					ind += 1
		if '^' in x:
			for ind in range(len(x)):
				if x[ind] == '^':
					x[ind-1], x[ind], x[ind+1] = 'x', 'x', str(float(x[ind - 1]) ** float(x[ind + 1]))
			x = [i for i in x if i != 'x']

		if 'v' in x:
			for ind in range(len(x)):
				if x[ind] == 'v':
					if float(x[ind+1]) < 0:
						print('Обнаружен корень из отрицательного числа ('+str(float(x[ind+1]))+').')
						print('Сначала преобразуем в положительное ('+str(0 - float(x[ind+1]))+').')
						x[ind+1] = str(0-float(x[ind+1]))
					x[ind], x[ind+1] = 'x', str(math.sqrt(float(x[ind+1])))
			x = [i for i in x if i != 'x']

		if '*' in x or '/' in x:
			for ind in range(len(x)):
				if x[ind] == '*':
					x[ind - 1],x[ind],x[ind+1] = 'x', 'x', str(float(x[ind - 1]) * float(x[ind + 1]))
				elif x[ind] == '/':
					x[ind-1], x[ind], x[ind+1] = 'x', 'x', str(float(x[ind - 1]) / float(x[ind + 1]))
			x = [i for i in x if i != 'x']

		if '-' in x or '+' in x:
			for ind in range(len(x)):
				if x[ind] == '-':
					x[ind-1], x[ind], x[ind+1] = 'x', 'x', str(float(x[ind - 1]) - float(x[ind + 1]))
				elif x[ind] == '+':
					x[ind-1], x[ind], x[ind+1] = 'x', 'x', str(float(x[ind - 1]) + float(x[ind + 1]))
			x = [i for i in x if i != 'x']

		return x[0]

	try:           # Универсальная проверка на дурака
		parser(expression)
		solution = calc(parsed)
		if solution == '(' or ')':
			outputstr = 'Неверное выражение, попробуйте ещё.'
		else:
			outputstr = 'Ответ: ' + str(solution)
	except:
		outputstr = 'Неверное выражение, попробуйте ещё.'
		
	return outputstr