class Solution:
    def floodFill(self, image, sr, sc, newColor):
        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image
    def dfs(self, image, m, n, oldValue, newValue):
        if m < 0 or m > len(image)-1 or n < 0 or n > len(image[0])-1 or image[m][n] == newValue:
            return
        if image[m][n] == oldValue:
            image[m][n] = newValue
            self.dfs(image, m-1, n, oldValue, newValue)
            self.dfs(image, m+1, n, oldValue, newValue)
            self.dfs(image, m, n-1, oldValue, newValue)
            self.dfs(image, m, n+1, oldValue, newValue)
        return
