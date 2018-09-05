ar1 = ['apple','banana','pear']

print('Voorbeeld van een list')

for x in ar1[1:]:
	print(x)

print('Voorbeeld van een tuple')
t1 = ('apple','banana','pear')
for x in t1:
  print(x)


print('Voorbeeld van een dictionary')
d1 =	{
  "voedsel": "twix",
  "cal": "255"
}
print(d1)  

print(d1.get('voedsel'))

koerswriter.writerow(var.get('title'), var.get('price'))

    '''        
    path = r"c:\users\pxm04\git\python\koersen.csv"

    csv_writer(output, path)

    # Create an S3 client
    s3 = boto3.client('s3')

    filename = r"c:\users\pxm04\git\python\koersen.csv"
    bucket_name = 'mostie-algemeen'

        # Uploads the given file using a managed uploader, which will split up large
        # files automatically and upload parts in parallel.
    s3.upload_file(filename, bucket_name, filename)
    '''