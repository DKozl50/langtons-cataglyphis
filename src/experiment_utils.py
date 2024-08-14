import dataclasses
import pathlib
import json
from typing import TypeAlias

from . import interfaces, timing


ChecksumType: TypeAlias = int
LangtonDataset: TypeAlias = list["LangtonExperiment"]


@dataclasses.dataclass(frozen=True, kw_only=True, slots=True)
class LangtonExperiment():
    ruleset_code: str
    field_side: int

    checksum: ChecksumType

    def __str__(self):
        return self.ruleset_code + str(self.field_side)


def dump_dataset(dataset: LangtonDataset, filepath: pathlib.Path) -> None:
    export_list = []
    for experiment in dataset:
        export_list.append(dataclasses.asdict(experiment))
    with filepath.open("w") as f:
        json.dump(export_list, f, indent=2)


def load_dataset(filepath: pathlib.Path) -> LangtonDataset:
    with filepath.open("r") as f:
        exported_dataset = json.load(f)
    dataset = LangtonDataset()
    for experiment in exported_dataset:
        dataset.append(LangtonExperiment(**experiment))
    return dataset


def run_measurements(dataset: LangtonDataset, implementations: list[interfaces.LangtonImpl]):
    registry = dict[str, dict[str, timing.TimeType]]()
    for experiment in dataset:
        registry[str(experiment)] = dict()
        for implementation in implementations:
            ruleset = implementation.ruleset(experiment.ruleset_code)
            engine = implementation.engine(experiment.field_side, ruleset)
            elapsed_time = timing.measure_manual(engine.evaluate)
            registry[str(experiment)][str(implementation)] = elapsed_time
            checksum = engine.get_result().get_checksum()
            assert checksum == experiment.checksum
    return registry
