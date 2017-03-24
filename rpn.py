#!/usr/bin/env python3

import operator
import statistics

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'mean': statistics.mean,
	'median': statistics.median,
	'stdev': statistics.stdev,
}

stat_operands = ['mean', 'median', 'stdev']


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			if not operand in stat_operands:
				arg2 = stack.pop()
				arg1 = stack.pop()
				operator_fn = OPERATORS[operand]
				result = operator_fn(arg1, arg2)
			else:
				nums = []
				for i in range(0, len(stack)):
					nums.append(stack.pop())
				operator_fn = OPERATORS[operand]
				result = operator_fn(nums)

			x = 0
			if x:
				x = 1
			stack.append(result)
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		print("Result:", result)

if __name__ == '__main__':
	main()
