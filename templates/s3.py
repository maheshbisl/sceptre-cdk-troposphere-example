from troposphere import Base64, Select, FindInMap, GetAtt
from troposphere import GetAZs, Join, Output, If, And, Not
from troposphere import Or, Equals, Condition
from troposphere import Parameter, Ref, Tags, Template
from troposphere.s3 import Bucket, WebsiteConfiguration

t = Template()

BucketName = Ref(t.add_parameter(Parameter("BucketName", Type="String")))

Bucket = t.add_resource(Bucket("Bucket", BucketName=BucketName ))


def sceptre_handler(sceptre_user_data):
    return t.to_yaml()