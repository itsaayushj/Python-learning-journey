price1 = 300000.19434
price2 = 392.11453
price3 = -89.55

print(f"${price1:.1f}")
print(f"${price2:.1f}")
print(f"${price3:.1f}")

print(f"${price1:10}") # 010 will add 10 0 in front
print(f"${price2:+}")
print(f"${price3:^100}")    # < > ^ 

print(f"{price1:+,.2f}")
