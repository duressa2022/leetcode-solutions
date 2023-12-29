class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i]=reversed(image[i])
            image[i]=map(lambda x: int(not x),image[i])
        return image

        