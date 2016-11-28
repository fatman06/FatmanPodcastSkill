from lambda_function import *
from test_event import *
from zipfile import *

x = test_event_obj()

print("\n")
print(lambda_handler(x,None))
print("\033[92m\nNO Guest Successful\n\033[0m")
y = test_event_obj_guest()
print("\n")
print(lambda_handler(y,None))
print("\033\n[92mWith Guest Successful\n\033[0m")
print("Packaging Modules")
with ZipFile(getVersion() + '.zip', 'w') as myzip:
    myzip.write('lambda_function.py')
    myzip.write('alexa.py')
    myzip.write('podcast.py')
    myzip.write('podcast_map.py')

