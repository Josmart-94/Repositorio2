class producto:
    def _init_(self):
        pass

    def CrearProducto(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def _str_(self) ->str:
        return f"{self.codigo} {self.nombre} {self.precio}"
    
    def ListaProductos(producto):
        for Misproductos in producto:
            print(f"{Misproductos}")