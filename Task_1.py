"""
Задание 1.
X красных машин и Y белых стоят в одном ряду Напишите программу,
которая выдаст, как нужно расположить красные и белые машины, чтобы рядом с
каждой красной стояла хотя бы одна белая, а рядом с каждой белой — хотя бы одна красная.
На вход подаются два числа - кол-во красных машин X и кол-во белых машин Y.
В ответе выведите какую-нибудь строку, в которой будет равно X символов “R” (красные машины)
и Y символов “W” (белые машины), удовлетворяющую условию задачи. Пробелы между символами выводить
не нужно. Если расставить машины согласно условию задачи невозможно, выведите строку “Нет решения”.

"""

def parking(red_cars:int, white_cars:int) -> str:
	res = ''
	if (red_cars > 2 * white_cars ) or (white_cars > 2 * red_cars):
		return 'Нет решения'

	if red_cars >= white_cars:
		diff = red_cars - white_cars
		for _ in range(diff):
			res += 'RWR'

		for _ in range(white_cars - diff):
			res += 'RW'
	else:
		diff = white_cars - red_cars
		for _ in range(diff):
			res += 'WRW'

		for _ in range(red_cars - diff):
			res += 'WR'

	return res


red, white = map(int, input('Введите кол-во красных и белых машин (через пробел): ').split())
print(f'Кол-во красных машин: {red}, белых: {white}')

print(parking(red, white))
