import os

def count_files(folder_path):
    """Count .py files in a folder"""
    # ABSOLUTE PATH from repo root
    repo_root = os.environ.get('GITHUB_WORKSPACE', '.')
    full_path = os.path.join(repo_root, folder_path)
    
    print(f"DEBUG: Checking: {full_path}")
    print(f"DEBUG: Exists? {os.path.exists(full_path)}")
    
    if not os.path.exists(full_path):
        # Try without arrays/ prefix
        alt_path = os.path.join(repo_root, folder_path.replace('arrays/', ''))
        print(f"DEBUG: Trying alt: {alt_path}")
        print(f"DEBUG: Alt exists? {os.path.exists(alt_path)}")
        
        if os.path.exists(alt_path):
            full_path = alt_path
        else:
            print(f"DEBUG: Returning 0 for {folder_path}")
            return 0
    
    try:
        files = os.listdir(full_path)
        print(f"DEBUG: All files: {files}")
        
        py_files = [f for f in files if f.endswith('.py')]
        print(f"DEBUG: .py files: {py_files}")
        print(f"DEBUG: Count: {len(py_files)}")
        
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
    
    print(f"\nFINAL: Total problems: {total}")

if __name__ == "__main__":
    generate_readme()

