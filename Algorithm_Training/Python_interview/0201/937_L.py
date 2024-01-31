# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#

logs = ["dig1 8 1 5 1", "let1 art can",
        "dig2 3 6", "let2 own kit dig", "let3 art zero"]

new_logs = [0] * len(logs)
let_logs = []
dig_logs = []

for i in range(len(logs)):
    new_logs[i] = logs[i].split()

    if new_logs[i][1].isalpha():
        let_logs.append(new_logs[i])
    else:
        dig_logs.append(new_logs[i])

for i in range(len(let_logs)):
    let_logs[i][1]

# print(new_logs)
print(let_logs)
print(dig_logs)
