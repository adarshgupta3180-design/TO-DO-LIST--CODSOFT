#!/usr/bin/env python3
"""
Professional To-Do List Application Entry Point
Author: Senior Python Developer
"""

import os
import sys

# Ensure the root directory and src directory are in the Python search path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, PROJECT_ROOT)

if __name__ == "__main__":
    from src.main import main
    main()
