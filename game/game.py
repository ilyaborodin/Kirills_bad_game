import pygame
import sys


def kirill_polniy_dibil():
	STEK = []
	n = 3


	def step1():
		if PLAY_FIELD[1][1] == 0:
			PLAY_FIELD[1][1] = 'O'
			STEK.append(1)
		else:
			PLAY_FIELD[0][0] = 'O'
			STEK.append(2)


	def step2():
		if STEK[0] == 1:
			if (PLAY_FIELD[2][0] and PLAY_FIELD[0][2]) or (PLAY_FIELD[0][2] and PLAY_FIELD[0][1]) or (
					PLAY_FIELD[2][0] and PLAY_FIELD[1][0]):
				PLAY_FIELD[0][0] = 'O'
				STEK.append(1)

			elif (PLAY_FIELD[1][2] and PLAY_FIELD[0][2]) or (PLAY_FIELD[2][0] and PLAY_FIELD[2][1]):
				PLAY_FIELD[2][2] = 'O'
				STEK.append(2)

			elif (PLAY_FIELD[0][0] and PLAY_FIELD[2][2]) or (PLAY_FIELD[0][0] and PLAY_FIELD[0][1]) or (
					PLAY_FIELD[2][2] and PLAY_FIELD[1][2]):
				PLAY_FIELD[0][2] = 'O'
				STEK.append(3)

			elif (PLAY_FIELD[0][0] and PLAY_FIELD[1][0]) or (PLAY_FIELD[2][1] and PLAY_FIELD[2][2]):
				PLAY_FIELD[2][0] = 'O'
				STEK.append(4)

			elif PLAY_FIELD[0][0] and PLAY_FIELD[2][0]:
				PLAY_FIELD[1][0] = 'O'
				STEK.append(5)

			elif PLAY_FIELD[0][0] and PLAY_FIELD[0][2]:
				PLAY_FIELD[0][1] = 'O'
				STEK.append(6)

			elif PLAY_FIELD[2][0] and PLAY_FIELD[2][2]:
				PLAY_FIELD[2][1] = 'O'
				STEK.append(7)

			elif PLAY_FIELD[0][2] and PLAY_FIELD[2][2]:
				PLAY_FIELD[1][2] = 'O'
				STEK.append(8)

			elif ((PLAY_FIELD[1][0] and PLAY_FIELD[2][2]) or (PLAY_FIELD[0][1] and PLAY_FIELD[2][2]) or
				  (PLAY_FIELD[1][0] and PLAY_FIELD[0][2]) or (PLAY_FIELD[2][1] and PLAY_FIELD[0][2]) or
				  (PLAY_FIELD[0][1] and PLAY_FIELD[2][0]) or (PLAY_FIELD[1][2] and PLAY_FIELD[2][0]) or
				  (PLAY_FIELD[2][1] and PLAY_FIELD[0][0]) or (PLAY_FIELD[1][2] and PLAY_FIELD[0][0])
			):
				if (PLAY_FIELD[2][1] and PLAY_FIELD[0][0]) or (PLAY_FIELD[1][2] and PLAY_FIELD[0][0]):
					PLAY_FIELD[2][2] = 'O'
					STEK.append(9)
				else:
					PLAY_FIELD[0][0] = 'O'
					STEK.append(10)
			elif ((PLAY_FIELD[1][0] and PLAY_FIELD[0][1]) or (PLAY_FIELD[0][1] and PLAY_FIELD[1][2]) or
				  (PLAY_FIELD[1][2] and PLAY_FIELD[2][1]) or (PLAY_FIELD[2][1] and PLAY_FIELD[1][0])
			):
				# Можно переделать elif в простой else без длинного условия!
				PLAY_FIELD[0][0] = 'O'
				STEK.append(11)

		if STEK[0] == 2:
			if PLAY_FIELD[0][1] or PLAY_FIELD[2][1]:
				if not PLAY_FIELD[0][1]:
					PLAY_FIELD[0][1] = 'O'
					STEK.append(12)
				else:
					PLAY_FIELD[2][1] = 'O'
					STEK.append(13)
			elif PLAY_FIELD[1][0] or PLAY_FIELD[1][2]:
				if not PLAY_FIELD[1][0]:
					PLAY_FIELD[1][0] = 'O'
					STEK.append(14)
				else:
					PLAY_FIELD[1][2] = 'O'
					STEK.append(15)
			elif PLAY_FIELD[2][0] or PLAY_FIELD[0][2]:
				if not PLAY_FIELD[2][0]:
					PLAY_FIELD[2][0] = 'O'
					STEK.append(16)
				else:
					PLAY_FIELD[0][2] = 'O'
					STEK.append(17)
			elif PLAY_FIELD[2][2]:
				PLAY_FIELD[0][2] = 'O'
				STEK.append(18)


	def step3():
		global END
		if STEK[1] == 1:
			if not PLAY_FIELD[2][2]:
				PLAY_FIELD[2][2] = 'O'
				# 	Проиграл
			elif PLAY_FIELD[0][2] and PLAY_FIELD[2][2]:
				PLAY_FIELD[1][2] = 'O'
				STEK.append(1)
			else:
				PLAY_FIELD[2][1] = 'O'
				STEK.append(2)
		elif STEK[1] == 2:
			if not PLAY_FIELD[0][0]:
				PLAY_FIELD[0][0] = 'O'
				# 	Проиграл
			elif PLAY_FIELD[0][2] and PLAY_FIELD[0][0]:
				PLAY_FIELD[0][1] = 'O'
				STEK.append(3)
			else:
				PLAY_FIELD[1][0] = 'O'
				STEK.append(4)
		elif STEK[1] == 3:
			if not PLAY_FIELD[2][0]:
				PLAY_FIELD[2][0] = 'O'
				# 	Проиграл
			elif PLAY_FIELD[0][2] and PLAY_FIELD[2][2]:
				PLAY_FIELD[1][2] = 'O'
				STEK.append(5)
			else:
				PLAY_FIELD[0][1] = 'O'
				STEK.append(6)
		elif STEK[1] == 4:
			if not PLAY_FIELD[0][2]:
				PLAY_FIELD[0][2] = 'O'
				# 	Проиграл
			elif PLAY_FIELD[2][2]:
				PLAY_FIELD[1][2] = 'O'
				STEK.append(7)
			else:
				PLAY_FIELD[0][1] = 'O'
				STEK.append(8)
		elif STEK[1] == 5 or STEK[1] == 8:
			if not PLAY_FIELD[1][2]:
				PLAY_FIELD[1][2] = 'O'
				# 	Проиграл
			elif not PLAY_FIELD[1][0]:
				PLAY_FIELD[1][0] = 'O'
				# 	Проиграл
			else:
				PLAY_FIELD[0][1] = 'O'
				STEK.append(9)
		elif STEK[1] == 6 or STEK[1] == 7:
			if not PLAY_FIELD[2][1]:
				PLAY_FIELD[2][1] = 'O'
				# 	Проиграл
			elif not PLAY_FIELD[0][1]:
				PLAY_FIELD[0][1] = 'O'
				# 	Проиграл
			else:
				PLAY_FIELD[1][0] = 'O'
				STEK.append(10)
		elif STEK[1] == 9:
			if not PLAY_FIELD[2][0]:
				PLAY_FIELD[2][0] = 'O'
				STEK.append(12)
			elif not PLAY_FIELD[1][0]:
				PLAY_FIELD[1][0] = 'O'
				STEK.append(11)
		elif STEK[1] == 10 or STEK[1] == 11:
			if not PLAY_FIELD[2][2]:
				PLAY_FIELD[2][2] = 'O'
				# 	Проиграл
			elif (PLAY_FIELD[1][2] and PLAY_FIELD[2][2]) or (PLAY_FIELD[0][1] and PLAY_FIELD[1][0]):
				PLAY_FIELD[0][2] = 'O'
				STEK.append(13)
			elif PLAY_FIELD[0][2] and PLAY_FIELD[2][2]:
				PLAY_FIELD[1][2] = 'O'
				STEK.append(31)
			elif not PLAY_FIELD[2][0]:
				PLAY_FIELD[2][0] = 'O'
				STEK.append(14)
			else:
				PLAY_FIELD[2][1] = 'O'
				STEK.append(30)
		elif STEK[1] == 12:
			if not PLAY_FIELD[0][2]:
				PLAY_FIELD[0][2] = 'O'
				# 	Проиграл
			else:
				PLAY_FIELD[2][0] = 'O'
				STEK.append(15)
		elif STEK[1] == 13:
			if not PLAY_FIELD[2][0]:
				PLAY_FIELD[2][0] = 'O'
				STEK.append(16)
			else:
				PLAY_FIELD[0][2] = 'O'
				STEK.append(17)
		elif STEK[1] == 14:
			if not PLAY_FIELD[2][0]:
				PLAY_FIELD[2][0] = 'O'
				# 	Проиграл
			else:
				PLAY_FIELD[0][2] = 'O'
				STEK.append(18)
		elif STEK[1] == 15:
			if not PLAY_FIELD[0][2]:
				PLAY_FIELD[0][2] = 'O'
				STEK.append(19)
			else:
				PLAY_FIELD[2][0] = 'O'
				STEK.append(20)
		elif STEK[1] == 16:
			if not PLAY_FIELD[1][0]:
				PLAY_FIELD[1][0] = 'O'
				STEK.append(21)
			else:
				PLAY_FIELD[1][2] = 'O'
				STEK.append(22)
		elif STEK[1] == 17:
			if not PLAY_FIELD[0][1]:
				PLAY_FIELD[0][1] = 'O'
				STEK.append(23)
			else:
				PLAY_FIELD[2][1] = 'O'
				STEK.append(24)
		else:
			if not PLAY_FIELD[0][1]:
				PLAY_FIELD[0][1] = 'O'
			# 	Проиграл
			else:
				PLAY_FIELD[2][1] = 'O'
				STEK.append(25)


	def step4():
		if STEK[2] == 1:
			if not PLAY_FIELD[1][0]:
				PLAY_FIELD[1][0] = 'O'
				# 	Проиграл
			else:
				draw_random()
		elif STEK[2] == 2:
			if not PLAY_FIELD[0][1]:
				PLAY_FIELD[0][1] = 'O'
				# 	Проиграл
			else:
				draw_random()
		elif STEK[2] == 3:
			if not PLAY_FIELD[2][1]:
				PLAY_FIELD[1][1] = 'O'
				# 	Проиграл
			else:
				draw_random()
		elif STEK[2] == 4:
			if not PLAY_FIELD[1][2]:
				PLAY_FIELD[1][2] = 'O'
				# 	Проиграл
			else:
				draw_random()
		elif STEK[2] == 5:
			if not PLAY_FIELD[1][0]:
				PLAY_FIELD[1][0] = 'O'
				# 	Проиграл
			else:
				draw_random()
		elif STEK[2] == 6:
			if not PLAY_FIELD[2][1]:
				PLAY_FIELD[2][1] = 'O'
				# 	Проиграл
			else:
				draw_random()
		elif STEK[2] == 7:
			if not PLAY_FIELD[0][1]:
				PLAY_FIELD[0][1] = 'O'
				# 	Проиграл
			else:
				draw_random()
		elif STEK[2] == 8:
			if not PLAY_FIELD[2][1]:
				PLAY_FIELD[2][1] = 'O'
				# 	Проиграл
			else:
				draw_random()
		elif STEK[2] == 9:
			if not PLAY_FIELD[2][1]:
				PLAY_FIELD[2][1] = 'O'
				# 	Проиграл
			elif PLAY_FIELD[2][0]:
				PLAY_FIELD[2][2] = 'O'
			else:
				PLAY_FIELD[2][0] = 'O'
		elif STEK[2] == 10:
			if not PLAY_FIELD[1][2]:
				PLAY_FIELD[1][2] = 'O'
				# 	Проиграл
			elif PLAY_FIELD[2][0]:
				PLAY_FIELD[0][2] = 'O'
			else:
				PLAY_FIELD[2][2] = 'O'
		elif STEK[2] == 11:
			if not PLAY_FIELD[1][2]:
				PLAY_FIELD[1][2] = 'O'
				# 	Проиграл
			elif not PLAY_FIELD[2][2]:
				PLAY_FIELD[2][2] = 'O'
			else:
				PLAY_FIELD[2][1] = 'O'
		elif STEK[2] == 12:
			if not PLAY_FIELD[0][2]:
				PLAY_FIELD[0][2] = 'O'
				# 	Проиграл
			else:
				PLAY_FIELD[1][0] = 'O'
		elif STEK[2] == 13 or STEK[2] == 14 or STEK[2] == 31 or STEK[2] == 30:
			if not PLAY_FIELD[2][0]:
				PLAY_FIELD[2][0] = 'O'
			else:
				draw_random()
		elif STEK[2] == 15:
			if not PLAY_FIELD[1][0]:
				PLAY_FIELD[1][0] = 'O'
			else:
				PLAY_FIELD[1][2] = 'O'
		elif STEK[2] == 16 or STEK[2] == 17:
			draw_random()
		elif STEK[2] == 18:
			if not PLAY_FIELD[0][1]:
				PLAY_FIELD[0][1] = 'O'
			else:
				PLAY_FIELD[2][1] = 'O'
		else:
			draw_random()


	def draw_random():
		for i in range(n):
			for j in range(n):
				if not PLAY_FIELD[i][j]:
					PLAY_FIELD[i][j] = 'O'
					break


	def victory_check(mas, sign):
		zeroes = 0
		for row in mas:
			zeroes += row.count(0)
			if row.count(sign) == 3:
				return sign
		for col in range(3):
			if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
				return sign
		if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
			return sign
		if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
			return sign
		if zeroes == 0:
			return 'Piece'
		return False


	pygame.init()
	size_block = 100
	margin = 15
	width = heigth = size_block * 3 + margin * 4
	size_window = (width, heigth)
	screen = pygame.display.set_mode(size_window)
	pygame.display.set_caption("Крестики-нолики")

	black = (0, 0, 0)
	red = (255, 0, 0)
	green = (0, 255, 0)
	white = (255, 255, 255)
	PLAY_FIELD = [[0] * 3 for i in range(3)]
	query = 0
	game_over = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)
			elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
				x_mouse, y_mouse = pygame.mouse.get_pos()
				col = x_mouse // (size_block + margin)
				row = y_mouse // (size_block + margin)
				if PLAY_FIELD[row][col] == 0:

					if query % 2 == 0:
						PLAY_FIELD[row][col] = 'X'
					else:
						if query == 1:
							step1()
						elif query == 3:
							step2()
						elif query == 5:
							step3()
						elif query == 7:
							step4()
					query += 1
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_over = False
				PLAY_FIELD = [[0] * 3 for i in range(3)]
				query = 0
				screen.fill(black)

		if not game_over:
			for row in range(3):
				for col in range(3):
					if PLAY_FIELD[row][col] == 'X':
						color = red
					elif PLAY_FIELD[row][col] == 'O':
						color = green
					else:
						color = white
					x = col * size_block + (col + 1) * margin
					y = row * size_block + (row + 1) * margin
					pygame.draw.rect(screen, color, (x, y, size_block, size_block))
					if color == red:
						pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 3)
						pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 3)
					elif color == green:
						pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)
		if query % 2 == 1:
			game_over = victory_check(PLAY_FIELD, 'X')
		else:
			game_over = victory_check(PLAY_FIELD, 'O')

		if game_over:
			screen.fill(black)
			font = pygame.font.SysFont('stxingkai', 80)
			text1 = font.render(game_over, True, white)
			text_rect = text1.get_rect()
			text_x = screen.get_width() / 2 - text_rect.width / 2
			text_y = screen.get_height() / 2 - text_rect.height / 2
			screen.blit(text1, [text_x, text_y])

		pygame.display.update()

kirill_polniy_dibil()
