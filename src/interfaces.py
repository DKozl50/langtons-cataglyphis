from __future__ import annotations

import abc
import dataclasses

from . import result


class BaseLangtonRuleset(abc.ABC):
    def __init__(self, ruleset_code: str):
        self._init_field(ruleset_code)

    @abc.abstractmethod
    def __len__(self) -> int:
        pass

    @abc.abstractmethod
    def _init_field(self, ruleset_code: str) -> None:
        pass


class BaseLangtonEngine(abc.ABC):
    def __init__(self, field_side: int, ruleset: BaseLangtonRuleset):
        self._field_side = field_side
        self._ruleset = ruleset
        self._init_inner()

        self._was_evaluated = False

    def evaluate(self) -> None:
        assert not self._was_evaluated
        self._was_evaluated = True
        self._evaluate()

    @abc.abstractmethod
    def _evaluate(self) -> None:
        pass

    @abc.abstractmethod
    def get_result(self) -> result.LangtonResult:
        pass

    @abc.abstractmethod
    def _init_inner(self) -> None:
        pass


################################


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class LangtonImpl():
    name: str

    ruleset: type[BaseLangtonRuleset]
    engine: type[BaseLangtonEngine]

    def __str__(self):
        return self.name
