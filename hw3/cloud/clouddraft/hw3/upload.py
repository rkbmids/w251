auth_endpoint = 'https://iam.bluemix.net/oidc/token'
service_endpoint = 'https://s3-api.us-geo.objectstorage.softlayer.net'
cos = ibm_boto3.client('s3',
   ibm_api_key_id=cos_credentials['apikey'],
   ibm_service_instance_id=cos_credentials['resource_instance_id'],
   ibm_auth_endpoint=auth_endpoint,
   config=Config(signature_version='oauth'),
   endpoint_url=service_endpoint)

for bucket in cos.list_buckets()['Buckets']:
   print(bucket['Name'])

cos.upload_file(Filename='forwarder.py', Bucket='hw3',Key='forwarder.py')
