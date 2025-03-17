import generator
import subprocess
import os
import difflib


# 用于清除输出文件里的版权信息
def clean_output_file(output_file):
    with open(output_file, 'r') as f:
        lines = f.readlines()

    if lines and lines[0].startswith("MARS"):
        lines = lines[1:]

    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    lines = lines[i:]

    with open(output_file, 'w') as f:
        f.writelines(lines)


def run_mips(input_file, output_file):
    mars = 'mars.jar'
    if not os.path.exists(mars):
        print(f"错误: mars.jar 未找到。")
        return
    
    asm_file = './test.asm'
    if not os.path.exists(asm_file):
        print(f"错误: '{asm_file}' 未找到。")
        return

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            subprocess.run(['java', '-jar', mars, asm_file], stdin=infile, stdout=outfile, check=True)
        print(f"输出已写入 {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"运行 MIPS 程序时出错: {e}")
    except FileNotFoundError as e:
        print(f"文件未找到: {e}")
    except Exception as e:
        print(f"发生意外错误: {e}")
    clean_output_file(output_file)


def mips_generate():
    for i in range(1, generator.test_num + 1):
        input_file = f"data/{i}.in"
        output_file = f"data/mips{i}.out"
        run_mips(input_file, output_file)


def judge_case(file1, file2, i):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        # 去掉结尾的空行
        while lines1 and not lines1[-1].strip():
            lines1.pop()
        while lines2 and not lines2[-1].strip():
            lines2.pop()

        print(len(lines1), lines1)
        print(len(lines2), lines2)
        if len(lines1) != len(lines2):
            print(f"\033[31mtest case {i}: Wrong Answer\033[0m")
            return

        for line1, line2 in zip(lines1, lines2):
            if line1.strip() != line2.strip():
                print(f"\033[31mtest case {i}: Wrong Answer\033[0m")
                return

        print(f"\033[32mtest case {i}: Accepted\033[0m")

    except FileNotFoundError as e:
        print(f"文件未找到: {e}")
    except Exception as e:
        print(f"发生错误: {e}")



def judge():
    for i in range(1, generator.test_num + 1):
        input_file = f"data/{i}.out"
        output_file = f"data/mips{i}.out"
        judge_case(input_file, output_file, i)


if __name__ == "__main__":
    generator.generate()
    mips_generate()
    judge()
