if __name__ == "__main__":
	try:
		__import__("ambf").make()
	except Exception as e:
		exit(str(e))
