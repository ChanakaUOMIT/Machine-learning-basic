import pandas as pd

Employee = {'number': [1, 2, 3, 4, 5], 'name': [
    'abby', 'john', 'lina', 'marc', 'bob'], 'hourly salary': [15, 25, 32, 27, 40]}

print(Employee)

table1 = pd.DataFrame(Employee)
print(table1)


print('--------------------------')
print(table1.head(3))
print(table1.tail(1))

print('--------------------------')
food1 = {'number': [1, 2, 3, 4, 5], 'name': [
    "corn", 'banana', 'chips', 'popcorn', 'pizza'], 'price': [2, 3, 4, 8, 6]}
food2 = {'number': [1, 2, 3, 4, 5], 'name': [
    "apple", 'banana', 'beans', 'popcorn', 'pizza'], 'price': [2, 3, 4, 8, 6]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = pd.merge(table1, table2)
print(fusion)

fusion1 = pd.merge(table1, table2, on="number")
print(fusion1)


print('--------------------------')
food3 = {'number': [1, 2, 3, 4, 5], 'name': [
    "apple", 'banana', 'chips', 'popcorn', 'pizza'], 'price': [2, 6, 4, 3, 5]}
food4 = {'color': ['red', 'yellow', 'orange', 'white', 'blue'],
         'weight': [100, 200, 150, 175, 225], 'qt': [1, 2, 1, 3, 4]}

table3 = pd.DataFrame(food3)
table4 = pd.DataFrame(food4)

fusion2 = table3.join(table4)
print(fusion2)


print('--------------------------')


color = pd.read_csv("C:\\Project\\DeepLearnig\\Playgroud\\pandas\\work.csv")
color.to_html("NiceColor")
