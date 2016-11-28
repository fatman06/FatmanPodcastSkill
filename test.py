from lambda_function import *
from test_event import *
from zipfile import *

x = test_event_obj()
print(lambda_handler(x,None))

with ZipFile(getVersion() + '.zip', 'w') as myzip:
    myzip.write('lambda_function.py')
    myzip.write('alexa.py')
    myzip.write('podcast.py')
    myzip.write('podcast_map.py')

