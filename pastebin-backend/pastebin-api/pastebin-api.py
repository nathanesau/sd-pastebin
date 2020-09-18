from app import app, db
from app.models import Pastes
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from sqlalchemy import text, func
import redis
import os

def expire_task():
    """
    checks whether any pastes have expired and deletes expired pastes
    """
    print("running expiry task at {}".format(datetime.now()))
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
sched.start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
