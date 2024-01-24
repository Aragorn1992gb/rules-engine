import operator
from settings import Node, ACCEPTED_VALUES, rule, data

# Example rule
# The main operation is defined by the main operator. It is structured as follows:
#    (rule) OPERATOR (rule)
# This structure is recursive, meaning the operator is between other potentially nested rules in brackets.
# Example:
# rule = Node(
#     op="OR",
#     left=Node(
#         op="AND",
#         left=Node(var="credit_rating", op=">", val=50),
#         right=Node(var="flood_risk", op="<", val=10)
#     ),
#     right=Node(var="revenue", op=">", val=1000000)
# )
# Is it possible to make unlimited comparisions nesting the rules

# Example data
# If a variable is not present, it is considered as 0.
# i.e. if flood_risk doesn't exist, it is 0.
# EXAMPLE_1 = {
#     "credit_rating": 75,
#     "flood_risk": 5,
#     "revenue": 1000
# }

# evaluate_rule is used to evaluate the rule based on operators, comparators, and data given in input.
def evaluate_rule(node, data):
    if node.op in ACCEPTED_VALUES["operators"]:
        # Execute the requested operation (taken from the operator library).
        return getattr(operator, node.op)(evaluate_rule(node.left, data), evaluate_rule(node.right, data))
    elif node.op in ACCEPTED_VALUES["comparators"]:
        # Execute the requested comparison (taken from the operator library).
        return getattr(operator, node.op)(data.get(node.var, 0), node.val)
    else:
        raise Exception(f"Exception: Invalid rule operator/comparator: {node.op}")


# Create the recursive tree for the rule.
# Every time you need to define the left and right sides.
# If the operator is an operator (and_, or_, xor), it means that the left and right sides have two other nodes.
# Recall the function recursively and create a Node of nodes (where left and right are two other nodes).
# If the operator is a comparator, it means that the left and right sides are respectively a variable and a value, forming the final node.
def create_tree():
    try:
        op = input("Insert new Rule operator or comparator: ")
        print("Insert left side")
        if op in ACCEPTED_VALUES["operators"]:
            left = create_tree()
        else:
            left = input()
        print("Insert right side")
        if op in ACCEPTED_VALUES["operators"]:
            right = create_tree()
        else:
            right = float(input())
        if op in ACCEPTED_VALUES["operators"]:
            return Node(op=op, left=left, right=right)
        elif op in ACCEPTED_VALUES["comparators"]:
            return Node(var=str(left), op=op, val=int(right))
        else:
            raise Exception(f"Exception: Invalid operator or comparator")
    except ValueError:
        raise("Exception: Variable must be a String and value must be a Float (. not ,)")
    except Exception as ex:
        raise(f"Exception: {ex}")


# Settings in put data
def create_data():
    try:
        var = input("Variable name: ")
        value = float(input("Variable value: "))
        data[var] = value
        c = input("Do you want to add other variables? (y or n)")
        if c == "y": create_data()
    except ValueError:
        raise("Exception: Variable must be a String and value must be a Float (. not ,)")
    except Exception as ex:
        raise(f"Exception {ex}")


def evaluate(rule, data):
    return evaluate_rule(rule, data)


if __name__ == '__main__':
    print("""
    ### Operators accepted ### 
        and_ -> AND
        or_ -> OR
        xor -> XOR
    ### Comparator accepted ###
        lt -> <
        le -> <=
        eq -> ==
        ne -> !=
        ge -> >=
        gt -> >
    ## write the rule using the left operators/comparators ##
    """)

    print("### (Default rule: revenue gt 1000000) or_ (credit_rating gt 50 and_ flood_risk lt 50) ###")
    c = input("Do you want to change the rule? (y or n) ")
    if c == 'y':
        # Invoke the function create_tree to create the tree of the rules
        rule = create_tree()
        
    print("Put your data")
    create_data()
    # Finally, evaluate the input data with the rule and return True or False
    print(evaluate(rule, data))