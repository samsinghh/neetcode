class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {}
        indegree = {}

        for word in words:
            for char in word:
                graph[char] = set()
                indegree[char] = 0

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for j in range(min(len(word1), len(word2))):
                c1 = word1[j]
                c2 = word2[j]

                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break

        queue = deque()

        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(indegree):
            return ""

        return "".join(result)