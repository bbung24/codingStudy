#!/usr/bin/env python
"""
Snakes and Ladders: The Quickest Way Up

Markov takes out his Snakes and Ladders game and stares at the board, and wonders: If he had absolute control on the die, and could get it to generate any number (in the range 1-6) he desired, what would be the least number of rolls of the die in which he'd be able to reach the destination square (Square Number 100) after having started at the base square (Square Number 1)?

Rules

Markov has total control over the die and the face which shows up every time he tosses it. You need to help him figure out the minimum number of moves in which he can reach the target square (100) after starting at the base (Square 1).

A die roll which would cause the player to land up at a square greater than 100, goes wasted, and the player remains at his original square. Such as a case when the player is at Square Number 99, rolls the die, and ends up with a 5.

If a person reaches a square which is the base of a ladder, (s)he has to climb up that ladder, and he cannot come down on it. If a person reaches a square which has the mouth of the snake, (s)he has to go down the snake and come out through the tail - there is no way to climb down a ladder or to go up through a snake.

Constraints

The board is always of the size 10 x 10 and Squares are always numbered 1 to 100. 
1 <= T <= 10 
1 <= Number of Ladders <= 15 
1 <= Number of Snakes <= 15 
Square number 1 and 100 will not be the starting point of a ladder or a snake. 
No square will have more than one of the starting or ending point of a snake or ladder (e.g. snake 56 to 44 and ladder 44 to 97 is not possible because 44 has both ending of a snake and a starting of a ladder)

Input Format

The first line contains the number of tests, T. T testcases follow.

For each testcase, the first line contain N(Number of ladders) and after that N line follow. Each of the N line contain 2 integer representing the starting point and the ending point of a ladder respectively.

The next line contain integer M(Number of snakes) and after that M line follow. Each of the M line contain 2 integer representing the starting point and the ending point of a snake respectively.

Output Format

For each of the T test cases, output one integer, each in a new line, which is the least number of moves (or rolls of the die) in which the player can reach the target square (Square Number 100) after starting at the base (Square Number 1). This corresponds to the ideal sequence of faces which show up when the die is rolled. 
If there is no solution, print -1.

Sample Input

2
3
32 62
42 68
12 98
7
95 13
97 25
93 37
79 27
75 19
49 47
67 17
4
8 52
6 80
26 42
2 72
9
51 19
39 11
37 29
81 3
59 5
79 23
53 7
43 33
77 21 
Sample Output

3
5
Explanation

For the first test: To traverse the board via the shortest route, the player first rolls the die to get a 5, and ends up at square 6. He then rolls the die to get 6. He ends up at square 12, from where he climbs the ladder to square 98. He then rolls the die to get '2', and ends up at square 100, which is the target square. So, the player required 3 rolls of the die for this shortest and best case scenario. So the answer for the first test is 3.

"""
from Queue import Queue

DICE_SIZE = 6
def find_shortest_path(board):
    current_queue = Queue()
    current_queue.put(0)
    next_queue = Queue()
    visited = [False for x in range(len(board))]
    move = 0
    while not current_queue.empty() or not next_queue.empty():
        if current_queue.empty():
            current_queue = next_queue
            next_queue = Queue()
            move += 1
        current = current_queue.get()
        if board[current] > 0:
            current = board[current]
        if current >= len(board)-1:
            return move
        elif visited[current] == False:
            visited[current] = True
            for n in range(1, DICE_SIZE+1):
                next_queue.put(n+current)
    return -1



import unittest
class TestClass(unittest.TestCase):
    def test_snakes_and_ladders1(self):
        sample_input = """\
        2
        3
        32 62
        42 68
        12 98
        7
        95 13
        97 25
        93 37
        79 27
        75 19
        49 47
        67 17
        4
        8 52
        6 80
        26 42
        2 72
        9
        51 19
        39 11
        37 29
        81 3
        59 5
        79 23
        53 7
        43 33
        77 21
        """
        expected = [3,5]
        self.run_snakes_and_ladders(sample_input, expected)

    def test_snakes_and_ladders2(self):
        sample_input = """\
        3
        3
        32 62
        42 68
        12 98
        7
        95 13
        97 25
        93 37
        79 27
        75 19
        49 47
        67 17
        4
        8 52
        6 80
        26 42
        2 72
        9
        51 19
        39 11
        37 29
        81 3
        59 5
        79 23
        53 7
        43 33
        77 21 
        1
        3 90
        7
        99 10
        97 20
        98 30
        96 40
        95 50
        94 60
        93 70
        """
        expected = [3,5,-1]
        self.run_snakes_and_ladders(sample_input, expected)

    def test_snakes_and_ladders3(self):
        sample_input = """\
        3
        2
        3 54
        37 100
        1
        56 33
        2
        3 57
        8 100
        1
        88 44
        1
        7 98
        1
        99 1
        """
        expected = [3,2,2]
        self.run_snakes_and_ladders(sample_input, expected)

    def run_snakes_and_ladders(self, sample_input, expected):
        sample_input = sample_input.split('\n')
        index = 0
        test_case = int(sample_input[index].strip())
        index += 1
        output_index = 0
        for n in range(test_case):
            board = [0 for x in range(100)]
            num_ladder = int(sample_input[index].strip())
            index += 1
            for x in range(num_ladder):
                start,end = map(int, sample_input[index].strip().split())
                board[start-1] = end-1
                index += 1
            num_snake = int(sample_input[index].strip())
            index += 1
            for x in range(num_snake):
                start,end = map(int, sample_input[index].strip().split())
                board[start-1] = end-1
                index += 1
            actual = find_shortest_path(board)
            self.assertEqual(expected[output_index], actual)
            output_index += 1

# Used in hackerrank
# test_case = int(raw_input().strip())
# for n in range(test_case):
#     board = [0 for x in range(100)]
#     num_ladder = int(raw_input().strip())
#     for x in range(num_ladder):
#         start,end = map(int, raw_input().strip().split())
#         board[start-1] = end-1
#     num_snake = int(raw_input().strip())
#     for x in range(num_snake):
#         start,end = map(int, raw_input().strip().split())
#         board[start-1] = end-1
#     print find_shortest_path(board)

if __name__ == "__main__":
    unittest.main()





















