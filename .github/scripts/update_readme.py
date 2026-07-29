import os

def count_files(folder_path):
    """Count .py files in a folder"""
    # Debug print
    print(f"DEBUG: Checking folder: {folder_path}")
    
    if not os.path.exists(folder_path):
        print(f"DEBUG: Folder NOT FOUND: {folder_path}")
        return 0
    
    try:
        files = os.listdir(folder_path)
        print(f"DEBUG: Files in {folder_path}: {files}")
        
        py_files = [f for f in files if f.endswith('.py')]
        print(f"DEBUG: .py files: {py_files}, Count: {len(py_files)}")
        
        return len(py_files)
        
    except Exception as e:
        print(f"DEBUG: Error: {e}")
        return 0

def generate_readme():
    topics = [
        ('arrays/hashmap', 'Hash Map'),
        ('arrays/searching', 'Searching'),
        ('arrays/sorting', 'Sorting'),
        ('arrays/two-pointers', 'Two Pointers'),
        ('strings', 'Strings'),
        ('stacks-queues', 'Stacks & Queues'),
        ('sliding-window', 'Sliding Window'),
        ('linked-lists', 'Linked Lists'),
        ('trees', 'Trees'),
        ('graphs', 'Graphs'),
        ('dynamic-programming', 'Dynamic Programming'),
        ('backtracking', 'Backtracking'),
    ]
    
    readme = """# DSA Practice
Daily logic-building problems for Data Engineering interviews.

## Topics

| Topic | Status | Files | Link |
|-------|--------|-------|------|
"""
    
    total = 0
    for folder, name in topics:
        count = count_files(folder)
        total += count
        status = "🟢 Active" if count > 0 else "⚪ Empty"
        link = f"[View]({folder}/)" if count > 0 else "—"
        readme += f"| {folder}/ | {status} | {count} | {link} |\n"
    
    readme += f"""
## Progress

| Topic | Solved |
|-------|--------|
"""
    
    for folder, name in topics:
        count = count_files(folder)
        readme += f"| {name} | {count} |\n"
    
    readme += f"| **Total** | **{total}** |\n"
    
    readme += """
## File Naming Convention
`XX_problem-name.py` (e.g., `01_floor-and-ceil.py`)
"""
    
    with open('README.md', 'w') as f:
        f.write(readme)
    
    print(f"README updated! Total problems: {total}")

if __name__ == "__main__":
    generate_readme()

