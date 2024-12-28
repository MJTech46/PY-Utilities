import py_compile

# Path to your .py file
source_file = "example.py"  # Replace with your file name

# Compile the .py file to a .pyc file
try:
    py_compile.compile(source_file, cfile=f"{source_file}c")
    print(f"Compiled {source_file} to {source_file}c successfully.")
except Exception as e:
    print(f"Error compiling {source_file}: {e}")
