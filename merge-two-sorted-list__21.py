# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        combined_list = ([*(list1 + list2)])
        print(type(combined_list))
        return sorted(combined_list)
    

if __name__ == "__main__":
    S = Solution()
    print(S.mergeTwoLists([int(x) for x in input().split()], [int(x) for x in input().split()]))
    