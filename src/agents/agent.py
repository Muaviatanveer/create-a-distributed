import logging
from typing import Any, Dict, Optional

# Initialize logger
logger = logging.getLogger(__name__)

class Agent:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.state = 'initialized'
        self.last_action = None

    def execute_action(self, action: str) -> Optional[str]:
        """
        Execute a given action safely by applying necessary checks and safeguards.
        
        Args:
            action (str): The action to be executed.
            
        Returns:
            Optional[str]: A message indicating the result of the action execution.
        """
        # Check if the agent is in a valid state to perform actions
        if self.state != 'active':
            return f"Error: Agent is not active. Current state: {self.state}"
        
        # Validate the action against allowed actions
        allowed_actions = ['move', 'attack', 'heal']
        if action not in allowed_actions:
            return f"Error: Invalid action '{action}'. Allowed actions: {allowed_actions}"
        
        # Perform the action
        try:
            if action == 'move':
                self.move()
            elif action == 'attack':
                self.attack()
            elif action == 'heal':
                self.heal()
            self.last_action = action
            return f"Action '{action}' executed successfully."
        except Exception as e:
            logger.error(f"Failed to execute action '{action}': {e}")
            return f"Error: Failed to execute action '{action}'."

    def move(self):
        """Simulate moving action."""
        logger.info("Agent moved.")
    
def attack(self):
        """Simulate attacking action."""
        logger.info("Agent attacked.")
    
def heal(self):
        """Simulate healing action."""
        logger.info("Agent healed.")
    
def update_state(self, new_state: str):
        """
        Update the agent's state safely.
        
        Args:
            new_state (str): The new state to set.
        """
        valid_states = ['initialized', 'active', 'inactive']
        if new_state not in valid_states:
            raise ValueError(f"Invalid state '{new_state}'. Valid states: {valid_states}")
        self.state = new_state
        logger.info(f"State updated to: {self.state}")
    
def get_last_action(self) -> Optional[str]:
        """Return the last action performed by the agent."""
        return self.last_action