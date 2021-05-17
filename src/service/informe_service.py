from flask import abort
from ..repository import InformeRepository
from ..util.web_util import to_date
from ..util.web_util import add_wrapper

class InformeService:

    def get_cantidad_procesos(self, informe_repository: InformeRepository, idservicio):
        print('------------ SERVICIO SELECCIONADO ----', idservicio, '----------------')
        procesos = {}
        data = informe_repository.get_cantidad_procesos_bd(idservicio)
        for result in data:
            print('------------ CANTIDAD DE PROCESOS ----', result, '----------------')
            procesos[result[1]] = {
                'cantidad': result[0],
                'fase': result[1]
            }
        return procesos

    def get_cliente_producto(self, informe_repository: InformeRepository, datos):
        response = {}
        pieLeyendaData = []
        pieChartData = []
        dataTable = []
        columnsTable = [
            {
                'label': 'Factura',
                'prop': 'id'
            },
            {
                'label': 'Producto',
                'prop': 'producto'
            },
            {
                'label': 'Cliente',
                'prop': 'cliente'
            },
            {
                'label': 'Cantidad',
                'prop': 'cantidad'
            },
            {
                'label': 'Precio Venta',
                'prop': 'precio'
            },
            {
                'label': 'Total',
                'prop': 'total'
            }
        ]

        # CONSULTA DE INFORMACION

        data = informe_repository.get_cantidad_cliente_producto(datos)
        for result in data:
            pieLeyendaData.append(result[1].capitalize())
            pieChartData.append(
                {
                    'value': int(result[0]),
                    'name': result[1].capitalize()
                }
            )

        data = informe_repository.get_cliente_producto_bd(datos)
        for result in data:
            dataTable.append(
                {
                    'id': result[0],
                    'producto': result[1],
                    'cliente': result[2],
                    'cantidad': float(result[3]),
                    'precio': float(result[4]),
                    'total': float(result[5]),
                    'fecha': result[6]
                }
            )
        
        # SE ESTRUCTURA EL OBJETO JSON DE RESPUESTA

        response = {
            'title': 'Cliente',
            'leyenda': pieLeyendaData,
            'datos': pieChartData,
            'columns': columnsTable,
            'data': dataTable
        }
        return response

    def get_producto_cliente(self, informe_repository: InformeRepository, datos):
        response = {}
        pieLeyendaData = []
        pieChartData = []
        dataTable = []
        columnsTable = [
            {
                'label': 'Factura',
                'prop': 'id'
            },
            {
                'label': 'Cliente',
                'prop': 'cliente'
            },
            {
                'label': 'Productos',
                'prop': 'producto'
            },
            {
                'label': 'Cantidad',
                'prop': 'cantidad'
            },
            {
                'label': 'Precio Venta',
                'prop': 'precio'
            },
            {
                'label': 'Total',
                'prop': 'total'
            },
            {
                'label': 'Fecha',
                'prop': 'fecha'
            }
        ]

        # CONSULTA DE INFORMACION

        data = informe_repository.get_cantidad_producto_cliente(datos)
        for result in data:
            pieLeyendaData.append(result[1].capitalize())
            pieChartData.append(
                {
                    'value': int(result[0]),
                    'name': result[1].capitalize()
                }
            )

        data = informe_repository.get_producto_cliente_bd(datos)
        for result in data:
            dataTable.append(
                {
                    'id': result[0],
                    'cliente': result[1],
                    'producto': result[2],
                    'cantidad': float(result[3]),
                    'precio': float(result[4]),
                    'total': float(result[5]),
                    'fecha': result[6],
                    'table': 'cliente'
                }
            )
        
        # SE ESTRUCTURA EL OBJETO JSON DE RESPUESTA

        response = {
            'title': 'Producto',
            'leyenda': pieLeyendaData,
            'datos': pieChartData,
            'columns': columnsTable,
            'data': dataTable
        }
        return response
    
    def get_cliente_vendedor(self, informe_repository: InformeRepository, datos):
        response = {}
        pieLeyendaData = []
        pieChartData = []
        dataTable = []
        columnsTable = [
            {
                'label': 'Factura',
                'prop': 'id'
            },
            {
                'label': 'Vendedor',
                'prop': 'vendedor'
            },
            {
                'label': 'Cliente',
                'prop': 'cliente'
            },
            {
                'label': 'Cantidad',
                'prop': 'cantidad'
            },
            {
                'label': 'Total',
                'prop': 'total'
            },
            {
                'label': 'Fecha',
                'prop': 'fecha'
            }
        ]

        # CONSULTA DE INFORMACION

        data = informe_repository.get_cantidad_cliente_vendedor(datos)
        for result in data:
            pieLeyendaData.append(result[1].capitalize())
            pieChartData.append(
                {
                    'value': int(result[0]),
                    'name': result[1].capitalize()
                }
            )

        data = informe_repository.get_cliente_vendedor_bd(datos)
        for result in data:
            dataTable.append(
                {
                    'id': result[0],
                    'vendedor': result[1],
                    'cliente': result[2],
                    'cantidad': int(result[3]),
                    'total': float(result[4]),
                    'fecha': result[5]
                }
            )
        
        # SE ESTRUCTURA EL OBJETO JSON DE RESPUESTA

        response = {
            'title': 'Cliente',
            'leyenda': pieLeyendaData,
            'datos': pieChartData,
            'columns': columnsTable,
            'data': dataTable
        }
        return response