from PIL import Image

fin = open('sample', 'r')

# from stackoverflow: https://stackoverflow.com/questions/1574678/efficient-way-to-convert-strings-from-split-function-to-ints-in-python
mona = [int(x) for x in fin.read().replace(';', '').replace('\n', ' ').split(' ')]
fin.close()

mona = Image.frombytes('L', (18,29), bytes(mona))
mona.show()