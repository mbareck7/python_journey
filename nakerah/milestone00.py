#!/usr/bin/python3

# import os
import json

def set_empty_value_to_NA(d):
	for k, v in d.items():
		if d[k] == "":
			d[k] = "NA"
	return d

def set_normal_user(d):
	if int(d["user_id"]) >= 1000:
		d["normal_user"] = True
	return d

def format_output(l):
	return json.dumps(l, indent=4)

def prepare_data(f):#return list
	res = []
	lines = open(f,'r')
	for l in lines:
		res.append(l.rstrip()) #
	lines.close()
	return res

def treat_line(l):
	data = l.split(":")
	res = {"user_name":data[0],"user_id":data[2],"home_dir":data[5],"login_shell":data[6],"normal_user":False}
	return set_empty_value_to_NA(set_normal_user(res))

def milestone00(users):
	results = []
	for user in users:
		results.append(treat_line(user))
	# results_file = open("results","w")
	# for line in results:
	# 	results_file.write(str(line) + "\n")
	return results

# def output(file_):
# 	output = open
# 	cmd = "sed 's/,/,\n/g; s/},/\n},/g; s/\\n//g'"
# 	os.system("sed 's/,/,\n/g; s/},/\n},/g; s/\\n//g' results.txt")

def main():
	users = prepare_data("milestone_00.txt")
	print(format_output(milestone00(users)))

if __name__ == '__main__':
	main()