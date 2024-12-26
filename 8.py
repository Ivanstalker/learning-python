def caeser_cipr(text, shift):
	new_text = ''
	for i in range(len(text)):
		if text[i].isalpha():
			if ord(text[i]) >= 1040:
				base = ord('А') if text[i].isupper() else ord('а')
			else:
				base = ord('A') if text[i].isupper() else ord('a')
			new_text += chr((ord(text[i]) - base + shift) % 26 + base)
		else :
			new_text += text[i]
	return new_text

print(caeser_cipr("Hello World!", 3))
print(caeser_cipr("Бананы!", 3))