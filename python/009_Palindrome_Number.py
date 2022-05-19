class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = list(str(x))
            halfway_point = int(len(x)/2)
            list1 = x[0:halfway_point]
            list2 = list1[::-1]
            if len(x) % 2 == 0:
                if list2 == x[halfway_point:(len(x))]:
                    return True
                else:
                    return False
            else:
                middle_value = int(len(x) / 2 - .5)
                del x[middle_value]
                if list2 == x[halfway_point:(len(x))]:
                    return True
                else:
                    return False