import instaloader
from collections import defaultdict

L = instaloader.Instaloader()

username = ''
password = ''

profile1_username = "ukrotitell"
profile2_username = "mr_azarov"

# Login or load session
L.login(username, password)  # (login)

# Obtain profile metadata
profile1 = instaloader.Profile.from_username(L.context, profile1_username)
profile2 = instaloader.Profile.from_username(L.context, profile2_username)


follow_list = []
for followee in profile1.get_followers():
    follow_list.append(followee.username)

for followee in profile2.get_followers():
    follow_list.append(followee.username)

D = defaultdict(list)
for i,item in enumerate(follow_list):
    D[item].append(i)
D = {k:v for k,v in D.items() if len(v)>1}
print(D)
