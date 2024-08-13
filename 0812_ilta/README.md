# 큐
|x|삽입위치|삭제위치|
|------|---|---|
|선형큐|rear += 1|front += 1|
|원형큐|rear = (rear + 1)%n|front = (front + 1)%n|