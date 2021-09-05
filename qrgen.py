#!/usr/bin/env python

import pyqrcode
import argparse

url = "empty"
file = "qrcode.svg"

def parse():
	parser = argparse.ArgumentParser(description="Generate QR Code for given input text")
	parser.add_argument('input_text', help="The text which will be encoded in the QR Code")
	parser.add_argument('output_file', help="The file in which the QR Code will be written")
	args = parser.parse_args()
	global url
	global file
	url = args.input_text
	file = args.output_file


def main():
	code = pyqrcode.create(url, error='L', version=3)
	code.svg(file, scale=10, quiet_zone=2, background="white")
	print(code.terminal(quiet_zone=1))
	exit(0)

if __name__ == "__main__":
	parse()
	main()

