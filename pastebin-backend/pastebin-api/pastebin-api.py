from app import app, db
from app.models import Pastes
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from sqlalchemy import text, func
import redis
import os

def analytics_task():
    """
    calculates hit counts using logfile and writes info to redis cache
    """
    hit_count = {}

    # calculate hit_count stats using logfile
    f = open("{}/log.txt".format(app.config['LOGS_FOLDER']))
    for line in f.read().splitlines():
        ip_addr, ymd, hms, method, url = line.split(' ')

        # only track hit counts for the GET paste endpoint
        if not (method == 'GET' and "/api/v1/paste" in url):
            continue

        year, month, day = ymd.split('-')
        period = "{}-{}".format(year, month)
        shortlink = url.split('shortlink=')[1]
        key = "{}-{}".format(period, shortlink)

        if key not in hit_count:
            hit_count[key] = 1
        else:
            hit_count[key] = hit_count[key] + 1
    
    # store hit count stats in the redis cache
    r = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])
    for key, value in hit_count.items():
        r.set(key, value)
    r.close()

def expire_task():
    """
    checks whether any pastes have expired and deletes expired pastes
    """
    result = Pastes.query.filter(Pastes.created_at \
        + func.make_interval(0,0,0,0,0,Pastes.expiration_length_in_minutes) < datetime.now())

    for row in result:
        # delete paste file
        os.remove(row.paste_path)

        # delete db entry
        db.session.delete(row)

    db.session.commit()

# delete expired tasks every minute
sched = BackgroundScheduler(daemon=True)
sched.add_job(expire_task, 'interval', seconds=60)
sched.add_job(analytics_task, 'interval', seconds=10)
sched.start()

if __name__ == "__main__":
    app.run()
