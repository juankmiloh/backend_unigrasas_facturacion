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
        data = ventas_repository.get_ventas_lista_meses_bd(tuple(datos))
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

    def get_ventas_productos(self, ventas_repository: VentasRepository, datos):
        productos = []
        children = []
        tableColumns = [{'label': 'Producto', 'prop': 'label', 'width': '200','width_xs': '200'},{'label': 'Cantidad', 'prop': 'cantidad', 'width': '', 'width_xs': '110'},
                        {'label': 'Total', 'prop': 'total', 'width': '', 'width_xs': '200'}, {'label': 'Promedio', 'prop': 'precio', 'width': '', 'width_xs': '110'}]
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
    
    def get_ventas_clientes(self, ventas_repository: VentasRepository, datos):
        clientes = []
        children = []
        tableColumns = [{'label': 'Cliente', 'prop': 'label', 'width': '','width_xs': '200'},{'label': 'Cantidad', 'prop': 'cantidad', 'width': '', 'width_xs': '110'},
                        {'label': 'Total', 'prop': 'total', 'width': '', 'width_xs': '200'}]
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
        tableColumns = [{'label': 'Vendedor', 'prop': 'label', 'width': '','width_xs': '200'},{'label': 'Cantidad', 'prop': 'cantidad', 'width': '', 'width_xs': '110'},
                        {'label': 'Total', 'prop': 'total', 'width': '', 'width_xs': '200'}]
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

    def get_ventas_ano(self, ventas_repository: VentasRepository, datos):
        ventas = {}
        xAxis = []
        series = []
        data = ventas_repository.get_ventas_ano_bd(datos)
        for result in data:
            xAxis.append(result[0])
            series.append(float(result[1]))

        mayor=series[0]
        pos=0
        for x in range(0, len(series)):
            if series[x] > mayor:
                mayor=series[x]
                pos=x
        
        series[pos] = {
            'value': float(mayor),
            'itemStyle': {
                'color': '#632e76'
            }
        }
        print('--------- series -------------------------')
        print(series)
        print('----------------------------------')

        ventas = {'xAxis': xAxis, 'data': series}
        return ventas
    
    def get_ventas_ano_mes(self, ventas_repository: VentasRepository, datos):
        ventas = []
        data = ventas_repository.get_ventas_ano_mes_bd(datos)
        for result in data:
            ventas.append(
                {
                    'ano': result[0],
                    'mes': result[1],
                    'venta': float(result[2]),
                }
            )
        return ventas