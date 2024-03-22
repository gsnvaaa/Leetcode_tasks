class Solution(object):
    def calPoints(self, ops):
        record = []
        for i in range(len(ops)):
            if ops[i] == 'C':
                record.pop()
            elif ops[i] == 'D':
                record.append(record[-1] * 2)
            elif ops[i] == '+':
                record.append(record[-1] + record[-2])
            else:
                record.append(int(ops[i]))
        return sum(record)