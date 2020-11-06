from transaccion import Transaccion
import json

#El uso de print('----------------------------------------') solo, es por estetica.

def test_creacion_archivo():

    transaccion_a = Transaccion(45990339, 'CONSUMO', 2000, 'RECHAZADO', 'MUSIMUNDO')
    transaccion_b = Transaccion(45990339, 'CONSUMO', 2000, 'APROBADO', 'MUSIMUNDO')
    transaccion_c = Transaccion(30949303, 'CASH_IN', 50000, 'APROBADO', 'PAGOFACIL')

    transaccion_a.guardar_movimiento(transaccion_a)
    transaccion_b.guardar_movimiento(transaccion_b)
    transaccion_c.guardar_movimiento(transaccion_c)


def test_monto_movimiento():

    transaccion_a = Transaccion(45990339, 'CONSUMO', 200000, 'APROBADO', 'DISCO')

    print(transaccion_a.verificacion_transaccion())
    print('---------------------------------------')


def test_json_movimiento():

    transaccion_a = Transaccion(30949303, 'CASH_IN', 500, 'APROBADO', 'PAGOFACIL')

    movimiento_to_dict = json.loads(transaccion_a.toJSON())

    for x,y in movimiento_to_dict.items():

        print(f'Key: {x}, Value: {y}')


test_creacion_archivo()
test_monto_movimiento()
test_json_movimiento()
