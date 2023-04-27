 
import os

# Define project root directory
PROJECT_ROOT = os.getcwd()
# Create necessary directories
os.makedirs(os.path.join(PROJECT_ROOT, 'data', 'streaming'), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, 'data', 'processed'), exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, 'code'), exist_ok=True)

# Create empty files
with open(os.path.join(PROJECT_ROOT, 'data', 'streaming', 'raw_data.txt'), 'w') as f:
    pass
with open(os.path.join(PROJECT_ROOT, 'data', 'processed', 'processed_data.txt'), 'w') as f:
    pass
with open(os.path.join(PROJECT_ROOT, 'code', 'main.py'), 'w') as f:
    pass
with open(os.path.join(PROJECT_ROOT, 'code', 'lambda_function.py'), 'w') as f:
    pass
with open(os.path.join(PROJECT_ROOT, 'code', 'streamlit_app.py'), 'w') as f:
    pass
with open(os.path.join(PROJECT_ROOT, 'code', 'fastapi_app.py'), 'w') as f:
    pass

