#  წიგნის რაოდენობა , რამდენი წიგნი უნდა წაიკითხოს , დარჩენილი დღე
a,b,c= map(int,input().split())
stack=list(map(int, input().split())) # რამდენი წიგნი წაიკითხა ვთქვათ  c=3 სამ დღეში 

for i in range(c):
    book = stack.pop()
    if book == 0:
        print("jemaliko gilocav Caabare")
    else:
        print("ver Caabare")

# 5 წიგნი 1  წიგნი წაკითხვა  3 დარჩენილი დღე 
# 4 წიგნი 1 წაიკითხა  2 დღე 
# 3 წიგნი 1 წაიკითხა 1 დღე 
# სულ 2 წიგნი დაჩა წასაკითხი 