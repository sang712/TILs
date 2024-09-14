def print_vote_results(vote_counts):
    for votes in vote_counts:
        result = ''
        # Add '++++' every 5 votes
        result += '++++ ' * (votes // 5)
        # Add '|' remaining votes
        result += '|' * (votes % 5)
        print(result.strip())  # Output current cndidtes

# Input 
T = int(input())  # No candidates
vote_counts = [int(input()) for _ in range(T)]  # Votes got for trump

print_vote_results(vote_counts)
