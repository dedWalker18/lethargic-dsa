# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def merge_sorted_lists(head1, head2):
#     dummy_head = Node(None)  # Create a dummy node to simplify head handling
#     tail = dummy_head

#     while head1 and head2:
#         if head1.data < head2.data:
#             tail.next = head1
#             head1 = head1.next
#         else:
#             tail.next = head2
#             head2 = head2.next
#         tail = tail.next

#     # Append the remaining elements of the non-empty list
#     tail.next = head1 or head2

#     return dummy_head.next  # Return the actual head of the merged list (excluding the dummy)

# # Example usage
# head1 = Node(1)
# head1.next = Node(3)
# head1.next.next = Node(5)

# head2 = Node(2)
# head2.next = Node(4)

# merged_head = merge_sorted_lists(head1, head2)

# while merged_head:
#     print(merged_head.data, end=" -> ")
#     merged_head = merged_head.next

# print("None")  # Print the end of the list

# cook your dish here
# s1, s2 = map(int, input().split(" "))

# # cook your dish here
# def min_operations(binary_string):
#     current_char = binary_string[0]
#     group_size = 0
#     min_ops = 0
#     for char in binary_string[1:]:
#         if char != current_char:
#           min_ops += 1
#           current_char = char
#           group_size = 1
#         else:
#           group_size += 1
        
#     if current_char != binary_string[0]:
#         min_ops += 1
    
#     return min_ops
    
# t = int(input())
# for i in range(t):
#     n=int(input())
#     s=input()
#     print(min_operations(s))

# print(len(set([" "])))

# def search(self, nums: List[int], target: int) -> int:


# Longest substring with no repeated chars
        # st = set()
        # mset = set()
        # for i in range(len(s)):
        #     if s[i] not in st:
        #         st.add(s[i])
        #         if len(st) > len(mset):
        #             mset = st.copy()
        #     else:
        #         if len(st) > len(mset):
        #             mset = st.copy()
        #         st = set(s[i])
        # return len(mset)


with open("read.txt","r") as f:
        input=f.readlines()
i=0
games=[]
ranked_games=[]

while i<len(input):
        if input[i]:
                nextline = input[i]
                newline = nextline.split(" ")
                games.append(newline)
                i+=1           
        else:
                break

def score_game(game):
        seen = {}
        for card in game:
                if card in seen:
                        seen[card]+=1
                else:
                        seen[card]=1
        
        counts = [v for v in seen.values()]
        if 5 in counts:
                return 6
        elif 4 in counts:
                return 5
        elif 3 in counts:
                if 2 in counts:
                        return 4
                else:
                        return 3
        elif 2 in counts:
                if counts.count(2) == 2:
                        return 2
                else:
                        return 1
        else:
                return 0

def sort_games(sublist):
        if isinstance(sublist[1], int):
                return (sublist[0])
        else:
                return (sublist[1])
        
for game in games:
        rank = score_game(game[0])
        ranked_games.append([game[0],rank,game[1]])
        
print(sorted(ranked_games,key=sort_games))