from subprocess import call
import reader, os

call(["python", "download.py"])
call(["mkdir", "raw"])
call(["mkdir", "json"])


for file in os.listdir("."):
	if file.endswith("xls"):
		print "Procesando {0} ...".format(file)
		reader.xls_to_json(file)

call("mv *.xls raw",  shell=True)
call("mv *.json json",  shell=True)

reader.generate_index("json")


