class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m = len(image)
        n = len(image[0])

        if color == image[sr][sc]:
            return image

        indices_to_update = [[sr,sc]]

        while len(indices_to_update) > 0:

            i, j = indices_to_update.pop(0)

            original_color = image[i][j]
            image[i][j] = color

            if color != original_color:
                if i > 0 and image[i-1][j] == original_color:
                    indices_to_update.append([i-1, j])

                if j > 0 and image[i][j-1] == original_color:
                    indices_to_update.append([i, j-1])
                
                if i < m-1 and image[i+1][j] == original_color:
                    indices_to_update.append([i+1, j])
                
                if j < n-1 and image[i][j+1] == original_color:
                    indices_to_update.append([i, j+1])
        
        return image