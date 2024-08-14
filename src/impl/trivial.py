import numpy as np

from src import interfaces, result


class TrivialLangtonRuleset(interfaces.BaseLangtonRuleset, str):
    """
    Well, currently it literally is a `str`,
    but I could not find an elegant way to use `str` without reimplementing it
    """
    def _init_field(self, ruleset_code: str) -> None:
        self._ruleset = ruleset_code

    def __len__(self) -> int:
        return len(self._ruleset)


class TrivialLangtonEngine(interfaces.BaseLangtonEngine):
    def _init_inner(self) -> None:
        assert isinstance(self._ruleset, TrivialLangtonRuleset)
        self._field = [[0] * self._field_side for _ in range(self._field_side)]
        self._steps = 0

    def _evaluate(self):
        #  y
        #  ^
        #  |     0
        #  |  3 ant 1
        #  |     2
        #  0-----------> x

        ant_x = self._field_side // 2
        ant_y = self._field_side // 2
        ant_orientation = 0

        while True:
            if ant_y < 0 or ant_x < 0 or ant_y >= self._field_side or ant_x >= self._field_side:
                return

            # rotate
            if self._ruleset[self._field[ant_x][ant_y]] == "L":
                ant_orientation = (ant_orientation - 1) % 4
            else:
                ant_orientation = (ant_orientation + 1) % 4

            # change state underneath
            self._field[ant_x][ant_y] = (self._field[ant_x][ant_y] + 1) % len(self._ruleset)

            # move
            match ant_orientation:
                case 0:
                    ant_y += 1
                case 1:
                    ant_x += 1
                case 2:
                    ant_y -= 1
                case 3:
                    ant_x -= 1
                case _:
                    pass

            self._steps += 1

    def get_result(self):
        return result.LangtonResult(
            field=np.array(self._field),
            steps=self._steps,
            ruleset=self._ruleset,
        )


trivial_impl = interfaces.LangtonImpl(
    name="Trivial",
    ruleset=TrivialLangtonRuleset,
    engine=TrivialLangtonEngine,
)
