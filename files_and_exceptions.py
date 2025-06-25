def read_file_to_dict(filename):
    d = dict()
    with open(filename, "r") as file:
        contenido = file.read()
        ventas = contenido.split(";")
        for venta in ventas:
            if venta.strip():
                producto, monto = venta.split(":")
                monto = float(monto)
                if producto in d:
                    d[producto].append(monto)
                else:
                    d[producto] = [monto] 
        return d

def process_dict(data):
        for producto, monto in data.items():
            total = sum(monto)
            promedio = total / len(monto)
            print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
        pass
