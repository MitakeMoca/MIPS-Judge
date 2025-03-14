# MIPS-Judge
评测 MIPS 程序是否正确

在运行之前，请将你用高级语言生成的 `std.exe` 文件放到同一目录下；将 `mars.jar` 文件放到同一目录下；将要进行测试的 MIPS 代码 `test.asm` 放到同一文件下。在运行前文件结构如下：

```
MIPS-JUDGE
│── generator.py
│── main.py
│── mars.jar
│── README.md
│── std.exe
└── test.asm
```

然后根据需要，修改 `generator` 数据生成器：

```python
# 测试样例个数
test_num = 5

# 每个测试样例如何生成，比如下面是生成了一个长度在 1 到 100 之间的整数数组
def generate_input():
    N = random.randint(1, 100)
    test = [random.randint(1, 100) for _ in range(N)]
    return test

# 描述输入格式
def write_file(case, filename):
    os.makedirs('data', exist_ok=True)
    with open(filename, 'w') as file:
        file.write(" ".join(map(str, case)) + "\n")
```

然后运行 `main.py`，就能看到每个评测点是否正确：

```python
python main.py
```

示例给出了一个汉诺塔问题的数据生成器和 `std.exe`。

生成的数据在 `/data` 目录下，`std` 生成的输出文件名称为 `x.in`，`MIPS` 生成的输出文件格式为 `mipsx.in`，可通过对比输出文件进行进一步的调试。
