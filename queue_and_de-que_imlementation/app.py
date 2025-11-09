from flask import Flask, render_template

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty, cannot dequeue.")
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profiles.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/projects/restaurant_simulator')
def restaurant():
    return render_template('restaurant.html', queue=q.queue)


@app.route('/enqueue/<item>')
def enqueue_item(item):
    q.enqueue(item)
    return f"Added '{item}' to the queue. Current queue: {q.queue}"


@app.route('/dequeue')
def dequeue_item():
    if q.is_empty():
        return "Queue is empty, nothing to remove."
    removed = q.dequeue()
    return f"Removed '{removed}' from the queue. Current queue: {q.queue}"
    

if __name__ == "__main__":
    app.run(debug=True)
