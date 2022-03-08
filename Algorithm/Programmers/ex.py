
participant = ["mislav", "stanko", "mislav", "ana"]

par_count = list(map(lambda x : [x,participant.count(x)] , list(set(participant))))

print(par_count)