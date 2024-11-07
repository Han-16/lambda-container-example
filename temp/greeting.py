import os
from datetime import datetime

def print_greeting():
    print("Greeting is called")
    store_current_time()

def store_current_time():
    output_dir = './output'
    os.makedirs(output_dir, exist_ok=True)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 파일 경로 및 시간 저장
    with open(os.path.join(output_dir, 'current_time.txt'), 'w') as file:
        file.write(current_time)

def read_current_time():
    with open('./output/current_time.txt', 'r') as file:
        return file.read()