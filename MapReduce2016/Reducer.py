#!/usr/bin/python
import fileinput

indexNazione = 0
indexImporto = 1
data = {}

for line in fileinput.input():
	values = line.split('\t')
	nazione = values[indexNazione]
	importo = float(values[indexImporto])
	temp = {nazione:importo}
	if nazione in data:
		data[nazione] = data[nazione] + temp[nazione]
	else:
		data.update(temp)
print(data)