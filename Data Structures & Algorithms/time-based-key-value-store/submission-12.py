class TimeMap:
    # key with a time and value
    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
            # dumb way is just to sort it lol 
        else:
            self.store[key].append((timestamp, value))
        self.store[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""
        # binary search


        if key in self.store:
            res = self.helper(self.store[key], timestamp)
        return res

    def helper(self, arr, timestamp):
        res = ""
        left = 0
        right = len(arr)-1
        while left <= right:
            mid = (left + right) // 2
            time, value = arr[mid]

            if time <= timestamp:
                res = value
                left = mid + 1
            else:
                right = mid - 1
        return res
