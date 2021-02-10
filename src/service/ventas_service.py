from ..repository import VentasRepository

class VentasService:

    def get_ventas_lista_anos(self, ventas_repository: VentasRepository):
        anos = []
        anos.append({'value': 0, 'label': 'TODOS'})
        data = ventas_repository.get_ventas_lista_anos_bd()
        for result in data:
            anos.append(
                {
                    'value': result[0],
                    'label': result[0],
                }
            )
        return anos
    
    def get_ventas_lista_meses(self, ventas_repository: VentasRepository, ano):
        nombres = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        meses = []
        meses.append({'value': 0, 'label': 'TODOS'})
        data = ventas_repository.get_ventas_lista_meses_bd(ano)
        for result in data:
            meses.append(
                {
                    'value': result[0],
                    'label': nombres[result[0] - 1],
                }
            )
        return meses
    
    def get_ventas_clientes(self, ventas_repository: VentasRepository, ano, mes):
        clientes = []
        clientes.append({'value': 0, 'label': 'TODOS'})
        data = ventas_repository.get_ventas_clientes_bd(ano, mes)
        for result in data:
            clientes.append(
                {
                    'value': result[0],
                    'label': result[1],
                }
            )
        return clientes
    
    def get_ventas_usuarios(self, ventas_repository: VentasRepository, cliente, ano, mes):
        usuarios = []
        usuarios.append({'value': 0, 'label': 'TODOS'})
        data = ventas_repository.get_ventas_usuarios_bd(cliente, ano, mes)
        for result in data:
            usuarios.append(
                {
                    'value': result[0],
                    'label': result[1],
                }
            )
        return usuarios
    
    def get_ventas_productos(self, ventas_repository: VentasRepository, cliente, usuario, ano, mes, producto):
        productos = []
        productos.append({'value': 0, 'label': 'TODOS'})
        data = ventas_repository.get_ventas_productos_bd(cliente, usuario, ano, mes, producto)
        for result in data:
            productos.append(
                {
                    'value': result[0],
                    'label': result[1],
                    'cantidad': result[2],
                    'precio': result[3],
                    'total': result[4],
                }
            )
        return productos

    def get_ventas(self, ventas_repository: VentasRepository,cliente, usuario, ano, mes, producto):
        ventas = []
        data = ventas_repository.get_ventas_bd(cliente, usuario, ano, mes, producto)
        for result in data:
            ventas.append(
                {
                    'ano': result[0],
                    'mes': result[1],
                    'venta': result[2],
                }
            )
        return ventas