# setup_project.py
import os

def create_project_structure():
    """Create the initial project directory structure."""
    
    # Define the directory structure
    directories = [
        'data/raw',
        'data/processed',
        'src/data',
        'src/models',
        'src/visualization',
        'notebooks',
        'tests'
    ]
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        # Create __init__.py files in Python package directories
        if directory.startswith('src'):
            init_file = os.path.join(directory, '__init__.py')
            open(init_file, 'a').close()
    
    # Create empty .gitkeep files in data directories
    open('data/raw/.gitkeep', 'a').close()
    open('data/processed/.gitkeep', 'a').close()
    
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
