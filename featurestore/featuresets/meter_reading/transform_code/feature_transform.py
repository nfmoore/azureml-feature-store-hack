from pyspark.sql import functions as F
from pyspark.ml import Transformer
from pyspark.sql.dataframe import DataFrame

class FeatureTransformer(Transformer):
    def _transform(self, df: DataFrame) -> DataFrame:
        res = (
            df
        )

        return res
