bad_chars=['0x80', '0x81', '0x82', '0x83', '0x84', '0x85', '0x86', '0x87', '0x88', '0x89', '0x8a', '0x8b', '0x8c', '0x8d', '0x8e', '0x8f', '0x90', '0x91', '0x92', '0x93', '0x94', '0x95', '0x96', '0x97', '0x98', '0x99', '0x9a', '0x9b', '0x9c', '0x9d', '0x9e', '0x9f', '0xa0', '0xa1', '0xa2', '0xa3', '0xa4', '0xa5', '0xa6', '0xa7', '0xa8', '0xa9', '0xaa', '0xab', '0xac', '0xad', '0xae', '0xaf', '0xb0', '0xb1', '0xb2', '0xb3', '0xb4', '0xb5', '0xb6', '0xb7', '0xb8', '0xb9', '0xba', '0xbb', '0xbc', '0xbd', '0xbe', '0xbf', '0xc0', '0xc1', '0xc2', '0xc3', '0xc4', '0xc5', '0xc6', '0xc7', '0xc8', '0xc9', '0xca', '0xcb', '0xcc', '0xcd', '0xce', '0xcf', '0xd0', '0xd1', '0xd2', '0xd3', '0xd4', '0xd5', '0xd6', '0xd7', '0xd8', '0xd9', '0xda', '0xdb', '0xdc', '0xdd', '0xde', '0xdf', '0xe0', '0xe1', '0xe2', '0xe3', '0xe4', '0xe5', '0xe6', '0xe7', '0xe8', '0xe9', '0xea', '0xeb', '0xec', '0xed', '0xee', '0xef', '0xf0', '0xf1', '0xf2', '0xf3', '0xf4', '0xf5', '0xf6', '0xf7', '0xf8', '0xf9', '0xfa', '0xfb', '0xfc', '0xfd', '0xfe', '0xff', '0x0']
jmp_esp_pointers=['0x625011af','0x625011bb','0x625011c7','0x625011d3','0x625011df','0x625011eb','0x625011f7','0x62501203','0x62501205']
bad_pointers=[]
good_pointers=[]
bad_chars=[x[2:] for x in bad_chars]
for x in jmp_esp_pointers:
	byte_data=[x[2:4],x[4:6],x[6:8],x[8:]]
	for y in byte_data:
		if y in bad_chars:
			print("Found bad char "+y+" in "+x)
			bad_pointers.append(x)
bad_pointers=list(set(bad_pointers))
for x in bad_pointers:
	if x in jmp_esp_pointers:
		jmp_esp_pointers.remove(x)
good_pointers=jmp_esp_pointers
print("\nAvailable JMP ESP pointers without bad characters are")
print(good_pointers)
