python
import os
from dotenv import load_dotenv

load_dotenv()

STREAMING_DIR = os.path.join(os.getcwd(), 'data', 'streaming')
PROCESSED_DIR = os.path.join(os.getcwd(), 'data', 'processed')

def process_data(raw_data):
    # Add business logic here to process raw data
    processed_data = raw_data.upper()
    return processed_data

def save_data(data, file_path):
    with open(file_path, 'a') as f:
        f.write(data)

if __name__ == "__main__":
    # Infinite loop to simulate streaming data
    while True:
        # Read raw data from streaming directory
        with open(os.path.join(STREAMING_DIR, 'raw_data.txt'), 'r') as f:
            raw_data = f.read()
        
        # Process raw data
        processed_data = process_data(raw_data)
        
        # Save processed data to processed directory
        save_data(processed_data, os.path.join(PROCESSED_DIR, 'processed_data.txt'))
