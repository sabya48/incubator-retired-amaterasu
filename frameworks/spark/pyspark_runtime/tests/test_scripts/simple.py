"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
from pyspark.sql.functions import udf
from pyspark.sql.types import StructType, StructField, IntegerType

from amaterasu.pyspark.runtime import ama_context


def pow(num):
    return num * num


pow_udf = udf(pow, IntegerType())
a = [[1], [2], [3], [4]]
schema = StructType([
    StructField('number', IntegerType(), True)
])
input_df = ama_context.spark.createDataFrame(a, schema)
sdf = input_df.withColumn("pow_number", pow_udf("number"))

ama_context.persist('odd', sdf, overwrite=True)
