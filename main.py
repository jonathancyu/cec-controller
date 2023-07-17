import cec
import time

class CECWrapper:
	def __init__(self):
		cec.init()
		devices = cec.list_devices()
		print(devices)
		me = None
		while me is None:
			me = [devices[i] for i in devices if devices[i].osd_string=='python-cec'][0]

		self.device = me
		print(self.device)
		cec.add_callback(self.callback, cec.EVENT_ALL)

	def callback(self, event, cmd):
		print(self.device.is_active())

	def run(self):
		try:
			while True:
				time.sleep(5)
				continue
		except KeyboardInterrupt:
			print('cya')
			cec.close() # contribute and make this do something...
if __name__=='__main__':
	wrapper = CECWrapper()
	wrapper.run()
