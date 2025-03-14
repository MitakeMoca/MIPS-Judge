import random
import os
import subprocess
import sys

test_num = 5

def generate_input():
    # N = random.randint(1, 100)
    # test = [random.randint(1, 100) for _ in range(N)]
    N = 1
    test = [random.randint(1, 15) for _ in range(N)]
    return test

def generate_inputs(num):
    tests = []
    for _ in range(num):
        tests.append(generate_input())
    return tests

def write_file(case, filename):
    os.makedirs('data', exist_ok=True)
    with open(filename, 'w') as file:
        file.write(" ".join(map(str, case)) + "\n")

def generate_output(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            subprocess.run(['std.exe'], stdin=infile, stdout=outfile, check=True)
    except FileNotFoundError:
        print("Error: 'std.exe' not found.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error while running std.exe: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error: {e}")
        sys.exit(1)

def generate():
    tests = generate_inputs(test_num)
    
    for i, case in enumerate(tests, 1):
        input_file = f"data/{i}.in"
        output_file = f"data/{i}.out"
        write_file(case, input_file)
        
        generate_output(input_file, output_file)
    
    print('数据生成完毕')

if __name__ == "__main__":
    generate()
