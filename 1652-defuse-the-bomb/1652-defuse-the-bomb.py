class Solution:
    def decrypt(self, code, k):
        n = len(code)

        if k == 0:
            return [0] * n

        result = [0] * n

        if k > 0:
            window_sum = sum(code[1:k+1])

            for i in range(n):
                result[i] = window_sum
                window_sum -= code[(i + 1) % n]
                window_sum += code[(i + k + 1) % n]

        else:
            k = abs(k)
            window_sum = sum(code[n-k:n])

            for i in range(n):
                result[i] = window_sum
                window_sum -= code[(i - k) % n]
                window_sum += code[i % n]

        return result