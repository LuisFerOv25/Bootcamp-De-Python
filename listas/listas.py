to_do = ["Me levante a las 6:00",'Entré a trabajar a las 8:00','Sali a las 12:00 a almorzar', 'Entre a trabajar a la 1:00 ', 'Sali del trabajo a las 5:30']
#print(to_do)
numbers = [1,2,3,4,"cinco",6,7,8,9,10]
print(type(numbers))
mix = ["uno",2,3.14,True,[1,2,3]]
#print(len(mix))
#print("primer elemento: ",mix[0])
#print("segundo elemento: ",mix[1])
#print("tercero elemento: ",mix[2])
#print("cuarto elemento: ",mix[3])
#print("quinto elemento: ",mix[-1])   
#print("quinto elemento: ",mix[-1][0]) 
#print(mix[0:2])
#print(mix[:2])
mix.append("Luis")
print(mix)
mix.insert(1,['a','b'])
print(mix)
print(mix.index(['a','b']))
numbers = [1,2,100,90.45,3,4,5]
print(numbers)
print("Mayor:",max(numbers))
print("Menor:",min(numbers))
del numbers[-1] 
print(numbers)
del numbers[:2]
print(numbers)
