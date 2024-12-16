import os

for file in os.listdir():
    pre, ext = os.path.splitext(file)
    if ext == '.html':
        os.rename(file, f"{pre}.php")