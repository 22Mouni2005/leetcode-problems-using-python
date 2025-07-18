class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)//3
        l,r,mid=[-i for i in nums[:n]],nums[2*n:],nums[n:2*n]
        l_sum,r_sum=[-sum(l)],[sum(r)]
        heapq.heapify(l)
        heapq.heapify(r)
        for i in mid:
            heapq.heappush(l,-i)
            l_sum.append(l_sum[-1]+i+heapq.heappop(l))
        for i in mid[::-1]:
            heapq.heappush(r,i)
            r_sum.append(r_sum[-1]+i-heapq.heappop(r))
        r_sum=r_sum[::-1]
        return min([i-j for i,j in zip(l_sum,r_sum)])