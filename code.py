# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        n = len(A)
        for i in range(0,n):
            res = 1
            for j in range(0,n):
                if i != j:
                    res *= A[j]
            B.append(res)
        return B
