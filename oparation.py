def cal_chek(x, y, z):

    operations = [
        ((x << 8) + y) ** z,
        (x & y) % z,
        round(x / y) >> z,
        int((2 + x) / y) | z
    ]

    total_sum = sum(operations)

    results = [
        f"rs {i+1}: {op}" for i, op in enumerate(operations)
    ]
    # results.append(f"Sum of all rs: {total_sum}")

    conditions = [
        f"cd x == y: {'yes' if x == y else 'no'}",
        f"cd x != y << z: {x != (y << z)}"
    ]

    for result in results + conditions:
        print(result)

inputs = ['x', 'y', 'z']
values = []

for inp in inputs:
    value = int(input(f"input {inp}: "))
    values.append(value)

cal_chek(*values)
