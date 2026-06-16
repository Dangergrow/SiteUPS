#!/usr/bin/env python3
# -*- coding: utf-8 -*-

path = r'C:\Users\Vladimir Kamashev\Desktop\Mod\ontek-ups-compare.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.index('<script>') + len('<script>')
end = content.index('</script>')
js = content[start:end]

lines = js.split('\n')

# Find transition between U array and next section
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith('];') and i > 0:
        print(f'Line {i+1}: {stripped}')
        print(f'  Prev: {lines[i-1].strip()[:80]}')
        print(f'  Next: {lines[i+1].strip()[:80]}')
        break

# Check for unterminated strings (odd number of double quotes)
issues = []
for i, line in enumerate(lines):
    s = line.strip()
    if not s or s.startswith('//') or s.startswith('*'):
        continue
    dq = s.count('"')
    if dq % 2 != 0 and not s.startswith('console'):
        issues.append((i+1, dq, s[:80]))

if issues:
    print(f'\nFound {len(issues)} lines with odd double quotes:')
    for ln, cnt, txt in issues[:20]:
        print(f'  L{ln}: {cnt} quotes: {txt}')
else:
    print('No unterminated string issues found')

# Check single quotes
for i, line in enumerate(lines):
    s = line.strip()
    if not s or s.startswith('//'):
        continue
    sq = s.count("'")
    if sq % 2 != 0:
        print(f'L{i+1}: odd single quotes: {s[:80]}')

# Check the function definitions are all complete
for keyword in ['function', 'const', 'let']:
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith(keyword + ' ') and '{' not in s and ';' not in s and s.count('=') == 0:
            if keyword == 'function' and not s.endswith('{') and not s.endswith(')'):
                pass  # multiline function defs are fine

# Check renderFilters function specifically
rf_start = js.find('function renderFilters()')
rf_end = js.find('function renderSer()', rf_start)
print(f'\nrenderFilters() at {rf_start}-{rf_end}')

# Check for the key issue: "battery" filter with "external" value  
print(f'\nBattery filter external: {"data-val=\"external\"" in js}')
print(f'Battery filter internal: {"data-val=\"internal\"" in js}')

# Check if "category" "all" button has active class
print(f'Category all active: {"data-val=\"all\">Все<" in js}')

# Check if switchTab is called at init
print(f'switchTab at init: {"switchTab(\'ups\')" in js}')
print(f'switchTab at init alt: {"switchTab(\"ups\")" in js}')

# Check last few lines
print('\nLast 10 lines of file:')
for line in lines[-10:]:
    print(f'  {line.strip()[:100]}')
