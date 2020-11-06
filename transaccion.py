import json
import uuid

class Transaccion(json.JSONEncoder):

    def __init__(self, dni_cliente, tipo_movimiento, monto_moviemiento, estado, nombre_comercio):

        self.transaccion_id = str(uuid.uuid4())
        self.dni_cliente = dni_cliente
        self.tipo_movimiento = tipo_movimiento
        self.monto_movimiento = monto_moviemiento
        self.estado = estado
        self.nombre_comercio = nombre_comercio


    def toJSON(self):

        return json.dumps(self, default=lambda o:o.__dict__, indent=4)


    def guardar_movimiento(self, transaccion):

        archivo = open(f'./data/{self.transaccion_id}.json', 'w')
        archivo.write(str(transaccion.toJSON()))


    def verificacion_transaccion(self):

        if self.monto_movimiento < 100000:

            return 'El movimiento no requiere justificación'

        else:

            return 'Se debe solicitar documentación que requiera la justificacion del movimiento'