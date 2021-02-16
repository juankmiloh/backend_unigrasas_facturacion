from ..repository import VentasRepository

class VentasService:

    def get_ventas_lista_anos(self, ventas_repository: VentasRepository):
        anos = []
        children = []
        data = ventas_repository.get_ventas_lista_anos_bd()
        for result in data:
            children.append(
                {
                    'id': result[0],
                    'label': result[0],
                }
            )
        tree = {'id': 0, 'label': 'Seleccionar todo', 'children': children, 'total': len(children)}
        anos.append(tree)
        return anos
    
    def get_ventas_lista_meses(self, ventas_repository: VentasRepository, datos):
        nombres = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        meses = []
        children = []
        data = ventas_repository.get_ventas_lista_meses_bd(datos)
        for result in data:
            children.append(
                {
                    'id': result[0],
                    'label': nombres[result[0] - 1].upper(),
                }
            )
        tree = {'id': 0, 'label': 'Seleccionar todo', 'children': children, 'total': len(children)}
        meses.append(tree)
        return meses
    
    def get_ventas_clientes(self, ventas_repository: VentasRepository, datos):
        clientes = []
        children = []
        data = ventas_repository.get_ventas_clientes_bd(datos)
        for result in data:
            children.append(
                {
                    'id': result[0],
                    'label': result[1],
                }
            )
        tree = {'id': 0, 'label': 'Seleccionar todo', 'children': children, 'total': len(children)}
        clientes.append(tree)
        return clientes
    
    def get_ventas_usuarios(self, ventas_repository: VentasRepository, datos):
        usuarios = []
        children = []
        data = ventas_repository.get_ventas_usuarios_bd(datos)
        for result in data:
            children.append(
                {
                    'id': result[0],
                    'label': result[1].upper(),
                }
            )
        tree = {'id': 0, 'label': 'Seleccionar todo', 'children': children, 'total': len(children)}
        usuarios.append(tree)
        return usuarios
    
    def get_ventas_productos(self, ventas_repository: VentasRepository, datos):
        productos = []
        children = []
        data = ventas_repository.get_ventas_productos_bd(datos)
        for result in data:
            children.append(
                {
                    'id': result[0],
                    'label': result[1],
                    'cantidad': str(result[2]),
                    'precio': str(result[3]),
                    'total': str(result[4]),
                }
            )
        tree = {'id': 0, 'label': 'Seleccionar todo', 'children': children, 'total': len(children)}
        productos.append(tree)
        return productos

    def get_ventas_ano(self, ventas_repository: VentasRepository, datos):
        ventas = []
        data = ventas_repository.get_ventas_ano_bd(datos)
        for result in data:
            ventas.append(
                {
                    'ano': result[0],
                    'venta': result[1],
                }
            )
        return ventas
    
    def get_ventas_ano_mes(self, ventas_repository: VentasRepository, datos):
        ventas = []
        data = ventas_repository.get_ventas_ano_mes_bd(datos)
        for result in data:
            ventas.append(
                {
                    'ano': result[0],
                    'mes': result[1],
                    'venta': result[2],
                }
            )
        return ventas