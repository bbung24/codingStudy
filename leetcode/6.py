"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

PYAIHRN
APLSIIG

P   A   H   N
A P L S I I G
Y   I   R

P     I     N
A   L S   I G
Y A   H R
P     I

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PA YP AL IS HI RI NG", 2) should return "PYAIHRNAPLSIIG". 
convert("PAY P ALI S HIR I NG", 3) should return "PAHNAPLSIIGYIR". 
convert("PAYP AL ISHI RI NG", 4) should return "PINALSIGYAHRPI". 

"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) < numRows:
            return s
        new_string = ''
        middle = numRows - 2
        for row in range(numRows):
            for i in range((len(s) / numRows) + (len(s) % numRows > 0)):
                index = i*(numRows+middle)+row
                print index
                if index < len(s):
                    if row == 0 or row == numRows-1:
                        new_string += s[index]
                    else:
                        new_string += s[index]
                        middle_index = (middle+numRows)*i+(numRows+middle)-row
                        print middle_index
                        if middle_index < len(s):
                            new_string += s[middle_index]
                print new_string
        return new_string


if __name__ == "__main__":
    test = Solution()
    result = test.convert("ABC", 2)
    print result, result == "ACB"