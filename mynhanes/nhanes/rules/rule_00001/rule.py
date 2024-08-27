from nhanes.workprocess.transformation_base import BaseTransformation
from nhanes.utils.logs import logger


class rule(BaseTransformation):
    """
    Rule Name: rule_00001
    Version: 0.0.0
    Description: teste

    This class applies the following transformations:
    (version / dataset / variable)
    - Input Variables: (nhanes / DEMO / RIDAGEYR), (nhanes / all datasets / RIAGENDR)
    - Output Variables: (normalized / DEMO / RIDAGEYR), (normalized / all datasets / RIAGENDR)

    The apply_normalization method should implement the logic for this rule.
    """

    def apply_transformation(self) -> bool:
        self.df_out = self.df_in.copy()

        msg = f"Starting normalization rule file to {self.rule.rule}"
        logger(self.log, "e", msg)

        # ----------------------------------------
        # START YOUR TRANSFORMATIONS HERE
        # ----------------------------------------

        # example transformation: Doubling the age
        self.df_out['version'] = 'normalized'
        self.df_out['RIDAGEYR'] = self.df_out['RIDAGEYR'] * 2

        # ----------------------------------------
        # END YOUR TRANSFORMATIONS HERE
        # ----------------------------------------

        return True