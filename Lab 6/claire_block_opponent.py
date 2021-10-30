# Claire's Block Opponent Code  
# def block_opponent(board,mark):
#     #Problem 4 (b): check if X is about to win
#     opponent_squares = check_opponent(board,mark)
    
#     index_list = []
#     for i in range(len(opponent_squares)):
#         opponent_index = opponent_squares[i][0]*3 + opponent_squares[i][1] + 1
#         index_list.append(opponent_index)
        
#     # 1,2 or 2,3 exist?
#     # 1,4 exist?
#     # 1,5 exist?
#     check_index_order = []
#     for i in range(len(index_list)+1):
#         check_index_order.append(index_list[i],index_list[i+1])
#         for j in range(1,6):
#             if check_index_order == [j, j+1]:
#                 print("next to each other", check_index_order)
    
    
# def check_opponent(board,mark):
#     if mark == "0":
#         opponent_mark = "X"
#     else:
#         opponent_mark = "0"
        
#     opponent_squares = []
    
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == opponent_mark: 
#                 opponent_square = [i, j]
#                 opponent_squares.append(opponent_square)
#     return opponent_squares