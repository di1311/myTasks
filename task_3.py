tests = { 'lesson': [1594663200, 1594666800],'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],'tutor': [1594663290, 1594663430, 1594663443, 1594666473] }
events = []
for k in tests:
    ev = tests[k]
    for i in range(len(ev)):
        events.append((ev[i], 1 - 2*(i%2))) # +-1 для чётного и нечетного индекса
events.sort()
cnt = 0
start = -1
elapsedtime = 0
for e in events:
    cnt += e[1]
    if cnt == 3:
        start = e[0]
    if cnt == 2 and start > 0:
        elapsedtime += e[0] - start
        start = -1