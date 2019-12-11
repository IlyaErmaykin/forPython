# Задача: Реализовать электронную очередь;

queue = [];

def add(element): # add to queue
    global queue;
    queue.append(element);
    print(element, 'added to queue');

def remove():
    global queue;
    if len(queue) == 0:
        return;

    result = queue[0];
    queue = queue[1:];
    print(result, 'remove from queue');
    return result;

add('user1');
add('user2');
remove();
remove();
remove();   


print(f'Queue has {len(queue)} users');