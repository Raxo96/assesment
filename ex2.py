#2. OOP with bank account.
#a) Write a bank Account class that has:
#
#    2 atributes: 
#        - name
#        - balance
#
#    and 2 methods:
#        - deposit (takes amount as argument, increase balance with amount)
#        - witdraw (takes amount as argument, decrease balance with amount if there is enough money on account)
#        
#    * implement magic method that allows to print Account instance in convenient way
#    
#    Example:
#    
#    client = Account('Bary', 100)
#    print(client)
#    
#    output:
#    'User name  :   Bary'
#    'Balance    :   100$'
#       
#   
# b) write GoldenAccount class that inherits Account,
#    GoldenAccount can withdraw any amount of money without restrictions about balance.

class Account:
  pass

class GoldenAccount:
  pass

client = Account('Bary', 100)
print(client)

client.deposit(50)
assert client.balance == 150
client.witdraw(100)
assert client.balance == 50
client.witdraw(50)
assert client.balance == 0


client2 = GoldenAccount('Bary', 100)
print(client2)
client2.witdraw(200)
assert client.balance == -50
