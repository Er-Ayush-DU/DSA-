def selection(arr):
  n= len(arr)
  for i in range(n-1):
    mini=i
    for j in range(i+1,n):
      if arr[mini]>arr[j]:
        mini=j
        arr[i],arr[mini]=arr[mini],arr[i]

arr=[20,30,50,40,10]
selection(arr)
print("array:", arr)

