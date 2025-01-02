N = int(input("give the N value: "))
soon = 0
soen = 0
for i in range(1,N+1):
    if i % 2 == 1:
        soon += i
    else:
        soen += i

if N % 2 == 0:
    nmbeven = N/2
else:
    nmbeven = (N-1)/2

if nmbeven == 0:
    avg = 0
else:
    avg = soen / nmbeven

print("sum of odd numbers", soon)
print("avg of even numbers", avg)
