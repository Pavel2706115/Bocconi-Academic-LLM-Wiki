''' The "admissions" function defines the best matches between
    Universities and Students, giving priority of choice to Universities.
    Since the approach used creates a dictionary with Students as keys,
    in the returned dictionary each key-value pair must be swapped.
'''

def admissions(UniPref, StudPref):

    universities = list(UniPref.keys())
    students = list(StudPref.keys())

    proposals = {}
    for u in universities:
        proposals[u] = []

    matches = {}
    for s in students:
        matches[s] = ''

    free_uni = list(UniPref.keys())


    while free_uni != []:
        uni = free_uni.pop(0)
        for stud in UniPref[uni]:
            if stud not in proposals[uni]:
                proposals[uni].append(stud)
                current_match = matches[stud]
                if current_match == '':
                    matches[stud] = uni
                    break
                else:
                    if StudPref[stud].index(uni) < StudPref[stud].index(current_match):
                        free_uni.append(current_match)
                        matches[stud] = uni
                        break


    UniStud_matches = {}
    for s, u in matches.items():
        UniStud_matches[u] = s

    return UniStud_matches



U = {'A': ['w', 'x', 'y', 'z'],
     'B': ['y', 'x', 'w', 'z'],
     'C': ['w', 'y', 'x', 'z'],
     'D': ['x', 'z', 'w', 'y']}

S = {'w': ['B', 'D', 'C', 'A'],
     'x': ['C', 'A', 'D', 'B'],
     'y': ['B', 'C', 'D', 'A'],
     'z': ['A', 'B', 'D', 'C']}


result = admissions(U, S)

for k, v in result.items():
    print(k, v, sep = " matches with ")
