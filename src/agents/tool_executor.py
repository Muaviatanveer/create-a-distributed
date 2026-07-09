```python
import subprocess
import logging
from typing import Dict, Any

# Setup logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ToolExecutor:
    """
    A class to handle the execution of external tools and integrate their outputs.
    """

    def __init__(self):
        self.tool_commands = {
            "ping": ["ping", "-c", "4"],
            "whois": ["whois"],
            "dig": ["dig"]
        }

    def execute_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """
        Execute an external tool and return its output.

        :param tool_name: The name of the tool to execute.
        :param kwargs: Additional arguments for the tool command.
        :return: A dictionary containing the output of the tool execution.
        """
        if tool_name not in self.tool_commands:
            raise ValueError(f"Tool '{tool_name}' is not supported.")

        # Construct the full command with additional arguments
        command = self.tool_commands[tool_name] + [str(value) for key, value in kwargs.items()]

        try:
            logger.info(f"Executing command: {' '.join(command)}")
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            error = None
        except subprocess.CalledProcessError as e:
            output = None
            error = e.stderr.decode('utf-8')

        return {
            "tool_name": tool_name,
            "command": command,
            "output": output,
            "error": error
        }

# Example usage
if __name__ == "__main__":
    executor = ToolExecutor()
    result = executor.execute_tool("ping", "example.com")
    print(result)
```

### Explanation:
1. **Logging Configuration**: The logging is set up to log information at the INFO level.
2. **Tool Executor Class**:
   - **Initialization**: A dictionary `tool_commands` maps tool names to their corresponding command lists.
   - **execute_tool Method**:
     - Checks if the provided tool name is supported.
     - Constructs the full command with additional arguments.
     - Uses `subprocess.run` to execute the command, capturing both standard output and standard error.
     - Handles exceptions using a try-except block to capture any errors during execution.
3. **Example Usage**: Demonstrates how to use the `ToolExecutor` class to execute the "ping" tool with an example domain.

This implementation ensures that external tools can be executed safely and their outputs are captured for further processing or integration.