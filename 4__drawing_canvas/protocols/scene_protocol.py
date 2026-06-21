from typing import Protocol
from commands.command_manager import CommandManager

class SceneProtocol(Protocol):
    command_manager: CommandManager
