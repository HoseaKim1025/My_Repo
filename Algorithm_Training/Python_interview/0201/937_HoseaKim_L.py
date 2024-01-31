class Solution:

    def reorderLogFiles(self, logs):

        new_logs = [0] * len(logs)
        let_logs = []
        dig_logs = []

        for i in range(len(logs)):
            new_logs[i] = logs[i].split()

            if new_logs[i][1].isalpha():
                let_logs.append(logs[i])
            else:
                dig_logs.append(logs[i])

        let_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return let_logs + dig_logs


logs = ["dig1 8 1 5 1", "let1 art can",
            "dig2 3 6", "let2 own kit dig", "let3 art zero"]

a = Solution()
print(a.reorderLogFiles(logs))
