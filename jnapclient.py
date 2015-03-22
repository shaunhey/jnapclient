#!/usr/bin/env python

import argparse
import json
import urllib2


class JNAPClient:
	JNAP_url = ""

	def __init__(self, host):
		self.JNAP_url = "http://" + host + "/JNAP/"

	def get_device_info(self):
		request = urllib2.Request(self.JNAP_url)
		request.add_header(
			"X-JNAP-Action",
			"http://linksys.com/jnap/core/GetDeviceInfo"
		)
		response = urllib2.urlopen(request, json.dumps({}))
		return json.load(response)


def parse_args():
	parser = argparse.ArgumentParser(description="Linksys JNAP Client")
	parser.add_argument(
		"host", type=str, nargs=1,
		help="IP address or host name for the Linksys router"
	)
	parser.add_argument(
		'-d', '--device-info', action='store_const', const=True,
		help='get router device and service information')

	return parser.parse_args()


def main():
	settings = parse_args()
	client = JNAPClient(settings.host[0])

	if settings.device_info is True:
		device_info = client.get_device_info()
		print json.dumps(device_info, indent=2)


if __name__ == "__main__":
	main()
