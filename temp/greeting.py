import os
from datetime import datetime

def print_greeting():
    print("Greeting is called")
    store_current_time()

def store_current_time():
    output_dir = '/tmp'
    
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(os.path.join(output_dir, 'current_time.txt'), 'w') as file:
        file.write(current_time)

def read_current_time():
    with open('/tmp/current_time.txt', 'r') as file:
        return file.read()