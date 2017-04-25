from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
	@task(2)
	def index(self):
		self.client.get("/")
		
	@task(1)
	def about(self):
		self.client.get("/about.html")
		
class MyLocust(HttpLocust):
	host = "http://brucecarson.test.godaddysites.com"
	task_set = MyTaskSet
	min_wait = 5000
	max_wait = 15000
	stop_timeout = 60
