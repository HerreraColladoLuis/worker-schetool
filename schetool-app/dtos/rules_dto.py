from dataclasses import dataclass


@dataclass
class RulesDto:
    rule_id: int
    rule_type: str
    rule_value: str
    rule_description: str
