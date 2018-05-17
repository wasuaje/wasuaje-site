# Don't forget to import your modules
import time
import logging
# log basic conf
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S',
                    filename='output.log',
                    level=logging.DEBUG)
# Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter(
    '%(asctime)s %(levelname)-8s: %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# lets play
logging.info('Starting the program')
# time delay to see better how time logging works
time.sleep(2)
# lets test a warning
# Notice: we get to handle the severity of the logs
logging.warn('Showing a warning')

a = 'a string'
try:
    b = a + 1
except TypeError as e:
    # we can combine our own text with the system output
    logging.error('OH! There has been an error: {}'.format(e))

# keep testing this
if isinstance(a, str):
    logging.fatal(
        'Huston we\'ve got a problem cannot sum strings to integers')

time.sleep(2)
# end of the fun
logging.info('End of the fun (by now)')
