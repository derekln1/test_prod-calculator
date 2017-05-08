#!/usr/bin/env python
import json
import sys

my_list = sys.argv[1]
my_budget = sys.argv[2]

with open(my_list, 'r') as groceries:
    grocery_list = json.load(groceries)

total_cost = 0
for item in grocery_list:
    print "Buying {} {}s at ${}/{}".format(grocery_list[item]["number"], item, grocery_list[item]["price"], item)
    total_cost += int(grocery_list[item]["number"]) * int(grocery_list[item]["price"])

print "Total cost is {}".format(total_cost)

with open(my_budget, 'r') as budget:
   funds = int(budget.read())

print "Our budget is ${}.".format(funds)
if total_cost < funds:
    print "We can buy the groceries! :)))"
else:
    print "We don't have enough for the groceries :(((("
    sys.exit(1)


