from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .models import Link

logger = get_task_logger(__name__)


# periodic task to run every 15 mins
@periodic_task(run_every=(crontab(minute='*/15')), name='rank all', ignore_result=True)
def rank_all():
    for link in Link.with_votes.all():
        link.set_rank()
    logger.info('Updated ranks for all links')
