# -*- coding: utf-8 -*-
import os

BASE = r"C:\Users\Vladimir Kamashev\Desktop"

files = [
    BASE + r"\Новый текстовый документ.txt",
    BASE + r"\Новый текстовый документ (2).txt",
    BASE + r"\Новый текстовый документ (3).txt",
]

all_data = {}

for fpath in files:
    with open(fpath, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8-sig").replace("\r\n", "\n")

    # Remove newlines inside quoted strings (multiline headers)
    in_quote = False
    clean_chars = []
    for ch in text:
        if ch == '"':
            in_quote = not in_quote
        if ch == "\n" and in_quote:
            clean_chars.append(" ")
        else:
            clean_chars.append(ch)
    text = "".join(clean_chars)

    lines = text.split("\n")
    for line in lines:
        line = line.rstrip("\r")
        if not line.strip() or line.startswith(u"\u043a\u0412\u0442"):  # кВт
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        try:
            load = int(parts[0].strip())
        except ValueError:
            continue

        # parts[0]=load, parts[1]=stray empty column, data starts at parts[2]
        vals = []
        for v in parts[2:]:
            v = v.strip().strip('"').strip()
            if v and v != "-":
                try:
                    vals.append(int(v))
                except:
                    vals.append(None)
            else:
                vals.append(None)
        while len(vals) < 28:
            vals.append(None)
        vals = vals[:28]

        all_data[load] = vals

sorted_loads = sorted(all_data.keys())
print("Total loads:", len(sorted_loads), "Range:", sorted_loads[0], "-", sorted_loads[-1])

# Check first few entries
for load in [1, 2, 3, 4, 5]:
    vals = all_data[load]
    print("Load %d: DBCL260-155=%s, DBCL260-170=%s, DBCM130-155=%s, DBCM130-170=%s" % (
        load, vals[0], vals[1], vals[14], vals[15]))

# Check models that had 0 entries before
for idx in [0, 3, 12, 13, 14, 17, 26, 27]:
    model_name = "DBCL" if idx < 14 else "DBCM"
    count = sum(1 for load in sorted_loads if all_data[load][idx] is not None)
    print("Index %d: %d entries" % (idx, count))

# Generate JS
import json

print()
print("const DISCHARGE_TABLE = {")

models = [
    "DBCL 260-155", "DBCL 260-170", "DBCL 260-200", "DBCL 260-211",
    "DBCL 260-260", "DBCL 260-300", "DBCL 260-350", "DBCL 260-480",
    "DBCL 260-570", "DBCL 260-670", "DBCL 260-830", "DBCL 260-900",
    "DBCL 260-670x2", "DBCL 260-670x3",
    "DBCM 130-155", "DBCM 130-170", "DBCM 130-200", "DBCM 130-211",
    "DBCM 130-260", "DBCM 130-300", "DBCM 130-350", "DBCM 130-480",
    "DBCM 130-570", "DBCM 130-670", "DBCM 130-830", "DBCM 130-900",
    "DBCM 130-670x2", "DBCM 130-670x3",
]
series = ["DBCL"]*14 + ["DBCM"]*14

print("  models: [")
for i, m in enumerate(models):
    comma = "," if i < len(models) - 1 else ""
    print('    {id:"dis_%d",series:"%s",model:"%s"}%s' % (i, series[i], m, comma))
print("  ],")
print("  rows: {")

for li, load in enumerate(sorted_loads):
    vals = all_data[load]
    cells = []
    for v in vals[:28]:
        cells.append(str(v) if v is not None else "null")
    comma = "," if li < len(sorted_loads) - 1 else ""
    print("    %d: [%s]%s" % (load, ",".join(cells), comma))

print("  }")
print("};")
