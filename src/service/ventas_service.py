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
        tableColumns = [{'label': 'Cliente', 'prop': 'label', 'width': '','width_xs': ''},{'label': 'Cantidad', 'prop': 'cantidad', 'width': '', 'width_xs': ''},
                        {'label': 'Total', 'prop': 'total', 'width': '', 'width_xs': ''}]
        data = ventas_repository.get_ventas_clientes_bd(datos)
        for result in data:
            children.append(
                {
                    'id': result[0],
                    'label': result[1],
                    'cantidad': float(result[2]),
                    'total': float(result[3]),
                }
            )
        tree = {'id': 0, 'label': 'Seleccionar todo', 'children': children, 'total': len(children), 'tablecolumns': tableColumns}
        clientes.append(tree)
        return clientes
    
    def get_ventas_usuarios(self, ventas_repository: VentasRepository, datos):
        usuarios = []
        children = []
        tableColumns = [{'label': 'Cliente', 'prop': 'label', 'width': '','width_xs': ''},{'label': 'Cantidad', 'prop': 'cantidad', 'width': '', 'width_xs': ''},
                        {'label': 'Total', 'prop': 'total', 'width': '', 'width_xs': ''}]
        data = ventas_repository.get_ventas_usuarios_bd(datos)
        for result in data:
            children.append(
                {
                    'id': result[0],
                    'label': result[1],
                    'cantidad': float(result[2]),
                    'total': float(result[3]),
                }
            )
        tree = {'id': 0, 'label': 'Seleccionar todo', 'children': children, 'total': len(children), 'tablecolumns': tableColumns}
        usuarios.append(tree)
        return usuarios
    
    def get_ventas_productos(self, ventas_repository: VentasRepository, datos):
        productos = []
        children = []
        tableColumns = [{'label': 'Producto', 'prop': 'label', 'width': '200','width_xs': ''},{'label': 'Cantidad', 'prop': 'cantidad', 'width': '', 'width_xs': ''},
                        {'label': 'Total', 'prop': 'total', 'width': '', 'width_xs': ''}, {'label': 'Promedio', 'prop': 'precio', 'width': '', 'width_xs': ''}]
        data = ventas_repository.get_ventas_productos_bd(datos)
        for result in data:
            children.append(
                {
                    'id': result[0],
                    'label': result[1],
                    'cantidad': float(result[2]),
                    'precio': float(result[3]),
                    'total': float(result[4]),
                }
            )
        tree = {'id': 0, 'label': 'Seleccionar todo', 'children': children, 'total': len(children), 'tablecolumns': tableColumns}
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