class Node:
    def __init__(self, op, left=None, right=None, var=None, val=None):
        self.op = op
        self.left = left
        self.right = right
        self.var = var
        self.val = val

# Define the node class for the rule tree.
# "op" is the operator (OR, AND, <, >, =).
# "left" is the left element of the comparison.
# "right" is the right element of the comparison.
# i.e., left OPERATOR right.
# "var" is the name of the variable (e.g., credit_rating).
# "val" is the value of the element.
        
global ACCEPTED_VALUES, rule, data

ACCEPTED_VALUES = {
    "operators": ["and_", "or_", "xor"],
    "comparators": ["lt", "le", "eq", "ne", "ge", "gt"]
}

rule = Node(
    op="or_",
    left=Node(
        op="and_",
        left=Node(var="credit_rating", op="gt", val=50),
        right=Node(var="flood_risk", op="lt", val=10)
    ),
    right=Node(var="revenue", op="gt", val=1000000)
)

data = {}
