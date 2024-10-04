lst = eval(input('Enter the elements: '))
lst = lst*2
asclst = sorted(lst)
deslst = sorted(lst, reverse=True)

print(f"Ascending list: {asclst}")
print(f"Descending list: {deslst}")
