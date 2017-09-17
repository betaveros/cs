def print_td(i, r, g, b):
	# https://www.w3.org/TR/AERT#color-contrast
	if 299 * r + 587 * g + 114 * b < 255 * 500:
		print('<td class="color" style="background-color: rgb({r}, {g}, {b}); color: white;">{i:3}</td>'.format(**locals()))
	else:
		print('<td class="color" style="background-color: rgb({r}, {g}, {b}); color: black;">{i:3}</td>'.format(**locals()))

rgb_scale = [0, 95, 135, 175, 215, 255]

i = 0

# print('<style>* { text-align: right; font-family: monospace; font-weight: bold; white-space: pre; }</style>')

print('<table>')

for h in [128, 255]:
	print('<tr>')
	for r in range(2):
		for g in range(2):
			for b in range(2):
				print_td(i, h * r, h * g, h * b)
				i += 1
	print('</tr>')

for r in range(6):
	for g in range(6):
		print('<tr>')
		for b in range(6):
			print_td(i, rgb_scale[r], rgb_scale[g], rgb_scale[b])
			i += 1
		print('</tr>')

for row in range(4):
	print('<tr>')
	for col in range(6):
		gray = (4 * row + col) * 10 + 8;
		print_td(i, gray, gray, gray);
		i += 1
	print('</tr>')

print('</table>')
