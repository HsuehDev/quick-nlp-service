from app.component.chat import RoleItem
from typing import List
import re

class Formatter():
    def __init__(self) -> None:
        self.chatlog_list: List[dict] = []
        self.system_message: str = ''

    def openai_to_chatlog(self, roles: List[RoleItem]) -> None:
        for role in roles:
            current_dict: dict = {
                "role": role.role,
                "content": role.content
            }

            if role.role == "system":
                self.chatlog_list.insert(0, current_dict)
            else:
                self.chatlog_list.append(current_dict)

    def openai_to_llama(self, roles: List[RoleItem]) -> str:
        result: str = ""
        first_user: bool = True

        self.openai_to_chatlog(roles)

        for chatlog in self.chatlog_list:
            current_role: str = chatlog['role']
            current_content: str = chatlog['content']

            if current_role == "system":
                self.system_message = current_content
                continue

            if current_role == "user":
                current_system_message: str = f"<<SYS>>{self.system_message}<</SYS>>" if first_user else ""
                current_content = f"[INST]{current_system_message}{current_content}[/INST]"

                first_user = False
            result += f"""{current_content}"""

        return result

    def llama_to_openai(self, input_text: str) -> List[RoleItem]:
        # get system message
        system_message_pattern = re.compile(r'<<SYS>>(.*?)<</SYS>>')
        
        system_message_match = re.search(system_message_pattern, input_text).group(1)
        if system_message_pattern:
            self.system_message = system_message_match.group(1)
        else:
            self.system_message = ""

        modified_text = re.sub(system_message_pattern, '', input_text)

        # get chatlog
        role_pattern = r'\[INST\]([^[]+)\[/INST\]([^[]+)'
        roles_matches = re.findall(role_pattern, modified_text)

        roles: List[RoleItem] = [RoleItem(role=role, content=content) for role, content in roles_matches]

        if self.system_message:
            roles.insert(0, RoleItem(role = 'system', content = self.system_message))
        
        return roles
