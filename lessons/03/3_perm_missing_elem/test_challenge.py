
from challenge import solution

def test_challenge_array():
    # Create empty array (dependent on test)
    # Create single entry array
    # Create an array with the answer at the start
    # Create an array with the answer at the end
    # Create an array with the answer in the middle
    assert solutionArray([9, 3, 9, 3, 9, 7, 9]) == [9, 3, 9, 3, 9, 7, 9]
    assert solutionArray([9, 3, 9, 3, 9, 1, 9]) == [9, 3, 9, 3, 9, 1, 9]
    assert solutionArray([9, 1, 9, 1, 9, 2, 9]) == [9, 1, 9, 1, 9, 2, 9]
    assert solutionArray([9, 1, 9, 1, 9, 2, 9]) == [9, 1, 9, 1, 9, 2, 9]
    # Single entry slot
    assert solutionArray([99]) == [99]
    # Answer in last slot
    assert solutionArray([2, 2, 3, 3, 4]) == [2, 2, 3, 3, 4]
    # Answer in first slot
    assert solutionArray([2, 3, 3, 4, 4]) == [2, 3, 3, 4, 4]
    # Answer in middle slot
    assert solutionArray([2, 2, 3, 4, 4]) == [2, 2, 3, 4, 4]

