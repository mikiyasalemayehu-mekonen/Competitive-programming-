# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        root = list(range(n))

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            root[find(x)] = find(y)

        email_to_index = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_index:
                    union(i, email_to_index[email])
                email_to_index[email] = i

        groups = defaultdict(set)
        for email, i in email_to_index.items():
            leader = find(i)
            groups[leader].add(email)

        result = []
        for i, emails in groups.items():
            name = accounts[i][0]
            result.append([name] + sorted(emails))
        return result
