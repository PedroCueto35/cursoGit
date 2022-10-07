
li = list(range(1,10))
a = [4,35,"jajajaja"]
nombre = '''Hola mundo
como te llamas
'''
edad = 34.00999
estado = True
dic = {"nombre":"Pedro","apellido":'Lopez',"edad":38}
s = {4,5,'jose','jose',True}
t = 'plata','oro',3.433,('k',322)

n = list(t)

print(n)
print(dic.keys())
print(dic.values())

dic["pais"]="Mexico"
del dic["edad"]

print(dic)
print(len(dic))

#imprime el Tipo de datos
print(type(n))

for i in range(5):
	print("Soooo", i, end="\n")
	print('N00 \t', i)

