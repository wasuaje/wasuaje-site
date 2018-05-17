# No olvidemos importar nuestros modulos
import time
import logging
# Configuracion basica del log
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    filename='output.log',
                    level=logging.DEBUG)
# Handler: escribe los mensajes a sys.etderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# configura un formato para la consola
formatter = logging.Formatter(
    '%(asctime)s %(levelname)-8s: %(message)s')
# le avisamos a la consola que formateador usar
console.setFormatter(formatter)
# le agregamos el handler al logger principal
logging.getLogger('').addHandler(console)
# comenzamos jugar
logging.info('Inicio de mi programa')
# agreguemos un tiempo para observar mejor el log
time.sleep(2)
# probamos con una advertencia
# Nota que queda de nuestro lado establecer la severidad del log
logging.warn('Una advertencia')

a = 'a string'
try:
    b = a + 1
except TypeError as e:
    # combinemos nuestro mensaje de error con la salida del interprete
    logging.error('OH! Ha ocurrido un error: {}'.format(e))

# sigamos probando como funciona esto!
if isinstance(a, str):
    logging.fatal(
        'Huston tenemos un problema! No podemos sumar strings y enteros')

time.sleep(2)
# fin de la diversion
logging.info('Fin de la diversion (por ahora)')
