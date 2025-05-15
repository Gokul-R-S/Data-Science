import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)  # Ensure project root is included
sys.path.insert(0, os.path.join(project_root, "backend"))  # Add backend
sys.path.insert(0, os.path.join(project_root, "frontend"))  # Add frontend

print("Updated sys.path:", sys.path)
