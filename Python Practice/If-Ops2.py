indian = ["In1","In2","In3","In4","In5","In6"]
chinese=["Chi1","Chi2","Chi3","Chi4","Chi5"]
italian=["It1","It2","It3","It4"]
dish =str(input("Enter Dish Name:"))
if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("Not Found")
