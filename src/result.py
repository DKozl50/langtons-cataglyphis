from __future__ import annotations

from typing import TypeAlias

import numpy as np
import matplotlib.pyplot as plt

from . import experiment_utils, interfaces


FieldElemType: TypeAlias = int

CHECKSUM_MOD = 100000007


class LangtonResult():
    def __init__(self, field: np.ndarray[FieldElemType], steps: int, ruleset: interfaces.BaseLangtonRuleset):
        self._field = field
        self._steps = steps
        self._ruleset = ruleset

    def show(self, mpl_kwargs: dict | None = None) -> plt.Axes:
        if mpl_kwargs is None:
            mpl_kwargs = {}
        return plt.matshow(self._field, origin='lower', **mpl_kwargs).axes

    def get_field(self) -> np.ndarray[FieldElemType]:
        return self._field

    def get_steps(self) -> int:
        return self._steps

    def get_checksum(self) -> experiment_utils.ChecksumType:
        checksum: experiment_utils.ChecksumType = 0
        ruleset_len: int = len(self._ruleset)
        for elem in self._field.flat:
            checksum = ruleset_len * checksum + elem
            checksum %= CHECKSUM_MOD
        return checksum
