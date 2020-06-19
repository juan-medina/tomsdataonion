# MIT License
#
# Copyright (c) 2020 Juan Medina
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import os

log = logging.getLogger(__name__)


def slice_layer_1(input_file_name, output_file_name):
	log.info("reading %s...", input_file_name)
	read_file = open(input_file_name, 'r')
	lines = read_file.readlines()
	read_file.close()
	write_file = open(output_file_name, 'w')
	log.info("writing %s...", output_file_name)
	grab_next = False
	for line in lines:
		if "[ Payload ]" in line:
			grab_next = True
		else:
			if grab_next and line.strip() != "":
				write_file.write(line)
	write_file.close()
	log.info("%s completed", output_file_name)


def main():
	log.info("Let's slice the onion...")
	if not os.path.exists("data"):
		log.info("creating data directory..")
		os.mkdir("data")
	else:
		log.warning("data directory already exists.")
	slice_layer_1("puzzle.txt", "data/layer_1_undecoded.dat")


if __name__ == "__main__":
	LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
	logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

	try:
		main()
	except Exception as ex:
		log.error(ex, exc_info=True)
		raise ex
