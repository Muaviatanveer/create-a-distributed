```python
import asyncio
from typing import List, Dict, Any

class ConsensusMechanism:
    def __init__(self, nodes: List[str]):
        self.nodes = nodes
        self.current_term = 0
        self.voted_for = None
        self.log = []
        self.commit_index = 0
        self.last_applied = 0
        self.state = 'follower'
        self.leader_id = None

    async def start_election(self):
        self.current_term += 1
        self.voted_for = self.nodes[0]
        votes_received = 1

        for node in self.nodes:
            if node != self.nodes[0]:
                await asyncio.sleep(0.1)  # Simulate network delay
                if await self.request_vote(node):
                    votes_received += 1
                    if votes_received > len(self.nodes) // 2:
                        self.state = 'leader'
                        self.leader_id = self.nodes[0]
                        await self.broadcast_heartbeat()
                        break

    async def request_vote(self, node: str) -> bool:
        # Simulate RPC call to the node
        response = await asyncio.sleep(0.1)
        return True  # Assume vote granted for simplicity

    async def broadcast_heartbeat(self):
        while self.state == 'leader':
            for node in self.nodes:
                if node != self.nodes[0]:
                    await asyncio.sleep(0.1)  # Simulate network delay
                    await self.send_heartbeat(node)
            await asyncio.sleep(1)  # Heartbeat interval

    async def send_heartbeat(self, node: str):
        # Simulate RPC call to the node
        pass

    async def append_entries(self, entries: List[Dict[str, Any]]):
        if self.state == 'follower':
            self.current_term = max(self.current_term, entries[0]['term'])
            self.voted_for = None
            self.log.extend(entries)
            await self.broadcast_heartbeat()
        elif self.state == 'leader':
            for node in self.nodes:
                if node != self.nodes[0]:
                    await asyncio.sleep(0.1)  # Simulate network delay
                    await self.send_append_entries(node, entries)

    async def send_append_entries(self, node: str, entries: List[Dict[str, Any]]):
        # Simulate RPC call to the node
        pass

    async def handle_client_request(self, request: Dict[str, Any]):
        if self.state == 'follower':
            await self.start_election()
        elif self.state == 'leader':
            await self.append_entries([request])

# Example usage
nodes = ['node1', 'node2', 'node3']
consensus = ConsensusMechanism(nodes)
asyncio.run(consensus.handle_client_request({'task': 'process_data', 'data': 'some_data'}))
```

This code provides a basic implementation of a Raft consensus mechanism in Python. It includes methods for starting an election, requesting votes, broadcasting heartbeats, appending entries, and handling client requests. The example usage demonstrates how to create a `ConsensusMechanism` instance and handle a client request.