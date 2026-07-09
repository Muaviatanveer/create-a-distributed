```python
import heapq
from typing import List, Dict, Tuple

class Task:
    def __init__(self, id: int, location: Tuple[int, int], priority: int):
        self.id = id
        self.location = location
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

class TaskPlanner:
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks
        self.task_heap = []

    def plan_tasks(self) -> List[Task]:
        # Initialize the task heap with all tasks based on priority
        for task in self.tasks:
            heapq.heappush(self.task_heap, task)

        planned_tasks = []
        while self.task_heap:
            # Pop the highest priority task from the heap
            current_task = heapq.heappop(self.task_heap)
            planned_tasks.append(current_task)

        return planned_tasks

# Example usage
if __name__ == "__main__":
    tasks = [
        Task(1, (0, 0), 3),
        Task(2, (1, 1), 1),
        Task(3, (2, 2), 2)
    ]
    planner = TaskPlanner(tasks)
    planned_tasks = planner.plan_tasks()
    for task in planned_tasks:
        print(f"Task ID: {task.id}, Location: {task.location}, Priority: {task.priority}")
```

This code defines a `Task` class to represent individual tasks with an ID, location, and priority. The `TaskPlanner` class uses a min-heap (priority queue) to plan tasks based on their priority. The `plan_tasks` method pops the highest priority task from the heap until all tasks are planned.

The example usage at the bottom demonstrates how to create a list of tasks and use the `TaskPlanner` to plan them.