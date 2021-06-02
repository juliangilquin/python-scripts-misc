import requests
import hashlib
import sys
import getpass

def request_api_data(query_char):
	url = "https://api.pwnedpasswords.com/range/" + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again.")
	return res

def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(":") for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0

def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char)
	return get_password_leaks_count(response, tail)

def get_the_pw():
	the_pw = getpass.getpass(prompt="Password to check : ")
	while len(the_pw) <= 0:
		the_pw = getpass.getpass(prompt="Incorrect input. Try again : ")
	return the_pw

def main():
	print("Check if a password appears in the database of the pwnedpasswords.com API")
	pw_to_check = get_the_pw()
	count = pwned_api_check(pw_to_check)
	if count:
		print(f"This password was found {count} times. Change it !")
	else:
		print("This password was not found in the database. You can use it !")
	return "End of Check"

if __name__ == '__main__':
	sys.exit(main())