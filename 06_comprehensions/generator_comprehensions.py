sales=[4,7,3,7,0,32,5,24,3,536,4,6,3,25,]

# ans=[sale for sale in sales if sale > 7]
ans=sum(sale for sale in sales if sale > 7)
print(ans)