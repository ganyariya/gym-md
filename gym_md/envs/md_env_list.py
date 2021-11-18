"""List of md_env."""
from typing import Final

from gym_md.envs.md_env import MdEnvBase


class TestMdEnv(MdEnvBase):
    """TestMdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "test"
        super(TestMdEnv, self).__init__(stage_name=stage_name)


class EdgeMdEnv(MdEnvBase):
    """EdgeMdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "edge"
        super(EdgeMdEnv, self).__init__(stage_name=stage_name)


class HardMdEnv(MdEnvBase):
    """HardMdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "hard"
        super(HardMdEnv, self).__init__(stage_name=stage_name)


class Random1MdEnv(MdEnvBase):
    """Random1Env Class."""

    def __init__(self):
        stage_name: Final[str] = "random_1"
        super(Random1MdEnv, self).__init__(stage_name=stage_name)


class Random2MdEnv(MdEnvBase):
    """Random1Env Class."""

    def __init__(self):
        stage_name: Final[str] = "random_2"
        super(Random2MdEnv, self).__init__(stage_name=stage_name)


class Gene1MdEnv(MdEnvBase):
    """Random1Env Class."""

    def __init__(self):
        stage_name: Final[str] = "gene_1"
        super(Gene1MdEnv, self).__init__(stage_name=stage_name)


class Gene2MdEnv(MdEnvBase):
    """Random1Env Class."""

    def __init__(self):
        stage_name: Final[str] = "gene_2"
        super(Gene2MdEnv, self).__init__(stage_name=stage_name)


class Strand1MdEnv(MdEnvBase):
    """Strand1MdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "strand_1"
        super(Strand1MdEnv, self).__init__(stage_name=stage_name)


class Strand2MdEnv(MdEnvBase):
    """Strand2MdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "strand_2"
        super(Strand2MdEnv, self).__init__(stage_name=stage_name)


class Strand3MdEnv(MdEnvBase):
    """Strand3MdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "strand_3"
        super(Strand3MdEnv, self).__init__(stage_name=stage_name)


class Strand4MdEnv(MdEnvBase):
    """Strand4MdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "strand_4"
        super(Strand4MdEnv, self).__init__(stage_name=stage_name)


class Strand5MdEnv(MdEnvBase):
    """Strand5MdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "strand_5"
        super(Strand5MdEnv, self).__init__(stage_name=stage_name)


class Check1MdEnv(MdEnvBase):
    """Check1MdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "check_1"
        super(Check1MdEnv, self).__init__(stage_name=stage_name)


class Check2MdEnv(MdEnvBase):
    """Check2MdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "check_2"
        super(Check2MdEnv, self).__init__(stage_name=stage_name)


class Check3MdEnv(MdEnvBase):
    """Check3MdEnv Class."""

    def __init__(self):
        stage_name: Final[str] = "check_3"
        super(Check3MdEnv, self).__init__(stage_name=stage_name)


class Holmgard0MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_0"
        super(Holmgard0MdEnv, self).__init__(stage_name=stage_name)


class Holmgard1MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_1"
        super(Holmgard1MdEnv, self).__init__(stage_name=stage_name)


class Holmgard2MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_2"
        super(Holmgard2MdEnv, self).__init__(stage_name=stage_name)


class Holmgard3MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_3"
        super(Holmgard3MdEnv, self).__init__(stage_name=stage_name)


class Holmgard4MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_4"
        super(Holmgard4MdEnv, self).__init__(stage_name=stage_name)


class Holmgard5MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_5"
        super(Holmgard5MdEnv, self).__init__(stage_name=stage_name)


class Holmgard6MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_6"
        super(Holmgard6MdEnv, self).__init__(stage_name=stage_name)


class Holmgard7MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_7"
        super(Holmgard7MdEnv, self).__init__(stage_name=stage_name)


class Holmgard8MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_8"
        super(Holmgard8MdEnv, self).__init__(stage_name=stage_name)


class Holmgard9MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_9"
        super(Holmgard9MdEnv, self).__init__(stage_name=stage_name)


class Holmgard10MdEnv(MdEnvBase):
    """Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "holmgard_10"
        super(Holmgard10MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard0MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_0"
        super(ConstantHolmgard0MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard1MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_1"
        super(ConstantHolmgard1MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard2MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_2"
        super(ConstantHolmgard2MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard3MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_3"
        super(ConstantHolmgard3MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard4MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_4"
        super(ConstantHolmgard4MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard5MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_5"
        super(ConstantHolmgard5MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard6MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_6"
        super(ConstantHolmgard6MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard7MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_7"
        super(ConstantHolmgard7MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard8MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_8"
        super(ConstantHolmgard8MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard9MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_9"
        super(ConstantHolmgard9MdEnv, self).__init__(stage_name=stage_name)


class ConstantHolmgard10MdEnv(MdEnvBase):
    """Constant Holmgard Class."""

    def __init__(self):
        stage_name: Final[str] = "ConstantHolmgard_10"
        super(ConstantHolmgard10MdEnv, self).__init__(stage_name=stage_name)
