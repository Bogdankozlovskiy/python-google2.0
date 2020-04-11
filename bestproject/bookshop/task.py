from celery import Celery
import logging
from time import sleep

logger = logging.getLogger("django")

app = Celery("myproject", broker="redis://localhost:6379/0")
app.conf.result_backend="redis://localhost:6379/0"


@app.task
def test_fun(pause):
	sleep(pause)
	logger.error("olololo ERrior))) from Celery")
	return "Done from Celery"

@app.task
def test_sched():
	return "done"

app.conf.beat_schedule = {
	"myproject":{
		"task":"bookshop.task.test_sched",
		"schedule":30.0,
	}
}









