# PRECEDÊNCIA
# 1. (n + n) -> PARÊNTESES
# 2. **
# 3. * / // %
# 4. +-

conta_1 = (1 + 1) ** (5 + 5) # 1024
print(conta_1)

conta_1 = 1 + 1 ** 5 + 5 # 7
print(conta_1)

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1024
print(conta_1)