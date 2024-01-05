from dataclasses import dataclass, field, InitVar

@dataclass
class Message:

    message:str
    payload:str=field(init=False)

    def __post_init__(self):
        self.payload = '{"text":"%s"}' % self.message