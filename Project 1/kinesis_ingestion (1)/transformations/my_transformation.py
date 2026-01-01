import dlt
from pyspark. sql. functions import from_json, col, struct
from pyspark.sql.types import MapType, StringType

kinesis_config = {
"streamName": "telematics-stream-tmh",
"region": "us-east-1",
.. "serviceCredential": "kinesis-service-credential"
"initialPosition": "earliest"

I