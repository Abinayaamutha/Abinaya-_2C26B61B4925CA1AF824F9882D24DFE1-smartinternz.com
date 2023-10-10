def                                                                       linelinearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
       indices.append(index)

  return indices


#Example usage:
product =                                                               ["shoes","boot","laofer","shoes","sandal","shoes"]
target = "shoes"
result =                                                                linelinearSearchProduct(product,target)
print(result)