import datetime
import subprocess
import sys

now = datetime.datetime.now().strftime("%Y%m%d")

domain_name = raw_input("What is the domain name? ")

key_file = "%s-%s.key" % (domain_name, now)
csr_file = "%s-%s.csr" % (domain_name, now)

# openssl genrsa -out ~/domain.com.ssl/domain.com.key 2048
subprocess.call(["openssl", "genrsa", "-out", key_file, "2048"], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

# openssl req -new -key ~/domain.com.ssl/domain.com.key -out ~/domain.com.ssl/domain.com.csr
subprocess.call(["openssl", "req", "-new", "-key", key_file, "-out", csr_file], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

# openssl req -noout -text -in ~/domain.com.ssl/domain.com.csr
subprocess.call(["openssl", "req", "-noout", "-text", "-in", csr_file], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

# aws iam upload-server-certificate --server-certificate-name domain.com-expires-20150925 --certificate-body file://cert.crt --private-key file://domain.com-20140819.key --certificate-chain file://chain.crt
