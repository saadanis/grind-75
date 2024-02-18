class Solution:
    def addBinary(self, a: str, b: str) -> str:

        result = ''
        carry = False

        a = a if len(a) >= len(b) else '0' * (len(b) - len(a)) + a
        b = b if len(b) >= len(a) else '0' * (len(a) - len(b)) + b

        for i in reversed(range(len(a))):
            if a[i] == b[i]:
                if a[i] == '0':
                    if carry:
                        result += '1'
                        carry = False
                    else:
                        result += '0'
                else:
                    if carry:
                        result += '1'
                    else:
                        result += '0'
                        carry = True
            else:
                if carry:
                    result += '0'
                else:
                    result += '1'

        if carry:
            result += '1'

        return result[::-1]