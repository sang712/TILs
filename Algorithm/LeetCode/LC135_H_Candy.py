"""
candies라는 다른 리스트를 하나 더 두고
rating으로 오름차순 정렬한 idx, rating 쌍의 리스트를 for문으로 돌면서
좌 혹은 우의 rating이 더 높으면서 candy 수가 작거나 같다면 
해당 candy에 1을 더한 값으로 초기화 하는 방식으로 candy의 수를 구했고
모두 더해 반환함으로 문제를 풀이하였음
"""
class Solution:
    def candy(self, ratings: List[int]) -> int:
        num_children = len(ratings)
        candies = [1] * num_children

        children_rating = sorted(list(enumerate(ratings)), key=lambda x: x[1])
        for child, rating in children_rating:
            if child > 0 and ratings[child - 1] > ratings[child] and candies[child - 1] <= candies[child]:
                candies[child - 1] = candies[child] + 1
            if child < num_children - 1 and ratings[child] < ratings[child + 1] and candies[child] >= candies[child + 1]:
                candies[child + 1] = candies[child] + 1
        
        return sum(candies)