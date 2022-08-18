class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        seg_cnt = 4
        ans = []
        segments = [0] * 4

        def dfs(cur_seg: int, seg_start_idx: int) -> None:
            if cur_seg == seg_cnt:
                if seg_start_idx == len(s):
                    ip_addr = ".".join(str(seg) for seg in segments)
                    ans.append(ip_addr)
                return
            if seg_start_idx == len(s):
                return

            if s[seg_start_idx] == "0":
                segments[cur_seg] = 0
                dfs(cur_seg + 1, seg_start_idx + 1)
            addr = 0
            for seg_end_idx in range(seg_start_idx, len(s)):
                addr = addr * 10 + (int(s[seg_end_idx]))
                if 0 < addr <= 0xFF:
                    segments[cur_seg] = addr
                    dfs(cur_seg + 1, seg_end_idx + 1)
                else:
                    break

        dfs(0, 0)
        return ans
