# -*- coding: utf-8 -*-
import csv, io, re

BASE = r"C:\Users\Vladimir Kamashev\Desktop"

files = [
    BASE + r"\Новый текстовый документ.txt",
    BASE + r"\Новый текстовый документ (2).txt",
    BASE + r"\Новый текстовый документ (3).txt",
]

# Model names in order (from header row)
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

# Series for each model
series = ["DBCL"]*14 + ["DBCM"]*14

def parse_file(path):
    """Returns dict {load: [28 runtimes or None]}"""
    with open(path, "r", encoding="utf-8-sig") as f:
        text = f.read()
    
    # Remove \r\n, split by lines
    lines = text.replace("\r\n", "\n").split("\n")
    
    result = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("кВт"):
            continue
        
        # Split by tab
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        
        # First column is load (kW)
        try:
            load = int(parts[0].strip())
        except ValueError:
            continue
        
        # Remaining columns: up to 28 runtime values
        vals = []
        for v in parts[1:]:
            v = v.strip().replace("\u2013", "-").replace("\u2014", "-")
            if v and v != "-":
                try:
                    vals.append(int(v))
                except ValueError:
                    vals.append(None)
            else:
                vals.append(None)
        
        result[load] = vals
    
    return result

# Parse all files
all_data = {}
for f in files:
    data = parse_file(f)
    all_data.update(data)

# Sort loads
sorted_loads = sorted(all_data.keys())
print(f"Total loads: {len(sorted_loads)}, range: {sorted_loads[0]}-{sorted_loads[-1]}")

# Generate JS
print("\nconst DISCHARGE_TABLE = {")
print("  models: [")
for i, m in enumerate(models):
    comma = "," if i < len(models) - 1 else ""
    print(f'    {{id:"dis_{i}",series:"{series[i]}",model:"{m}"}}{comma}')
print("  ],")
print("  rows: {")

for li, load in enumerate(sorted_loads):
    vals = all_data[load]
    # Pad to 28 values if needed
    while len(vals) < 28:
        vals.append(None)
    
    cells = []
    for v in vals[:28]:
        if v is not None:
            cells.append(str(v))
        else:
            cells.append("null")
    
    comma = "," if li < len(sorted_loads) - 1 else ""
    print(f'    {load}: [{",".join(cells)}]{comma}')

print("  }")
print("};")

# Also count non-null per model
print("\n// Stats per model:")
for i, m in enumerate(models):
    count = sum(1 for load in sorted_loads if all_data.get(load, [None]*28)[i] is not None)
    print(f"// {m}: {count} load levels")
