#score = [1, 2, 3, 4, 2.7, 8.1, 34.3, 3.234]
users = [
    {'name': 'Jack1', 'score': 1, 'age': 81},
    {'name': 'Jack2', 'score': 2, 'age': 82},
    {'name': 'Jack3', 'score': 3, 'age': 89},
    {'name': 'Jack4', 'score': 4, 'age': 60},
    {'name': 'Jack5', 'score': 2.7, 'age': 12},
    {'name': 'Jack6', 'score': 8.1, 'age': 73},
    {'name': 'Jack7', 'score': 34.3, 'age': 8},
    {'name': 'Jack8', 'score': 3.234, 'age': 100},
]

def user_with_max_score(users):
    max_score = -1;
    max_user = None;
    for user in users:
        if max_score < user['score']:
            max_score = user['score'];
            max_user = user;
    
    return max_user;

print (user_with_max_score(users));