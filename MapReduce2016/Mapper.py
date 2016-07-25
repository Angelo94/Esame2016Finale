#!/usr/bin/python
import fileinput

indexNazione = 2
indexCheckIn = 4
indexImporto = 6

for line in fileinput.input():
  values = line.split(';')
  nazione = values[indexNazione]
  CheckIn = values[indexCheckIn]
  Importo = values[indexImporto]
  if(values[indexCheckIn].split('-')[0] == '2016'):
  	print(('{0}\t{1}'.format(nazione, Importo)).replace("\n",""))
