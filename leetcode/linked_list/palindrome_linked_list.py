"""
LeetCode 234. Palindrome Linked List
url: https://leetcode.com/problems/palindrome-linked-list/
writer: Harim Kang
Language: Python3
Date: 2020.09.22
Status: Success, Runtime: 76 ms, Memory Usage: 24.2 MB
Follow up: Could you do it in O(n) time and O(1) space?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        temp = []
        node = head
        while True:
            if node is None:
                break
            temp.append(node.val)
            node = node.next

        if temp == temp[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2
    output_1 = False
    answer_1 = Solution().isPalindrome(node_1)
    if answer_1 == output_1:
        print('Success: {}'.format(answer_1))
    else:
        print('Failed: {}'.format(answer_1))

    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2
    node_3 = ListNode(2)
    node_2.next = node_3
    node_4 = ListNode(1)
    node_3.next = node_4
    output_1 = True
    answer_1 = Solution().isPalindrome(node_1)
    if answer_1 == output_1:
        print('Success: {}'.format(answer_1))
    else:
        print('Failed: {}'.format(answer_1))
