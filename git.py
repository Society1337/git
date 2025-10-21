import os
import random

try:
    NUM_COMMITS = int(input("Enter the number of commits to create: "))
except ValueError:
    print("Please enter a valid integer for the number of commits.")
    exit(1)

try:
    year = int(input("Enter the year for the commits (e.g., 2024): "))
except ValueError:
    print("Please enter a valid year.")
    exit(1)

file_path = 'test.txt'
with open(file_path, 'a') as file:
    file.write('Initial commit\n')
os.system('git add test.txt')
os.system('git commit -m "Initial commit"')

for i in range(NUM_COMMITS):
    month = random.randint(1, 12)
    day_offset = i % 28 + 1  

    commit_date_str = f"{year}-{month:02d}-{day_offset:02d} 12:00:00"

    with open(file_path, 'a') as file:
        file.write(f'Commit for {commit_date_str}\n')
    
    try:
        os.system('git add test.txt')
        os.system(f'git commit --date="{commit_date_str}" -m "Commit #{i+1}"')
    except Exception as e:
        print(f"Error during commit {i+1}: {e}")

try:
    os.system('git push -u origin main')
except Exception as e:
    print(f"Error pushing to repository: {e}")


