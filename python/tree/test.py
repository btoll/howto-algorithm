size = 10
arr = [n for n in range(size)]

print(f"Tree of {size} nodes:")

for n in range(len(arr)//2):
    print(f"\nparent node {arr[n]}")
    print(f"left child {arr[2*n+1]}")
#    if 2*n+2 < len(arr):
    try:
        print(f"right child {arr[2*n+2]}")
    except:
        pass
