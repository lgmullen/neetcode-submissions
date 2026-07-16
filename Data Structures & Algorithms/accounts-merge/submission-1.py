class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = defaultdict(list)  # email -> list of neighbor emails

        # Build graph: connect every email in an account to the first email
        for acc in accounts:
            name = acc[0]
            first = acc[1]
            for email in acc[1:]:
                email_to_name[email] = name
                graph[first].append(email)
                graph[email].append(first)

        res = []
        visited = set()
        for email in graph:
            if email in visited:
                continue
            stack = [email]
            group = []
            visited.add(email)
            while stack:
                cur = stack.pop()
                group.append(cur)
                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
            entry = [email_to_name[email]] + group
            res.append(entry)
            # res.append([email_to_name[email], group])
        return res