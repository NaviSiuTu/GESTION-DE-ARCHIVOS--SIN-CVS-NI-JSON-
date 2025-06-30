def mezclar_diccionarios(dic1, dic2):
    nuevo_dic = dic2.copy()
    nuevo_dic.update(dic1)  # El primero sobrescribe valores si hay claves repetidas
    return nuevo_dic

# Ejemplo:
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
resultado = mezclar_diccionarios(d1, d2)
print(resultado)  # {'b': 2, 'c': 3, 'a': 1}
