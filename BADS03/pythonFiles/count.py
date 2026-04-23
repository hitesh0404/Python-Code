import ast
import os
from pathlib import Path

class DefinitionCounter(ast.NodeVisitor):
    def __init__(self):
        self.function_count = 0
        self.class_count = 0
        self.method_count = 0

    def visit_FunctionDef(self, node):
        # Counts both functions and methods. Differentiation is handled below.
        self.function_count += 1
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        # Handle async functions as well
        self.function_count += 1
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.class_count += 1
        # Temporarily store the current function count to find methods within the class
        initial_func_count = self.function_count
        self.generic_visit(node)
        # Methods are FunctionDefs defined within a ClassDef.
        self.method_count += (self.function_count - initial_func_count)

def count_definitions_in_file(filename):
    with open(filename, 'r', encoding='ISO-8859-1') as f:
        tree = ast.parse(f.read(), filename=filename)
    counter = DefinitionCounter()
    counter.visit(tree)
    # Total functions is all function definitions minus those that are methods
    total_functions = counter.function_count - counter.method_count
    return total_functions, counter.class_count, counter.method_count

# Example usage for a single file:
# Replace 'your_file.py' with the path to your Python file
file_path = '/Library/Frameworks/Python.framework/Versions/3.10/bin/python3' 
if os.path.exists(file_path):
    functions, classes, methods = count_definitions_in_file(file_path)
    print(f"File: {file_path}")
    print(f"Total top-level functions: {functions}")
    print(f"Total classes: {classes}")
    print(f"Total methods inside classes: {methods}")
else:
    print(f"Error: {file_path} not found.")

