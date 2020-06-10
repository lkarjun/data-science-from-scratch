users = [
    {'id': 0, 'name': 'lalkrishna'},
    {'id': 1, 'name': 'arjun'},
    {'id': 2, 'name': 'sachu'},
    {'id': 3, 'name': 'hari'}, 
    {'id': 4, 'name': 'appu'},
    {'id': 5, 'name': 'sayand'},
    {'id': 6, 'name': 'amar'},
    {'id': 7, 'name': 'lal'},
    {'id': 8, 'name': 'niyas'},
    {'id': 9, 'name': 'kichu'}
]

friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

friendships = {user['id']: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

def number_of_friends(user):
    user_id = user['id']
    friend_ids = friendships[user_id]
    return len(friend_ids)


total_connections = sum(number_of_friends(user)
                        for user in users)

print(total_connections)
print()
num_users = len(users)
avg_connections = total_connections / num_users
print(avg_connections)

num_friends_by_id = [(user['id'], num_friends_by_id(user))
                    for user in users]
