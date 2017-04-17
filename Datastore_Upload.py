from csv import reader
import logging
from subprocess import call
import gzip
import shutil

def fastq_to_datastore(SRR_Number):
	logging.basicConfig(filename="Datastore_Upload.log", level=logging.DEBUG)
	logging.info("Splitting and coverting %s to fastq format" % SRR_Number)
	i = 0
	while i <= 5:
		f_dump = call(['fastq-dump', '--split-files', SRR_Number])
		if f_dump == 0:
			logging.info('Successfully split %s and converted to fastq format.' %(SRR_Number))
			fastq_file_1 = "%s_1.fastq" % (SRR_Number) 
			fastq_file_2 = "%s_2.fastq" % (SRR_Number)
			break
	logging.info('Compressing files %s and %s' % (fastq_file_1, fastq_file_2))
	with open(fastq_file_1, 'r') as f_1, gzip.open('%s.gz' % (fastq_file_1), 'w') as gz_1:
		shutil.copyfileobj(f_1, gz_1)
	with open(fastq_file_2, 'r') as f_2, gzip.open('%s.gz' %(fastq_file_2), 'w') as gz_2:
		shutil.copyfileobj(f_2, gz_2)
	gzip_1 = "%s.gz" % fastq_file_1
	gzip_2 = "%s.gz" % fastq_file_2
	logging.info('Uploading %s to datastore' % gzip_1)
	k = 0
	while k <= 5:
		load_1 = call(['iput', '-TV', gzip_1, './coge_data/'])
		if load_1 == 0:
			logging.info('%s successfully uploaded to datastore' % gzip_1)
			break
	logging.info('Uploading %s to datastore' % gzip_2)
	n = 0
	while n <= 5:
		load_2 = call(['iput', '-TV', gzip_2, './coge_data/'])
		if load_2 == 0:
			logging.info('%s successfully uploaded to datastore' % gzip_2)
			break
	if load_1 != 0:
		logging.debug('%s could not be uploaded to datastore. Will have to upload manually' % gzip_1)
	if load_2 != 0:
		logging.debug('%s could not be uploaded to datastore. Will have to upload manually' % gzip_2)
	if f_dump != 0:
		logging.debug('Could not split and convert %s to fastq format. Will have to convert manually.' % (SRR_Number))


if __name__ == "__main__":
	SRR_Number = sys.argv[1]
