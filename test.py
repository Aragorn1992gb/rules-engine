import main
from settings import Node

import pytest

# For the test suite, I opt for the external library "pytest," the "industry standard" Python library for testing
# (the most widely used by the community). Then, I chose to define the test technique "Table test"

# For Table test, I define the test cases as a list of tuples (input_values, expected_result)
test_cases = [
    # TEST CASE 1:
    (
        (
            Node(
                op="or_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="gt", val=50),
                    right=Node(var="flood_risk", op="lt", val=10)
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ), # The rule
            {
                "credit_rating": 75,
                "flood_risk": 5,
                "revenue": 1000
            }
        ), # Data input that satisfy the rule
    True), # Output that I expect (True)
    # TEST CASE 2:
    (
        (
            Node(
                op="or_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="gt", val=50),
                    right=Node(var="flood_risk", op="lt", val=10)
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "credit_rating": 50,
                "flood_risk": 5,
                "revenue": 1000
            }
        ),
    False),
    # TEST CASE 3:
    (
        (Node(
            op="or_",
            left=Node(
                op="and_",
                left=Node(var="credit_rating", op="gt", val=50),
                right=Node(var="flood_risk", op="lt", val=10)
            ),
            right=Node(var="revenue", op="gt", val=1000000)
        ),
        {
            "credit_rating": 45,
            "flood_risk": 5,
            "revenue": 123456789
        }
        ),
    True),
    # TEST CASE 4:
    (
        (
            Node(
                op="or_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="ge", val=50),
                    right=Node(var="flood_risk", op="lt", val=10)
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "credit_rating": 50,
                "flood_risk": 5,
                "revenue": 123456789
            },
        ),
    True),
    # TEST CASE 5:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="ge", val=50),
                    right=Node(var="flood_risk", op="lt", val=10)
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "credit_rating": 40,
                "flood_risk": 5,
                "revenue": 123456789
            }
        ),
    False),
    # TEST CASE 6:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="ge", val=50),
                    right=Node(var="flood_risk", op="le", val=10)
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
        {
            "credit_rating": 40,
            "flood_risk": 5,
            "revenue": 123456789
        },
        ),
    False),
    # TEST CASE 7:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="ge", val=50),
                    right=Node(var="flood_risk", op="le", val=10)
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "credit_rating": 50,
                "flood_risk": 10,
                "revenue": 123456789
            },
        ),
    True),
    # TEST CASE 8:
    (
        (
            Node(
                    op="and_",
                    left=Node(
                        op="and_",
                        left=Node(var="credit_rating", op="ge", val=50),
                        right=Node(var="flood_risk", op="le", val=10)
                    ),
                    right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "flood_risk": 10,
                "revenue": 123456789
            }
        ),
    False),
    # TEST CASE 9:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="le", val=9),
                    right=Node(var="flood_risk", op="le", val=10)
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "flood_risk": 10,
                "revenue": 123456789
            }
        ),
    True),
    # TEST CASE 10:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="le", val=9),
                    right=Node(var="flood_risk", op="le", val=10)
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "flood_risk": 10,
                "revenue": 123456789,
                "other": 999
            }
        ),
    True),
    # TEST CASE 11:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="le", val=9),
                    right=Node(
                        op="or_",
                        left=Node(var="flood_risk", op="eq", val=9),
                        right=Node(var="other", op="ge", val=100)
                    )
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "flood_risk": 10,
                "revenue": 123456789,
                "other": 999
            }
        ),
    True),
    # TEST CASE 12:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="le", val=9),
                    right=Node(
                        op="xor",
                        left=Node(var="flood_risk", op="eq", val=9),
                        right=Node(var="other", op="ge", val=100)
                    )
                    
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "flood_risk": 10,
                "revenue": 123456789,
                "other": 999
            }
        ),
    True),
    # TEST CASE 13:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="le", val=9),
                    right=Node(
                        op="or_",
                        left=Node(var="flood_risk", op="eq", val=9),
                        right=Node(var="other", op="ge", val=1000)
                    )
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "flood_risk": 10,
                "revenue": 123456789,
                "other": 999
            }
        ),
    False),
    # TEST CASE 14:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="le", val=9),
                    right=Node(
                        op="and_",
                        left=Node(var="flood_risk", op="ne", val=9),
                        right=Node(var="other", op="ge", val=100)
                    ) 
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "flood_risk": 10,
                "revenue": 123456789,
                "other": 999
            }
        ),
    True),
    # TEST CASE 15:
    (
        (
            Node(
                op="and_",
                left=Node(
                    op="and_",
                    left=Node(var="credit_rating", op="le", val=9),
                    right=Node(
                        op="and_",
                        left=Node(var="flood_risk", op="ne", val=9),
                        right=Node(var="other", op="ge", val=100)
                    )
                    
                ),
                right=Node(var="revenue", op="gt", val=1000000)
            ),
            {
                "flood_risk": 9,
                "revenue": 123456789,
                "other": 999
            }
        ),
    False)
]

# I use the @pytest.mark.parametrize decorator to create the table-driven test
@pytest.mark.parametrize("input_values, expected_result", test_cases)
def test_evaluate(input_values, expected_result):
    result = main.evaluate(*input_values)
    assert result == expected_result