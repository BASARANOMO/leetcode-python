class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq, cnt = Counter(), Counter()
        ans = max_freq = 0
        for i, num in enumerate(nums):
            if cnt[num]:
                freq[cnt[num]] -= 1
            cnt[num] += 1
            max_freq = max(max_freq, cnt[num])
            freq[cnt[num]] += 1
            if (
                max_freq == 1
                or freq[max_freq] * max_freq + freq[max_freq - 1] * (max_freq - 1)
                == i + 1
                and freq[max_freq] == 1
                or freq[max_freq] * max_freq == i
                and freq[1] == 1
            ):
                ans = max(ans, i + 1)
        return ans
